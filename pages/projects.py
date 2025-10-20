import streamlit as st
import pandas as pd
import os
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="My Projects Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .project-card {
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin: 0.5rem 0;
        transition: transform 0.2s;
        background: white;
    }
    .project-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .project-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .project-type {
        background-color: #e0e0e0;
        padding: 0.2rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        display: inline-block;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

def load_projects_data():
    """Load projects data from Excel file"""
    try:
        df = pd.read_excel('projects.xlsx')
        return df
    except FileNotFoundError:
        st.error("projects.xlsx file not found! Please make sure it exists.")
        return pd.DataFrame()

def load_image(image_path):
    """Load image from local path or URL"""
    print( image_path)
    if not image_path or image_path == 0:
        image_path = "images/default.jpg"
    image_path = "images/" + image_path
    try:
        if image_path.startswith('http'):
            # For URL images
            return image_path
        else:
            # For local images
            if os.path.exists(image_path):
                return Image.open(image_path)
            else:
                st.warning(f"Image not found: {image_path}")
                return None
    except Exception as e:
        st.warning(f"Could not load image: {image_path} - {e}")
        return None

def display_project_card(project, index):
    """Display a project card in the grid"""
    with st.container():
        st.markdown(f'<div class="project-card">', unsafe_allow_html=True)
        
        # Project type badge
        st.markdown(f'<div class="project-type">{project["Project Type"]}</div>', unsafe_allow_html=True)
        
        # Project title
        st.markdown(f'<div class="project-title">{project["Title"]}</div>', unsafe_allow_html=True)
        
        # Project image
        image = load_image(project['photo'])
        if image:
            if isinstance(image, str):  # URL
                st.image(image, width=200,use_container_width=True)
            else:  # PIL Image
                st.image(image, width=200, use_container_width=True)
            
            st.markdown("""
                    <style>
                    .stImage img {
                        width: 100% !important;
                    }
                    </style>
                """, unsafe_allow_html=True)

        # Short description (truncated)
        short_desc = project['description'][:100] + "..." if len(project['description']) > 100 else project['description']
        st.write(short_desc)
        
        # View Details button
        if st.button("View Details", key=f"btn_{index}"):
            st.session_state.selected_project = index
        
        st.markdown('</div>', unsafe_allow_html=True)

def display_project_details(project):
    """Display detailed view of a single project"""
    st.markdown("---")
    st.button("← Back to All Projects", on_click=lambda: st.session_state.pop('selected_project', None))
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Project image
        image = load_image(project['photo'])
        if image:
            st.image(image,  use_container_width=True)
            st.markdown("""
                    <style>
                    .stImage img {
                        width: 100% !important;
                    }
                    </style>
                """, unsafe_allow_html=True)

        # Project metadata
        st.subheader("Project Info")
        st.write(f"**Type:** {project['Project Type']}")
        if pd.notna(project.get('url')) and project['url']:
            st.write(f"**URL:** [View Project]({project['url']})")
        
        # Additional fields (you can add more as needed)
        additional_fields = ['tech_stack', 'duration', 'status']  # Add your actual column names
        for field in additional_fields:
            if field in project and pd.notna(project[field]):
                st.write(f"**{field.replace('_', ' ').title()}:** {project[field]}")
    
    with col2:
        # Project details
        st.title(project['Title'])
        st.markdown(f"**Description:**")
        st.write(project['description'])
        
        # You can add more detailed sections here
        if pd.notna(project.get('features')):
            st.markdown("**Key Features:**")
            features = project['features'].split(',') if isinstance(project['features'], str) else []
            for feature in features:
                st.write(f"• {feature.strip()}")

def show_projects():
    st.title("🚀 My Software Projects Portfolio")
    st.markdown("Browse through my collection of 40+ software projects")
    
    # Load data
    projects_df = load_projects_data()
    
    if projects_df.empty:
        st.warning("No projects data found. Please check your Excel file.")
        return
    
    # Initialize session state
    if 'selected_project' not in st.session_state:
        st.session_state.selected_project = None
    
    # If a project is selected, show its details
    if st.session_state.selected_project is not None:
        selected_project_data = projects_df.iloc[st.session_state.selected_project]
        display_project_details(selected_project_data)
        return
    
    # Sidebar filters
    st.sidebar.title("🔍 Filters")
    
    # Project type filter
    project_types = ['All'] + list(projects_df['Project Type'].unique())
    selected_type = st.sidebar.selectbox("Project Type", project_types)
    
    # Search filter
    search_term = st.sidebar.text_input("Search Projects")
    
    # Apply filters
    filtered_projects = projects_df.copy()
    
    if selected_type != 'All':
        filtered_projects = filtered_projects[filtered_projects['Project Type'] == selected_type]
    
    if search_term:
        mask = filtered_projects.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
        filtered_projects = filtered_projects[mask]
    
    # Display project count
    st.sidebar.write(f"**Showing {len(filtered_projects)} of {len(projects_df)} projects**")
    
    # Display projects in a grid
    st.subheader(f"Projects ({len(filtered_projects)})")
    
    # Create columns for grid layout
    cols = st.columns(3)  # 3-column layout
    
    for index, (_, project) in enumerate(filtered_projects.iterrows()):
        with cols[index % 3]:
            display_project_card(project, filtered_projects.index.get_loc(project.name))
    
    # If no projects match filters
    if len(filtered_projects) == 0:
        st.info("No projects match your current filters. Try adjusting your search criteria.")

if __name__ == "__main__":
    show_projects()
import streamlit as st 
from pages import projects 
from pages import  test

st.title("Haider Ali Khalil")

tab_home, tab_apps, tab_tools, tab_python, tab_courses,  tab_elections, tab_about = st.tabs(
        ["Home",
         "Apps",
         "Online Tools",
         "Python Programming",
         "Courses",
         "Elections",
         "About"
        ])

# Display dashboards based on selection

    
with tab_home:
    st.write("Haider Ali Khalil is a software developer and data scientist with expertise in Python, Django, Flutter, and data analysis. He has created several web applications and online tools, and offers courses on Udemy.")

with tab_apps:
    # Include projects content directly
    st.subheader("Software Projects Portfolio")
    projects.show_projects()
    # exec(open("pages//1_projects.py").read())
with tab_tools:
    url = "https://mediawall.streamlit.app/"
    st.markdown("[Media Wall](%s)" % url)
    
    url = "https://areacal.streamlit.app/"
    st.markdown("[Area Calculator](%s)" % url)
with tab_elections:
    url = "https://pecbln.streamlit.app/"
    st.markdown("[PEC Balochistan](%s)" % url)

    url = "https://ge2018.streamlit.app/"
    st.markdown("[General Elections 2018](%s)" % url)


with tab_courses:
    st.subheader("Courses on Udemy")
    url = "https://www.udemy.com/course/django-in-2-hours/learn/?referralCode=F07B59289EFE77488AE9"
    st.markdown("Django in 2 Hours [Click](%s)" % url)


    url = "https://www.udemy.com/course/flutter-and-firebase/learn/?referralCode=04B1F35F6411EE7A1BEA"
    st.markdown("Flutter and Firebase [Click](%s)" % url)

    url = "https://www.udemy.com/course/build-a-real-estate-website-with-drupal-a-beginners-course/?referralCode=BA8E407149569D8A5EFB"
    st.markdown("Build a Real Estate Website with Drupal [Click](%s)" % url)

    url = "https://www.udemy.com/user/haider-ali-65/"
    st.markdown("Build an OpenAI + LangChain App in Python [Click](%s)" % url)

with tab_python:
    st.subheader("Python Programming Book")
    url="https://haiderkhalil.gumroad.com/l/python_book"
    st.markdown("Python Programming Book [Click](%s)" % url)





import streamlit as st 
st.title("Haider Ali Khalil")
st.write("Tools developed")
col1, col2, col3 = st.columns(3)

with col1:
    url = "https://pecbln.streamlit.app/"
    st.markdown("[PEC Balochistan](%s)" % url)

    url = "https://ge2018.streamlit.app/"
    st.markdown("[General Elections 2018](%s)" % url)

with col2:
    url = "https://mediawall.streamlit.app/"
    st.markdown("[Media Wall](%s)" % url)
    
with col3:
    url = "https://areacal.streamlit.app/"
    st.markdown("[Area Calculator](%s)" % url)

st.subheader("Courses on Udemy")
url = "https://www.udemy.com/course/django-in-2-hours/learn/?referralCode=F07B59289EFE77488AE9"
st.markdown("Django in 2 Hours [Click](%s)" % url)


url = "https://www.udemy.com/course/flutter-and-firebase/learn/?referralCode=04B1F35F6411EE7A1BEA"
st.markdown("Flutter and Firebase [Click](%s)" % url)

url = "https://www.udemy.com/course/build-a-real-estate-website-with-drupal-a-beginners-course/?referralCode=BA8E407149569D8A5EFB"
st.markdown("Build a Real Estate Website with Drupal [Click](%s)" % url)

url = "https://www.udemy.com/user/haider-ali-65/"
st.markdown("Build an OpenAI + LangChain App in Python [Click](%s)" % url)


url="https://haiderkhalil.gumroad.com/l/python_book"
st.markdown("Python Programming Book [Click](%s)" % url)





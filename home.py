import streamlit as st

st.title('การทดสอบเขียนเว็บด้วย Python')
st.header('นาย นรุตม์ แก้วพิจิตร')
st.subheader('สาขาเทคโนโลยีสารสนเทศ')
st.markdown("----")

col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
    st.image('./pic/profile-icon-design-free-vector.jpg')
with col2:
    st.image('./pic/bahen_organic_milk_3_1024x1024.jpg')
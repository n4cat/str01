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

html_1 = """
<div style="background-color:#7ED8FF;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd

dt=pd.read_csv('./data/iris.csv')
st.write(dt.head(10))
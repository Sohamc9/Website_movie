import streamlit as st
import pandas as pd

st.title("Disney")
st.header("Welcome to HomePage")
st.subheader("This is a website to showcase different Movies")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

#with st.container():
#    st.subheader("Kia")
#    st.image("artifacts\images\Kia.webp")
#    st.subheader("Koniegsegg")
#    st.image("artifacts\images\koniegsegg.webp")
#    st.subheader("Lamborgini")
#    st.image("artifacts\images\lambor.webp")

col1, col2, col3 = st.columns([2, 2, 2],gap="medium",vertical_alignment='center',border=True)
col1.subheader("Kia")
col1.image("artifacts/images/Kia.webp")
col2.subheader("Koniegsegg")
col2.image("artifacts/images/koniegsegg.webp")
col3.subheader("Lamborgini")
col3.image("artifacts/images/lambor.webp")  
st.selectbox("Pick one", ["None","Kia", "Koniegsegg","Lamborgini"],placeholder="None")

price = st.slider("Enter Your Budget", min_value=100000, max_value=10000000,step=1000000,value=500000)
st.write(f"Your Selected Budget is :- {price}")
st.text_input("Enter Your name")
st.text_input("Enter your COntact no")
st.text_input("Enter your Email Id")
st.text_area("Enter your full address",placeholder="Mumbai")
if st.button("Submit"):
    st.switch_page('pages/form_feedback.py')

 
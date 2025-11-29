import streamlit as st

st.title("My streamlit app")
st.header("Welcome to the Demo app")
st.write("This is a single app built with streamlit!")

name=st.text_input("Hello! Your good name please! :")
if name:
    st.success(f"Hello, {name}")

age = st.slider("Select your age,",1,100,25)
st.write("Your age is: ",age)
import streamlit as st

st.title("Simple calculator")

num1 = st.number_input("Enter a first number")
num2 = st.number_input("Enter a second number")
operation = st.selectbox("Choose operation",["Add","Subract","Multiply","Divide"])

if st.button("Calculate"):
    if operation=="Add":
        res=num1+num2
    elif operation=="Subract":
        res=num1-num2
    elif operation=="Multiply":
        res=num1*num2
    elif operation=="Divide":
        res= num1/num2 if num2!=0 else "Connot divide by zero"
    st.success("Result: {}".format(res))
# python -m streamlit run calculator.py
# streamlit run calculator.py

import streamlit as st

st.title("Basic Calculator Application")
st.subheader("Perform basic arithmetic operations")
# st.markdown("For normal content writing")
c1,c2 = st.columns(2)
fnum = c1.number_input("Enter first number")
snum = c2.number_input("Enter Second number")

options = ["Add","Sub","Div","Mul"]
op= st.radio("Select an operation", options)

button = st.button("Calculate")

result = 0
if button:
    if op == "Add":
        result = fnum + snum
    if op == "Sub":
        result = fnum - snum
    if op == "Mul":
        result = fnum * snum
    if op == "Div":
        result = fnum / snum
st.success (f"Result:{result}")

# to make it more interacting you can add popups
st.balloons()
# st.snow()
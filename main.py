import streamlit as st
import streamlit as st

number = st.slider("Pick a number: ", min_value=1, max_value=10)
st.text("Your number is " + str(number))



st.write("""
# Keluarga Senyum
""")
a = st.text_input("Nama : ")
b = st.text_input("Kelas : ")
st.write("Nama : ",a)
st.write("Kelas : ",b)

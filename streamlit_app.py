import streamlit as st

st.title("🎈Hi Mrs. Karp")
st.write(
    "I am sad"
)
st.button("press me!")
st.button("don't press me!")
if st.button("don't press me!"):
    st.write("Ow! Don't you listen?")
if st.button("press me!"):
    st.write("You just took orders from a button.")

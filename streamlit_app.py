import streamlit as st

st.title("🎈Hi Mrs. Karp")
st.write(
    "I am sad"
)
st.button("press me!")
if st.button("press me!"):
    st.stop()
st.button("don't press me!")
if st.button("don't press me!"):
    st.stop()

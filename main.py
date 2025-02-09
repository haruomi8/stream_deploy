import streamlit as st
name = st.text_input("wat's your name")
if st.button("input"):
    st.text(f"hello {name} i going to your house good bye(don't worry this is fake)")
    if st.button("delete"):
        st.text(" ")
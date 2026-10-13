import streamlit as st
st.title("Basic Streamlit App")
st.write("Welcome to the basic Streamlit app!")
st.write("This app demonstrates the basic usage of Streamlit.")
user_name = st.text_input("Enter your name:")
if user_name:
    #st.write(f"Hello {user_name}! ")
    if st.session_state.get("clicked"):
        st.write(f"Nice to meet you, {user_name}!")

def click_button():
    st.session_state.clicked = True
    st.write(f"Hello {user_name}! ")

st.button("Greet Me", on_click=click_button)
import streamlit as st

st.title(':rainbow[To Do List] :rainbow:')

work = st.checkbox('Work')
gym = st.checkbox('Go to gym')
book = st.checkbox('Book')

if work and gym and book:
    st.write('You did EVERYTHING :thumbsup:')
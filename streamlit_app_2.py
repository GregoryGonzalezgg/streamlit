import streamlit as st
from datetime import time,datetime

############################# EXEMPLO 1 #############################

st.header('st.slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write('Im', age, 'years old')

############################# EXEMPLO 2 #############################

st.subheader('Range slider')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

############################# EXEMPLO 3 #############################

st.subheader('Ranger time slider')

appoiment = st.slider(
    'Schedule your appoiment:',
    value = (time(11, 30), time(12, 45)))
st.write("You're schedule for:", appoiment)

############################# EXEMPLO 4 #############################

st.subheader('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value = datetime(2020, 1, 1, 9, 30),
    format = "MM/DD/YYYY - hh:mm")
st.write("Start time:", start_time)
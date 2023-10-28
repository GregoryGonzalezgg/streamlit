import streamlit as st
from datetime import time,datetime
import numpy as np
import pandas as pd

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

  ############################# AULA 3 #############################
############################# EXEMPLO 5 #############################

st.subheader('Line chart')

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

############################# EXEMPLO 6 #############################

st.subheader('st.selectbox')

option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Black', 'Green'))

st.write('Your favorite color is ', option)

############################# EXEMPLO 7 #############################

st.subheader('st.multiselect')

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow','Red'])

st.write('You select:', options)

############################# EXEMPLO 8 #############################

st.subheader('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great! Here's Some more")

if coffee:
    st.write("Pkay, here's some coffee")

if cola:
    st.write("Here you go")
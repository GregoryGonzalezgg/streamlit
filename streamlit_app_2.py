import streamlit as st
import time as tm
from datetime import datetime,time
import numpy as np
import pandas as pd
# import ydata_profiling
# from ydata_profiling import st


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

############################# EXEMPLO 9 #############################

# st.subheader('`streamlit_pandas_profiling`')

# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
# pr = df.profile_report()
# profile_report(pr)

############################# EXEMPLO 10 #############################

st.subheader('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

############################# EXEMPLO 11 #############################

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)


############################# EXEMPLO 12 #############################

# st.title('st.secrets')

# st.write(st.secrets['message'])

############################# EXEMPLO 13 #############################

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
else:
    st.info('☝️ Upload a CSV file')

############################# EXEMPLO 14 #############################

#st.set_page_config(layout= 'wide')

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
    st.write('This app shows the various ways on how you can layout your Streamlit app.')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)  

st.sidebar.header('Input') 
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')

############################# EXEMPLO 15 #############################
st.title('st.progress')

with st.expander('About this app'):
   st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)

for percent_complete in range(100):
   tm.sleep(0.05)
   my_bar.progress(percent_complete + 1)

st.balloons()

############################# EXEMPLO 16 #############################


st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')

    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)

############################# EXEMPLO 17 #############################

st.title('st.experimental_get_query_params')

with st.expander('About this app'):
   st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")


   #1 instructions

st.subheader('1 Instructions')
st.markdown('''In the above URL bar of your internet browser, append the following:
`?firstname=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')

# 2. Contents of st.experimental_get_query_params
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())


# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Hello **{firstname} {surname}**, how are you?')
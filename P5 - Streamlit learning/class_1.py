import streamlit as st

# Text/Title
st.title('Streamlit Tutorials')

# Header/Subheader
st.header('This is a header')
st.subheader('This is a subheader')

# Text
st.text('Hello Streamlit')

# Markdown
st.markdown('### This is a Markdown')

# Error/Colorful text
st.success('Successfull')
st.info('Information')
st.warning('This is a warning')
st.error('This is an error message')

st.exception('NameError("name three now defined")')

# Get Help info about Python
st.help(range)

# Writing text
st.write('Text with write function')
st.write(range(10))

# Images
from PIL import Image
img = Image.open('Elnur _sekil.jpg')
# st.image(img)
# st.image(img, width=300, caption='Simple image')

# Videos
# vid_file = open('example.mp4', 'rb').read()
# st.video(vid_file)

# Audio
# audio_file = open('examplemusic.mp3', 'rb').read()
# st.audio(audio_file, format='audio/mp3')

# Widget
# Checkbox
if st.checkbox('Show/Hide'):
    st.text('Showing or Hiding Widget')

# Radio
status = st.radio('What is the status', ('Active', 'Inactive'))

if status == 'Active':
    st.success('You are Active')
else:
    st.error('You are not Active')

# Select Box
occupation = st.selectbox('Your Occupation', ['Programmer', 'Data Scientist', 'Doctor', 'Engineer'])
st.write('You selected this option', occupation)

# MultiSelect Box
location = st.multiselect('Where do you work?', ('London', 'New York', 'Accra', 'Kiev', 'Baku'))
st.write('You selected ', len(location), ' locations')

# Slider
age = st.slider('What is your age?', min_value=1, max_value=100)

# Buttons
st.button('Simple Button')

if st.button('About'):
    st.text('Streamlit is cool')

# Text input
firstname = st.text_input('Enter your first name: ','Type here...')
lastname = st.text_input('Enter your last name:')
st.write(lastname)

if st.button('Submit'):
    result = firstname.title() + ' ' + lastname.title()
    st.success(result)

if st.button('Submit2'):
    result = firstname + ' ' + lastname
    st.success(result)

# Text Area
message = st.text_area('Enter your message')
if st.button('Submit3'):
    result = message.title()
    st.success(result)

# date input
import datetime
today = st.date_input('Today is', datetime.datetime.now())

# Time
time = st.time_input('Time is ', datetime.time())

# Displaying JSON
st.text('Display JSON')
st.json({'name': 'Jesse', 'gender': 'Jane'})

# Display Raw Code
st.text('Display Raw Code')
st.code('import numpy as np')

#Display Raw code
with st.echo():
    # This will also show as a comment
    import pandas as pd
    df = pd.DataFrame()

# Progress bar
import time
my_bar = st.progress(0)
for p in range(100):
    # time.sleep(0.1)
    my_bar.progress(p)

# Spinner
# with st.spinner('Waiting'):
#     time.sleep(0.1)
st.success('Finish')

# st.balloons()

# Sidebars
st.sidebar.header('About')
st.sidebar.text('This is Streamlit tutorial')

# Functions
@st.cache
def run_multiple():
    return range(100)
st.write(run_multiple())

# Plot
st.pyplot()

# Dataframes
st.dataframe(df)

# Tables
st.table(df)

st.
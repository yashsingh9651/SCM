import streamlit as st
import pandas as pd
import json

# Function to load data from JSON files
def load_data(file_name):
    return pd.read_json(file_name, orient='records', lines=True)

# Streamlit app
st.title('University Data Visualizer')

# Sidebar for file selection
st.sidebar.header('File Selection')
data_type = st.sidebar.selectbox('Select Data Type', [
    'Departments',
    'Courses',
    'Students',
    'Faculties',
    'Classes',
    'Labs',
    'Timetable',
    'Students ML',
    'Faculties ML',
    'Classes ML'
])

# Load and display data based on selection
if data_type == 'Departments':
    df = load_data('departments_timetable.json')
    st.header('Departments Data')
elif data_type == 'Courses':
    df = load_data('courses_timetable.json')
    st.header('Courses Data')
elif data_type == 'Students':
    df = load_data('students_timetable.json')
    st.header('Students Data')
elif data_type == 'Faculties':
    df = load_data('faculties_timetable.json')
    st.header('Faculties Data')
elif data_type == 'Classes':
    df = load_data('classes_timetable.json')
    st.header('Classes Data')
elif data_type == 'Labs':
    df = load_data('labs_timetable.json')
    st.header('Labs Data')
elif data_type == 'Timetable':
    df = load_data('timetable.json')
    st.header('Timetable Data')
elif data_type == 'Students ML':
    df = load_data('students_ml.json')
    st.header('Students ML Data')
elif data_type == 'Faculties ML':
    df = load_data('faculties_ml.json')
    st.header('Faculties ML Data')
elif data_type == 'Classes ML':
    df = load_data('classes_ml.json')
    st.header('Classes ML Data')

# Display the selected data
st.write(df)

# Optional: Add some charts for better visualization
if data_type in ['Students', 'Faculties', 'Classes']:
    st.subheader('Data Statistics')
    st.write(df.describe())

if data_type == 'Timetable':
    st.subheader('Timetable Analysis')
    st.write(df.groupby(['Day', 'Time']).size().reset_index(name='Count'))

if data_type == 'Students':
    st.subheader('CGPA Distribution')
    st.bar_chart(df['CGPA'].value_counts())

if data_type == 'Faculties':
    st.subheader('Faculty Positions Distribution')
    st.bar_chart(df['Position'].value_counts())

if data_type == 'Classes':
    st.subheader('Classroom Capacity Distribution')
    st.histogram(df['Capacity'])

# Run the Streamlit app
if __name__ == "__main__":
    st.run()

import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('creadentials.json', scope)

# Authenticate with Google Sheets
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open_by_key('1J2E14wqCu88P1H2atbJFbCUux67TR85P8RieFSr3v8g').worksheet("Sheet1")

# Streamlit app
st.title('CRUD App')

# Create
st.header('Create')
name = st.text_input('Name')
email = st.text_input('Email')
if st.button('Create'):
    sheet.append_row([name, email])

# Read
st.header('Read')
data = sheet.get_all_records()
st.write(data)

# Update
st.header('Update')
row_num = st.number_input('Row Number')
new_name = st.text_input('New Name')
new_email = st.text_input('New Email')
if st.button('Update'):
    sheet.update_cell(row_num, 1, new_name)
    sheet.update_cell(row_num, 2, new_email)

# Delete
st.header('Delete')
row_num = st.number_input('Row Number')
if st.button('Delete'):
    sheet.delete_row(row_num)
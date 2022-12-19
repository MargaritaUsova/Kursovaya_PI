import streamlit as st
from docx import Document
from bs4 import BeautifulSoup
import requests
import json 
from parser_gost import parser
import os


def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)


inputs = {"doc": filename}

if st.button('Parse'):
   res = requests.post(url = "http://127.0.0.1:8000/parser", data = json.dumps(inputs))
   st.subheader(res.text)



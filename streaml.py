import streamlit as st
from docx import Document
from bs4 import BeautifulSoup
import requests
from parser_gost import parser

#ocument = Document('TestKURS.docx')
#document.save('TestKURS.docx')


uploaded_file = st.file_uploader("Upload a file")

if uploaded_file:
   st.write("Filename: ", uploaded_file.name)

result = parser(uploaded_file)
st.write("Результат: ")
st.write(result)



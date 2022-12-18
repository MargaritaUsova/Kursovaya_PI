import streamlit as st
import requests
import os.path
import pathlib

if st.button('Загрузить файл'):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        data = uploaded_file.getvalue().decode('utf8')
        path_1 = pathlib.Path(__file__).parent.parent.resolve()
        path  = os.path.join(path_1, "data")
        fullname = os.path.join(path, uploaded_file.name)

        pathfile = open(fullname, "w")
        pathfile.write(data)
        pathfile.close()





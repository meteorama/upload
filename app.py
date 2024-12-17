import streamlit as st
import os
from glob import glob



st.title("Quick File Share")

uploaded_file = st.file_uploader("Choose a file to upload")

if uploaded_file is not None:
    bytes_data = uploaded_file.read()

    with open(os.path.join(os.getcwd(),"files",uploaded_file.name),"wb") as f:
        f.write(uploaded_file.getbuffer())
        st.success("File Uploaded")

st.header("Available Files")

files_list = glob(os.path.join(os.getcwd(),"files","*.*"))

for file in files_list:
    with open(file, 'rb') as f:
        st.download_button('Download {}'.format(os.path.basename(file)), f, file_name=os.path.basename(file))


if st.button("Delete All Files"):
    files_list = glob(os.path.join(os.getcwd(),"files","*.*"))
    for f in files_list:
        if(os.path.exists(f)):
            os.remove(f)
    st.info("All files deleted!!! Refresh the page to see changes.")


st.caption("Manaruchi Mohapatra")

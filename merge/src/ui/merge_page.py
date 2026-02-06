import streamlit as st
import zipfile
import io
from merge_csv import merge_csv_files

def merge():
    st.title('CSV Merger')
    uploaded_files = st.file_uploader('Upload CSV files to merge',
                                      type=['csv'],
                                      accept_multiple_files=True
                                      )

    if st.button('Merge Files'):
        if not uploaded_files:
            st.warning('Please upload at least one CSV file to merge.')
            return
        
        with st.spinner('Merging files...'):
            merged_files = merge_csv_files(uploaded_files)                      #Merges uploaded csv files
        
        st.success('Files merged successfully!')

        zip_buffer = io.BytesIO()                           
        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
            for file_path in merged_files:
                zip_file.write(file_path, arcname=file_path.split('/')[-1])     #Converts merged files to zip file
        
        zip_buffer.seek(0)

        st.download_button("Download merged files as ZIP",                      #Downloads zip file
                           data=zip_buffer,
                           file_name="merged_csv_files.zip",
                           mime="application/zip")
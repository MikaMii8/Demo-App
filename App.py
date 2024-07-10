# pip install streamlit
# pip install openpyxl # for excel files

import streamlit as st
import pandas as pd

st.title('DataFrame Upload and Visualization')

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the file
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        st.success("File uploaded successfully")

        # Display the dataframe
        st.write("DataFrame:")
        st.dataframe(df)

        # Plotting (example: displaying a bar chart)
        if st.checkbox('Show Bar Chart'):
            st.bar_chart(df.select_dtypes(include=['float', 'int']).head())

    except Exception as e:
        st.error(f"Error: {e}")

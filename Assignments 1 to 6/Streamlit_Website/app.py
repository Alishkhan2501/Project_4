import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Weather Data Analyzer")

# File uploader to upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

# If a file is uploaded
if uploaded_file is not None:
    # Read the uploaded CSV
    df = pd.read_csv(uploaded_file)

    # Show a preview of the data
    st.subheader("Data Preview")
    st.write(df.head())
    
    # Show data summary
    st.subheader("Data Summary")
    st.write(df.describe())

    # Get columns for filtering
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    
    # Get unique values of selected column
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)
    
    # Filter data based on selection
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)
    
    # Apply the new gradient background
    gradient_style = """
        <style>
            .stApp {
                background: rgb(163,245,237);
                background: linear-gradient(90deg, rgba(163,245,237,1) 0%, rgba(20,124,199,1) 51%, rgba(238,241,233,1) 100%);
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                min-height: 100vh;  /* Ensure the background covers the entire page */
            }
        </style>
    """
    st.markdown(gradient_style, unsafe_allow_html=True)

    # Plot Data section
    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting on file upload...")
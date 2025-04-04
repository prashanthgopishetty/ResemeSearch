# import streamlit as st


# def show():
#     st.title("ℹ️ Resume Processor")
    
#     res = scan_resumes.process_resumes()
#     st.write(res)

import streamlit as st
import pandas as pd
import scan_resumes
import json
def show():
    # Set page title and layout
    # st.set_page_config(page_title="Dynamic Table Display", layout="centered")

    # Panel area below to display table dynamically
    st.write("---")  # Horizontal line for separation
    st.subheader("Resume Info")

    # Create two horizontally aligned buttons
    col1, col2 = st.columns(2)

    with col1:
        btn1 = st.button("Show Data 1")

    with col2:
        btn2 = st.button("Show Data 2")



    # Sample data for tables
    data1 = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"]
    })

    data2 = pd.DataFrame({
        "Product": ["Laptop", "Phone", "Tablet"],
        "Price ($)": [1000, 500, 300],
        "Stock": [10, 50, 30]
    })




    # Display table based on button click
    if btn1:
        res = scan_resumes.process_resumes()
        df = pd.DataFrame(res)

        # Column configuration (Skill Set is given a fixed width)
        column_config = {
            "Name": st.column_config.TextColumn("Name", width="small"),
            "Location": st.column_config.TextColumn("Location", width="small"),
            "Phone Number": st.column_config.TextColumn("Phone Number", width="small"),
            "Skill Set": st.column_config.TextColumn("Skill Set", width="large")  # Reduce width of Skill Set
        }

        # Display dataframe with custom column widths
        st.dataframe(df, column_config=column_config)
    elif btn2:
        st.table(data2)  # Show second table
    


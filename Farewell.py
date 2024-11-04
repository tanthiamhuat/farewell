# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

# App title
st.title("Farewell Message Generator")

# Input fields
st.subheader("Enter Farewell Details")

# Input for the person's name
name = st.text_input("Name of the departing colleague:")

# Input for the department
department = st.text_input("Department:")

# Input for years of service
years_of_service = st.number_input("Years of Service:", min_value=0, max_value=50, step=1)

# Input for a custom message
custom_message = st.text_area("Your custom farewell message:")

# Generate Farewell Button
if st.button("Generate Farewell Message"):
    # If all fields are filled out, generate the message
    if name and department and custom_message:
        # Display the farewell message
        st.write("🎉 **Farewell Message** 🎉")
        st.write(f"**Dear {name},**")
        st.write(f"Thank you for your {years_of_service} years of dedicated service to the {department} department.")
        st.write(f"{custom_message}")
        st.write("We will miss you and wish you all the best in your future endeavors!")
    else:
        st.warning("Please fill out all fields to generate the farewell message.")

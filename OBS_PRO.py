import streamlit as st

# Define the correct password
correct_password = "1234"  # Replace "your_password_here" with your actual password

# Display a text input box for the user to enter the password
password_input = st.text_input("Enter the password:", type="password")

# Check if the entered password matches the correct password
if password_input == correct_password:
    st.title("TITLE")

    # Display the embedded content only if the correct password is entered
    st.markdown('''
    <body>
    <iframe src="https://app.powerbi.com/view?r=eyJrIjoiNzI5ZWM3NWEtZTRjZS00ZjU4LTkwNTAtZWFlYzk0M2ZhNTc0IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" title="Embedded Page" style="width: 100%; height: 100vh; border: none;"></iframe>
    </body>
    ''', unsafe_allow_html=True)
else:
    st.error("Incorrect password. Please try again.")

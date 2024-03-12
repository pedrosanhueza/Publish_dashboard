import streamlit as st

st.title("TITLE")

st.markdown('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <style>
    iframe {
      width: 100%;
      height: 100vh; /* You can adjust the height as needed */
      border: none; /* Remove iframe border */
    }
  </style>
</head>
            
<body>

<iframe src="https://app.powerbi.com/view?r=eyJrIjoiNzI5ZWM3NWEtZTRjZS00ZjU4LTkwNTAtZWFlYzk0M2ZhNTc0IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" title="Embedded Page"></iframe>

</body>
</html>
            ''', unsafe_allow_html=True)
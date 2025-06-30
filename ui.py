# import streamlit as st
# import requests
# import os
# from PIL import Image

# st.set_page_config(page_title="Virtual Try-On", layout="wide")
# st.title("👕 Virtual Try-On System")

# col1, col2 = st.columns(2)

# with col1:
#     st.subheader("Upload Images")
#     person_file = st.file_uploader("Upload Person Image", type=["jpg", "png"])
#     cloth_file = st.file_uploader("Upload Clothing Image", type=["jpg", "png"])

# if st.button("Try On"):
#     if not person_file or not cloth_file:
#         st.warning("Please upload both images.")
#     else:
#         with st.spinner("Processing..."):
#             files = {
#                 "person": person_file.getvalue(),
#                 "cloth": cloth_file.getvalue()
#             }
#             response = requests.post("http://127.0.0.1:5000/process", files=files)

#             if response.status_code == 200:
#                 output_path = response.json()["output"]
#                 with col2:
#                     st.subheader("Result")
#                     st.image(output_path, caption="Try-On Output")
#             else:
#                 st.error("Error processing images.")

# st.sidebar.markdown("📌 Make sure Flask backend is running before using this UI!")
import torch
print(torch.__version__)
print(torch.version.cuda)
print(torch.cuda.is_available())

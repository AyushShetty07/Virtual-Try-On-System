


# import streamlit as st
# import os
# import subprocess
# from PIL import Image

# # Define directories
# DATASET_DIR = "./datasets/test/"
# PAIR_FILE = "./datasets/test_pairs.txt"
# RESULTS_DIR = "./results/"
# PERSON_DIR = os.path.join(DATASET_DIR, "image/")   # Folder for person images
# CLOTH_DIR = os.path.join(DATASET_DIR, "cloth/")    # Folder for clothing images

# # Custom Labels for Clothing Items (Modified names)
# custom_labels = {
#     "cloth1.jpg": "Red Dress",
#     "cloth2.jpg": "Blue Jeans",
#     "cloth3.jpg": "Black Jacket",
#     "cloth4.jpg": "White Top",
#     "cloth5.jpg": "Green Blazer",
#     "cloth6.jpg": "Pink Sweater"
# }

# # Custom Labels for Person Images (Modified names)
# person_labels = {
#     "girl1.jpg": "Girl 1",
#     "girl2.jpg": "Girl 2",
#     "girl3.jpg": "Girl 3",
#     "girl4.jpg": "Girl 4",
#     "girl5.jpg": "Girl 5"
# }

# # Streamlit UI
# st.set_page_config(page_title="Virtual Try-On", layout="wide")
# st.title("👕 Virtual Try-On System 🧥")
# st.write("🔹 Select a **Person Image** and a **Clothing Item** to generate a try-on result.")

# # Load available images
# person_images = [f for f in os.listdir(PERSON_DIR) if f.endswith(("jpg", "png"))]
# cloth_images = [f for f in os.listdir(CLOTH_DIR) if f.endswith(("jpg", "png"))]

# # Custom function to format clothing names
# def format_label(filename):
#     return custom_labels.get(filename, filename.split(".")[0].replace("_", " ").title())

# # Custom function to format person names
# def format_person_label(filename):
#     return person_labels.get(filename, filename.split(".")[0].replace("_", " ").title())

# # ---- Person Image Selection ----
# st.subheader("👤 Select a Person Image")
# selected_person = st.selectbox("", person_images, format_func=lambda x: format_person_label(x))

# # Display person images in a grid
# cols = st.columns(5)  # Adjust grid size
# for i, person in enumerate(person_images):
#     with cols[i % 5]:  # Arrange images in rows
#         st.image(os.path.join(PERSON_DIR, person), caption=format_person_label(person), use_container_width=True)

# # ---- Clothing Image Selection ----
# st.subheader("👗 Select a Clothing Item")
# selected_cloth = st.selectbox("", cloth_images, format_func=format_label)

# # Display clothing images in a grid
# cols = st.columns(5)
# for i, cloth in enumerate(cloth_images):
#     with cols[i % 5]:
#         st.image(os.path.join(CLOTH_DIR, cloth), caption=format_label(cloth), use_container_width=True)

# # ---- Generate Button ----
# st.markdown("---")
# st.markdown("<h3 style='text-align: center;'>✨ Click to Generate Try-On Image ✨</h3>", unsafe_allow_html=True)
# btn_col = st.columns([1, 2, 1])  # Center the button
# with btn_col[1]:
#     generate_btn = st.button("🚀 Generate Try-On", use_container_width=True)

# # ---- Processing & Display Result ----
# if generate_btn:
#     with open(PAIR_FILE, "w") as f:
#         f.write(f"{selected_person} {selected_cloth}\n")

#     with st.spinner("🛠️ Processing your Try-On... Please wait!"):
#         subprocess.run(["python", "test.py", "--name", "streamlit_tryon", "--dataset_list", "test_pairs.txt"])

#     # Display Result
#     output_image_path = os.path.join(RESULTS_DIR, "streamlit_tryon", f"{selected_person.split('_')[0]}_{selected_cloth}")

#     if os.path.exists(output_image_path):
#         st.success("✅ Try-On Completed Successfully!")
#         st.image(Image.open(output_image_path), caption="✨ Generated Try-On Image", use_container_width=True)
#     else:
#         st.error("⚠️ Try-On failed. Check test.py for errors.")


import streamlit as st
import os
import subprocess
from PIL import Image

# Define directories
DATASET_DIR = "./datasets/test/"
PAIR_FILE = "./datasets/test_pairs.txt"
RESULTS_DIR = "./results/"
PERSON_DIR = os.path.join(DATASET_DIR, "image/")   # Folder for person images
CLOTH_DIR = os.path.join(DATASET_DIR, "cloth/")    # Folder for clothing images

# Custom Labels for Clothing Items (Modified names)
custom_labels = {
    "cloth1.jpg": "Red Dress",
    "cloth2.jpg": "Blue Jeans",
    "cloth3.jpg": "Black Jacket",
    "cloth4.jpg": "White Top",
    "cloth5.jpg": "Green Blazer",
    "cloth6.jpg": "Pink Sweater"
}

# Custom Labels for Person Images (Modified names)
person_labels = {
    "girl1.jpg": "Girl 1",
    "girl2.jpg": "Girl 2",
    "girl3.jpg": "Girl 3",
    "girl4.jpg": "Girl 4",
    "girl5.jpg": "Girl 5"
}

# Streamlit UI
st.set_page_config(page_title="Virtual Try-On", layout="wide")
st.title("👕 Virtual Try-On System 🧥")
st.write("🔹 Select a **Person Image** and a **Clothing Item** to generate a try-on result.")

# Load available images
person_images = [f for f in os.listdir(PERSON_DIR) if f.endswith(("jpg", "png"))]
cloth_images = [f for f in os.listdir(CLOTH_DIR) if f.endswith(("jpg", "png"))]

# Custom function to format clothing names
def format_label(filename):
    return custom_labels.get(filename, filename.split(".")[0].replace("_", " ").title())

# Custom function to format person names
def format_person_label(filename):
    return person_labels.get(filename, filename.split(".")[0].replace("_", " ").title())

# ---- Person Image Selection ----
st.subheader("👤 Select a Person Image")
selected_person = st.selectbox("", person_images, format_func=lambda x: format_person_label(x))

# Display person images in a grid
cols = st.columns(5)  # Adjust grid size
for i, person in enumerate(person_images):
    with cols[i % 5]:  # Arrange images in rows
        st.image(os.path.join(PERSON_DIR, person), caption=format_person_label(person), width=150)

# ---- Clothing Image Selection ----
st.subheader("👗 Select a Clothing Item")
selected_cloth = st.selectbox("", cloth_images, format_func=format_label)

# Display clothing images in a grid
cols = st.columns(5)
for i, cloth in enumerate(cloth_images):
    with cols[i % 5]:
        st.image(os.path.join(CLOTH_DIR, cloth), caption=format_label(cloth), width=150)

# ---- Generate Button ----
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>✨ Click to Generate Try-On Image ✨</h3>", unsafe_allow_html=True)
btn_col = st.columns([1, 2, 1])  # Center the button
with btn_col[1]:
    generate_btn = st.button("🚀 Generate Try-On", use_container_width=True)

# ---- Processing & Display Result ----
if generate_btn:
    with open(PAIR_FILE, "w") as f:
        f.write(f"{selected_person} {selected_cloth}\n")

    with st.spinner("🛠️ Processing your Try-On... Please wait!"):
        subprocess.run(["python", "test.py", "--name", "streamlit_tryon", "--dataset_list", "test_pairs.txt"])

    # Display Result
    output_image_path = os.path.join(RESULTS_DIR, "streamlit_tryon", f"{selected_person.split('_')[0]}_{selected_cloth}")

    if os.path.exists(output_image_path):
        st.success("✅ Try-On Completed Successfully!")
        st.image(Image.open(output_image_path), caption="✨ Generated Try-On Image", width=400)
    else:
        st.error("⚠️ Try-On failed. Check test.py for errors.")
# import streamlit as st
# import os
# import subprocess
# from PIL import Image

# # Define directories
# DATASET_DIR = "./datasets/test/"
# PAIR_FILE = "./datasets/test_pairs.txt"
# RESULTS_DIR = "./results/"
# PERSON_DIR = os.path.join(DATASET_DIR, "image/")
# CLOTH_DIR = os.path.join(DATASET_DIR, "cloth/")

# # Custom labels
# custom_labels = {
#     "cloth1.jpg": "Red Dress",
#     "cloth2.jpg": "Blue Jeans",
#     "cloth3.jpg": "Black Jacket",
#     "cloth4.jpg": "White Top",
#     "cloth5.jpg": "Green Blazer",
#     "cloth6.jpg": "Pink Sweater"
# }

# person_labels = {
#     "girl1.jpg": "Girl 1",
#     "girl2.jpg": "Girl 2",
#     "girl3.jpg": "Girl 3",
#     "girl4.jpg": "Girl 4",
#     "girl5.jpg": "Girl 5"
# }

# # Streamlit UI config
# st.set_page_config(page_title="Virtual Try-On", layout="wide")
# st.title("👕 Virtual Try-On System 🧥")
# st.write("🔹 Select a **Person** and a **Garment** to generate a virtual try-on result.")

# # Load image filenames
# person_images = sorted([f for f in os.listdir(PERSON_DIR) if f.endswith(("jpg", "png"))])
# cloth_images = sorted([f for f in os.listdir(CLOTH_DIR) if f.endswith(("jpg", "png"))])

# # ---- Person Selection ----
# st.subheader("👤 Select a Person Image")
# person_labels_list = [person_labels.get(p, p) for p in person_images]
# selected_person_label = st.radio("Choose a person:", person_labels_list, horizontal=True)
# selected_person = person_images[person_labels_list.index(selected_person_label)]

# # Show selected person image
# st.image(os.path.join(PERSON_DIR, selected_person), caption=f"👤 {selected_person_label}", width=200)

# # ---- Cloth Selection ----
# st.subheader("👗 Select a Clothing Item")
# cloth_labels_list = [custom_labels.get(c, c) for c in cloth_images]
# selected_cloth_label = st.radio("Choose a clothing item:", cloth_labels_list, horizontal=True)
# selected_cloth = cloth_images[cloth_labels_list.index(selected_cloth_label)]

# # Show selected clothing image
# st.image(os.path.join(CLOTH_DIR, selected_cloth), caption=f"👗 {selected_cloth_label}", width=200)

# # ---- Generate Try-On ----
# st.markdown("---")
# st.markdown("<h3 style='text-align: center;'>✨ Click to Generate Try-On Image ✨</h3>", unsafe_allow_html=True)
# btn_col = st.columns([1, 2, 1])
# with btn_col[1]:
#     generate_btn = st.button("🚀 Generate Try-On", use_container_width=True)

# # ---- Processing ----
# if generate_btn:
#     if not selected_person or not selected_cloth:
#         st.error("⚠️ Please select both a person image and a clothing item.")
#     else:
#         with open(PAIR_FILE, "w") as f:
#             f.write(f"{selected_person} {selected_cloth}\n")

#         with st.spinner("🛠️ Processing your Try-On... Please wait!"):
#             subprocess.run(["python", "test.py", "--name", "streamlit_tryon", "--dataset_list", "test_pairs.txt"])

#         # Check and display result
#         output_image_path = os.path.join(RESULTS_DIR, "streamlit_tryon", f"{selected_person.split('_')[0]}_{selected_cloth}")
#         if os.path.exists(output_image_path):
#             st.success("✅ Try-On Completed Successfully!")
#             st.image(Image.open(output_image_path), caption="✨ Generated Try-On Image", width=400)
#         else:
#             st.error("⚠️ Try-On failed. Check the test.py output.")

# import streamlit as st
# import os
# import subprocess
# from PIL import Image
# import torch

# # Define directories
# DATASET_DIR = "./datasets/test/"
# PAIR_FILE = "./datasets/test_pairs.txt"
# RESULTS_DIR = "./results/"
# PERSON_DIR = os.path.join(DATASET_DIR, "image/")
# CLOTH_DIR = os.path.join(DATASET_DIR, "cloth/")

# # Custom Labels for Clothing Items
# custom_labels = {
#     "cloth1.jpg": "Red Dress",
#     "cloth2.jpg": "Blue Jeans",
#     "cloth3.jpg": "Black Jacket",
#     "cloth4.jpg": "White Top",
#     "cloth5.jpg": "Green Blazer",
#     "cloth6.jpg": "Pink Sweater"
# }

# # Custom Labels for Person Images
# person_labels = {
#     "girl1.jpg": "Girl 1",
#     "girl2.jpg": "Girl 2",
#     "girl3.jpg": "Girl 3",
#     "girl4.jpg": "Girl 4",
#     "girl5.jpg": "Girl 5"
# }

# # Streamlit UI
# st.set_page_config(page_title="Virtual Try-On", layout="wide")
# st.title("👕 Virtual Try-On System 🧥")
# st.write("🔹 Select a **Person Image** and a **Clothing Item** to generate a try-on result.")

# # Load available images
# person_images = [f for f in os.listdir(PERSON_DIR) if f.endswith(("jpg", "png"))]
# cloth_images = [f for f in os.listdir(CLOTH_DIR) if f.endswith(("jpg", "png"))]

# def format_label(filename):
#     return custom_labels.get(filename, filename.split(".")[0].replace("_", " ").title())

# def format_person_label(filename):
#     return person_labels.get(filename, filename.split(".")[0].replace("_", " ").title())

# # ---- Person Image Selection ----
# st.subheader("👤 Select a Person Image")
# selected_person = st.selectbox("", person_images, format_func=format_person_label)

# cols = st.columns(5)
# for i, person in enumerate(person_images):
#     with cols[i % 5]:
#         st.image(os.path.join(PERSON_DIR, person), caption=format_person_label(person), width=150)

# # ---- Clothing Image Selection ----
# st.subheader("👗 Select a Clothing Item")
# selected_cloth = st.selectbox("", cloth_images, format_func=format_label)

# cols = st.columns(5)
# for i, cloth in enumerate(cloth_images):
#     with cols[i % 5]:
#         st.image(os.path.join(CLOTH_DIR, cloth), caption=format_label(cloth), width=150)

# # ---- Generate Button ----
# st.markdown("---")
# st.markdown("<h3 style='text-align: center;'>✨ Click to Generate Try-On Image ✨</h3>", unsafe_allow_html=True)
# btn_col = st.columns([1, 2, 1])
# with btn_col[1]:
#     generate_btn = st.button("🚀 Generate Try-On", use_container_width=True)

# # ---- Processing & Display Result ----
# if generate_btn:
#     with open(PAIR_FILE, "w") as f:
#         f.write(f"{selected_person} {selected_cloth}\n")

#     with st.spinner("🛠️ Processing your Try-On... Please wait!"):
#         subprocess.run(["python", "test.py", "--name", "streamlit_tryon", "--dataset_list", "test_pairs.txt"])

#     output_image_path = os.path.join(RESULTS_DIR, "streamlit_tryon", f"{selected_person.split('_')[0]}_{selected_cloth}")

#     if os.path.exists(output_image_path):
#         st.success("✅ Try-On Completed Successfully!")
#         image = Image.open(output_image_path)
#         st.image(image, caption="✨ Generated Try-On Image", width=400)

#         # ---- Download Button ----
#         with open(output_image_path, "rb") as img_file:
#             st.download_button(
#                 label="⬇️ Download Your Try-On Look",
#                 data=img_file,
#                 file_name="tryon_result.jpg",
#                 mime="image/jpeg"
#             )

#         # ---- Share Section ----
#         st.markdown("### 📲 Share Your Look!")
#         st.write("Share your look on social media:")

#         twitter_url = f"https://twitter.com/intent/tweet?text=Check%20out%20my%20virtual%20try-on%20look!%20%23VirtualTryOn"
#         facebook_url = f"https://www.facebook.com/sharer/sharer.php?u=https://your-app-url"

#         col1, col2 = st.columns(2)
#         with col1:
#             st.markdown(f"[🐦 Share on Twitter]({twitter_url})", unsafe_allow_html=True)
#         with col2:
#             st.markdown(f"[📘 Share on Facebook]({facebook_url})", unsafe_allow_html=True)
#     else:
#         st.error("⚠️ Try-On failed. Check test.py for errors.")

import streamlit as st
from PIL import Image
import zipfile
import io

st.set_page_config(page_title="Hand Gesture Classification App", layout="centered")

st.markdown(
    """
    # ✋ Hand Gesture Classification App
    Upload a gesture image or a ZIP file containing images in subfolders (A to Z).
    """
)

uploaded_file = st.file_uploader("Upload a gesture image or ZIP file", type=["jpg", "jpeg", "png", "zip"])

def extract_images_from_nested_zip(zip_file):
    images = []
    try:
        with zipfile.ZipFile(zip_file) as z:
            for file_name in z.namelist():
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg')) and not file_name.endswith('/'):
                    try:
                        with z.open(file_name) as image_file:
                            image = Image.open(image_file)
                            images.append((file_name, image.copy()))  # avoid lazy loading issues
                            image.close()
                    except Exception as e:
                        st.warning(f"⚠️ Skipped file `{file_name}` due to error: {e}")
    except zipfile.BadZipFile:
        st.error("❌ Invalid ZIP file. Please upload a valid ZIP.")
    return images

if uploaded_file is not None:
    if uploaded_file.name.endswith(".zip"):
        images = extract_images_from_nested_zip(uploaded_file)
        if not images:
            st.error("❌ No valid images found in the ZIP file.")
        else:
            st.success(f"✅ Found {len(images)} valid images!")
            for file_name, img in images:
                st.image(img, caption=file_name, use_column_width=True)
    else:
        try:
            image = Image.open(uploaded_file)
            st.success("✅ Image uploaded successfully!")
            st.image(image, caption=uploaded_file.name, use_column_width=True)
        except Exception as e:
            st.error(f"❌ Unable to load image: {e}")

import streamlit as st
import cv2
import numpy as np

# Function to apply filters
def apply_filter(image, filter_type, blur_param=None):
    if filter_type == 'Gray':
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'Blur':
        # Ensure blur_param is odd
        blur_param = blur_param if blur_param % 2 != 0 else blur_param + 1
        return cv2.GaussianBlur(image, (blur_param, blur_param), 0)
    elif filter_type == 'Edge':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# Streamlit App
def main():
    st.title("Image Filters App")

    # Upload Image
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Read image
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)

        # Convert BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Display original image
        original_image_loc = st.image(image_rgb, caption="Original Image", use_column_width=True)

        # Select filter
        filter_type = st.selectbox("Select Filter", ["None", "Gray", "Blur", "Edge"])

        if filter_type == 'Blur':
            # Get blur parameter from user
            blur_param = st.slider("Select Blur Parameter", 1, 10, 3)
        else:
            blur_param = None

        # Apply selected filter
        if filter_type != 'None':
            filtered_image = apply_filter(image, filter_type, blur_param)
            filtered_image_rgb = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)
            # Update original image location with filtered image
            original_image_loc.image(filtered_image_rgb, caption=f"{filter_type} Filtered Image", use_column_width=True)

if __name__ == '__main__':
    main()

import streamlit as st
import os
import numpy as np                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

model = load_model('image_classifier_model.h5')

class_labels = ['people', 'landscape', 'buildings', 'animals', 'documents']

def predict_image(img_path):

    img = Image.open(img_path).convert('RGB') 
    img = img.resize((150, 150)) 
    img_array = np.array(img) / 255.0  
    img_array = np.expand_dims(img_array, axis=0) 
    
    prediction = model.predict(img_array)
    predicted_class = class_labels[np.argmax(prediction)]
    
    return predicted_class

def process_uploaded_images(uploaded_files):

    for uploaded_file in uploaded_files:

        img_path = os.path.join('temp', uploaded_file.name)
        os.makedirs('temp', exist_ok=True)
        with open(img_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())

        predicted_class = predict_image(img_path)

        st.image(img_path, caption=f"Uploaded Image: {uploaded_file.name}", use_column_width=True)
        st.write(f"Predicted Class: {predicted_class}")
        
        target_dir = os.path.join('sorted_pics', predicted_class)
        os.makedirs(target_dir, exist_ok=True)
        
        new_img_path = os.path.join(target_dir, uploaded_file.name)
        os.rename(img_path, new_img_path)
        
        st.write(f"Image saved to: {new_img_path}")

st.title("Image Classification and Sorting")
st.write("Upload a folder of images or single images for classification.")

uploaded_files = st.file_uploader("Choose Images", accept_multiple_files=True)

if uploaded_files:
    process_uploaded_images(uploaded_files)


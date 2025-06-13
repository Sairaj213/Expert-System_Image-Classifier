# Image Classifier Project

This project trains an image classifier to categorize images into predefined classes (e.g., people, landscape, buildings, animals, documents). It uses a pre-trained ResNet18 model fine-tuned on a custom dataset and provides a Streamlit interface for easy interaction.

## Project Structure

```markdown-tree
image_classifier/
├── data/                 # Your image data (organized into class folders)
│   ├── people/
│   ├── landscape/
│   ├── buildings/
│   ├── animals/
│   ├── documents/
│   └── ...
├── sorted_pics/          # Output folder for classified images
├── data_preparation.py   # Preprocesses and splits the data
├── model_training.py     # Trains the model
├── app.py                # Streamlit interface
└── README.md             # Project documentation
```
## Description

- `data/` - Contains training data, organized into class folders.
- `sorted_pics/` - Stores the images after classification.
- `data_preparation.py` - Prepares and splits the dataset for training.
- `model_training.py` - Defines and trains the image classification model.
- `app.py` - Provides a user-friendly Streamlit interface for classification.
- `README.md` - Documentation for the project.

## Setup and Usage

### 1. Clone the Repository
```bash
https://github.com/Sairaj213/Expert-System_Image-Classifier.git
cd image_classifier
```

### 2. Create and Organize Your Data
Create a `data/` directory and subdirectories for each image category (e.g., `data/people`, `data/landscape`, etc.). Place your images into the corresponding folders.

### 3. Data Preparation
Run `data_preparation.py` to preprocess and split your data into training, validation, and test sets.
```bash
python data_preparation.py --data_dir data/  # Adjust data_dir if needed
```

### 4. Model Training
Train the model using `model_training.py`. This script loads the preprocessed data, fine-tunes a ResNet18 model, and saves the trained model.
```bash
python model_training.py --num_classes <number_of_classes> --device <cpu or cuda>  # Replace placeholders accordingly
```

### 5. Streamlit App (For Folder/Multiple Image Classification)
Run the Streamlit app to classify images from a folder or upload individual images.
```bash
streamlit run app.py
```
The app allows you to upload a folder of images or individual images. It will then classify the images and organize them into subfolders within the `sorted_pics/` directory.

## Customization

- **Pre-trained Model**: Modify `model_training.py` to use a different pre-trained model (e.g., EfficientNet, MobileNet).
- **Data Augmentation**: Enhance `data_preparation.py` by adding data augmentation techniques to improve model robustness.
- **Hyperparameters**: Adjust parameters such as learning rate, batch size, and number of epochs in `model_training.py`.
- **Streamlit Interface**: Customize `app.py` to modify the Streamlit interface.

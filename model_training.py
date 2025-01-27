import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

def create_model(input_shape=(150, 150, 3), num_classes=5):

    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model(train_dir, val_dir, input_shape=(150, 150, 3), batch_size=32, epochs=10):

    train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=20, width_shift_range=0.2,
                                      height_shift_range=0.2, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    val_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(train_dir, target_size=input_shape[:2],
                                                        batch_size=batch_size, class_mode='categorical')
    val_generator = val_datagen.flow_from_directory(val_dir, target_size=input_shape[:2],
                                                    batch_size=batch_size, class_mode='categorical')

    model = create_model(input_shape=input_shape, num_classes=len(train_generator.class_indices))
    
    history = model.fit(train_generator, epochs=epochs, validation_data=val_generator)

    model.save('image_classifier_model.h5')
    print("Model training complete and saved as 'image_classifier_model.h5'.")

train_directory = input("Enter the path to your training data directory: ")
val_directory = input("Enter the path to your validation data directory: ")

train_model(train_directory, val_directory)

import os
import shutil
import random

def organize_data(source_dir, target_dir, train_ratio=0.8):
    categories = os.listdir(source_dir)
    
    train_dir = os.path.join(target_dir, 'train')
    val_dir = os.path.join(target_dir, 'val')
    
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    
    for category in categories:
        category_path = os.path.join(source_dir, category)
        if os.path.isdir(category_path):
            os.makedirs(os.path.join(train_dir, category), exist_ok=True)
            os.makedirs(os.path.join(val_dir, category), exist_ok=True)
            images = [f for f in os.listdir(category_path) if os.path.isfile(os.path.join(category_path, f))]
            random.shuffle(images)
            
            split_index = int(len(images) * train_ratio)
            train_images = images[:split_index]
            val_images = images[split_index:]
            
            for image in train_images:
                shutil.move(os.path.join(category_path, image), os.path.join(train_dir, category, image))
                
            for image in val_images:
                shutil.move(os.path.join(category_path, image), os.path.join(val_dir, category, image))

    print(f"Data organized into {train_dir} and {val_dir}.")

source_directory = r'C:\Users\saira\Downloads\Lang\IMG'
target_directory = r'C:\Users\saira\Downloads\Lang'
organize_data(source_directory, target_directory)

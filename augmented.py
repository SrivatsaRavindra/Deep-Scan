import os
import random
import cv2
import imgaug.augmenters as iaa
import numpy as np

def augment_images(source_folder, destination_folder, total_augmented_images):
    os.makedirs(destination_folder, exist_ok=True)
    image_files = [f for f in os.listdir(source_folder) if f.endswith(('jpg', 'jpeg', 'png'))]
    
    if not image_files:
        print("No images found in source folder.")
        return
    
    # Define augmentation techniques
    augmenters = [
        iaa.Multiply((0.5, 1.5)),  # Change brightness
        iaa.GaussianBlur(sigma=(0.0, 3.0)),  # Apply Gaussian blur
        iaa.AdditiveGaussianNoise(scale=(10, 50)),  # Add noise
        iaa.Affine(rotate=(-30, 30)),  # Rotate
        iaa.Fliplr(0.5),  # Flip horizontally
        iaa.Flipud(0.5),  # Flip vertically
        iaa.Affine(scale=(0.8, 1.2)),  # Scale (zoom in/out)
        iaa.Sharpen(alpha=(0.0, 1.0), lightness=(0.75, 1.5))  # Sharpen
    ]
    
    count = 0
    while count < total_augmented_images:
        img_name = random.choice(image_files)  # Randomly pick an image
        img_path = os.path.join(source_folder, img_name)
        image = cv2.imread(img_path)
        
        if image is None:
            continue
        
        augmenter = random.choice(augmenters)  # Randomly pick an augmentation
        augmented_img = augmenter.augment_image(image)
        
        augmented_name = f"aug_{count:05d}_{img_name}"  # Unique filename
        save_path = os.path.join(destination_folder, augmented_name)
        cv2.imwrite(save_path, augmented_img)
        
        count += 1
    
    print(f"Successfully generated {total_augmented_images} augmented images.")

if __name__ == "__main__":
    source_folder = r"/home/sanjana-r/Desktop/Dataset/train/F1"  # Replace with actual path
    destination_folder = r"/home/sanjana-r/Desktop/Dataset/train/F"  # Replace with actual path
    total_augmented_images = 10000
    augment_images(source_folder, destination_folder, total_augmented_images)


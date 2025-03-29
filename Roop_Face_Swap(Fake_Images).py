import os
import random
import subprocess

# Set paths
MAIN_FOLDER = r"C:\roop\Dataset\daily soap Cropped"  # Folder containing all subfolders with images
OUTPUT_FOLDER = r"C:\roop\Dataset\fake\Daily_soap"  # Output directory where results will be saved
NUM_TARGET_IMAGES = 10  # Number of target images to randomly select from each target folder

def get_images(folder):
    """Returns a list of image file paths in a folder."""
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith((".jpg", ".png", ".jpeg"))]

def swap_faces(face_image, target_image, output_image):
    """Perform face swap using Roop."""
    command = [
        "python", "run.py",
        "--execution-provider", "cuda",
        "--source", face_image,  # Face image
        "--target", target_image,  # Target image
        "--output", output_image
    ]
    subprocess.run(command)

def process_folders(main_folder, output_folder, num_target_images):
    """Rotate each subfolder as the face folder and swap with randomly selected images from others."""
    subfolders = [os.path.join(main_folder, sf) for sf in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, sf))]
    completed_folders = set(os.listdir(output_folder)) if os.path.exists(output_folder) else set()

    for face_folder in subfolders:
        face_folder_name = os.path.basename(face_folder)  # Extract only folder name
        
        if face_folder_name in completed_folders:
            print(f"Skipping {face_folder_name} (Already Processed)")
            continue  # Skip already processed folders

        face_images = get_images(face_folder)
        if not face_images:
            print(f"Skipping {face_folder}, no images found.")
            continue

        face_output_folder = os.path.join(output_folder, face_folder_name)  # Create subfolder in output
        os.makedirs(face_output_folder, exist_ok=True)  # Ensure the directory exists

        for target_folder in subfolders:
            if target_folder == face_folder:
                continue  # Skip if face folder and target folder are the same

            target_images = get_images(target_folder)
            if not target_images:
                print(f"Skipping {target_folder}, no images found.")
                continue

            selected_targets = random.sample(target_images, min(num_target_images, len(target_images)))

            for target_image in selected_targets:
                face_image = random.choice(face_images)  # Pick a random face image
                face_name = os.path.basename(face_image)
                target_name = os.path.basename(target_image)
                output_name = f"{face_name}_{target_name}"
                output_path = os.path.join(face_output_folder, output_name)  # Save in face-specific subfolder

                swap_faces(face_image, target_image, output_path)
                print(f"Swapped {face_image} -> {target_image}, saved as {output_path}")

# Run the batch process
process_folders(MAIN_FOLDER, OUTPUT_FOLDER, NUM_TARGET_IMAGES)

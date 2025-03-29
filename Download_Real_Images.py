import os
import time
import requests
import random
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from duckduckgo_search import DDGS  # ✅ Use new DDGS class

# ✅ CONFIGURATION
NUM_IMAGES_PER_ACTOR = 2950  # Number of images per actor
OUTPUT_DIR = "Images"  # Folder for images

# ✅ LIST OF ACTORS
actors = [ 
#Name of the personalities 
]

# ✅ SETUP SELENIUM WEBDRIVER
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

# ✅ Function to Download Image
def download_image(url, folder, filename):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            with open(os.path.join(folder, filename), "wb") as file:
                file.write(response.content)
    except Exception as e:
        print(f"❌ Error downloading {filename}: {e}")

# ✅ Function to Download Images for an Actor
def download_actor_images(actor_name):
    print(f"📸 Downloading images for: {actor_name.replace('_', ' ')}")

    # ✅ Create actor folder
    actor_folder = os.path.join(OUTPUT_DIR, actor_name)
    os.makedirs(actor_folder, exist_ok=True)

    # ✅ Search for Images using DuckDuckGo's new method
    search_query = f"{actor_name.replace('_', ' ')} face"
    search_results = list(DDGS().images(search_query, max_results=NUM_IMAGES_PER_ACTOR))

    if not search_results:
        print(f"❌ No images found for {actor_name}")
        return

    # ✅ Download Images
    for idx, result in enumerate(tqdm(search_results, desc=f"📥 {actor_name}")):
        img_url = result.get("image")
        if img_url:
            download_image(img_url, actor_folder, f"{actor_name}_{idx+1}.jpg")
        time.sleep(random.uniform(0.5, 1.5))  # Random delay to avoid blocking

# ✅ MAIN SCRIPT
if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)  # Create main directory

    # ✅ Initialize Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # ✅ Process Each Actor
    for actor in actors:
        download_actor_images(actor)

    # ✅ Quit WebDriver
    driver.quit()

    print("✅ All images downloaded successfully!")

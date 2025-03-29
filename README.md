# Deep-Scan
<br/>
<div align="center">
<a href="https://github.com/SrivatsaRavindra/Deep-Scan">
</a>
<p align="center">
A CNN-based model for detecting deepfake images
<br/>
<br/>
</p>
</div>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Dataset Informnation](#dataset-information)
  - [Prerequisites](#prerequisites)
- [Web Interface](#web-interface)
- [Roadmap](#roadmap)


## About The Project

DeepFakeDetector tackles the growing threat of AI-generated deepfakes by leveraging a custom dataset of real and synthetic images. Unlike generic models, this project:

-Uses Roop-generated deepfakes for realistic training data.

-Combines public figures (celebrities, politicians) with private consented images (not shared publicly).

### Built With

This project was built with the following technologies:

- TensorFlow
- CNN
- ResNet

## Dataset Information
This dataset exclusively focuses on **Indian faces** across multiple high-visibility domains!
### Dataset Creation Pipeline
1. **Real Images Collection**:
   - Downloaded images of prominent figures from:
     - Bollywood (Actors)
     - Business Leaders (Tech CEOs, Entrepreneurs)
     - Daily Soap Actors
     - Politicians (Indian)
     - Cricketers (Indian Players)
     - Musicians (Indian)
   - Private consented images (not shared publicly)
   - [Image Downloader Script](Download_Real_Images.py) (Google Images scraping)
   - [Face Cropping Script](Face_Crop.ipynb) (Haar Cascade/MediaPipe)

2. **Fake Images Generation**:
   - Created deepfakes using [Roop](https://github.com/s0md3v/roop)
   - [Face Swapping Script](Roop_Face_Swap(Fake_Images).py) (Roop implementation)

### Dataset Statistics
| Category       | Count | Source Breakdown          |
|----------------|-------|---------------------------|
| Real Images    | 92,122| Bollywood, Politicians, and Others |
| Fake Images    | 92,122| Distributed swaps across all categories|

### Why This Dataset?
This dataset provides **three critical advantages** over existing benchmarks:

1. **Diversity in Ethnicity/Context**:
   - Covers Indian faces (often underrepresented in Western datasets)
   - Includes varied lighting conditions (studio shots vs. public appearances)

2. **Real-World Testing Ground**:
   - Politicians/Celebrities are common deepfake targets
   - Business leaders represent "high-stakes" verification scenarios
   - Personalised( The dataset consists of our own images plus consented images of known people

3. **Controlled Artifacts**:
   - Roop-generated fakes exhibit consistent manipulation patterns


## Prerequisites
1. Install Dataset 
2. This project requires python to be installed in your system. If you don&#39;t have it installed, you can follow these steps:

- Install python [Python](https://www.python.org/downloads/)
- Run the installer and check the box for "Add Python to PATH" before clicking "Install Now."
- Verify the installation by opening Command Prompt (Win + R, type cmd, press Enter) and running:
  
  ```sh
  python --version
  ```

  If python has been installed correctly, your terminal should display the version of python installed on your machine.
3. Ensure all the nessasary packages are installed.

  Use 'pip install' to install any packages required.
  For Example
  ```sh
  pip install tenserflow
  ```
  ```sh
  pip install OpenCV
  ```
  ```sh
  pip install tqmd
  ```
4. Install Jupiter Notebook (To use ipynb).
  
## Model Development 

- **Pre-Processing**: Data images were of variable size, rescaled it to 512x512 (link to the file)
- **Pre Trained model**: ResNet50 is used to train the CNN model
- **Optimizer**: Adam 
- **Activation functions**: ReLU and Sigmoid are used as Activation Functions.
- **Train-val-test**: split into 80:10:10 ratio
- For generalization and robustness of the model we have used regularization technique (L1 regularization) and hyperparameter tuning.
- **Loss Function**:



## Roadmap

The roadmap includes both completed and future goals. Here&#39;s what we have accomplished and looking forward to:

- [x] Data Creation
- [ ] Add more data to the data set
- [x] Data Preprocessing
  - [x] Face Crop
  - [x] Filtered out the Unprocessed Fake images.
  - [x] Resized the variable sized images.
- [x] Model Development
  - [x] CNN
  - [x] Pretrained model (ResNet)
  - [ ] More Accurate Model Building using RNN, GANS etc
  - [ ] Integrate video/audio deepfake detection
- [ ] Publish cleaned Indian-face dataset (public subset)
- [x] Web development
    

We continue our commitment to improving and expanding the capabilities of Deep-Scan to provide an efficient and seamless experience to our users.





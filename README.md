# Deep-Scan
<br/>
<div align="center">
<a href="https://github.com/SrivatsaRavindra">
</a>
<p align="center">
A CNN-based model for detecting deepfake images
<br/>
<br/>
</p>
</div>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](https://github.com/SrivatsaRavindra/Deep-Scan/edit/main/README.md#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)
- [Notice](#notice)

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
   - Downloaded images of prominent figures from Google of these:
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
3. Ensure all the nessasary packages are installed
  Use 'pip install' to install any packages required. For Example
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
  
(((## Model Development 

- Pre-Processing: Data images were of variable size, resacled it to 512x512 (link to the file)
- Pre Trained model ResNet50 is used train the CNN model
- Optimizer: Adam, Activation functions: ReLU and Sigmoid.
- Train-val-test split into 80:10:10 ratio
- For generalization and robustness of the model we have used regularization technique (L1 regularization) and hyperparameter tuning.
- Loss Function 

)))


((### Installation

Please follow the following steps for successful installation:

1. **Clone the Repository:** Get started by cloning the repository to your local machine.

   ```
   https://github.com/ShaanCoding/makeread.me
   ```

2. **Install Frontend Packages:** Navigate to the &quot;/frontend&quot; directory and install the required yarn packages by executing the following command in your terminal:

   ```sh
   yarn install
   ```

3. **Install Backend Packages:** Similarly, navigate to the &quot;/backend&quot; directory and install the required yarn packages by executing the following command in your terminal:

   ```sh
   yarn install
   ```

4. **Set Up Environment:**

   - In the &quot;/backend&quot; directory, copy the content of &quot;.env.example&quot; file and create a new file named &quot;.env&quot;. Adjust the environment variables according to your requirements or you can leave them as it is.

   - Navigate to &quot;frontend/api/generated/readMeGenerator.ts&quot; and set the BASE parameter to your backend API route. For instance, if you are running backend on your local server at port 8080, you should set:

     ```javascript
     BASE: "http://localhost:8080/api";
     ```

5. **Run the Backend:** Navigate to &quot;/backend&quot; directory and type the following command in your terminal to run your backend server:

   ```sh
   yarn dev
   ```

6. **Run the Frontend:** Finally, navigate to &quot;/frontend&quot; directory and type the following command in your terminal to run your frontend server:

   ```sh
   yarn dev
   ```

   Now, your application should be successfully up and running!)))

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
- [ ] 
    

We continue our commitment to improving and expanding the capabilities of makeread.me to provide an efficient and seamless readme generation experience to our users.

See the [open issues](https://github.com/ShaanCoding/makeread.me/issues) for a full list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag &quot;enhancement&quot;.
Don&#39;t forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m &#39;Add some AmazingFeature&#39;`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the Mozilla Public License 2.0 License. See [Mozilla Public License 2.0 License](https://github.com/ShaanCoding/makeread.me/blob/main/LICENSE.md) for more information.

## Contact

If you have any questions or suggestions, feel free to reach out to us:

- Raise an issue on the repository: [GitHub Repository](https://github.com/ShaanCoding/makeread.me)
- Connect with us on Twitter: [@ShaanCoding](https://twitter.com/ShaanCoding)

## Acknowledgments

A special thanks to the following for their contributions, support and inspiration:

- [makeread.me](https://github.com/ShaanCoding/makeread.me)
- [Othneil Drew](https://github.com/othneildrew/Best-README-Template)

## Notice

This ReadMe was generated using [makeread.me](https://www.makeread.me/) 🚀

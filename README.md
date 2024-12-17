# EEG-Based Epileptic Seizure Prediction Using Ensemble Learning

## Overview

Epilepsy, a pervasive neurological disorder marked by unpredictable seizures, poses profound challenges for affected individuals, impacting their daily lives and overall well-being. Identifying seizures ahead of time is paramount for individuals coping with epilepsy to maintain a sense of control over their health. Through this project, we delve into cutting-edge technology to enhance seizure prediction methodologies. By fine-tuning these approaches, our objective is to furnish more precise and dependable forecasts, thereby empowering swift responses that mitigate the disruptive repercussions of seizures.

## Other Contributors

| S. No        | Name                 |
|-------------|----------------------|
| 1      | B. Gowthami          |
| 2      | R. G. S. Sai Vanaja  |
| 3      | P. Mounika           |

## Table of Contents

- Project Description
- System Architecture
- Dataset
- Feature Extraction and Selection
- Model Training
- Web Application
- Installation and Usage
- Results
- Future Work
  
## Project Description

Our project capitalizes on the intricacies of scalp EEG signals, integrating deep learning models, such as Convolutional Neural Networks (CNNs) and Long Short-Term Memory (LSTM), to automatically learn and extract features from EEG signals. By combining these features with ensemble learning methods (SVM, Random Forests, and XGBoost), we create a sophisticated predictive model. Unlike traditional approaches, our system seeks to transcend the limitations of individual models by combining the strengths of diverse algorithms through a majority voting strategy.

## System Architecture

![image](https://github.com/nikhilarokkam/EEG-BASED-EPILEPTIC-SEIZURE-PREDICTION-USING-ENSEMBLE-LEARNING/assets/115566678/9f0cd0ac-db5f-43e6-b9ef-4244095e762f)

## Dataset

We utilized the preprocessed CHB-MIT scalp EEG database. The dataset is balanced and available from [IEEE DataPort](https://ieee-dataport.org/open-access/preprocessed-chb-mit-scalp-eeg-database).

## Feature Extraction and Selection

- **Feature Extraction**:
  - **Time-Domain Features**
  - **Frequency-Domain Features**
  - **Time-Frequency Domain Features**

- **Feature Selection**:
  - Methods applied to select the most relevant features for the prediction task.

## Model Training

Ensemble learning techniques were employed to combine multiple classifiers for improved performance:
- **Support Vector Machine (SVM)**
- **Random Forests (RF)**
- **XGBoost**

The final prediction is made using a majority voting strategy.

## Web Application

We developed a web application using Streamlit. Users can input EEG readings, and after clicking the "Predict" button, the application provides an output:
- **If a seizure is predicted**: "A seizure is going to occur in a few minutes. Take necessary precautions!!"
- **If no seizure is predicted**: "No seizure is going to occur. Keep calm and carry on!"

![screencapture-localhost-8501-2024-04-02-09_58_41](https://github.com/nikhilarokkam/EEG-BASED-EPILEPTIC-SEIZURE-PREDICTION-USING-ENSEMBLE-LEARNING/assets/115566678/98af72d6-f38c-4fab-b9b7-6d925e219e98)
![screencapture-localhost-8501-2024-04-02-09_47_16](https://github.com/nikhilarokkam/EEG-BASED-EPILEPTIC-SEIZURE-PREDICTION-USING-ENSEMBLE-LEARNING/assets/115566678/f31b1a35-eb85-4f93-b27a-f6ffae08dd34)
![image (2)](https://github.com/nikhilarokkam/EEG-BASED-EPILEPTIC-SEIZURE-PREDICTION-USING-ENSEMBLE-LEARNING/assets/115566678/5d631894-8ffa-4764-87fa-15365741bf72)

## Installation and Usage

To run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/nikhilarokkam/EEG-BASED-EPILEPTIC-SEIZURE-PREDICTION-USING-ENSEMBLE-LEARNING.git
   cd EEG-Based-Epileptic-Seizure-Prediction
2. Install the required packages:
   ```bash
   pip install scikit-learn
   pip install streamlit
3. Run the Streamlit application:
   ```bash
   streamlit run main.py

## Results

Through rigorous training, validation, and testing, the developed model seeks to enhance the accuracy, specificity, and sensitivity of seizure prediction. Detailed results and performance metrics are documented in the results section of our project book.  Here are the key performance metrics:

- Accuracy: 94%
- Specificity: 97%

## Future Work
Future improvements could include:

- Enhancing the model's performance with larger datasets.
- Developing a mobile application for real-time seizure prediction.

## Project Book:
[Project Book](https://github.com/nikhilarokkam/EEG-BASED-EPILEPTIC-SEIZURE-PREDICTION-USING-ENSEMBLE-LEARNING/files/15372250/Project.Book.1.pdf)

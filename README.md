# Year_4_Project_II__Energy_Management_Control_for_Sustainable_and_Reliable_Microgrids (ACN data)

# AMLS_assignment23_24-SN20007754 (MLS project)
This repository is used to document the progress made for the AMLS assignment. 

## Project Overview
Nowadays, the field of machine learning plays a pivotal role in addressing complex challenges in various domains. In this context, the Applied Machine Learning Systems (AMLS) assignment provides an opportunity to delve into real-world datasets and apply machine learning concepts learned in lectures and labs. In the code, I have implemented three ML models - SVM, KNN and RandomForest Models for Task A - Binary classification task and one ML models - CNN model, for Task B - Multi-class classification task. 

## Project Brief
The project consists of two tasks:
1. Task A - Binary classification task (using PneumoniaMNIST dataset). The objective is to classify an image onto "Normal" (no pneumonia) or "Pneumonia" (presence of pneumonia)
2. Task B - Multi-class classification task (using PathMNIST dataset): The objective is to classify an image onto 9 different types of tissues.


## Running the Project
When adding pneumoniamnist.npz and pathmnist.npz files to the folder "Datasets", remember to delete the empty file inside the "Datasets" folder.
Afterwards, remember to replace the ```np.load()``` section with the correct directory of the datasets in your PC in every files when loading the datasets.
To run the project, run the following command:
```
python3 main.py
```
if you want to run seperate models, comment out the unwanted model section(s) in the ```main.py``` file.

## Project Structure and Role of each file
The repository is structured as follows:

```
AMLS_23_24_SN20007754

|__A
|  |__DataReshape.py #contains DataReshape function
|  |__function.py #defines three functions for training and predicting with different machine learning models: svm_classification, KNN_classification, and RandomForest_classification
|  |__KNN.py #contains KNN model
|  |__RandomForest.py #contains RandomForest Model
|  |__SVM.py #contains SVM model

|__B
|  |__function.py #defines a function for training and evaluating a Convolutional Neural Network (CNN) using the Keras library: CNN_classifications 
|  |__CNN.py #contains CNN model

|__Datasets #empty folder (should copy and paste the data here)

|__results_and_analysis
|  |__Task_A #contains results for Task A
      |  |__Confusion Matrix - SVM.pdf #contains Confusion Matrix for SVM Model
      |  |__Learning Curve - SVM.pdf #contains Learning Curve for SVM Model
      |  |__Confusion Matrix - RF.pdf #contains Confusion Matrix for RandomForest Model
      |  |__Learning Curve - RF.pdf #contains Learning Curve for RandomForest Model
      |  |__Confusion Matrix - KNN.pdf #contains Confusion Matrix for KNN Model
      |  |__Learning Curve - KNN.pdf #contains Learning Curve for KNN Model
|  |__Task_B #contains results for Task B
      |  |__Confusion Matrix - CNN.pdf #contains Confusion Matrix for CNN Model
      |  |__Training and Validation Accuracy Curve - CNN.pdf #contains Training and Validation Accuracy Curve for CNN Model

|__main.py #main file to run tasks (A and B)

|__README.md #instructions and notices for running the code

|__requirements.txt #requirements to be installed

```

## Requirements
To install the required packages, run the following command:
```
pip install -r requirements.txt
```

## Acknowledgements
The datasets used in this project are from the MedMNIST repository, which can be downloaded via the link: https://medmnist.com/, and are cited as follows:
```
Jiancheng Yang, Rui Shi, Donglai Wei, Zequan Liu, Lin Zhao, Bilian Ke, Hanspeter Pfister, Bingbing Ni. Yang, Jiancheng, et al. "MedMNIST v2-A large-scale lightweight benchmark for 2D and 3D biomedical image classification." Scientific Data, 2023.
                            
Jiancheng Yang, Rui Shi, Bingbing Ni. "MedMNIST Classification Decathlon: A Lightweight AutoML Benchmark for Medical Image Analysis". IEEE 18th International Symposium on Biomedical Imaging (ISBI), 2021.
```
The instructions and inspiration for this project can be found in the ELEC0134 module, led by Dr. Miguel Rodrigues at UCL.

# Year_4_Project_II__Energy_Management_Control_for_Sustainable_and_Reliable_Microgrids (ACN data)
This repository is used to document the progress made for the 4th year Project - Energy Management Control for Sustainable and Reliable Microgrids.

## Project Overview
Nowadays, the field of machine learning plays a pivotal role in addressing complex challenges in various domains. In this context, the Applied Machine Learning Systems (AMLS) assignment provides an opportunity to delve into real-world datasets and apply machine learning concepts learned in lectures and labs. In the code, I have implemented three ML models - SVM, KNN and RandomForest Models for Task A - Binary classification task and one ML models - CNN model, for Task B - Multi-class classification task. 

## Project Brief
The project consists of two tasks:
1. Task A - Binary classification task (using PneumoniaMNIST dataset). The objective is to classify an image onto "Normal" (no pneumonia) or "Pneumonia" (presence of pneumonia)
2. Task B - Multi-class classification task (using PathMNIST dataset): The objective is to classify an image onto 9 different types of tissues.


## Running the Project
Remember to replace the ```C:\Users\Lu34\OneDrive\Desktop\Year 4 Project II\Matlab simulation\acn_data\final codes\`` sections with the correct directory of every files (eg. combined_hourly_csv.csv) in your PC.
To run the project, run the main code:
```
EMS_controller_MPC_with_NN_validation_RMSE_final_final.mlx.
```
Other codes are codes that helps the main code, or copied/derived from the main code, as stated below. 

## Project Structure and Role of each file
The repository is structured as follows:

```
Year_4_Project_II__Energy_Management_Control_for_Sustainable_and_Reliable_Microgrids

|__final codes
|  |__YALMIP-master #
|  |__best_para.mlx #
|  |__combined_hourly_csv.csv #
|  |__csv conversion.py #
|  |__EMS_controller_MPC_with_NN_validation_RMSE_final_final.mlx #
|  |__hourly_data.pkl #
|  |__MPC_predicted_horizon_choice #
|  |__NN #

|__final results
|  |__original_acn_data #
|  |__Best Hyperparameters Hidden Units=12, Epochs=125, MiniBatchSize=128; Minimum Validation RMSE 1.105913 #
   |  |__1 #
   |  |__2 #
   |  |__3 #
   |  |__4 #
   |  |__5 #
   |  |__6 #
   |  |__7 #
   |  |__8 #
   |  |__resultsORscreenshots #
|  |__1.21rmse #

|__acndata_sessions_1.json
|  |__

|__acndata_sessions_2.json
|  |__

|__acndata_sessions_3.json
|  |__

|__conbine_3csv.py
|  |__

|__data_pkl.py
|  |__

|__hourly.py
|  |__

|__time_kwhdelivered.py
|  |__

|__README.md # Instructions and notices for running the code

|__requirements.txt # Matlab version and toolbox to be installed 

```

## Requirements
The required matlab version is MATLAB R2023b,with deep learning toolbox installed.

## Acknowledgements
The datasets used in this project are from the ACN-Data repository, which can be downloaded via the link: https://ev.caltech.edu/dataset, and are cited as follows:
```
@inproceedings{lee_acndata_2019,
  author = {Lee, Zachary J. and Li, Tongxin, and Low, Steven H.},
  title = { {ACN}-{Data}: {Analysis} and {Applications} of an {Open} {EV} {Charging} {Dataset} },
  booktitle = {Proceedings of the Tenth International Conference on Future Energy Systems},
  series = {e-Energy '19},
  month = jun,
  year = {2019},
  location = {Phoenix, Arizona}
}
```
The instructions and inspiration for this project are from Dr. Francesca Boem at UCL.

# Mobile Price Prediction MLOps Project
### This projects was inspired by ML Deployment course on Udemy

The project is an end-to-end machine learning project that predicts the price category of a mobile phone based on various features. The Random Forest model is used for training, and the project uses a Scikit-Learn Pipeline for data preprocessing and training and inference.For the sake of simplicity there is only one step of data preprocessing which is Feature Scaling.The model is then deployed using FastAPI and is automatically tested, built, and deployed to Render using CircleCI.


The project architecture consists of several components:

Data Collection: The training mobile price dataset is downloaded from Kaggle and placed into the data folder.

Data Preprocessing: For the sake of simplicity only one step included in this step which is Feature Scaling.

Model Training: The Random Forest model is trained using the preprocessed data.

Model Serving: The model is deployed using FastAPI, which provides a REST API for making predictions.

Automated Testing: The project includes automated testing using the Tox library. CircleCI is used to automatically run the tests every time new code is pushed to the repository.

Docker Building and Deployment: The project is built into a Docker container and automatically deployed to Render using CircleCI.

It is just a simple achitecture that might be brought to the advanced level by modifying and adding new steps and featues.

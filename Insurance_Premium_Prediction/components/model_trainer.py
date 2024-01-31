import os
import sys
import pandas as pd
import numpy as np

from dataclasses import dataclass
from Insurance_Premium_Prediction.exception import customexception
from Insurance_Premium_Prediction.logger import logging
from Insurance_Premium_Prediction.utils.utils import save_object, evaluate_model

from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from xgboost import XGBRegressor

# Configuration class for model trainer
@dataclass
class InsuranceModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'insurance_model.pkl')

# Model trainer class
class InsuranceModelTrainer:
    def __init__(self):
        self.model_trainer_config = InsuranceModelTrainerConfig()

    # Method to initiate model training
    def initate_model_training(self, train_array, test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            # Splitting data into features and target variables
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            # Dictionary containing different regression models
            models = {
                'Linear Regression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet(),
                'Gradient Boosting': GradientBoostingRegressor(),
                'Random Forest': RandomForestRegressor(),
                'XGBoost': XGBRegressor()
            }

            # Evaluating models and obtaining model report
            model_report = evaluate_model(X_train, y_train, X_test, y_test, models)
            
            # Printing model report
            logging.info(f'Model Report : {model_report}')

            # Finding the best model based on model report
            best_model_name = max(model_report, key=model_report.get)
            best_model_score = model_report[best_model_name]
            best_model = models[best_model_name]

            # Saving the best model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

        except Exception as e:
            logging.error('Exception occurred at Model Training')
            raise customexception(e, sys)

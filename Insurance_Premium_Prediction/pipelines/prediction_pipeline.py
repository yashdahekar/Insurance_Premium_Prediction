import os
import sys
import pandas as pd
from Insurance_Premium_Prediction.exception import customexception
from Insurance_Premium_Prediction.logger import logging
from Insurance_Premium_Prediction.utils.utils import load_object


class InsurancePremiumPredictor:
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model_path = os.path.join("artifacts", "insurance_model.pkl")
            
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)
            
            scaled_data = preprocessor.transform(features)
            
            pred = model.predict(scaled_data)
            
            return pred
            
        except Exception as e:
            raise customexception(e, sys)
    
    
class CustomData:
    def __init__(self, age: float, bmi: float, children: float, sex: str, smoker: str, region: str):
        self.age = age
        self.bmi = bmi
        self.children = children
        self.sex = sex
        self.smoker = smoker
        self.region = region
                
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'age': [self.age],
                'bmi': [self.bmi],
                'children': [self.children],
                'sex': [self.sex],
                'smoker': [self.smoker],
                'region': [self.region]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occurred in prediction pipeline')
            raise customexception(e, sys)

from Insurance_Premium_Prediction.logger import logging
from Insurance_Premium_Prediction.exception import customexception
import numpy as np
import pandas as pd
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

# Configuration class for data ingestion
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")

# Data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    # Method to perform data ingestion
    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        
        try:
            # Reading data from CSV file
            data = pd.read_csv(Path(os.path.join("notebooks/data", "insurance.csv")))
            logging.info("Data read as a DataFrame")
            
            # Creating directories if they don't exist and saving raw data
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw dataset saved in artifacts folder")
            
            logging.info("Performing train test split")
            
            # Splitting data into train and test sets
            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("Train test split completed")
            
            # Saving train and test data
            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            
            logging.info("Data ingestion completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            logging.error("Exception occurred during data ingestion")
            raise customexception(e, sys)

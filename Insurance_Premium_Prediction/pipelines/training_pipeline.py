from Insurance_Premium_Prediction.components.data_ingestion import DataIngestion
import os 
import sys
from Insurance_Premium_Prediction.logger import logging
from Insurance_Premium_Prediction.exception import customexception
import pandas as pd

obj = DataIngestion()

obj.initiate_data_ingestion()
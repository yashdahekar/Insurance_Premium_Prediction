from Insurance_Premium_Prediction.pipelines.prediction_pipeline import CustomData
 
custdataobj = CustomData(43,25.1,0,'female','no','northeast')

data = custdataobj.get_data_as_dataframe()

print(data)
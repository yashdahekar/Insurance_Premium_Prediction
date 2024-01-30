from Insurance_Premium_Prediction.pipelines.prediction_pipeline import CustomData, InsurancePremiumPredictor
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        data = CustomData(
            age=float(request.form.get('age')),
            bmi=float(request.form.get('bmi')),
            children=float(request.form.get('children')),
            sex=request.form.get('sex'),
            smoker=request.form.get('smoker'),
            region=request.form.get('region')
        )
        
        final_data = data.get_data_as_dataframe()
        predictor = InsurancePremiumPredictor()
        pred = predictor.predict(final_data)
        result = round(pred[0], 2)
        
        return render_template("result.html", final_result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

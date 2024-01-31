<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insurance Premium Prediction</title>
</head>
<body>
    <h1>Insurance Premium Prediction</h1>

    <h2>Overview</h2>
    <p>Insurance Premium Prediction is a comprehensive project designed to forecast insurance premiums by leveraging machine learning algorithms. It takes into account various factors such as age, BMI, number of children, gender, smoking status, and region to provide accurate predictions. This project utilizes historical data analysis and machine learning techniques to offer insights into future insurance premium trends.</p>

    <h2>Installation</h2>
    <ol>
        <li><strong>Clone the repository:</strong><br>
            <code>git clone https://github.com/yashdahekar/Insurance_Premium_Prediction<br>
            cd Insurance_Premium_Prediction</code></li>
        <li><strong>Set up the environment:</strong><br>
            <code>./init_setup.sh</code></li>
        <li><strong>Install dependencies:</strong><br>
            <code>pip install -r requirements.txt</code></li>
        <li><strong>Run the Flask application:</strong><br>
            <code>python application.py</code></li>
        <li><strong>Access the application:</strong><br>
            Open a web browser and go to <code>http://localhost:8080</code> to use the application.</li>
    </ol>

    <h2>Technology Used</h2>
    <ul>
        <li><strong>Python:</strong> Core programming language</li>
        <li><strong>Flask:</strong> Web application framework</li>
        <li><strong>pandas:</strong> Data manipulation library</li>
        <li><strong>NumPy:</strong> Numerical computing library</li>
        <li><strong>scikit-learn:</strong> Machine learning library</li>
        <li><strong>XGBoost:</strong> Gradient boosting library</li>
    </ul>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.9</li>
        <li>Flask</li>
        <li>pandas</li>
        <li>NumPy</li>
        <li>scikit-learn</li>
        <li>XGBoost</li>
    </ul>

    <h2>Algorithms Used</h2>
    <p>The project employs various machine learning algorithms for insurance premium prediction:</p>
    <ul>
        <li>Linear Regression</li>
        <li>Lasso Regression</li>
        <li>Ridge Regression</li>
        <li>ElasticNet Regression</li>
        <li>Gradient Boosting Regressor</li>
        <li>Random Forest Regressor</li>
        <li>XGBoost Regressor</li>
    </ul>

    <h2>Project Structure</h2>
    <!-- Project structure goes here -->

    <h2>Next Steps</h2>
    <ol>
        <li>Explore the Jupyter notebooks in the <code>notebooks</code> directory for data exploration and analysis.</li>
        <li>Train machine learning models using the provided scripts in the <code>pipelines</code> directory.</li>
        <li>Serve the prediction model using the Flask application in <code>application.py</code>.</li>
        <li>Utilize the web interface to make predictions on new data.</li>
    </ol>

    <h2>Author</h2>
    <p>This project was created by Yash Dahekar. For any inquiries or feedback, please contact <a href="mailto:yashdahekar@gmail.com">yashdahekar@gmail.com</a>.</p>
</body>
</html>

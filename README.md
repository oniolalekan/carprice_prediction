# Car Price Prediction Service

This is a Django Rest Framework service to help predict price of car given some core dependent variables.
The service is based on a prediction model trained using data and a kernel from a Kaggle challenge. <a href="https://www.kaggle.com/goyalshalini93/car-price-prediction-linear-regression-rfe"> Kaggle Challenge</a>


The service is deployed on heroku: http://carpricepredict.herokuapp.com/

The end point exposed: https://carpricepredict.herokuapp.com/predict

List of significant variables after Visual analysis: horsepower, carwidth, hatchback, and highend

Sample api call: https://carpricepredict.herokuapp.com/predict?horsepower=154&carwidth=65.50&ishatchback=0&ishighend=0

The endpoint can be queried using Postman.

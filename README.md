# Car Price Prediction Service

This is a Django Rest Framework service to help predict price of car given some core dependent variables. 
The service is based on a prediction model trained using data and a kernel from a Kaggle challenge. <a href="https://www.kaggle.com/goyalshalini93/car-price-prediction-linear-regression-rfe"> Kaggle Challenge</a>

The aim was to construct a model that can predict the price of car (the dependent attribute) from the attribute variables (the independent attributes) like car {horsepower, width, company name, fuel type, engine size, cylinder number, etc.}. This is a classical example of a regression problem where the objective is to predict a continuous value - the price of a car. 

New features were derived from existing ones. One worthy of mention is "Car Range" - a categorical data. This feature was derived by binning the Car Companies based on avg prices of each Company to give three features: Budget, Medium, and Highend.

Dummy variables were created by coding the categorical data. For example, Car Range was coded into two nominal variables of Medium and Highend.  

From the Exploratory Data Analysis, it was discovered that most of the collected and derived independent variables had little or no effect on the price of the car. In other words, there was little or no correlation between the variables and the price of car. Consequently, those variables were dropped. However <b>carwidth</b>, <b>horsepower</b>, <b>hatchback</b>, and <b>highend</b> were found to have significant positive correlation with price.  

Ordinary least squares (OLS) regression method of analysis was used to estimates the relationship between the indenpedent variables and the dependent variable - the price of car. The model was saved on disk and deployed as a RESTFUL service. 

<figure>
  Ordinary least squares (OLS)
</figure>

The service is deployed on heroku: <a href="http://carpricepredict.herokuapp.com/"> Car Price Prediction </a>

The end point exposed: https://carpricepredict.herokuapp.com/predict

List of significant variables after Visual analysis of the data: horsepower, carwidth, hatchback, and highend

Sample api call: https://carpricepredict.herokuapp.com/predict?horsepower=154&carwidth=65.50&ishatchback=0&ishighend=0

The endpoint can be queried using Postman.

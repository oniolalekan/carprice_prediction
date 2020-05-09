from django.shortcuts import render
import pickle
from rest_framework.decorators import api_view
from pathlib import Path
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np
import os


def rescale_horsepower(hpower):
    result = (hpower - 48.000000) / (288.000000 - 48.000000)
    return result 

def rescale_carwidth(cwidth):
    result = (cwidth - 60.300000) / (72.300000 - 60.300000)
    return result



@api_view(["POST"])
def predict_carprice(request):
    try:        
        # Highly correlated variables to price are - horsepower, carwidth, hatchback, and highend.

        horsepower = request.GET.get('horsepower')
        carwidth = request.GET.get('carwidth')
        hatchback = request.GET.get('ishatchback')
        highend = request.GET.get('ishighend')
        fields = [1.0, horsepower,carwidth, hatchback, highend]
        if not None in fields:
            # Datapreprocessing: Convert the values to float and perform scaling
            horsepower = rescale_horsepower(float(str(horsepower))) 
            carwidth = rescale_carwidth(float(str(carwidth)))
            hatchback = int(str(hatchback))
            highend = int(str(highend))

            result = [1.0, horsepower,carwidth, hatchback, highend]
            #Passing data to model & loading the model from disks

            

            data_folder = Path("/carprice_api/carprice_deploy/")

            file_to_open = data_folder / "model.pkl"

            print(file_to_open)

            #path = "c:\\Users\\CBT532\\carprice_api\\carprice_deploy\\api\\model.pkl"

            
            regressor = pickle.load(open(file_to_open, 'rb'))
            prediction = regressor.predict([result])[0]

            # Min-Max Scaler. Scale up the car price by using the Min-Max scaling algorithm that was used in training.
            min_price = 5118.000000
            max_price = 45400.000000
            actual_price = prediction * (max_price - min_price) + min_price
            prediction = {
                'error' : '0',
                'message' : 'Successfull',
                'prediction' : actual_price,            
            }    
        else:
            prediction = {
            'error' : '1',
            'message': 'Invalid Parameters'                
            }
    except Exception as e:
        prediction = {
            'error' : '2',
            "message": str(e)
        }
    
    return Response(prediction)

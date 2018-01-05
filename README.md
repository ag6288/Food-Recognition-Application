# Food-Recognition-Application

# Project Overview:

- User can upload an image of food item.
- Image recognition is done in background and food item is recognized.
- User location is obtained and based on it, restaurants are recommended with the particular food item.
- AWS services used are EC2, S3, Lambda, API Gateway, RDS and Cognito.
- EatStreet API is used to access the restaurant menu.

# Implementation:

- Authentication and registration of the user.
- Image is uploaded to S3 which invokes  the Lambda function through API Gateway.
- Tensor flow model is deployed on an EC2 instance and Lambda function is used to communicate with the model and recognise the image.
- Using the result of the model, restaurant details are fetched by searching for the menu item in RDS.



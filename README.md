# FACE_SONG API  
Using AWS Sagemaker, API Gateway, Lambda, cloud9, and Deep learning 

![Github License](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Code Coverage](https://img.shields.io/badge/coverage-80%25-green)
![python Version](https://img.shields.io/pypi/pyversions/Flask)


<img src="https://github.com/mankar1257/FACE_SONG_API/blob/main/Images/Image1.png" alt="drawing" width="850" height ="500"/>


### Suggesting songs using Face emotions 

Songs play a crucial  role in our life,  I am a person who likes to listen to songs while working on my PC 

Now, Image a situation when You are working on your personal computer while enjoying music and your computer knows which song to play next to keep you pumped up !!!

With the evolution of machine learning technologies, This is possible 

This is an API that predicts the song based on the face of the listener, given the image, it detects the face, predicts the emotion, and accordingly suggests the songs :)

## Table of content

- [**Getting Started**](#getting-started)
- [overview ](#overview)
- [Built With](#built-with)
- [Contributing](#contributing)
- [License](#license)
- [Get Help](#get-help)


## Getting Started 

In order to mimic the project, you need to have 

  1. an AWS account (free tier ) 
  
  2. A basic understanding of AWS services ( s3, Sagemaker, Lambda, API gateway, Cloud9 .. )
  
  3. Understanding of Machine learning and deep learning 

Before we start, prepare the following: 

1. AWS Sagemaker instance 

2. S3 bucket  


### upload the following files in the Sagemaker Jupiter notebook directory 

  1. [train.py](https://github.com/mankar1257/FACE_SONG_API/blob/main/Sagemaker/train.py)
  
  2. [Data.py](https://github.com/mankar1257/FACE_SONG_API/blob/main/Sagemaker/Data.py)
  
  3. [FaceSong.ipynb](https://github.com/mankar1257/FACE_SONG_API/blob/main/Sagemaker/FaceSong.ipynb)
  
  
### Upload the following data files in the S3 
   1. [S3](https://github.com/mankar1257/FACE_SONG_API/tree/main/S3)
   
   2. [lambda layer 1](https://github.com/mankar1257/FACE_SONG_API/tree/main/Lambda/Child_lambda/Lambda_layer)
   
   3. [lambda_layer_2](https://github.com/mankar1257/FACE_SONG_API/tree/main/Lambda/Parent_lambda/Lambda_Layer)
   
   
   
## Overview 


#### Process flow :

<img src="https://github.com/mankar1257/FACE_SONG_API/blob/main/Images/Image2.png" alt="drawing" width="750" height ="400"/>


This process includes 

1. [Training and deploying the model using sagemaker](https://github.com/mankar1257/FACE_SONG_API/blob/main/Sagemaker/FaceSong.ipynb)

2. [Creating the lambda functions](https://github.com/mankar1257/FACE_SONG_API/tree/main/Lambda)

3. [Setting up the API gateway](https://aws.amazon.com/blogs/machine-learning/call-an-amazon-sagemaker-model-endpoint-using-amazon-api-gateway-and-aws-lambda/)


## API Input / Output and calling 


please check this 
[Here](https://github.com/mankar1257/FACE_SONG_API/blob/main/Caller.ipynb)

## Contributing


#### Issues
In the case of a bug report, bugfix or suggestions, please feel free to open an issue.

#### Pull request
Pull requests are always welcome, and we will do our best to do reviews as fast as we can.


## License

This project is licensed under the [GPL License](https://github.com/mankar1257/FACE_SONG_API/blob/main/LICENSE)


## Get Help
- Contact : mankarvaibhav819@gmail.com 
- If appropriate, [open an issue](https://github.com/mankar1257/FACE_SONG_API/issues) on GitHub


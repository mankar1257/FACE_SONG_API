## Getting started 

<img src="https://github.com/mankar1257/FACE_SONG_API/blob/main/Images/Image2.png" alt="drawing" width="750" height ="400"/>



there are two lambda functions 

### parent lambda 

the main lambda function handling interaction of child lambda, Sagemaker endpoint and API gateway

### Child lambda

the function for face detection 


## Lambda layers 

Both lambda functions have layer dependency, i.e you have to create the lambda layers and add them to respective lambda functions.
the steps for adding the lambda function is given in the lambda layer folder in each lambda function

## Connecting child lambda function with parent lambda : 

please follow this artical : 

https://www.sqlshack.com/calling-an-aws-lambda-function-from-another-lambda-function/ 




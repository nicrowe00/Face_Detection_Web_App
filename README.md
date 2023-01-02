# Face Detection Web App

## Overview

The Face Detection Web App is a web application that when run will start a webpage containing a view that displays the video through the default webcam on your machine. When a face is detected, the application will take the encodings of that face and check them against the encodings of any of the faces in the images in the 'faces' folder. If the encodings match, a red rectangle will be drawn around the person's face in the web app in real time while the name of the file that they matched with will be displayed next to their face. For maximum effectiveness, it is recommended to name each image file, which must be in .jpg format in order to be used, after the person whose face is in the image. For example, if there was a picture of Tom Hanks in the 'Faces' folder, it is recommended to name that file 'Tom Hanks.jpg' so that the name 'Tom Hanks' will appear next to the image of Tom Hanks gathered by the webcam.

## Requirements

To run this project, download it onto your local machine using the following command:
> git clone https://github.com/nicrowe00/Face_Detection_Web_APP.git

Once the project is on your local machine, there are several other packages that must be installed. Python v3.8 or later must be present on your machine in order to run the application. Below are commands to install the other required packages for the application:

>pip install opencv2-python

>pip install face-recognition

>pip install numpy

>pip install -U Flask

Once the above packages are installed, move the face images you wish to match against into the 'faces' folder, making sure they are of .jpg type.
Once this is done, simply start the application by running the 'app.py' file.
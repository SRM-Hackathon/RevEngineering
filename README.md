Made by _Abhilash Pal_, _Saurav Saha_, _Sounak_, _Arko Chatterjee_, _Sukrit Bhattacharya_
# SRM Hackathon 2018 | RevEngineering

[Demo video]<br>

## Problem Statement

Physical fitness is the key concern of today’s generation. It is the state of well-being and the ability to perform aspects of sports and daily activities. One can be physically fit when he/she is mentally fit. Thus the common mass also demands products that will help in maintaining and tracking their physical/mental fitness. In today's busy and competitive world, most employees tend to be mentally stressed out. Thus a system has to be made which helps in reducing the mental stress so that a person can be physically as well as mentally fit.

### Approach

The system we wish to build in turn is a recommender system for betterment of mental health of the user. It takes as input the facial features or text based mood and outputs a host of media, like movies, songs and poems for the user.

We will use a** Computer Vision** trained model using OpenCV to extract the facial features and Keras to detect mood from the same using a Deep Learning model and similiarly use nltk or other associated Natural Language Processing Libraries to ascertain the mood of the user from the textual input. A recommendation system is then built using Spotipy API and LastFM 360k music Dataset for the music and the IMDB Dataset for the movies part.

We also use Neural Style Transfer to apply a filter on the image of the user using Deep Learning in OpenCV. The poetry recommendation system runs using a self built dataset and a model to recommend poems based on specific query words.

We wish to deploy the model using Django for a WebApp. 

### Application

A Recommendation System web app has been made which detects expressions of the user either by facial expression or a text input by the user and in return recommends movies, songs, quotes and funny memes in accordance with the emotions of the user, thus helping in uplifting the mood of the user.

### Usage

```bash
make
```

This will start the local server at localhost:8000.

_*Deps*: sklearn, pandas, django, requests, bs4_



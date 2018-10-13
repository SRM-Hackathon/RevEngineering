Made by _Abhilash Pal_, _Saurav Saha_, _Sounak Bhattacharya_, _Arko Chatterjee_, _Sukrit Bhattacharya_
# SRM Hackathon 2018 | RecomMate.ai | RevEngineering

## Problem Statement

Physical fitness is the key concern of today’s generation. It is the state of well-being and the ability to perform aspects of sports for top notch athletes and daily activities and tasks for other professionals such as those in the IT sector. One can be physically fit when he/she is mentally fit. Thus the common mass also demands products that will help in maintaining and tracking their physical/mental fitness. In today's busy and competitive world, most employees tend to be mentally stressed out. Thus a system has to be made which helps in reducing the mental stress so that a person can be physically as well as mentally fit. Statistics in recent times about the mental fitness of the population have provided us with some important conclusions. 1 in 5 people in the country need some kind of psychiatric or psycological attention. 45% or the corporate professionals suffer from some form of depression and this might transform into clinical depression if left unattended.

### Approach

The system we wish to build in turn is a recommender system for betterment of mental health of the user. It takes as input the facial features or text based mood and outputs a host of media, like movies, songs and poems for the user.

We will use a** Computer Vision** trained model using OpenCV to extract the facial features and Keras to detect mood from the same using a Deep Learning model and similiarly use nltk or other associated Natural Language Processing Libraries to ascertain the mood of the user from the textual input. A recommendation system is then built using LastFM 360k music Dataset and the LastFM python API- PyLast for the music and the IMDB Dataset for the movies part.

We also use Neural Style Transfer to apply a filter on the image of the user using DNN module in OpenCV. 

We wish to deploy the model using Django for a WebApp. 

### Application

People get tense during stressful situations and they require a moment of pure tranquility before the given event. For athletes it might probably be playing in their life's most important matches such as the finals of an important championship, where they need to be at their best, or for a working professional, where they need to give a presentation for getting an important promotion, or simply for students who are tense before an important exam. 

People might start to feel sad if they probably had a bad day or things didn't go their way for some or the other thing during the day. 

In all these situations people look forward to something to get out of the muck and just feel a bit better. For all these situations our recommendation system can work like a charm and cheer up the mood of our user.

The RecomMate.ai web-app detects the user's emotions through a facial recognition system which first recognises a face from a live video feed and in turn provides the facial input to the emotion recognition engine using Keras built on a tensorflow backend. The users can also provide input in the form of text, where our sentimental analysis engine detects how positively or negatively a user is thinking or feeling by creating a proper analysis on the textual input. After detecting the emotions using text or facial input the user is recommended movies, songs, quotes and funny memes, thus helping in uplifting the mood of the user or simply maintaining the their happy state of mind.

### Usage

```bash
git clone https://github.com/SRM-Hackathon/RevEngineering.git
cd Django Frontend/frontend
pip install requirements.txt
python manage.py runserver
```

This will start the local server at localhost:8000.

_*Deps*: 
pylast
numpy
imutils
imageio
matplotlib
textblob
Django
pandas
Keras
scikit_learn_

### Developed with love by

![Alt Text](https://github.com/SRM-Hackathon/RevEngineering/blob/master/src/REVlogo.jpg)



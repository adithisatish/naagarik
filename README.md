# Naagarik
### Analysing Civic Issue Complaints made by Citizens on Twitter
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Naagarik is a machine learning framework, which analyses real-time data obtained from tweets and classifies them into civic issue categories, in order to understand citizen proactivity on social media platforms and help improve responsiveness of local government by making categorised data accessible.

### Dataset
- Reap Benefit's Neighbourhood Dashboard data
- Janaagraha data
- Tweets scraped using Tweepy and GetOldTweets3

Hyperlocal tweets scraped using the Twitter Streaming API are preprocessed and passed to a binary Logistic Regression classifier, which classifies the tweet as a civic issue or a non-civic issue; the latter being filtered out. The civic issue tweets are then passed to a linear kernel Support Vector Machine which categorises the tweets into predefined categories like Waste/Garbarge, Potholes, Water, Sanitation, etc. Sentiment analysis is finally performed on these tweets using the VADER Sentiment Analyser to determine whether the tweets are complaints requiring urgent attention, neutral feedback or compliments to the authorities for a job well done. 

### Required Libraries
Run ```pip install -r requirements.txt```

### Run 

To test the framework on a text file of inputs, ```data/testdata.txt```, run ```python framework.py```

To test it on real-time streaming tweets, run ```python streaming.py```. Please note that Twitter Developer credentials are required to run this file.

Implemented using Python.

### Citation

If you use this repository for research, please cite the following reference paper:

    A. Satish, S. B. Shankar and K. N. Kavitha, "Naagarik: A Machine Learning Framework for Intelligent Analysis of Civic Issues," 2021 Asian Conference on Innovation in Technology (ASIANCON), 2021, pp. 1-6, doi: 10.1109/ASIANCON51346.2021.9544777.}

### Authors:
- Adithi Satish
- Shriya Shankar

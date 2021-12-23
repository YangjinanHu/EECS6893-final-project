# EECS6893-final-project
## Introduction
Social Media Analytics: Developing a Bloomberg Function Like Tool that Inform Trading Strategies   
With increasing volume of retail trading in the US stock market, we have witnessed growing influence from retail trader's action on the price of particular stock. To understand this trend, we develop a Bloomberg Function like social media analytic tool to gain insight on retail investor's trading strategies, sentiments and stock of choice. 

There are three parts in this project CUberg_frontend is the frontend website for twitter and reddit data analytics. Lambda Function fetch the data from the twitter api and reddit api to store them in the S3 buckets. Sagemaker contains a notebook instance and relevant datasets where we trained our model. 

## Prerequisites
### AWS Service
- AWS Lambda  
- AWS Sagemaker
- AWS S3
- AWS Kinesis Data Firehose
- AWS QuickSight

### Packages
- Python 3.6.9
- Tensorflow 2.4.0
- HTML 5
- CSS 2.1

## Datasets
Data used in this projects are live streaming tweets from Twitter and posts in a predefined timeframe in Subreddit r/wallstreetbets. The live stream are fetched by functions we define in AWS lambda every hour. These data are first filtered using a list of traded stock name and company's name as keywords. For Twitter data, we first filter out non English content using python regular expression. Then the parsed data are sent to topic classification model to filter out data related to commerce and technology. Next, the data is sent to the rumor filtering model to filter out low quality data that's been classified as rumors. We add the company tag to the cleaned data JSON and put it to AWS kinesis firehose delivery stream. The delivery stream uses dynamic partitioning to send each tweets or reddit submission/comments to relevant company's folder stored in S3 buckets. 

Data are updated every hour to provide the most recent insights on the retail community. Every hour, a total of 1000 tweets are collected for ten company in the tech sector. To be specific, they are Tencent, Alibaba, Amazon, Apple, Meta, Google, Uber, Tesla, Netflix and Microsoft. Another 1000 sumbission and comments are also collected from the Subreddit wallstreetbets. Data from Reddit are put to similar delivery streams and are stored in another S3 bucket. A sample data of Tesla related tweets contains 64000 characters in one single update.

## Model
BiLSTM-Att model to train the classifier with following steps: 

- We introduced GloVe Embedding (100d, 2B Twitter) for word representations. 
- Construct the word_dict for the training data w.r.t. word frequency, and we select the top 30,000 words to form a word_dict. 
- Match the word_dict with the GloVe Embedding, 64% of the words in Topic Classification task and 62% of the words in Fake News Detection task are assigned with a Glove Embedding, the rest are randomly initialized. 
- For Topic Classification task, the original 4 label topics are redefined as Other (0), Business (1), Tech/Sci (2), class 1 and 2 are what we desired. 
- For Fake News Detection task, we truncated the input texts if they exceed the maximum length of 256, Fake News (1), Reliable News (0). 


## Results
- Website Frontend
- Word Cloud
- Sentiment Analysis Visualization



## Organization



```


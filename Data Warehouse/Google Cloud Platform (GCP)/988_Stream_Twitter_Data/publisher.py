# https://theappliedarchitect.com/setting-up-gcp-pub-sub-integration-with-python/
# https://faun.pub/writing-a-pub-sub-stream-to-bigquery-401b44c86bf
# https://www.syntio.net/en/labs-musings/streaming-data-from-twitter-to-gcp

# pip3 install --upgrade google-api-python-client
# pip3 install --upgrade google-cloud-pubsub
# gsutil cp gs://qwiklabs-gcp-01-ea893043e169/qwiklabs-gcp-01-ea893043e169-2bb84456ce58.json .
# pip3 install tweepy

# environment variable setup for private key file
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="qwiklabs-gcp-01-ea893043e169-2bb84456ce58.json"

import json
import base64
import time

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from google.cloud import pubsub_v1

consumer_key = 'Gy6PkzZMlHFzH7ju8bpcHRqss'          
consumer_secret = 'yQzhNUXL1FthwOtSgsVkxWTf76LggWWIyiZJQZNMJ3FF3QqdiD'
access_token = '1320070118697828352-KJQA2LMSJ8FzZDmZixnZnuXSSMK1uz'
access_secret = 'AHY7fyK1Oq7pvId79mzU3Kaq6N9HGVcqfIOMLP5iTbggq'


# GCP topic, project & subscription ids
PUB_SUB_TOPIC = "my-python-topic"
PUB_SUB_PROJECT = "qwiklabs-gcp-01-ea893043e169"
PUB_SUB_SUBSCRIPTION = "my-python-topic-sub"

# Pub/Sub consumer timeout
timeout = 3.0

# For Publisher

class listener(StreamListener):
	def __init__(self, topic, project):
		self.publisher = pubsub_v1.PublisherClient() 
		self.topic_path = self.publisher.topic_path(topic, project)  
		self.count = 0
		self.tweets = []
		self.batch_size = 50
		self.total_tweets = 1000

	def on_data(self, data):
		def write_to_pubsub(data_lines):
			messages = []
			for line in data_lines:
				messages.append({'data': line})
			body = {'messages': messages}
			str_body = json.dumps(body)
			data = base64.urlsafe_b64encode(bytearray(str_body, 'utf8'))
			self.publisher.publish(self.topic_path, data=data)
			time.sleep(20)
		
		msg = json.loads( data )
		'''
		created_at = msg['created_at']
		id = msg['id']
		text = msg['text']
		source = msg['source']
		retweet_count = msg['retweet_count']
		user_name = msg['user_name']
		user_location = msg['user_location']
		user_followers_count = msg['user_followers_count']
		user_statuses_count = msg['user_statuses_count']
		'''
		print( msg['text'].encode('utf-8') )
		tw = msg['text']
		self.tweets.append(tw)
		if len(self.tweets) >= self.batch_size:
			write_to_pubsub(self.tweets)
			self.tweets = []
		#self.publisher.publish(self.topic_path, data=msg['text'].encode('utf-8'))
		self.count += 1
		if self.count >= self.total_tweets:
			return False
		if (self.count % 50) == 0:
			print("count is: {}".format(self.count))
		return True



auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
twitterStream = Stream(auth, listener(PUB_SUB_PROJECT, PUB_SUB_TOPIC))
twitterStream.filter(track=["covid"])





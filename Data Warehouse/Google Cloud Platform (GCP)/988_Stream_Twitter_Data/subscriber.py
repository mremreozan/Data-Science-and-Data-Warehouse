# pip3 install --upgrade google-cloud-bigquery

# environment variable setup for private key file
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="qwiklabs-gcp-01-ea893043e169-2bb84456ce58.json"

import json
import base64

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from google.cloud import pubsub_v1

from google.cloud import bigquery

# GCP topic, project & subscription ids
PUB_SUB_TOPIC = "my-python-topic"
PUB_SUB_PROJECT = "qwiklabs-gcp-01-ea893043e169"
PUB_SUB_SUBSCRIPTION = "my-python-topic-sub"
DATASET_ID = "tiwtter_dataset"
TABLE_ID = "twitter_table"
TIMEOUT=200

# For Subscriber 
def receive_tweets(project, subscription_name, callback, timeout):
	subscriber = pubsub_v1.SubscriberClient()
	subscription_path = subscriber.subscription_path(
		project, subscription_name)
	streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
	with subscriber:
		try:
			# When `timeout` is not set, result() will block indefinitely,
			# unless an exception is encountered first.                
			streaming_pull_future.result(timeout=timeout)
		except TimeoutError:
			streaming_pull_future.cancel()

def callback(message):
	#print('Received message: {}'.format(message))
	collect_tweets(message.data, DATASET_ID, TABLE_ID)
	message.ack()	

def collect_tweets(data, dataset_id, table_id):
	tweets = []
	stream = base64.urlsafe_b64decode(data)
	#print(stream)
	twraw = json.loads(stream.decode('utf-8'))
	twmessages = twraw.get('messages')
	for message in twmessages:
		tweets.append(message['data'])

	write_tweets_to_bq(dataset_id, table_id, tweets)

def write_tweets_to_bq(dataset_id, table_id, tweets):
	client = bigquery.Client()
	dataset_ref = client.dataset(dataset_id)
	table_ref = dataset_ref.table(table_id)
	table = client.get_table(table_ref)
	rows_to_insert = []
	for tweet in tweets:
		rows_to_insert.append({u'text':tweet})
	print(rows_to_insert)
	errors = client.insert_rows_json(table, rows_to_insert, row_ids=[None] * len(rows_to_insert))  # Make an API request.
	if errors == []:
		print("New rows have been added.")
	else:
		print("Encountered errors while inserting rows: {}".format(errors))



receive_tweets(PUB_SUB_PROJECT, PUB_SUB_SUBSCRIPTION, callback, TIMEOUT)


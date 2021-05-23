## 1) Create Service Acoount in IAM
	Roles: Pub/Sub Publisher, Pub/Sub Subscriber,
	       Bigquery Admin, Compute Engine Admin
	create json key and download it
	upload it to cloud storage

## 2) Create a database and a table in Bigquery
	you have to create fields according to your data.
	your data coming from pub/sub is dictionary
	your fields have to be same with keys of the distionary

## 3) Create a topic in Pub/Sub 
	you have to be sure to select default subscription while creating topic


## 4) create compute engine 
	install libraries in terminal
		- pip3 install --upgrade google-api-python-client
		- pip3 install --upgrade google-cloud-pubsub
		- pip3 install --upgrade google-cloud-bigquery
		- pip3 install tweepy
	copy json file here from cloud storage
		- gsutil cp gs://qwiklabs-gcp-01-ea893043e169/qwiklabs-gcp-01-ea893043e169-2bb84456ce58.json .

## 5) Change variables in publisher.py and subscriber.py
	GOOGLE_APPLICATION_CREDENTIALS
	PUB_SUB_TOPIC
	PUB_SUB_PROJECT
	PUB_SUB_SUBSCRIPTION
	DATASET_ID
	TABLE_ID

## 6) run publisher.py in terminal 
## 7) run subscriber.py in terminal

## 8) References
	# https://theappliedarchitect.com/setting-up-gcp-pub-sub-integration-with-python/
	# https://faun.pub/writing-a-pub-sub-stream-to-bigquery-401b44c86bf
	# https://www.syntio.net/en/labs-musings/streaming-data-from-twitter-to-gcp
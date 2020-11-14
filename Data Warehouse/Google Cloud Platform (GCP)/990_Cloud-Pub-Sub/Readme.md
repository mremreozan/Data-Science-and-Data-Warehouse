# Streaming Data Processing: Publish Streaming Data into PubSub 

## Objectives

In this lab, you will perform the following tasks:

-- Create a Pub/Sub topic and subscription

-- Simulate your traffic sensor data into Pub/Sub

| Content | Description |
|---|---|
| Task 1 | Preparation |
| Task 2 | Create Pub/Sub topic and subscription |
| Task 3 | Simulate traffic sensor data into Pub/Sub |
| Task 4 | SVerify that messages are received |


## Task 1: Preparation

You will be running a sensor simulator from the training VM. There are several files and some setup of the environment required.
### Open the SSH terminal and connect to the training VM

1. In the Console, on **the Navigation menu**, click **Compute Engine > VM instances**.

2. Locate the line with the instance called **training-vm**.

3. On the far right, under **Connect**, click on **SSH** to open a terminal window.

4. In this lab, you will enter CLI commands on the **training-vm**.

### Verify initialization is complete

 5. The **training-vm** is installing some software in the background. Verify that setup is complete by checking the contents of the new directory.
```bash
ls /training
```
The setup is complete when the result of your list (ls) command output appears as in the image below. If the full listing does not appear, wait a few minutes and try again. Note: It may take 2 to 3 minutes for all background actions to complete.


### Download Code Repository

6. Next you will download a code repository for use in this lab.
```bash
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```
### Identify a project

One environment variable that you will set is **$DEVSHELL_PROJECT_ID** that contains the Google Cloud project ID required to access billable resources.

7. In the Console, on the Navigation menu, click Home. In the panel with Project Info, the Project ID is listed. You can also find this information in the Qwiklabs tab under Connection Details, where it is labeled GCP Project ID.

8. On the training-vm SSH terminal, set the DEVSHELL_PROJECT_ID environment variable and export it so it will be available to other shells. The following command obtains the active Project ID from the Google Cloud environment.
```bash
export DEVSHELL_PROJECT_ID=$(gcloud config get-value project)
```

## Task 2: Create Pub/Sub topic and subscription

 1. On the training-vm SSH terminal, navigate to the directory for this lab.
```bash
cd ~/training-data-analyst/courses/streaming/publish
```
### Verify that the Pub/Sub service is accessible and working using the gcloud command.

2. Create your topic and publish a simple message.
```bash
gcloud pubsub topics create sandiego
```
3. Publish a simple message.
```bash
gcloud pubsub topics publish sandiego --message "hello"
```
4. Create a subscription for the topic.
```bash
gcloud pubsub subscriptions create --topic sandiego mySub1
```
5. Pull the first message that was published to your topic.
```bash
gcloud pubsub subscriptions pull --auto-ack mySub1
```
Do you see any result? If not, why?

6. Try to publish another message and then pull it using the subscription.
```bash
gcloud pubsub topics publish sandiego --message "hello again"
gcloud pubsub subscriptions pull --auto-ack mySub1
```
Did you get any response this time?

7. In the training-vm SSH terminal, cancel your subscription.
```bash
gcloud pubsub subscriptions delete mySub1
```
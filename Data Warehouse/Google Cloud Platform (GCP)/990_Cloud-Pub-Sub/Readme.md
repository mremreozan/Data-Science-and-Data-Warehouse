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

    Next you will download a code repository for use in this lab.

git clone https://github.com/GoogleCloudPlatform/training-data-analyst

Identify a project

One environment variable that you will set is $DEVSHELL_PROJECT_ID that contains the Google Cloud project ID required to access billable resources.

    In the Console, on the Navigation menu ( 7a91d354499ac9f1.png), click Home. In the panel with Project Info, the Project ID is listed. You can also find this information in the Qwiklabs tab under Connection Details, where it is labeled GCP Project ID.

    On the training-vm SSH terminal, set the DEVSHELL_PROJECT_ID environment variable and export it so it will be available to other shells. The following command obtains the active Project ID from the Google Cloud environment.

export DEVSHELL_PROJECT_ID=$(gcloud config get-value project)

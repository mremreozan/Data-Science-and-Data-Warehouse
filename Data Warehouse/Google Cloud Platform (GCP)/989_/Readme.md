# Streaming Data Processing: Streaming Data Pipelines 

## Objectives

In this lab, you will perform the following tasks:

-- Launch Dataflow and run a Dataflow job

-- Understand how data elements flow through the transformations of a Dataflow pipeline

-- Connect Dataflow to Pub/Sub and BigQuery

-- Observe and understand how Dataflow autoscaling adjusts compute resources to process input data optimally

-- Learn where to find logging information created by Dataflow

-- Explore metrics and create alerts and dashboards with Cloud Monitoring

| Content | Description |
|---|---|
| Task 1 | Preparation |
| Task 2 | Create a BigQuery Dataset and Cloud Storage Bucket |
| Task 3 | Simulate traffic sensor data into Pub/Sub |
| Task 4 | Launch Dataflow Pipeline |
| Task 5 | Explore the pipeline |
| Task 6 | Determine throughput rates |
| Task 7 | Review BigQuery output |
| Task 8 | Observe and understand autoscaling |
| Task 9 | Refresh the sensor data simulation script |
| Task 10 | Cloud Monitoring integration |
| Task 11 | Explore metrics |
| Task 12 | Create alerts |
| Task 13 | Set up dashboards |
| Task 14 | Launch another streaming pipeline |
  
## Task 1: Preparation

You will be running a sensor simulator from the training VM. In Lab 1 you manually setup the Pub/Sub components. In this lab several of those processes are automated.
Open the SSH terminal and connect to the training VM

1. In the Console, on the Navigation menu ( 7a91d354499ac9f1.png), click Compute Engine > VM instances.

2. Locate the line with the instance called training-vm.

3. On the far right, under Connect, click on SSH to open a terminal window.

4. In this lab, you will enter CLI commands on the training-vm.

### Verify initialization is complete

5. The training-vm is installing some software in the background. Verify that setup is complete by checking the contents of the new directory.
```bash
ls /training
```
The setup is complete when the result of your list (ls) command output appears as in the image below. If the full listing does not appear, wait a few minutes and try again. Note: It may take 2 to 3 minutes for all background actions to complete.

### Download Code Repository

6. Next you will download a code repository for use in this lab.
```bash
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```
### Set environment variables

7. On the training-vm SSH terminal enter the following:
```bash
source /training/project_env.sh
```
This script sets the DEVSHELL_PROJECT_ID and BUCKET environment variables.

## Task 2: Create a BigQuery Dataset and Cloud Storage Bucket

The Dataflow pipeline will be created later and will write into a table in the BigQuery dataset.
### Create a BigQuery Dataset
#### Open BigQuery Console

In the Google Cloud Console, select Navigation menu > BigQuery:

The Welcome to BigQuery in the Cloud Console message box opens. This message box provides a link to the quickstart guide and lists UI updates.

Click Done.

In your BigQuery project, create a new dataset entitled **demos**.

1. In the left pane in the Resources section, click on your BigQuery project (qwiklabs-gcp-xxxx).

2. To the right, under the Query editor, click CREATE DATASET.

The Create dataset dialog opens.

3. Set the Dataset ID to demos and leave all other options at their default values.

4. To finish, click the blue Create dataset button

### Verify the Cloud Storage Bucket

A bucket should already exist that has the same name as the Project ID.

5. In the Console, on the Navigation menu ( 7a91d354499ac9f1.png), click Storage > Browser.

6. Observe the following values:

| Property | Value

(type value or select option as specified) |
|---|---|
| Name | <Same as the Project ID> |
| Default storage class | Regional |
| Location | us-central1 |


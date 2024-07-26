# Docker Image for NER API

This guide provides detailed instructions on how to build, run, and test the Docker image for this Named Entity Recognition (NER) API.

## Building the Docker Image

### Step 1: Build the Docker Image

To build the Docker image for the FastAPI application, navigate to the `ner_api` directory in the terminal and run the following command:

```sh
docker build -t ner-api:latest .
```

### Step 2: Run the Docker Container

After successfully building the image, run a container from it using the following command:

```sh
docker run -d -p 8000:8000 --name ner-api-container ner-api:latest
```

### Step 3: Verify the Deployment

Once the container is running, you can test your API by sending a POST request to http://localhost:8000/predict/.


To verify the FastAPI application is running inside the container, open a web browser and navigate to:

```bash
http://localhost:8000/docs
```

## Testing the Docker Image

### Step 1: Ensure the Container is Running

Before testing the API, ensure that the Docker container is running. You can check the status of your container using the following command:

```sh
docker ps
```

This command lists all running containers. Look for ner-api-container in the output to confirm that your container is running.

### Step 2: Run the Test Script

To test the API, you can use the provided `tests/test_api.py` script. This script sends a POST request to the API and prints the response. Run the script with the following command:

```sh
python tests\test_api.py "John Smith lives in Los Angeles"
```

If the API is working correctly, the script will output the NER predictions for the input text. Here is an example of the expected output:

```
{
  "entities": [
    ["john", "B-PER"], 
    ["smith", "I-PER"],
    ["lives", "O"], 
    ["in", "O"], 
    ["los", "B-LOC"], 
    ["angeles", "I-LOC"]
  ]
} 

Entities and their tags:

Token: john, Tag: B-PER
Token: smith, Tag: I-PER
Token: lives, Tag: O
Token: in, Tag: O
Token: los, Tag: B-LOC
Token: angeles, Tag: I-LOC
```
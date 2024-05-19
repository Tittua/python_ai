Data Cleaning and Analysis Script
This script performs data extraction, cleaning, and analysis from a given API endpoint. It fetches messages with sources, processes the data, computes similarity scores between responses and their corresponding sources using spaCy's NLP model, and outputs a JSON structure with IDs and links based on a similarity threshold.

Prerequisites
Python 3.6 or higher
Required Python libraries: json, requests, pandas, spacy
spaCy language model: en_core_web_lg
Installation
Step 1: Clone the Repository
Clone the repository to your local machine:

sh
Copy code
git clone (https://github.com/Tittua/python_ai.git)
cd data-cleaning-script

Step 2: Install Dependencies
Install the required libraries:

Copy code
pip install requests pandas spacy
Step 3: Download spaCy Model
Download the en_core_web_lg model:


python -m spacy download en_core_web_lg
Usage
Step 1: Run the Script
Run the Python script:

sh
Copy code
python data_cleaning_script.py
Step 2: Output
The script will print the resulting JSON structure with IDs and links based on the similarity threshold.

Detailed Explanation
Script Overview
The script performs the following steps:

Import the Libraries: Imports necessary libraries for JSON handling, HTTP requests, data manipulation, and natural language processing.
Load the spaCy Model: Loads the en_core_web_lg model from spaCy for NLP tasks.
Fetch Data from the API Endpoint: Makes an HTTP GET request to fetch data from the specified API endpoint and parses the response into JSON format.
Initialize Lists for Data Cleaning and Analysis: Initializes several lists to store various elements extracted from the JSON data such as IDs, responses, sources, and links.
Extract Data from JSON and Populate Lists: Iterates over the JSON data to extract and append id, response, and source into their respective lists.
Create a DataFrame from Extracted Data: Uses pandas to create a DataFrame from the extracted data, organizing it into a tabular format.
Compute Similarity and Filter Results: For each response, computes the similarity between the response and each of its sources using spaCy's NLP model. If the similarity score is above a threshold (0.45), appends the relevant IDs and links to the lists.
Convert Filtered Results into JSON Format: Combines the filtered results into a list of dictionaries, each containing an id and a link. Converts this list into a JSON string with pretty-print formatting.
Print the JSON Output: Outputs the JSON string containing the filtered results.

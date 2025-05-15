Streetwear JSON API Project – Digital Ecosystem (DES)

Project Overview

As part of our Digital Ecosystem (DES) course, we completed a project that involved creating a custom JSON API hosted on GitHub Pages, and then developing a Python script to fetch and display this data.

We chose the theme of a streetwear brand, which allowed us to work on concepts related to data management, API usage, and static web hosting through GitHub Pages.

The goal was to apply the skills learned in class to manipulate JSON data and use Python to interact with external APIs.

Project Description

We created a JSON file (streetwear_data.json) containing several objects representing different items from the streetwear brand. Each object includes:

name: the name of the item (e.g., "Sneakers X")
description: a short description of the item
specifications: an object with technical details (color, size, etc.)
tags: an array of keywords related to the item (e.g., ["shoes", "urban", "comfort"])
This data is publicly hosted on GitHub Pages to be accessible via a URL.

How the Python Script Works

The fetch_data.py script uses the Python requests library to fetch the JSON data directly from the GitHub Pages URL.

Once downloaded, the script parses the data (converts it into Python objects) and then prints the key information of each item in the console: name, description, specifications, and tags.

The script also includes simple error handling to display a clear message if data retrieval fails (network issues, incorrect URL, etc.).

Installation and Usage

To use this project, follow these steps:

Clone the repository
Open your terminal and type:
git clone https://github.com/Sekou2oo4/streetwear-json-project.git
Install the requests library
If it’s not already installed on your machine, run:
pip install requests
Run the Python script
Navigate to the project folder and execute:
cd streetwear-json-project
python3 fetch_data.py
You will then see the information for each streetwear item clearly displayed in the console.

Project File Structure

Here is the structure of our project:

streetwear-json-project/
│
├── fetch_data.py           # Python script that fetches and displays the JSON data
├── streetwear_data.json    # JSON file containing our streetwear item data
├── README.md               # Project documentation
Hosting and Accessing the JSON Data

The streetwear_data.json file is hosted on GitHub Pages, making it accessible via the public URL:

https://sekou2oo4.github.io/streetwear-json-project/streetwear_data.json

This URL is used by the Python script to fetch the data.

Challenges and Solutions

Error handling in Python: We had to add try/except blocks to manage cases where the connection to the URL might fail.
Hosting on GitHub Pages: We learned how to enable GitHub Pages to make our JSON file publicly accessible.
These steps enhanced our practical understanding of collaborative tools and web development.

Group Members

Sekou Doucoure
Dikra
Joelle

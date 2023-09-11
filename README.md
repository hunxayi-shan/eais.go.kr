# Eais [eais.go.kr]
Issuance of Building Ledger - eais.go.kr

# Recording of the execution of the script
https://github.com/hunxayi-shan/eais.go.kr/assets/96914475/42557311-2acd-4fdc-912d-3d692308001f

# Assessment Task - Crawling RPA

This repository documents my experience and approach to completing a Crawling RPA (Robotic Process Automation) assessment task assigned by a company. The task involved extracting data from a website, and I'd like to share the process and challenges I encountered during the assessment.

## Table of Contents
- [Introduction](#introduction)
- [Challenges Faced](#challenges-faced)
- [My Approach](#my-approach)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)
- [Requirements to Run the Script](#requirements-to-run-the-script)

## Introduction

I was approached by a company to attempt an assessment test, which included Task 1, Crawling RPA. Here's a breakdown of my experience and the challenges I encountered during the assessment.

## Challenges Faced

1. **Authentication Issues:** Initially, I faced issues with the provided usernames and passwords. They did not work, so I had to create my own international account to proceed with the task.

2. **Language Choice:** The assessment recommended using JavaScript libraries, but my expertise lies in Python. Therefore, I decided to implement the task using Python, Selenium, and the Selenium Chrome driver manager.

3. **Data Quality:** There was an option (link) that contained null values for many of the addresses provided in the assessment. As a result, I chose the first option to attempt the task:
  
   ![red](https://github.com/hunxayi-shan/eais.go.kr/assets/96914475/c646b380-ea4c-41b9-a1d5-7e8c79f4227b)


## My Approach

I designed a Python script to address the assessment task, which involved handling multiple addresses from a list. Here's a summary of my approach:

1. **Address Formatting:** I formatted the addresses to the specified usable format on the website.

2. **Automation:** I used Selenium and the Selenium Chrome driver manager to automate the web scraping process.

3. **PDF Generation:** I iterated over the list of addresses, saving a PDF file for each address as per the assessment requirements saved it to local downloads directory of the project.

## Usage

Feel free to explore the code and adapt it to your needs. You can clone this repository and run the Python script to automate web scraping and PDF generation based on your specific requirements.

## Acknowledgements

I would like to thank the company for providing me with the opportunity to attempt this assessment. Despite the challenges I faced, it was a valuable learning experience.

If you have any questions or suggestions, please don't hesitate to reach out.

## Requirements to Run the Script

To run the script on your local system, you will need the following:

- Python 3.8 or above
- Jupyter Notebook
- Chrome browser
- Python libraries: pandas, selenium, os, json, pathlib
- Visual Studio Code (recommended as the development environment)
- Use pip to install the required libraries

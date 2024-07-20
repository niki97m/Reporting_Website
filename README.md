# Report Unusual Effects

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data Requirements](#data-requirements)
6. [Form Description](#form-description)
7. [Web Application](#web-application)
8. [Code Structure](#code-structure)
9. [Contact](#contact)

## Introduction

The Report Unusual Effects tool is a web application designed to collect and report unusual or concerning effects from drugs in British Columbia. This tool is vital for public health and safety professionals, researchers, and harm reduction advocates.

Understanding the effects of various drugs is crucial for:
- Assessing the safety of drugs in the community
- Developing appropriate harm reduction strategies
- Informing medical treatment protocols for drug-related incidents
- Guiding policy decisions and public health interventions

This application uses a data-driven approach to provide a platform for anonymous reporting, ensuring that the information can be used to keep the community safe.

## Features

1. **Interactive Form**: Users can fill out a detailed form to report their experiences with drugs.
2. **Anonymous Reporting**: Ensures confidentiality and anonymity of the users.
3. **Validation**: Validates user inputs to ensure completeness and correctness.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
   
   ```bash
   git clone https://github.com/niki97m/report-unusual-effects.git
   cd report-unusual-effects

2. Create a virtual environment (optional but recommended):
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. Install the required packages:
   
   ```bash
   pip install -r requirements.txt
   
## Usage

To run the application:

1. Navigate to the project directory.
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
3. Open a web browser and go to http://localhost:8501 (or the address provided in the terminal).

## Data Requirements

The application reads a CSV file with the following structure:
- The first column should contain the names of the drugs.

Ensure that the CSV file is placed in the same directory as the Streamlit app script and named `Drug_list.csv`.

## Form Description

The form includes the following fields:
1. **When did this happen?**: A date input field.
2. **Location**: A dropdown to select the location where the incident happened.
3. **I'm in British Columbia**: A checkbox to confirm the user is in British Columbia.
4. **Describe your experience**: A text area for detailed descriptions of the experience.
5. **Was the batch tested previously in a lab?**: A radio button to select Yes or No.
6. **What did you take?**: A multi-select dropdown to choose the drugs taken.
7. **Where did you get it?**: A dropdown to select the source of the drug.
8. **Email (optional)**: An optional email input for further contact.

## Web Application

The web application is built using Streamlit and consists of several sections:

1. **Title and Introduction**: Explains the purpose and importance of the tool.
2. **Explanations**: Provides details about harm reduction and the anonymous nature of the report.
3. **Instructions**: Guides users on how to fill out the form.
4. **Form**: Includes fields for date, location, experience description, and more.
5. **Submission Handling**: Validates inputs and submits the data to Formspree.

## Code Structure

The main application code (`app.py`) is structured as follows:

1. **Import Statements**: Importing necessary libraries (Streamlit, Pandas, Requests, Datetime).
2. **Title and Introduction**: Setting up the app's title and introductory text.
3. **Form Definition**: Implementing the form fields for user input.
4. **Data Processing**: Reading the CSV file to get the list of drugs.
5. **Form Validation**: Ensuring that all required fields are filled in correctly.
6. **Form Submission**: Sending the form data to Formspree for email handling.

## Contact

For questions, suggestions, or collaborations, please contact:

[Niki Mahmoodzadeh]  
Email: [niki.mahmoodzadeh@mail.mcgill.ca]

Project Link: [https://github.com/niki97m/report-unusual-effects](https://github.com/niki97m/report-unusual-effects)

Live Application: [https://report-unusual-effects.streamlit.app](https://report-unusual-effects.streamlit.app)

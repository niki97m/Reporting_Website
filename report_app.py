import streamlit as st
import pandas as pd
import os
import requests
from datetime import date

# Function to get the list of drugs from a CSV file
def get_drug_list(csv_path):
    if not os.path.isfile(csv_path):
        st.error(f"File not found: {csv_path}")
        return []
    df = pd.read_csv(csv_path)
    drug_list = df.iloc[:, 0].tolist()  # the drugs are in the first column
    drug_list.sort()  # Sort the list alphabetically
    return drug_list

# Function to send form data via Formspree
def send_formspree(submitted_data):
    formspree_url = "https://formspree.io/f/myzgzljj"  # Replace with Formspree endpoint URL
    response = requests.post(formspree_url, data=submitted_data)
    
    # if response.status_code == 200:
    #     st.success("Report submitted successfully and email sent.")
    # else:
    #     st.error(f"Failed to send email: {response.status_code} - {response.text}")

# Path to CSV file in the repository
csv_path = 'Drug_list.csv'

# Get the list of drugs
drug_list = get_drug_list(csv_path)

if not drug_list:
    st.error("Drug list is empty. Please check the CSV file.")
else:
    st.title('Report Unusual Effects')
    
    st.write("""
    **Harm Reduction Report**

    This report is used for harm reduction, it is totally anonymous, not protecting by law or police, and is for research processes and wellness awareness.

    If you or someone you know has experienced unexpected or concerning effects from drugs in British Columbia, please let us know below. This will help keep others safe.

    Please provide as much information as you can, it will be kept confidential and won't be shared with anyone else. You also don't need to give us any personal information if you don't want to.

    **Please do not use this form if you need immediate help - we can't guarantee a quick response. **If you're experiencing an emergency, please call 911 immediately.**
    """)

    # Form
    with st.form(key='report_form'):
        when_happened = st.date_input('When did this happen?', value=None, max_value=date.today())
        location = st.selectbox('Location', ['Please specify', 'Vancouver', 'Victoria', 'Kelowna', 'Burnaby', 'Other'], help="Select the location where the incident happened.")
        in_bc = st.checkbox("I'm in British Columbia")

        experience = st.text_area('Describe your experience*', 
                                  help="Please provide as much information as you can. This can include symptoms, any overdose experience, anything unusual, etc.", 
                                  placeholder="Describe your experience here")

        batch_tested = st.radio("Was the batch tested previously in a lab?*", ['Yes', 'No'], index=None)
        
        drug_list.insert(0, "Please specify")
        drug_taken = st.multiselect('What did you take?*', drug_list, help="Select the drug(s) you took from the list.")
        where_got = st.selectbox('Where did you get it?', ['Please specify', 'Bought it online', 'From a friend', 'From a dealer', 'Other'], help="Select where you got the drug.")
        
        email = st.text_input('Email (optional)', 
                              help="Provide your email if you want us to contact you for more information.")

        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if not experience or not drug_taken or batch_tested not in ['Yes', 'No']:
            st.error('Please fill in all required fields before submitting the form.')
        else:
            # Validate the email field
            if email and '@' not in email:
                st.error('Please enter a valid email address.')
            else:
                st.success('Thank you for your report. We will review the information provided.')

                # Process the form data as needed
                submitted_data = {
                    'When': str(when_happened) if when_happened != date.today() else "Not specified",
                    'Location': location if location != 'Please specify' else "Not specified",
                    'In BC': in_bc,
                    'Experience': experience,
                    'Batch Tested': batch_tested,
                    'Drug Taken': ", ".join(drug_taken) if drug_taken else "Not specified",
                    'Where Got': where_got if where_got != 'Please specify' else "Not specified"
                }

                if email:
                    submitted_data['Email'] = email

                send_formspree(submitted_data)

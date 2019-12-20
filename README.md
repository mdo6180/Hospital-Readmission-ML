# Hospital-Readmission-ML
A machine learning model to classify patients who are at risk of hospital readmission

Dataset is available at: https://archive.ics.uci.edu/ml/datasets/diabetes+130-us+hospitals+for+years+1999-2008#

Dataset statistics available in the paper in tables 1, 2, & 3: https://www.hindawi.com/journals/bmri/2014/781670/

Features weight, payer_code, and medical_specialty were removed from the dataset because 97%, 52%, and 53% of data points were missing values for these features respectively

Features Encounter ID (encounter_id), Patient Number (patient_nbr) were removed from data set because both features are just identifiers for the hospital visit and the patient and therefore irrelevent. 

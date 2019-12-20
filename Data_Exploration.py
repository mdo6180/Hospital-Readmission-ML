from pandas import read_csv

dataset = read_csv('./dataset_diabetes/diabetic_data.csv')

# dropping 'weight', 'payer_code', 'medical_specialty' because fields are missing in 97%, 52%, and 53% of data points respectively
# dropping 'encounter_id', 'patient_nbr' because fields are just identifiers
dataset = dataset.drop(columns=['encounter_id', 'patient_nbr', 'weight',
                                'payer_code', 'medical_specialty', 'change', 'diabetesMed'])

# dropping data point if patient has no record of readmission
NO_index = dataset[dataset['readmitted'] == 'NO'].index
dataset = dataset.drop(index=NO_index)

print(dataset.shape)
print(dataset.columns.values)





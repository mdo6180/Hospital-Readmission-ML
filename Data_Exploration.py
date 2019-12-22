from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np

dataset = read_csv('./dataset_diabetes/diabetic_data.csv')

# dropping 'weight', 'payer_code', 'medical_specialty' because fields are missing in 97%, 52%, and 53% of data points respectively
# dropping 'encounter_id', 'patient_nbr' because fields are just identifiers
dataset = dataset.drop(columns=['encounter_id', 'patient_nbr', 'weight',
                                'payer_code', 'medical_specialty', 'change', 'diabetesMed'])

num_less_than_30 = len(dataset[dataset['readmitted'] == '<30'].index)
num_more_than_30 = len(dataset[dataset['readmitted'] == '>30'].index)
num_not_readmitted = len(dataset[dataset['readmitted'] == 'NO'].index)
labels_stats = [num_less_than_30, num_more_than_30, num_not_readmitted]
ind = np.arange(len(labels_stats))

plt.bar(ind, labels_stats, align='center', width=0.35)
plt.title('Hospital Readmission Statistics')
plt.ylabel('Number of Patients', labelpad=5)
plt.xlabel('Time Frame of Readmission', labelpad=5)
plt.xticks(ind, ('<30 Days', '>30 Days', 'Not Readmitted'))
plt.show()

'''
# dropping data point if patient has no record of readmission
NO_index = dataset[dataset['readmitted'] == 'NO'].index
dataset = dataset.drop(index=NO_index)

over_30 = dataset[dataset['readmitted'] == '>30'].index
over_30 = over_30[0:13000]
dataset = dataset.drop(index=over_30)

'''




from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np

data_set = read_csv('./dataset_diabetes/diabetic_data.csv')

# dropping 'weight', 'payer_code', 'medical_specialty' because fields are missing in 97%, 52%, and 53% of data points respectively
# dropping 'encounter_id', 'patient_nbr' because fields are just identifiers
data_set = data_set.drop(columns=['encounter_id', 'patient_nbr', 'weight',
                                  'payer_code', 'medical_specialty', 'change', 'diabetesMed'])

'''
num_less_than_30 = len(data_set[data_set['readmitted'] == '<30'].index)
num_more_than_30 = len(data_set[data_set['readmitted'] == '>30'].index)
num_not_readmitted = len(data_set[data_set['readmitted'] == 'NO'].index)
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
NO_index = data_set[data_set['readmitted'] == 'NO'].index
data_set = data_set.drop(index=NO_index)

# balance data set by dropping 23,000 '>30' data points to reduce data set to a little over 12,000 '>30' data points
over_30 = data_set[data_set['readmitted'] == '>30'].index
over_30 = over_30[0:23000]
data_set = data_set.drop(index=over_30)

data_set = data_set.sample(frac=1, random_state=1)    # shuffle data set

'''
num_less_than_30 = len(data_set[data_set['readmitted'] == '<30'].index)
num_more_than_30 = len(data_set[data_set['readmitted'] == '>30'].index)
labels_stats = [num_less_than_30, num_more_than_30]
ind = np.arange(len(labels_stats))

plt.bar(ind, labels_stats, align='center')
plt.title('Hospital Readmission Statistics')
plt.ylabel('Number of Patients', labelpad=5)
plt.xlabel('Time Frame of Readmission', labelpad=5)
plt.xticks(ind, ('<30 Days', '>30 Days'))
plt.show()
'''

num_a1c_over8 = len(data_set[data_set['A1Cresult'] == '>8'])
num_a1c_over7 = len(data_set[data_set['A1Cresult'] == '>7'])
num_a1c_normal = len(data_set[data_set['A1Cresult'] == 'Norm'])
num_a1c_none = len(data_set[data_set['A1Cresult'] == 'None'])
labels_stats = [num_a1c_over8, num_a1c_over7, num_a1c_normal, num_a1c_none]
ind = np.arange(len(labels_stats))

plt.bar(ind, labels_stats, align='center')
plt.title('A1C Results Statistics')
plt.ylabel('Number of Patients', labelpad=5)
plt.xlabel('A1C Results (%)', labelpad=5)
plt.xticks(ind, ('>8', '>7', 'Normal', 'None'))
plt.show()

glucose_over200 = len(data_set[data_set['max_glu_serum'] == '>200'])
glucose_over300 = len(data_set[data_set['max_glu_serum'] == '>300'])
glucose_normal = len(data_set[data_set['max_glu_serum'] == 'Norm'])
glucose_none = len(data_set[data_set['max_glu_serum'] == 'None'])
labels_stats = [glucose_over200, glucose_over300, glucose_normal, glucose_none]
ind = np.arange(len(labels_stats))

plt.bar(ind, labels_stats, align='center')
plt.title('Max Glucose Serum Test Results Statistics')
plt.ylabel('Number of Patients', labelpad=5)
plt.xlabel('Max Glucose Serum Test Results', labelpad=5)
plt.xticks(ind, ('>200', '>300', 'Normal', 'None'))
plt.show()

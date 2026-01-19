import pandas as pd

df = pd.read_csv("students.csv")
print(df.head())
print(df.info())


mean_value = df['Attendance'].mean()
print('mean attendeance: '+str(mean_value))

min_values = df['Attendance'].min()
print('lowest attendance: '+str(min_values))

max_values = df['Attendance'].max()
print('highest attendance: '+str(max_values))

below = df[df['Attendance'] <= 80]
print('learners with a chance of failures: '+str(below))

above = df[df['Attendance'] >= 90]
print('learners with a chance of passing: '+str(above))

grade_counts = df['Grade'].value_counts().sort_index()
print('number of students achieving each grade: '+str(grade_counts))

learner_at_risk = df[df['Attendance'] <= 80]
print('learners at risk: '+str(learner_at_risk))

at_risk = df[df['Attendance'] < 80 ][['Name']]
print('learners at risk due to low attendance: '+str(at_risk))
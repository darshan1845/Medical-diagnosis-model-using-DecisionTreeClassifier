import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv(r'medical_diagnosis_1200rows_training.csv')
# print(df.head())

# print(df.isna().sum())
# print(df.shape)
# print(df.duplicated().sum())

df.dropna(inplace=True)
# print(df.isna().sum())
# print(df.shape)

#Encoding
oe = OrdinalEncoder()
df[['FamilyHistory','Smoking','Alcohol','StressLevel','Disease']] = oe.fit_transform(df[['FamilyHistory','Smoking','Alcohol','StressLevel','Disease']])
# print(df[['FamilyHistory','Smoking','Alcohol','StressLevel','Disease']].head())
# outlier removal

Q1 = df['Disease'].quantile(0.25)
Q3 = df['Disease'].quantile(0.75)
# print(Q1, Q3)

IQR = Q3 - Q1
# print(IQR)

min = Q1 - 1.5 * IQR
max = Q3 + 1.5 * IQR
# print(min, max)

df = df.loc[(df['Disease']>=min) & (df['Disease']<=max)]
# print(df.shape)

x = df[['Age','BP_systolic','Cholesterol','Weight_kg','BMI','BloodSugar','FastingSugar','ExerciseHours_Week','FamilyHistory','Smoking','Alcohol','StressLevel']]
y = df['Disease']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
accuracy = round(accuracy * 100, 2)
print('Model accuracy: ',accuracy,'%')

fh= open('model.pkl', 'wb')
pickle.dump(model, fh)

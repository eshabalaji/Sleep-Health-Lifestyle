# Sleep Health & Lifestyle

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#To display the Data set

data=pd.read_csv('C:\\Users\\balaj\\Downloads\\archive (2)\\Sleep_health_and_lifestyle_dataset.csv')
data

data.describe()

data.isnull().sum()

data.info()

(data==0).sum(axis=0)

data['Sleep Disorder'] = data['Sleep Disorder'].fillna('None')

#Renaming Normal Weight as Normal for easier analysis
data['BMI Category'] = data['BMI Category'].replace({'Normal Weight': 'Normal'})

#To display the count of each category
plt.figure(figsize=(16, 16))

# Gender
plt.subplot(4, 3, 1)
g=sns.countplot(x='Gender', data=data)
g.bar_label(g.containers[0])
plt.title('Gender Distribution')

# Age
plt.subplot(4, 3, 2)
a=sns.histplot(data['Age'], kde=True)
a.bar_label(a.containers[0])
plt.title('Age Distribution')

# Occupation
plt.subplot(4, 3, 3)
o=sns.countplot(x='Occupation', data=data)
o.bar_label(o.containers[0])
plt.title('Occupation Distribution')

# Sleep Duration
plt.subplot(4, 3, 4)
s=sns.histplot(data['Sleep Duration'], kde=True)
s.bar_label(s.containers[0])
plt.title('Sleep Duration Distribution')

# Quality of Sleep
plt.subplot(4, 3, 5)
q=sns.countplot(x='Quality of Sleep', data=data)
q.bar_label(q.containers[0])
plt.title('Quality of Sleep Distribution')

# Physical Activity Duration
plt.subplot(4, 3, 6)
p=sns.histplot(data['Physical Activity Level'], kde=True)
p.bar_label(p.containers[0])
plt.title('Physical Activity Duration Distribution')

# Stress Levels
plt.subplot(4, 3, 7)
sns.histplot(data['Stress Level'], kde=True)
plt.title('Stress Levels Distribution')

# BMI Category
plt.subplot(4, 3, 8)
bm=sns.countplot(x='BMI Category', data=data)
plt.title('BMI Category Distribution')

# Daily Steps
plt.subplot(4, 3, 9)
sns.histplot(data['Daily Steps'], kde=True)
plt.title('Daily Steps Distribution')


#heart rate
plt.subplot(4, 3, 10)
sns.histplot(data['Heart Rate'], kde=True)
plt.title('Heart Rate')


#sleep diorder
plt.subplot(4, 3, 11)
sd=sns.countplot(x='Sleep Disorder', data=data)
sd.bar_label(sd.containers[0])

plt.title('Sleep Disorder')

#blood pressure
plt.subplot(4, 3, 12)
sns.histplot(data['Blood Pressure'], kde=True)
plt.title('Blood Pressure')

plt.tight_layout()
plt.show()

#Describes the Data count of each category
data.describe()

#Total there are 374 entries in this data set.
#1)Age group of the people in the data set is from 27-59
#2)the minimum sleep duration of a person is about 4hrs and maximim is 8.5hrs.maj of the people sleep around 7hrs.
#3)on an average step count is around 7k
#4)daily activity is around 30-90min daily.

# Gender vs Sleep Duration
plt.figure(figsize=(3,3))
t=sns.barplot(x='Gender', y='Sleep Duration', data=data)
t.bar_label(t.containers[0])
plt.title('Gender vs. Sleep Duration')
plt.show()

'''From the above plot we can infer that avg men sleep around 7.03hrs where as women sleep around 7.22hrs which is slightly 
more than men.'''

# Age vs Heart Rate:
plt.figure(figsize=(3,3))
sns.scatterplot(x='Age', y='Heart Rate', data=data)
plt.title('Age vs. Heart Rate')
plt.show()

plt.figure(figsize = (20, 10))

plt.subplot(2, 1, 1)
plt.gca().set_title('Variable Occupation')
occ=sns.countplot(x = 'Occupation', palette = 'Set2', data = data)
occ.bar_label(occ.containers[0])

plt.subplot(2, 1, 2)
plt.gca().set_title('Variable Blood Pressure')
bp=sns.countplot(x = 'Blood Pressure', palette = 'Set2', data = data)


labels=data['Occupation'].unique()
sizw=data['Occupation'].value_counts()
p=plt.pie(sizw,labels=labels)
plt.show()

plt.title("Boxplot Sleep Duration", fontdict = {'fontsize': 20})
sns.boxplot(x=data["Sleep Duration"])

plt.title("Boxplot Quality of Sleep", fontdict = {'fontsize': 20})
sns.boxplot(x=data["Quality of Sleep"])


plt.figure(figsize = (20, 10))
plt.suptitle("Analysis Of Variable Sleep Disorder",fontweight="bold", fontsize=20)

plt.subplot(2, 1, 1)
plt.gca().set_title('Variable Gender')
sl=sns.countplot(x = 'Gender', hue = 'Sleep Disorder', palette = 'Set2', data = data)
sl.bar_label(sl.containers[0])

plt.subplot(2, 1, 2)
plt.gca().set_title('Variable BMI Category')
c=sns.countplot(x = 'BMI Category', hue = 'Sleep Disorder', palette = 'Set2', data = data)
c.bar_label(c.containers[0])

plt.figure(figsize = (25, 20))
plt.suptitle("Analysis Of Variable Sleep Disorder",fontweight="bold", fontsize=20)

plt.subplot(4,2,1)
sns.lineplot(x="Sleep Disorder", y="Age", data=data, marker='o')
plt.title("Age vs. Sleep Disorder")

plt.subplot(4,2,2)
sns.lineplot(x="Sleep Disorder", y="Sleep Duration", data=data,marker='o')

plt.subplot(4,2,3)
sns.lineplot(x="Sleep Disorder", y="Quality of Sleep", data=data,marker='o')

plt.subplot(4,2,4)
sns.lineplot(x="Sleep Disorder", y="Physical Activity Level", data=data,marker='o')

plt.subplot(4,2,5)
sns.lineplot(x="Sleep Disorder", y="Stress Level", data=data,marker='o')

plt.subplot(4,2,6)
sns.lineplot(x="Sleep Disorder", y="Heart Rate", data=data,marker='o')

plt.subplot(4,2,7)
sns.lineplot(x="Sleep Disorder", y="Daily Steps", data=data,marker='o')

plt.figure(figsize=(12, 4))#plot Age vs Sleep Duration
sns.heatmap(data.pivot_table(index='Physical Activity Level', values='Sleep Duration', 
                             aggfunc='mean'), annot=True, cmap='viridis')
plt.ylabel('Physical Activity Level')#plt.xlabel('Sleep Duration')
plt.title('Physical Activity Level vs. Sleep Duration')
plt.show()

'''x-axis represents Sleep Duration and y-axis represents Physical Activity Level.
The average sleep duration of people doing defferent physical activities are given by calculating the mean sleep duration.'''

#To display the sleep duration vs occupation
occupation_sleep_heatmap = data.pivot_table(index='Occupation', values='Sleep Duration', aggfunc='mean')

plt.figure(figsize=(12, 4))
sns.heatmap(occupation_sleep_heatmap, annot=True, cmap='viridis', fmt=".1f", linewidths=.5)

# Set labels and title
#plt.xlabel('Sleep Duration')
plt.ylabel('Occupation')
plt.title('Occupation vs. Sleep Duration')

plt.show()

#To display the Quality of Sleep vs occupation
occupation_sleep_heatmap = data.pivot_table(index='Occupation', values='Quality of Sleep', aggfunc='mean')

plt.figure(figsize=(12, 4))
sns.heatmap(occupation_sleep_heatmap, annot=True, cmap='viridis', fmt=".1f", linewidths=.5)

# Set labels and title
#plt.xlabel('Sleep Duration')
plt.ylabel('Occupation')
plt.title('Occupation vs. Quality of Sleep')

plt.show()
'''
CONCLUSION:From this data set few of the conclusions that we can draw is
    1)there are more male than female
    2)majority people have their occupation as Nurse,Engineers and doctors
    3)many people are normal and few of them are suffering from sleep apnea and insomania
    4)people suffering from insomania have high stress levels when compared to others.
    5)people suffering from sleep apnea have generally higher heart rate
    6)the average step count is around 7K which is the min step count suggested by WHO
    7)people who have more physical activities have normal sleeping hrs 
    8)As per the survey Engineers have more sleep duration and better sleep quality.
'''

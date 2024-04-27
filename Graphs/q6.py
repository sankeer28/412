import matplotlib.pyplot as plt
import csv
import numpy as np
#go through csv and record store answers
responses=[]
with open('ChatGPT (Responses) - Form Responses 1.xlsx - in.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        responses.append(row[5])
#count answers
q1=responses.count("Teenager:13-19 years")
q2=responses.count("Young adult: 20-29 years")
q3=responses.count("Middle-aged adult: 30-59 years")
q4=responses.count("Senior citizen: 60 years and older")
#info for graph
x=np.array([q1,q2,q3,q4])
mlabels=["Teenager:13-19 years","Young adult: 20-29 years",
         "Middle-aged adult: 30-59 years","Senior citizen: 60 years and older"]
#create graph
plt.pie(x,labels=mlabels,autopct='%1.1f%%', textprops={'fontweight': 'bold'})
plt.title("Ages of Sample", fontweight='bold')
plt.show()

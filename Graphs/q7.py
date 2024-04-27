import matplotlib.pyplot as plt
import csv
import numpy as np
#go through csv and store answers
responses=[]
with open('ChatGPT (Responses) - Form Responses 1.xlsx - in.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        responses.append(row[7])
#count answers
q1=responses.count("Male")
q2=responses.count("Female")
q3=responses.count("Prefer not to say")
q4=responses.count("Trans woman")
#create info for craph
x=np.array([q1,q2,q3,q4])
mlabels=["Male","Female",
         "Prefer not to say","Trans woman"]
#create graph
plt.pie(x,labels=mlabels,autopct='%1.1f%%', textprops={'fontweight': 'bold'})
plt.title("Genders of Sample", fontweight='bold')
plt.show()

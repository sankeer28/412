import matplotlib.pyplot as plt
import csv
import numpy as np
#go through csv and record answers
responses=[]
with open('ChatGPT (Responses) - Form Responses 1.xlsx - in.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        responses.append(row[4])
#count each answer
q1=responses.count("The education system should adapt to coexist with it.")
q2=responses.count("ChatGPT is not reliable enough to be used in education or professionally")
q3=responses.count("It should be banned")

#create info for graph
x=np.array([q1,q2,q3])
mlabels=["Institutions should adapt to coexist with it","ChatGPT is not reliable enough to be used in education",
         "It should be banned"]
#create graph
plt.pie(x,labels=mlabels,autopct='%1.1f%%', textprops={'fontweight': 'bold'})
plt.title("Future of ChatGPT in schools", fontweight='bold')
plt.show()

import matplotlib.pyplot as plt
import csv
import numpy as np
#go through csv file and collect results
responses=[]
with open('ChatGPT (Responses) - Form Responses 1.xlsx - in.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        responses.append(row[13])
#count results
q1=responses.count("Yes")
q2=responses.count("No")
q3=responses.count("Maybe")
q4=(len(responses))-(q1+q2+q3)#All other answers
#create info for graph
x=np.array([q1,q2,q3,q4])
mlabels=["Yes","No","Maybe","Other"]
#create graph
plt.pie(x,labels=mlabels,autopct='%1.1f%%', textprops={'fontweight': 'bold'})
plt.title("Is chatGTP reliable", fontweight='bold')
plt.show()

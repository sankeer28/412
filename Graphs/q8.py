import matplotlib.pyplot as plt
import csv
import numpy as np
#go through csv file and collect results
responses=[]
with open('ChatGPT (Responses) - Form Responses 1.xlsx - in.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        responses.append(row[9])
#count results
q1=responses.count("Yes")
q2=responses.count("No")
q3=responses.count("It will be adapted to coexist with you")

#create info for graph
x=np.array([q1,q2,q3])
mlabels=["Yes","No",
         "It will be adapted to coexist with you"]
        
#create graph
plt.pie(x,labels=mlabels,autopct='%1.1f%%', textprops={'fontweight': 'bold'})
plt.title("Will chatGPT replace the workforce", fontweight='bold')
plt.show()

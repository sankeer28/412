import matplotlib.pyplot as plt
import csv
import numpy as np
#go through csv and record all results
responses=[]
with open('ChatGPT (Responses) - Form Responses 1.xlsx - in.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        responses.append(row[3])
#count each response
q1=responses.count("1")
q2= responses.count("2")
q3=responses.count("3")
q4=responses.count("4")
q5=responses.count("5")
q6=responses.count("5+")
#create info for graph
x=np.array([q1,q2,q3,q4,q5,q6])
mlabels=["1","2","3","4","5","5+"]
poppin = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)#space sections of pie graph
#create graph
plt.pie(x,labels=mlabels,autopct='%1.1f%%',explode=poppin, textprops={'fontweight': 'bold'})
plt.title("Year of Students", fontweight='bold')
plt.show()

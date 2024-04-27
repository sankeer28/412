import matplotlib.pyplot as plt
import csv
import numpy as np
#go through csv file and collect results
responses=[]
with open('ChatGPT (Responses) - Form Responses 1.xlsx - in.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        responses.extend(row[14].split(', ')) # split the responses by ', ' and add them to the list

#count results
q1=responses.count("Save time")
q2=responses.count("Help brainstorm")
q3=responses.count("Teach a confusing concept")
q4=responses.count("Research")
q5=responses.count("Essay proofreading/grammar checking")
q6=responses.count("Decreasing the workload of teachers")
q7=responses.count("Enhancing the learning experience for students and teachers")
#create info for graph
x=np.array([q1,q2,q3,q4,q5,q6,q7])
mlabels=["Save time","Help brainstorm","Teach a confusing concept","Research","Essay proofreading/grammar checking",
         "Decreasing workload ","Enhancing the learning experience"]
#create graph
plt.pie(x,labels=mlabels,autopct='%1.1f%%', textprops={'fontweight': 'bold'})
plt.title("Uses of Chatgpt", fontweight='bold')
plt.show()

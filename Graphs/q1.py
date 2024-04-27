import matplotlib.pyplot as plt
import csv
import numpy as np
#go through csv and add all responses
responses=[]
with open('ChatGPT (Responses) - Form Responses 1.xlsx - in.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        responses.append(row[0])
#count each response
Yes_count=responses.count("Yes")
No_count= responses.count("No")
f_count=responses.count("It's fine as long as references are used")
r_count=responses.count("It depends on the context")
#create info for graph
x=np.array([Yes_count,No_count,f_count,r_count])
mlabels=["Yes","No","It's fine as long as references are used","It depends on the context"]
#create graph
plt.pie(x,labels=mlabels,autopct='%1.1f%%', textprops={'fontweight': 'bold'})
plt.title("Do you think the use ChatGPT is considered plagiarism?", fontweight='bold')
plt.show()



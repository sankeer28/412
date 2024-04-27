import matplotlib.pyplot as plt
import csv
import numpy as np
# go through csv file and record all responses
responses=[]
with open('ChatGPT (Responses) - Form Responses 1.xlsx - in.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        responses.append(row[1])
#count responses
Yes_count=responses.count("Yes")
No_count= responses.count("No")
f_count=responses.count("Depends on the purpose for use")
r_count=responses.count("Not Sure")
#create info for graph
x=np.array([Yes_count,No_count,f_count,r_count])
mlabels=["Yes","No","Depends on the purpose for use","Not Sure"]
#create graph
plt.pie(x, labels=mlabels, autopct='%1.1f%%', textprops={'fontweight': 'bold'})
plt.title("Do you think that the use of AI tools such as ChatGPT would inhibit education?", fontweight='bold')
plt.show()

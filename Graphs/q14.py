import matplotlib.pyplot as plt
import csv
import numpy as np
#go through csv file and collect results
responses=[]
with open('ChatGPT (Responses) - Form Responses 1.xlsx - in.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        responses.append(row[15])
q1=0
q2=0
q3=0
q4=0
q5=0
q6=0
q7=0
q8=0
q9=0
#count results
for i in responses:
    if "Asian or Asian American" in i:
        q1+=1
    if "Black or African American" in i:
        q2+=1
    if "Hispanic or Latino/Latina" in i:
        q3+=1
    if "Middle Eastern or Arab American" in i:
        q4+=1
    if "Native American or Alaskan Native" in i:
        q5+=1
    if "Pacific Islander or Native Hawaiian" in i:
        q6+=1
    if "White or Caucasian" in i:
        q7+=1
    if "Prefer not to disclose" in i:
        q8+=1
    
#create info for graph
quests=[q1,q2,q3,q4,q5,q6,q7,q8]


mlabels=["Asian or Asian American","Black or African American"
         ,"Hispanic or Latino/Latina","Middle Eastern or Arab American","ative American or Alaskan Native"
         ,"Pacific Islander or Native Hawaiian"," White or Caucasian","Prefer not to disclose"]

plt.title("Ethnicities of Sample", fontweight='bold')
#change format of axis to make graph visble
x_pos = np.arange(len(mlabels))
 
plt.bar(x_pos, quests)
 
plt.yticks(np.arange(0, max(quests)+1, 5), fontweight='bold')
plt.xticks(x_pos, mlabels, rotation=90, fontweight='bold')
 

#make graph
plt.show()

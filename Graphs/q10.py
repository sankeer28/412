import matplotlib.pyplot as plt
import csv
import numpy as np
#go through csv file and collect results
responses=[]
with open('ChatGPT (Responses) - Form Responses 1.xlsx - in.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        responses.append(row[11])
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
    if "Over-reliance on technology" in i:
        q1+=1
    if "Potential for plagiarism" in i:
        q2+=1
    if "Inaccuracy of generated responses" in i:
        q3+=1
    if "Unequal access to technology" in i:
        q4+=1
    if "diminish the value of original thought and creativity" in i:
        q5+=1
    if "create a \"lazy\" learning culture among students" in i:
        q6+=1
    if "hinder the development of communication and interpersonal skills" in i:
        q7+=1
    if "I do not believe ChatGPT poses any harms to the learning experience of students." in i:
        q8+=1
    
#create info for graph
quests=[q1,q2,q3,q4,q5,q6,q7,q8]


mlabels=["Over-reliance on technology","Plagiarism"
         ,"Inaccurate responses","Unequal access to technology","diminish original thought and creativity","create a lazy learning culture",
         "hinder communication and interpersonal skills",
         "I do not believe ChatGPT poses any harms",]

plt.title("Effects of ChatGPT on Learning", fontweight='bold')
#change format of axis to make graph visble
x_pos = np.arange(len(mlabels))
 
plt.bar(x_pos, quests)
 
plt.yticks(np.arange(0, max(quests)+1, 5), fontweight='bold')
plt.xticks(x_pos, mlabels, rotation=90, fontweight='bold')
 

#make graph
plt.show()

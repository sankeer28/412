import matplotlib.pyplot as plt
import csv
import numpy as np

#go through csv file and collect results
responses=[]
with open('ChatGPT (Responses) - Form Responses 1.xlsx - in.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        responses.append(row[2])
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
    if "Homework help: aid with homework by answering questions and guiding problem-solving." in i:
        q1+=1
    if "Study aid: helps with exam preparation by providing study materials such as flashcards and quizzes." in i:
        q2+=1
    if "Research assistance: assist with research and answer specific questions." in i:
        q3+=1
    if "Writing assistance:improves writing by suggesting sentence structures, correcting grammar, and generating ideas." in i:
        q4+=1
    if "Mental health support: offer emotional support and guidance for mental health issues." in i:
        q5+=1
    if "Personal development: tutorials and instructions for learning new skills like coding and cooking." in i:
        q6+=1
    if "Language learning: help with language practice by providing translations, definitions, and pronunciation help." in i:
        q7+=1
    if "Academic misconduct" in i:
        q8+=1
    if "I have never used ChatGPT" in i:
        q9+=1
   
#create info for graph
quests=[q1,q2,q3,q4,q5,q6,q7,q8,q9]

mlabels=["Homework help","Study aid"
         ,"Research assistance","Writing assistance"
         ,"Mental health support","Personal development",
         "Language learning.","Academic misconduct","I have never used ChatGPT"]

plt.title("Use of ChatGPT by students", fontweight='bold')
#change format of axis to make graph visble
x_pos = np.arange(len(mlabels))
 
plt.bar(x_pos, quests)

plt.yticks(np.arange(0, max(quests)+1, 5), fontweight='bold') # set y-axis tick labels

for i in range(len(quests)):
    plt.text(x=i, y=quests[i]+0.1, s=quests[i], ha='center', fontweight='bold') # add text annotations
 
plt.xticks(x_pos, mlabels, rotation=90, fontweight='bold')
 

#make graph
plt.show()

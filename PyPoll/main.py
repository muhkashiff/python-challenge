#import modules
import os
import csv
#import files path
csvpath = os.path.join('Resources','election_data.csv')
#read csv file with open command
with open(csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #skip the header
    header= next(csvreader)
    #list of variable 
    votesCount=0
    candidatesName=[]
    candidateName=[]
    candidate_vote_count=0
    winner=" "
    Result_name=[]
    Result_percentage=[]
    Result_votes=[]
    #creat set for getting list
    
    #Total Number of Vote Cast
    for row in csvreader:
        votesCount=votesCount+1
        candidateName=str(row[2])
        candidatesName.append(candidateName)
    #A complete list of candidates who received votes     
    #chatgpt search the use of set for unique string to avoid duplicates
    
    for candidate in set(candidatesName):
        candidateName. __add__(candidate)
    #Reference https://github.com/shrawantee/Python-PyBank-and-PyPoll/blob/master/HomeworkPython/PyPoll/PyPoll.py   
        candidate_vote_count=candidatesName.count(candidate)
        candidate_percentage=round(candidate_vote_count/votesCount*100,2)
        if candidate_percentage>50:
            winner=candidate
        
        
        
        print(candidate)
        print(candidate_vote_count)
        print(candidate_percentage)
        print(winner)    
    print(votesCount)
        

    # The percentage of votes each candidate won

    # The total number of votes each candidate won

    # The winner of the election based on popular vote
path=os.path.join("analysis","Election Results.txt")
with open(path, "w", newline='') as datafile:
    datafile.write("Election Result\n")
    datafile.write("------------------\n")
    datafile.write(f"Total votes:{votesCount}\n")
    datafile.write("------------------\n")
    for candidate in (set(candidatesName)):
            
        datafile.write(candidate+'\n')
    datafile.write("------------------\n")
    datafile.write(f"winner:{winner}\n")
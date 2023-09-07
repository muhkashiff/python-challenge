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
    nextCount=0
    #creat set for getting list
    candidate_set=set()
    #Total Number of Vote Cast
    for row in csvreader:
        votesCount=votesCount+1
        candidateName=str(row[2])
        candidatesName.append(candidateName)
    for candidate in set(candidatesName):
        candidateName.__add__(candidate)
        print(candidate)
            # candidateName_list=list(candidateName)
            # print(candidateName_list)
    
    print(votesCount)
    #A complete list of candidates who received votes

    # The percentage of votes each candidate won

    # The total number of votes each candidate won

    # The winner of the election based on popular vote
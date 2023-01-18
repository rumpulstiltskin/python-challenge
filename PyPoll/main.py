import csv 

with open ('Resources/election_data.csv') as csvfile: 

    csvreader=csv.reader(csvfile, delimiter=',') #Specify delimiter and variable that holds contents
    header=next(csvreader) #Read the header row first

    #Prepare variables
    voterids=[] #Generate list named "voterids" for the "Voter ID" column
    counties=[] #Generate list named "counties" for the "County" column
    candidates=[] #Generate list named "candidates" for the "Candidate" column
    candidatenames=[] #Generate list for actual candidate names
    totaleachcan=[] #Generate list for total votes for each found candidate
    resultprintcan=[] #Generate list for result printout of each found candidate
    totaleachcanperc=[] #Generate list for percentage of votes for each found candidate

    #Set start conditions
    line_count=0
    winnervotes=0
    loservotes=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0
    
    #Read in each row of data after the header and write data into assigned lists
    for row in csvreader:
        voterid=row[0] 
        county=row[1] 
        candidate=row[2] #
        voterids.append(voterid) 
        counties.append(county) 
        candidates.append(candidate) 
    
    line_count= len(voterids)
    
    

#Data analysis

candidatenames.append(candidates[0]) 


for loop1 in range (line_count-1):
    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in candidatenames:
        candidatenames.append(candidates[loop1+1])

n=len(candidatenames)




for loop2 in range (n): 
    totaleachcan.append(candidates.count(candidatenames[loop2])) #Count total votes of candidates and add to list total


loservotes=line_count #Pre-load loservoters with maximum votes for < comparison

for loop3 in range(n): 
    totaleachcanperc.append(f'{round((totaleachcan[loop3]/line_count*100), 4)}%') 
    if totaleachcan[loop3]>winnervotes: 
        winner=candidatenames[loop3]
        winnervotes=totaleachcan[loop3]
    if totaleachcan[loop3]<loservotes: 
        loser=candidatenames[loop3]
        loservotes=totaleachcan[loop3]


for loop4 in range(n):
    resultprintcan.append(f'{candidatenames[loop4]}: {totaleachcanperc[loop4]} ({totaleachcan[loop4]})') 

resultlines='\n'.join(resultprintcan) #Prepare new combined list of results for printout (each candidate with the result gets a new line)



analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {line_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner} :)\n\
Last: {loser} :(\n\
----------------------------\n'

print(analysis) #Output results on screen

file1=open("pypoll.txt","w") #Open or if file does not exist then create file named pypoll.txt
file1.writelines(analysis) #Write analysis into pypoll.txt
file1.close() #Close pypoll.txt write mode
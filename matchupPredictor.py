import csv
import pprint
from string import digits
import random
import math

with open('kenPomRatings.csv') as csvfile:
    inputOne = ''
    inputTwo = ''
    reader = csv.DictReader(csvfile)
    dict_list = {}
    for line in reader:
        mySchool = line['School']
        for char in '1234567890':
            mySchool = mySchool.replace(char,'')
        dict_list[mySchool.strip()] = line
    while(True):
        inputOne = input('Enter team one here (or type \'quit\' to end the program): ')
        if inputOne == 'quit':
            break
        inputTwo = input('Enter team two here: ')
        if inputTwo == 'quit':
            break
        adjEMOne = float(dict_list[inputOne]['AdjEM'])
        print(adjEMOne)
        adjEMTwo = float(dict_list[inputTwo]['AdjEM'])
        print(adjEMTwo)
        teamOneWPCT = (math.pow(adjEMOne,10.25)) / (math.pow(adjEMOne,10.25)+math.pow(adjEMTwo,10.25))
        teamTwoWPCT = (math.pow(adjEMTwo,10.25)) / (math.pow(adjEMOne,10.25)+math.pow(adjEMTwo,10.25))

        winningOdds = float(random.randint(0,1000)) / 1000
        winningTeam = ''
        if teamOneWPCT > winningOdds:
            winningTeam = inputOne
        else:
            winningTeam = inputTwo

        print('|Teams  |{0:^15}|{1:^15}|'.format(inputOne,inputTwo))
        print('|-------|---------------|---------------|')
        print('|Win%   |{0:^15}|{1:^15}|'.format(str(round(teamOneWPCT*100,3)) + '%',str(round(teamTwoWPCT*100,3)) + '%',))
        print('|RndPick|{0:^31}|'.format(winningTeam))

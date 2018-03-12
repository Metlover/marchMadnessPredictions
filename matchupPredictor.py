import csv
import pprint
from string import digits
import random
import math

class KenPom(): #initializes KenPom dataFrame for dealing with predictions.
    def__init__(self, fileName):
        with open(fileName) as csvfile:
            reader = csv.dictReader(csvfile)
            kenPomDict = {}
            for line in reader:
                school = line['School'] #gets school name to use as key
                for char in '1234567890':
                    school = school.replace(char,'') #if a seeding is present, removes the seeding and prints only the name
                kenPomDict[school.strip()] = line
        self.KenPom = kenPomDict

def school_info(myKenPom, schoolName): #prints information for school names
    if schoolName not in myKenPom.kenPom.keys():
        raise Exception('School not found! Please enter a valid school name.')
    return(pprint.ppformat(myKenPom.kenPom[schoolName]))

def schoolEWPCT(myKenPom, schoolNameOne, schoolNameTwo): #returns the expected win percent of schoolNameOne over schoolNameTwo
    if schoolNameOne not in myKenPom.kenPom.keys():
        raise Exception('School one not found! Please enter a valid school name.')
    elif schoolNameTwo not in myKenPom.kenPom.keys():
        raise Exception('School two not found! Please enter a valid school name.')
    adjEMOne = float(dict_list[inputOne]['AdjEM'])
    adjEMTwo = float(dict_list[inputTwo]['AdjEM'])
    return((math.pow(adjEMOne,10.25)) / (math.pow(adjEMOne,10.25)+math.pow(adjEMTwo,10.25)))

def makeAPick(myKenPom, schoolNameOne, schoolNameTwo): #returns a winner for a matchup randomly weighted based on expected win percent
    schoolOneWPCT = schoolEWPCT(myKenPom, schoolNameOne, schoolNameTwo)
    winningOdds = float(random.randint(0,1000)) / 1000
    winningTeam = ''
    if teamOneWPCT > winningOdds:
        winningTeam = schoolNameOne
    else:
        winningTeam = schoolNameTwo
    return(winningTeam)

def main():
    myKenPom = KenPom('kenPomRatings.csv')
    inputOne = ''
    inputTwo = ''
    while(True):
        inputOne = input('Enter team one here (or type \'quit\' to end the program): ')
        if inputOne == 'quit':
            break
        inputTwo = input('Enter team two here: ')
        if inputTwo == 'quit':
            break
    schoolOneWinPct = schoolEWPCT(myKenPom, inputOne, inputTwo)
    schoolTwoWinPct = schoolEWPCT(myKenPom, inputTwo, inputOne)
    myPick = makeAPick(myKenPom, inputOne, inputTwo)
    print('|Teams  |{0:^15}|{1:^15}|'.format(inputOne,inputTwo))
    print('|-------|---------------|---------------|')
    print('|Win%   |{0:^15}|{1:^15}|'.format(str(round(schoolOneWinPct*100,3)) + '%',str(round(schoolTwoWinPct*100,3)) + '%',))
    print('|RndPick|{0:^31}|'.format(myPick))

if __name__ == '__main__':
    main()

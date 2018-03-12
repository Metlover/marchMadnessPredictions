import matchupPredictor
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

class Bracket():
    def __init__(self, mySoup, myKenPom, mostLikely=False):
        soup = mySoup

        namesToBeReplaced = ['Pennsylvania','NC St.', 'Charleston', 'CS Fullerton', 'Loyola-Chicago', 'Loyola (Chi)', 'Miami', 'Texas A&M']
        replacementNames = ['Penn', 'North Carolina St.', 'College of Charleston', 'Cal St. Fullerton', 'Loyola Chicago', 'Loyola Chicago', 'Miami FL','Texas A&M;']

        roundOne = {}
        roundTwo = {}
        roundThree = {}
        roundFour = {}
        roundFive = {}
        roundSix = {}

        roundOf64 = []
        roundOf32 = []
        sweet16 = []
        elite8 = []
        final4 = []
        championshipGame = []
        Champion = ''

        n=0
        gameCounter = 1
        val = 15
        while n < val:
            teamA = soup.find_all('div')[36].find_all('a')[n]['title']
            if 'State' in teamA:
                teamA = teamA.replace('State', 'St.')
            for name in range(0,len(namesToBeReplaced)):
                if teamA == namesToBeReplaced[name]:
                    teamA = replacementNames[name]
            try:
                teamB = soup.find_all('div')[36].find_all('a')[n+1]['title']
                if 'State' in teamB:
                    teamB = teamB.replace('State', 'St.')
                for name in range(0,len(namesToBeReplaced)):
                    if teamB == namesToBeReplaced[name]:
                        teamB = replacementNames[name]
                roundOne[('Game ' + str(gameCounter) + ', South')] = [teamA,teamB]
            except:
                roundOne[('Game ' + str(gameCounter) + ', South')] = [teamA,'Last In']
                n = n + 1
                val = val + 1
            n = n + 2
            gameCounter = gameCounter + 1
        n=0
        gameCounter = 1
        val = 15
        while n < val:
            teamA = soup.find_all('div')[46].find_all('a')[n]['title']
            if 'State' in teamA:
                teamA = teamA.replace('State', 'St.')
            for name in range(0,len(namesToBeReplaced)):
                if teamA == namesToBeReplaced[name]:
                    teamA = replacementNames[name]
            try:
                teamB = soup.find_all('div')[46].find_all('a')[n+1]['title']
                if 'State' in teamB:
                    teamB = teamB.replace('State', 'St.')
                for name in range(0,len(namesToBeReplaced)):
                    if teamB == namesToBeReplaced[name]:
                        teamB = replacementNames[name]
                roundOne[('Game ' + str(gameCounter) + ', West')] = [teamA,teamB]
            except:
                roundOne[('Game ' + str(gameCounter) + ', West')] = [teamA,'Last In']
                n = n + 1
                val = val + 1
            n = n + 2
            gameCounter = gameCounter + 1
        n=0
        gameCounter = 1
        val = 15
        while n < val:
            teamA = soup.find_all('div')[56].find_all('a')[n]['title']
            if 'State' in teamA:
                teamA = teamA.replace('State', 'St.')
            for name in range(0,len(namesToBeReplaced)):
                if teamA == namesToBeReplaced[name]:
                    teamA = replacementNames[name]
            try:
                teamB = soup.find_all('div')[56].find_all('a')[n+1]['title']
                if 'State' in teamB:
                    teamB = teamB.replace('State', 'St.')
                for name in range(0,len(namesToBeReplaced)):
                    if teamB == namesToBeReplaced[name]:
                        teamB = replacementNames[name]
                roundOne[('Game ' + str(gameCounter) + ', East')] = [teamA,teamB]
            except:
                roundOne[('Game ' + str(gameCounter) + ', East')] = [teamA,'Last In']
                n = n + 1
                val = val + 1
            n = n + 2
            gameCounter = gameCounter + 1
        n=0
        gameCounter = 1
        val = 15
        while n < val:
            teamA = soup.find_all('div')[67].find_all('a')[n]['title']
            if 'State' in teamA:
                teamA = teamA.replace('State', 'St.')
            for name in range(0,len(namesToBeReplaced)):
                if teamA == namesToBeReplaced[name]:
                    teamA = replacementNames[name]
            try:
                teamB = soup.find_all('div')[67].find_all('a')[n+1]['title']
                if 'State' in teamB:
                    teamB = teamB.replace('State', 'St.')
                for name in range(0,len(namesToBeReplaced)):
                    if teamB == namesToBeReplaced[name]:
                        teamB = replacementNames[name]
                roundOne[('Game ' + str(gameCounter) + ', Midwest')] = [teamA,teamB]
            except:
                roundOne[('Game ' + str(gameCounter) + ', Midwest')] = [teamA,'Last In']
                n = n + 1
                val = val + 1
            n = n + 2
            gameCounter = gameCounter + 1
        self.roundOne = roundOne


        for game in roundOne.keys():
            if mostLikely:
                roundOne[game] = [roundOne[game], matchupPredictor.mostLikely(myKenPom, roundOne[game][0], roundOne[game][1])]
            else:
                roundOne[game] = [roundOne[game], matchupPredictor.makeAPick(myKenPom, roundOne[game][0], roundOne[game][1])]
            roundOf64 = roundOf64 + [roundOne[game][0][0]] + [roundOne[game][0][1]]

        self.roundOf64 = roundOf64

        roundTwo['Game 9, South'] = [roundOne['Game 1, South'][1],roundOne['Game 2, South'][1]]
        roundTwo['Game 10, South'] = [roundOne['Game 3, South'][1],roundOne['Game 4, South'][1]]
        roundTwo['Game 11, South'] = [roundOne['Game 5, South'][1],roundOne['Game 6, South'][1]]
        roundTwo['Game 12, South'] = [roundOne['Game 7, South'][1], roundOne['Game 8, South'][1]]

        roundTwo['Game 9, West'] = [roundOne['Game 1, West'][1],roundOne['Game 2, West'][1]]
        roundTwo['Game 10, West'] = [roundOne['Game 3, West'][1],roundOne['Game 4, West'][1]]
        roundTwo['Game 11, West'] = [roundOne['Game 5, West'][1],roundOne['Game 6, West'][1]]
        roundTwo['Game 12, West'] = [roundOne['Game 7, West'][1], roundOne['Game 8, West'][1]]

        roundTwo['Game 9, East'] = [roundOne['Game 1, East'][1],roundOne['Game 2, East'][1]]
        roundTwo['Game 10, East'] = [roundOne['Game 3, East'][1],roundOne['Game 4, East'][1]]
        roundTwo['Game 11, East'] = [roundOne['Game 5, East'][1],roundOne['Game 6, East'][1]]
        roundTwo['Game 12, East'] = [roundOne['Game 7, East'][1], roundOne['Game 8, East'][1]]

        roundTwo['Game 9, Midwest'] = [roundOne['Game 1, Midwest'][1],roundOne['Game 2, Midwest'][1]]
        roundTwo['Game 10, Midwest'] = [roundOne['Game 3, Midwest'][1],roundOne['Game 4, Midwest'][1]]
        roundTwo['Game 11, Midwest'] = [roundOne['Game 5, Midwest'][1],roundOne['Game 6, Midwest'][1]]
        roundTwo['Game 12, Midwest'] = [roundOne['Game 7, Midwest'][1], roundOne['Game 8, Midwest'][1]]

        for game in roundTwo.keys():
            if mostLikely:
                roundTwo[game] = [roundTwo[game], matchupPredictor.mostLikely(myKenPom, roundTwo[game][0], roundTwo[game][1])]
            else:
                roundTwo[game] = [roundTwo[game], matchupPredictor.makeAPick(myKenPom, roundTwo[game][0], roundTwo[game][1])]
            roundOf32 = roundOf32 + [roundTwo[game][0][0]] + [roundTwo[game][0][1]]

        self.roundTwo = roundTwo
        self.roundOf32 = roundOf32

        roundThree['Game 13, South'] = [roundTwo['Game 9, South'][1],roundTwo['Game 10, South'][1]]
        roundThree['Game 14, South'] = [roundTwo['Game 11, South'][1],roundTwo['Game 12, South'][1]]

        roundThree['Game 13, West'] = [roundTwo['Game 9, West'][1],roundTwo['Game 10, West'][1]]
        roundThree['Game 14, West'] = [roundTwo['Game 11, West'][1],roundTwo['Game 12, West'][1]]

        roundThree['Game 13, East'] = [roundTwo['Game 9, East'][1],roundTwo['Game 10, East'][1]]
        roundThree['Game 14, East'] = [roundTwo['Game 11, East'][1],roundTwo['Game 12, East'][1]]

        roundThree['Game 13, Midwest'] = [roundTwo['Game 9, Midwest'][1],roundTwo['Game 10, Midwest'][1]]
        roundThree['Game 14, Midwest'] = [roundTwo['Game 11, Midwest'][1],roundTwo['Game 12, Midwest'][1]]

        for game in roundThree.keys():
            if mostLikely:
                roundThree[game] = [roundThree[game], matchupPredictor.mostLikely(myKenPom, roundThree[game][0], roundThree[game][1])]
            else:
                roundThree[game] = [roundThree[game], matchupPredictor.makeAPick(myKenPom, roundThree[game][0], roundThree[game][1])]
            sweet16 = sweet16 + [roundThree[game][0][0]] + [roundThree[game][0][1]]

        self.roundThree = roundThree
        self.sweet16 = sweet16

        roundFour['Game 15, South'] = [roundThree['Game 13, South'][1],roundThree['Game 14, South'][1]]
        roundFour['Game 15, West'] = [roundThree['Game 13, West'][1],roundThree['Game 14, West'][1]]
        roundFour['Game 15, East'] = [roundThree['Game 13, East'][1],roundThree['Game 14, East'][1]]
        roundFour['Game 15, Midwest'] = [roundThree['Game 13, Midwest'][1],roundThree['Game 14, Midwest'][1]]

        for game in roundFour.keys():
            if mostLikely:
                roundFour[game] = [roundFour[game], matchupPredictor.mostLikely(myKenPom, roundFour[game][0], roundFour[game][1])]
            else:
                roundFour[game] = [roundFour[game], matchupPredictor.makeAPick(myKenPom, roundFour[game][0], roundFour[game][1])]
            elite8 = elite8 + [roundFour[game][0][0]] + [roundFour[game][0][1]]

        self.roundFour = roundFour
        self.elite8 = elite8

        roundFive['Game 1, Final Four'] = [roundFour['Game 15, South'][1],roundFour['Game 15, West'][1]]
        roundFive['Game 2, Final Four'] = [roundFour['Game 15, East'][1],roundFour['Game 15, Midwest'][1]]

        for game in roundFive.keys():
            if mostLikely:
                roundFive[game] = [roundFive[game], matchupPredictor.mostLikely(myKenPom, roundFive[game][0], roundFive[game][1])]
            else:
                roundFive[game] = [roundFive[game], matchupPredictor.makeAPick(myKenPom, roundFive[game][0], roundFive[game][1])]
            final4 = final4 + [roundFive[game][0][0]] + [roundFive[game][0][1]]

        self.roundFive = roundFive
        self.final4 = final4

        roundSix['Championship'] = [roundFive['Game 1, Final Four'][1],roundFive['Game 2, Final Four'][1]]
        if mostLikely:
            roundSix['Championship'] = [roundSix['Championship'], matchupPredictor.mostLikely(myKenPom, roundSix['Championship'][0], roundSix['Championship'][1])]
        else:
            roundSix['Championship'] = [roundSix['Championship'], matchupPredictor.makeAPick(myKenPom, roundSix['Championship'][0], roundSix['Championship'][1])]

        championshipGame = [roundSix['Championship'][0][0], roundSix['Championship'][0][1]]
        self.championshipGame = championshipGame

        self.roundSix = roundSix

        Champion = roundSix['Championship'][1]
        self.champion = Champion

    def __str__(self):
        f = open('bracketFormat.txt', 'r', encoding="utf8")
        content = f.read()
        myList = [''] * 127
        #print(content.format())
        return(content.format(self.roundOne['Game 1, South'][0][0],self.roundTwo['Game 9, South'][0][0],
        self.roundOne['Game 1, South'][0][1],self.roundThree['Game 13, South'][0][0],self.roundOne['Game 2, South'][0][0],
        self.roundTwo['Game 9, South'][0][1],self.roundOne['Game 2, South'][0][1],self.roundFour['Game 15, South'][0][0],
        self.roundOne['Game 3, South'][0][0],self.roundTwo['Game 10, South'][0][0],self.roundOne['Game 3, South'][0][1],
        self.roundThree['Game 13, South'][0][1],self.roundOne['Game 4, South'][0][0],self.roundTwo['Game 10, South'][0][1],
        self.roundOne['Game 4, South'][0][1],self.roundFive['Game 1, Final Four'][0][0],self.roundOne['Game 5, South'][0][0],
        self.roundTwo['Game 11, South'][0][0],self.roundOne['Game 5, South'][0][1],self.roundThree['Game 14, South'][0][0],
        self.roundOne['Game 6, South'][0][0],self.roundTwo['Game 11, South'][0][1],self.roundOne['Game 6, South'][0][1],
        self.roundFour['Game 15, South'][0][1],self.roundOne['Game 7, South'][0][0],self.roundTwo['Game 12, South'][0][0],
        self.roundOne['Game 7, South'][0][1],self.roundThree['Game 14, South'][0][1],self.roundOne['Game 8, South'][0][0],
        self.roundTwo['Game 12, South'][0][1],self.roundOne['Game 8, South'][0][1],self.roundSix['Championship'][0][0],
        self.roundOne['Game 1, West'][0][0],self.roundTwo['Game 9, West'][0][0],
        self.roundOne['Game 1, West'][0][1],self.roundThree['Game 13, West'][0][0],self.roundOne['Game 2, West'][0][0],
        self.roundTwo['Game 9, West'][0][1],self.roundOne['Game 2, West'][0][1],self.roundFour['Game 15, West'][0][0],
        self.roundOne['Game 3, West'][0][0],self.roundTwo['Game 10, West'][0][0],self.roundOne['Game 3, West'][0][1],
        self.roundThree['Game 13, West'][0][1],self.roundOne['Game 4, West'][0][0],self.roundTwo['Game 10, West'][0][1],
        self.roundOne['Game 4, West'][0][1],self.roundFive['Game 1, Final Four'][0][1],self.roundOne['Game 5, West'][0][0],
        self.roundTwo['Game 11, West'][0][0],self.roundOne['Game 5, West'][0][1],self.roundThree['Game 14, West'][0][0],
        self.roundOne['Game 6, West'][0][0],self.roundTwo['Game 11, West'][0][1],self.roundOne['Game 6, West'][0][1],
        self.roundFour['Game 15, West'][0][1],self.roundOne['Game 7, West'][0][0],self.roundTwo['Game 12, West'][0][0],
        self.roundOne['Game 7, West'][0][1],self.roundThree['Game 14, West'][0][1],self.roundOne['Game 8, West'][0][0],
        self.roundTwo['Game 12, West'][0][1],self.roundOne['Game 8, West'][0][1],self.roundSix['Championship'][1],
        self.roundOne['Game 1, East'][0][0],self.roundTwo['Game 9, East'][0][0],
        self.roundOne['Game 1, East'][0][1],self.roundThree['Game 13, East'][0][0],self.roundOne['Game 2, East'][0][0],
        self.roundTwo['Game 9, East'][0][1],self.roundOne['Game 2, East'][0][1],self.roundFour['Game 15, East'][0][0],
        self.roundOne['Game 3, East'][0][0],self.roundTwo['Game 10, East'][0][0],self.roundOne['Game 3, East'][0][1],
        self.roundThree['Game 13, East'][0][1],self.roundOne['Game 4, East'][0][0],self.roundTwo['Game 10, East'][0][1],
        self.roundOne['Game 4, East'][0][1],self.roundFive['Game 2, Final Four'][0][0],self.roundOne['Game 5, East'][0][0],
        self.roundTwo['Game 11, East'][0][0],self.roundOne['Game 5, East'][0][1],self.roundThree['Game 14, East'][0][0],
        self.roundOne['Game 6, East'][0][0],self.roundTwo['Game 11, East'][0][1],self.roundOne['Game 6, East'][0][1],
        self.roundFour['Game 15, East'][0][1],self.roundOne['Game 7, East'][0][0],self.roundTwo['Game 12, East'][0][0],
        self.roundOne['Game 7, East'][0][1],self.roundThree['Game 14, East'][0][1],self.roundOne['Game 8, East'][0][0],
        self.roundTwo['Game 12, East'][0][1],self.roundOne['Game 8, East'][0][1],self.roundSix['Championship'][0][1],
        self.roundOne['Game 1, Midwest'][0][0],self.roundTwo['Game 9, Midwest'][0][0],
        self.roundOne['Game 1, Midwest'][0][1],self.roundThree['Game 13, Midwest'][0][0],self.roundOne['Game 2, Midwest'][0][0],
        self.roundTwo['Game 9, Midwest'][0][1],self.roundOne['Game 2, Midwest'][0][1],self.roundFour['Game 15, Midwest'][0][0],
        self.roundOne['Game 3, Midwest'][0][0],self.roundTwo['Game 10, Midwest'][0][0],self.roundOne['Game 3, Midwest'][0][1],
        self.roundThree['Game 13, Midwest'][0][1],self.roundOne['Game 4, Midwest'][0][0],self.roundTwo['Game 10, Midwest'][0][1],
        self.roundOne['Game 4, Midwest'][0][1],self.roundFive['Game 2, Final Four'][0][1],self.roundOne['Game 5, Midwest'][0][0],
        self.roundTwo['Game 11, Midwest'][0][0],self.roundOne['Game 5, Midwest'][0][1],self.roundThree['Game 14, Midwest'][0][0],
        self.roundOne['Game 6, Midwest'][0][0],self.roundTwo['Game 11, Midwest'][0][1],self.roundOne['Game 6, Midwest'][0][1],
        self.roundFour['Game 15, Midwest'][0][1],self.roundOne['Game 7, Midwest'][0][0],self.roundTwo['Game 12, Midwest'][0][0],
        self.roundOne['Game 7, Midwest'][0][1],self.roundThree['Game 14, Midwest'][0][1],self.roundOne['Game 8, Midwest'][0][0],
        self.roundTwo['Game 12, Midwest'][0][1],self.roundOne['Game 8, Midwest'][0][1]
        ))

    def __eq__(self, other):
        return(str(self) == str(other))

class MultipleBrackets():
    def __init__(self, nBrackets, soup, myKenPom):
        allBrackets = []
        roundOf32 = []
        sweet16 = []
        elite8 = []
        final4 = []
        championshipGame = []
        champion = []

        iterations = nBrackets

        mySoup = soup

        for n in range(1,iterations):
            myBracket = Bracket(mySoup, myKenPom)
            allBrackets = allBrackets + [myBracket]
            roundOf32 = roundOf32 + myBracket.roundOf32
            sweet16 = sweet16 + myBracket.sweet16
            elite8 = elite8 + myBracket.elite8
            final4 = final4 + myBracket.final4
            championshipGame = championshipGame + myBracket.championshipGame
            champion = champion + [myBracket.champion]

        allTeams = allBrackets[0].roundOf64
        self.roundOf64Teams = allTeams
        self.roundOf32Teams = roundOf32
        self.sweet16Teams = sweet16
        self.elite8Teams = elite8
        self.final4Teams = final4
        self.championshipGameTeams = championshipGame
        self.championTeams = champion
        self.brackets = allBrackets

def generateRoundOdds(myIterations, soup, myKenPom):
    brackets = MultipleBrackets(myIterations, soup, myKenPom)

    mainDataDict = {}

    iterations = myIterations

    for team in brackets.roundOf64Teams:
        mainDataDict[team] = {}
        mainDataDict[team]['Round of 32'] = brackets.roundOf32Teams.count(team)/iterations
        mainDataDict[team]['Sweet Sixteen'] = brackets.sweet16Teams.count(team)/iterations
        mainDataDict[team]['Elite Eight'] =  brackets.elite8Teams.count(team)/iterations
        mainDataDict[team]['Final Four'] = brackets.final4Teams.count(team)/iterations
        mainDataDict[team]['Championship Game'] = brackets.championshipGameTeams.count(team)/iterations
        mainDataDict[team]['Champions'] = brackets.championTeams.count(team)/iterations

    return(mainDataDict)

def teamOdds(myIterations, soup, myKenPom, myTeam):
    myDict = generateRoundOdds(myIterations, soup, myKenPom)
    return(myDict[myTeam])

def main():
    kenPomUrl = 'kenPomRatings.csv'
    myKenPom = matchupPredictor.KenPom(kenPomUrl)
    ESPNurl = 'http://www.espn.com/mens-college-basketball/tournament/bracket'
    f = requests.get(ESPNurl)
    mySoup = bs(f.text, 'html.parser')

    mainDataDict = generateRoundOdds(100000, mySoup, myKenPom)
    (pd.DataFrame.from_dict(data=mainDataDict, orient='index').to_csv('round_odds.csv'))

#    myBrackets = MultipleBrackets(5000, mySoup, myKenPom)
#    uniqueBrackets = []
#    for bracket in myBrackets.brackets:
#        uniqueBrackets = uniqueBrackets + [str(bracket)]
#    uniqueBracketSet = list(set(uniqueBrackets))
#    uniqueBracketVals = []
#    for n in range(0,len(uniqueBracketSet)):
#        uniqueBracketVals = uniqueBracketVals + [uniqueBrackets.count(uniqueBracketSet[n])]

#    print(uniqueBracketVals)

if __name__ == '__main__':
    main()

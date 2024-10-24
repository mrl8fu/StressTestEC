import numpy as np
import pandas as pd


def main():
    votingData = pd.read_csv("votingData2.csv")
    votingData = votingData.iloc[1:]
    cleanData(votingData)
    votingData.insert(4, "Voters per Elector", calculateElectorsPerPop(votingData), True)
    #votingData.insert(5, "VoterTurnout per Elector", calculateElectorsPerPopVoting(votingData), True)
    sortVotingData(votingData)
    print(votingData)

    #sortVotingDataVoting(votingData)
    #print(votingData)

    stressTest = apportionActualTurnout(votingData)


    print(stressTest)

def calculateElectorsPerPop(votingData):
    electorsPerPop = []
    for i in range(votingData.shape[0]):
        votes = votingData.iat[i, 1]
        electors = votingData.iat[i, 3]
        votesPerPop = int(votes/electors)
        electorsPerPop.append(votesPerPop)
    return electorsPerPop

def calculateElectorsPerPopVoting(votingData):
    electorsPerPopVoting = []
    for i in range(votingData.shape[0]):
        votes = votingData.iat[i, 2]
        electors = votingData.iat[i, 3]
        votesPerPop = int(votes/electors)
        electorsPerPopVoting.append(votesPerPop)
    return electorsPerPopVoting

def cleanData(votingData):
    for i in range(votingData.shape[0]):
        votingData.iat[i, 1] = int(votingData.iat[i, 1].replace(",", ""))
        votingData.iat[i, 2] = int(votingData.iat[i, 2].replace(",", ""))

def sortVotingData(votingData):
    votingData.sort_values(["Voters per Elector"], ascending=[False], inplace=True)

def sortVotingDataVoting(votingData):
    votingData.sort_values(["VoterTurnout per Elector"], ascending=[False], inplace=True)

def apportionFullTurnout(votingData):
    # First assuming 100% voter turnout
    electorsA = 0
    votesA = 0
    electorsB = 0
    votesB = 0
    for i in range(votingData.shape[0]):
        if (electorsA + int(votingData.iat[i, 3])) < 270:
            electorsA += votingData.iat[i, 3]
            votesA += votingData.iat[i, 1]
            print(votingData.iat[i, 0] + " Goes to A")
        else:
            electorsB += votingData.iat[i, 3]
            votesB += np.ceil(votingData.iat[i, 1]/2)
            votesA += np.floor(votingData.iat[i, 1]/2)
            print(votingData.iat[i, 0] + " Goes to B")

    return [int(electorsA), int(electorsB), int(votesA), int(votesB)]

def apportionActualTurnout(votingData):
    # Assuming actual turnout percentages
    electorsA = 0
    votesA = 0
    electorsB = 0
    votesB = 0
    for i in range(votingData.shape[0]):
        if (electorsA + int(votingData.iat[i, 3])) < 270:
            electorsA += votingData.iat[i, 3]
            votesA += votingData.iat[i, 2]
            print(votingData.iat[i, 0] + " Goes to A")
        else:
            electorsB += votingData.iat[i, 3]
            votesB += np.ceil(votingData.iat[i, 2] / 2)
            votesA += np.floor(votingData.iat[i, 2] / 2)
            print(votingData.iat[i, 0] + " Goes to B")

    return [int(electorsA), int(electorsB), int(votesA), int(votesB)]


if __name__ == "__main__":
    main()



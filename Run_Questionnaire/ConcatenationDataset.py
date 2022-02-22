import os
import glob
import pandas as pd

WORKINGPATH = os.getcwd()
DATAPATH = "./Run_Questionnaire/DataSet/"

def concatenationDataset():

    CSVList = glob.glob(WORKINGPATH + DATAPATH + "*csv")

    listData = []

    for csv in CSVList:
        dataLue = pd.read_csv(csv)
        listData.append(dataLue)

    dataConcatene = pd.concat(listData, ignore_index=True)

    return dataConcatene

if __name__ == "__main__":
    dataConcatene = concatenationDataset()
    dataConcatene.to_csv(WORKINGPATH + DATAPATH + "../DataSetTotal.csv", index=False)
import pandas as pd

CSVsList=[ "CLEANEDFID_642.csv", "CLEANEDFID_643.csv", "CLEANEDFID_648.csv" ]


for csvfile in CSVsList:
    inputCSV=csvfile
    df = pd.read_csv(inputCSV)
    # print(df)
    df_cleaned = df.dropna(axis='columns',how='all')
    print ( "###################### "+inputCSV + " ######################")
    print(df_cleaned)

# speciesName=df['Species name']
# print (speciesName)
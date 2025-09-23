import pandas as pd
import numpy as np
CSVsList=["FID_486.csv","FID_489.csv","FID_492.csv","FID_494.csv","FID_495.csv","FID_496.csv","FID_503.csv","FID_508.csv","FID_510.csv","FID_511.csv","FID_512.csv","FID_515.csv","FID_516.csv","FID_520.csv","FID_523.csv","FID_524.csv","FID_527.csv","FID_528.csv","FID_529.csv","FID_535.csv","FID_547.csv","FID_550.csv","FID_555.csv","FID_556.csv","FID_559.csv","FID_561.csv","FID_571.csv","FID_576.csv","FID_585.csv","FID_587.csv","FID_598.csv","FID_611.csv","FID_619.csv","FID_621.csv","FID_634.csv","FID_642.csv","FID_643.csv","FID_648.csv","FID_649.csv","FID_670.csv","FID_671.csv","FID_672.csv","FID_673.csv","FID_674.csv","FID_675.csv","FID_676.csv","FID_677.csv","FID_678.csv","FID_679.csv","FID_680.csv","FID_681.csv","FID_682.csv","FID_683.csv","FID_684.csv","FID_685.csv","FID_686.csv","FID_687.csv","FID_688.csv","FID_689.csv","FID_690.csv","FID_691.csv","FID_692.csv"]
spList=[]
spDict = {}
finalCSV="FinalFID_CSVv2/FinalCSV.csv"
mdf=pd.read_csv(finalCSV)
# mdf.loc[mdf['FID-Species'] == 'FID_642','Bistorta_affinis'] = 1000

# mdf.loc[mdf['Bistorta_affinis'] == 0, 'Heracleum_pinnatum'] = 28
# print(mdf)
for csvfile in CSVsList:
    inputCSV="FinalFID_CSVv2/"+csvfile
    df_cleaned = pd.read_csv(inputCSV)
    # print(df)
    # df_cleaned = df.dropna(axis='columns',how='all')
    # df_cleaned['individuals_freq'] = np.where(pd.isna(df_cleaned['individuals_freq']), df_cleaned['Cover_percent'], df_cleaned['individuals_freq'])
    print ("inputCSV = ",inputCSV)
    csvRowKey=inputCSV.split('/')[1].split('.')[0].strip()
    # print("csvRowKey = ",csvRowKey)
    # print(df_cleaned)
    speciesListInCurrCSV=df_cleaned['Species'].to_list()
    # print('#####speciesListInCurrCSV#####\n', speciesListInCurrCSV)
    for specName in speciesListInCurrCSV:
        individuals=(df_cleaned.loc[df_cleaned['Species']== specName.strip()]['individuals_freq'])
        # individuals=int(individuals)
        # int(ser.iloc[0])
        print('individuals = ',individuals.iloc[0])
        mdf.loc[mdf['FID-Species'] == csvRowKey,specName] = individuals.iloc[0]
mdf.to_csv('Output_Final.csv',index=False)

import pandas as pd
import numpy as np

CSVsList=["CLEANED#FID_642.csv","CLEANED#FID_643.csv","CLEANED#FID_648.csv"]

spList=[]
spDict = {}
spDictFinal = {'Ephedra_intermedia': 0, 'Nepeta_glutinosa': 0, 'Delphinium_cashmerianum': 0, 'Acontholimon_lycopodiodes': 0, 'Oxytropis_glabra': 0, 'Oxytropis_tatarica': 0, 'Polygonum_rottboellioides': 0, 'Arnebia_euchroma': 0, 'Dianthus_anatolicus': 0, 'Nepeta_discolor': 0, 'Potentilla_multifida': 0, 'Cotoneaster_affinis': 0, 'Lonicera_spinosa': 0, 'Scorzonera_virgata': 0, 'Potentilla_saundersiana': 0, 'Puccinellia_distans': 0, 'Epilobium_angustifolium': 0, 'Silene_caespitella': 0, 'Atragalus_oplites': 0, 'Piptatherum_laterale_(g)': 0, 'Aconogon_tortuosum': 0, 'Psychrogeton_andryaloides': 0, 'Artemisia_brevifolia': 0, 'Euphorbia_thomsoniana': 0, 'Elymus_schrenkianus_(g)': 0, 'Rheum_webbianum': 0, 'Ephedra_geradiana': 0, 'Cicer_microphyllum': 0, 'Lonicera_asperifolia': 0, 'Lindelofia_stylosa': 0, 'Caragana_versicolor': 0, 'Elymus_canaliculatus_(g)': 0, 'Bistorta_affinis': 0, 'Geranium_himalayense': 0, 'Heracleum_pinnatum': 0}
finalCSV="MuchNeeded.csv"
mdf=pd.read_csv(finalCSV)
# mdf.loc[mdf['FIDSpecies'] == 'FID_642','Bistorta_affinis'] = 1000


# mdf.loc[mdf['Bistorta_affinis'] == 0, 'Heracleum_pinnatum'] = 28

# print(mdf)

for csvfile in CSVsList:
    inputCSV=csvfile
    df = pd.read_csv(inputCSV)
    # print(df)
    df_cleaned = df.dropna(axis='columns',how='all')
    df_cleaned['#individuals'] = np.where(pd.isna(df_cleaned['#individuals']), df_cleaned['Cover_(%)'], df_cleaned['#individuals'])
    csvRowKey=inputCSV.split('#')[1].split('.')[0].strip()
    print("csvRowKey = ",csvRowKey)
    # spSet=set(spList)

    # print ( "###################### "+inputCSV + " ######################")
    print(df_cleaned)
    speciesListInCurrCSV=df_cleaned['Species'].to_list()
    for phylum in speciesListInCurrCSV:
        individuals=(df_cleaned.loc[df_cleaned['Species'] == phylum]['#individuals'])
        # individuals=int(individuals)
        # print('individuals = ',individuals)
        mdf.loc[mdf['FIDSpecies'] == csvRowKey,phylum] = individuals

# speciesName=df['Species name']
# print (speciesName). df_cleaned['#individuals'] == '' or

spDict= dict.fromkeys(spList,0);
print (spList)
mdf.to_csv('Output.csv',index=False)
mdfT=mdf.transpose()
mdfT.to_csv('OutputTF.csv',index=False)
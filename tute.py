import pandas as pd
import numpy as np

CSVsList=['CLEANED#FID_486.csv', 'CLEANED#FID_496.csv', 'CLEANED#FID_503.csv', 'CLEANED#FID_508.csv', 'CLEANED#FID_511.csv', 'CLEANED#FID_512.csv', 'CLEANED#FID_515.csv', 'CLEANED#FID_516.csv', 'CLEANED#FID_520.csv', 'CLEANED#FID_523.csv', 'CLEANED#FID_524.csv', 'CLEANED#FID_527.csv', 'CLEANED#FID_528.csv', 'CLEANED#FID_529.csv', 'CLEANED#FID_535.csv', 'CLEANED#FID_547.csv', 'CLEANED#FID_550.csv', 'CLEANED#FID_555.csv', 'CLEANED#FID_559.csv', 'CLEANED#FID_571.csv', 'CLEANED#FID_576.csv', 'CLEANED#FID_585.csv', 'CLEANED#FID_587.csv', 'CLEANED#FID_598.csv', 'CLEANED#FID_611.csv', 'CLEANED#FID_619.csv', 'CLEANED#FID_621.csv', 'CLEANED#FID_634.csv', 'CLEANED#FID_642.csv', 'CLEANED#FID_643.csv', 'CLEANED#FID_648.csv', 'CLEANED#FID_649.csv', 'CLEANED#FID_670.csv', 'CLEANED#FID_671.csv', 'CLEANED#FID_672.csv', 'CLEANED#FID_673.csv', 'CLEANED#FID_674.csv', 'CLEANED#FID_675.csv', 'CLEANED#FID_676.csv', 'CLEANED#FID_677.csv', 'CLEANED#FID_678.csv', 'CLEANED#FID_679.csv', 'CLEANED#FID_680.csv', 'CLEANED#FID_681.csv', 'CLEANED#FID_682.csv', 'CLEANED#FID_683.csv', 'CLEANED#FID_684.csv', 'CLEANED#FID_685.csv', 'CLEANED#FID_686.csv', 'CLEANED#FID_687.csv', 'CLEANED#FID_688.csv', 'CLEANED#FID_689.csv', 'CLEANED#FID_690.csv', 'CLEANED#FID_691.csv', 'CLEANED#FID_692.csv']
# CSVsList=['CLEANED#FID_550.csv']
spList=[]
spDict = {}
# spDictFinal = {'Ephedra_intermedia': 0, 'Nepeta_glutinosa': 0, 'Delphinium_cashmerianum': 0, 'Acontholimon_lycopodiodes': 0, 'Oxytropis_glabra': 0, 'Oxytropis_tatarica': 0, 'Polygonum_rottboellioides': 0, 'Arnebia_euchroma': 0, 'Dianthus_anatolicus': 0, 'Nepeta_discolor': 0, 'Potentilla_multifida': 0, 'Cotoneaster_affinis': 0, 'Lonicera_spinosa': 0, 'Scorzonera_virgata': 0, 'Potentilla_saundersiana': 0, 'Puccinellia_distans': 0, 'Epilobium_angustifolium': 0, 'Silene_caespitella': 0, 'Atragalus_oplites': 0, 'Piptatherum_laterale_(g)': 0, 'Aconogon_tortuosum': 0, 'Psychrogeton_andryaloides': 0, 'Artemisia_brevifolia': 0, 'Euphorbia_thomsoniana': 0, 'Elymus_schrenkianus_(g)': 0, 'Rheum_webbianum': 0, 'Ephedra_geradiana': 0, 'Cicer_microphyllum': 0, 'Lonicera_asperifolia': 0, 'Lindelofia_stylosa': 0, 'Caragana_versicolor': 0, 'Elymus_canaliculatus_(g)': 0, 'Bistorta_affinis': 0, 'Geranium_himalayense': 0, 'Heracleum_pinnatum': 0}

for csvfile in CSVsList:
    inputCSV=csvfile
    df = pd.read_csv(inputCSV)
    print('inputCSV = ',inputCSV)
    df_cleaned = df.dropna(axis='columns',how='all')
    df_cleaned['individuals_Numbers'] = np.where(pd.isna(df_cleaned['individuals_Numbers']), df_cleaned['Cover_percent'], df_cleaned['individuals_Numbers'])
    print(df_cleaned)
    spLocal= set(df_cleaned['Species_Name'].tolist())
    spList=list(spLocal | set(spList))
    # spSet=set(spList)
    # print (spSet)

    # print ( "###################### "+inputCSV + " ######################")
    # print(df_cleaned)

# speciesName=df['Species_Name name']
# print (speciesName). df_cleaned['individuals_Numbers'] == '' or

# spDict= dict.fromkeys(spList,0);
print (spList)


# Species_Name,individuals_Numbers,Cover_percent
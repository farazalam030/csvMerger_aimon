CSVs=["FID_642.csv", "FID_643.csv", "FID_648.csv"]


for csv in CSVs:
    writeFlag=False
    with open (csv,"r+") as f:
        for line in f:
            cleanedCSV="CLEANED"+csv
            with open(cleanedCSV,'a') as of:
                if ("Species" in line or writeFlag):
                    writeFlag=True;
                    of.write(line);



import pdfplumber
import csv

with pdfplumber.open("revisedflora_ladakh.pdf") as pdf:
    with open("outputfomPDF.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table:
                    writer.writerow(row)

#THIS IS FOR TESTING ONLY, IGNORE THIS CODE

import pdfplumber
import pandas as pd

def pdf_to_csv(pdf_path, output_csv, columns):
    with pdfplumber.open(pdf_path) as pdf:
        rows = []
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table:
                    if any(cell.strip() for cell in row if cell):
                        rows.append([cell.strip() for cell in row])

        # Convert rows into a DataFrame with the specified columns
        df = pd.DataFrame(rows, columns=columns)
        
        # Save to CSV
        df.to_csv(output_csv, index=False)

# Define the column structure for AHTN 2017
columns_2017 = ["AHTN 2017", "Descriptions"]

# Define the column structure for AHTN 2022
columns_2022 = ["Hdg. No.", "AHTN 2022 Code", "Description", "MFN", "ATIGA", "ASEAN Member States Enjoying Concession"]

# Process the AHTN 2017 PDF
pdf_to_csv(
    r"C:\Users\user\Downloads\AHTN 2017.pdf",
    r"C:\Users\user\Downloads\AHTN_2017_Chapter_85.csv",
    columns_2017
)

# Process the AHTN 2022 PDF
pdf_to_csv(
    r"C:\Users\user\Downloads\AHTN 2022.pdf",
    r"C:\Users\user\Downloads\AHTN_2022_Chapter_85.csv",
    columns_2022
)
import pdfplumber
import pandas as pd

def extract_ahtn_data(pdf_path):
    ahtn_data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split('\n')
            
            for line in lines:
                # Assuming AHTN code and description are separated by a space or tab
                parts = line.split(maxsplit=1)
                if len(parts) == 2:
                    code, description = parts
                    ahtn_data.append((code, description))

    return ahtn_data

# Paths to your PDFs
pdf_paths = {
    "2017": r"C:\Users\user\Downloads\AHTN 2017.pdf",
    "2022": r"C:\Users\user\Downloads\AHTN 2022.pdf"
}

# Extract data from each PDF
ahtn_data_2017 = extract_ahtn_data(pdf_paths["2017"])
ahtn_data_2022 = extract_ahtn_data(pdf_paths["2022"])

# Convert to DataFrames for easier handling
df_2017 = pd.DataFrame(ahtn_data_2017, columns=["Code", "Description"])
df_2022 = pd.DataFrame(ahtn_data_2022, columns=["Code", "Description"])

# Save to CSV
df_2017.to_csv(r"C:\Users\user\Downloads\AHTN_2017.csv", index=False)
df_2022.to_csv(r"C:\Users\user\Downloads\AHTN_2022.csv", index=False)

print("Extraction complete. Data saved to CSV files.")
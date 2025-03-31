import pdfplumber
import pandas as pd
import os
import zipfile


pdf_path = "pdfs/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"  


data = []

# Abrir o PDF
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                data.append(row)  


df = pd.DataFrame(data)


csv_filename = "tabela_rol_procedimentos.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8")

# Compactar o arquivo CSV em ZIP
zip_filename = "Teste_SeuNome.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    zipf.write(csv_filename)

print(f"Tabela extraída e salva como {csv_filename}, compactada em {zip_filename}")

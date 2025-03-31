import requests
from bs4 import BeautifulSoup
import os
import zipfile

# site
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"


response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


pdf_links = []
for link in soup.find_all("a", href=True):
    if link["href"].endswith(".pdf"):
        pdf_links.append(link["href"])


os.makedirs("pdfs", exist_ok=True)


for pdf in pdf_links:
    pdf_name = pdf.split("/")[-1]
    pdf_path = os.path.join("pdfs", pdf_name)
    
    pdf_response = requests.get(pdf)
    with open(pdf_path, "wb") as f:
        f.write(pdf_response.content)
    print(f"Baixado: {pdf_name}")


zip_name = "anexos.zip"
with zipfile.ZipFile(zip_name, "w") as zipf:
    for pdf in os.listdir("pdfs"):
        zipf.write(os.path.join("pdfs", pdf), pdf)

print(f"Todos os PDFs foram baixados e compactados em {zip_name}")

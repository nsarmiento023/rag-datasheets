from pathlib import Path
from src.ingestion.extract import extract_pdf

pdf_path = Path("data/raw/esp32.pdf")
pages = extract_pdf(pdf_path)

page=pages[9]

print(f"Document : {page['document']}")
print(f"Page : {page['page']}")
print(page["text"])
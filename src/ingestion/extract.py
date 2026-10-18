from pathlib import Path
import pymupdf

def extract_pdf(path):
    doc=pymupdf.open(path)
    nom_pdf = Path(path).name
    pages_data=[]

    for nb_page, page in enumerate(doc, start=1) :
        text = page.get_text()
        pages_data.append({
            "document": nom_pdf,
            "page" : nb_page,
            "text" : text
        })

    return pages_data
    
    
if __name__ == "__main__":
    dossier = Path("data/raw")
    
    for fichier_pdf in dossier.glob("*.pdf"):
        # On passe 'fichier_pdf' (qui change à chaque tour) et non un nom fixe
        result = extract_pdf(fichier_pdf) 
        print(f"Fichier : {fichier_pdf.name} | Nombre de pages : {len(result)}")
from pathlib import Path
import pymupdf


def extract_pdf(path):
    nom_pdf = Path(path).name
    pages_data=[]
    with pymupdf.open(path) as doc :
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
    
    for fichier_pdf in sorted(dossier.glob("*.pdf")):
        # On passe 'fichier_pdf' (qui change à chaque tour) et non un nom fixe
        result = extract_pdf(fichier_pdf) 
        total_caracteres = 0
        page_vide=0

        for pages in result :
            text = pages["text"]
            vide=text.strip()
            total_caracteres+=len(text)
            if vide=="":
                page_vide+=1
        print(f"Fichier : {fichier_pdf.name} | Nombre de pages : {len(result)} | Nombre de caracteres : {total_caracteres} | Pages vides : {page_vide}")


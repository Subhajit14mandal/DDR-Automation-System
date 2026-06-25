
import fitz


def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    pages = []

    for page_no in range(len(doc)):

        page = doc[page_no]

        pages.append({
            "page": page_no + 1,
            "text": page.get_text()
        })

    return pages

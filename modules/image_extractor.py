
import fitz
import os


def extract_images(
        pdf_path,
        output_dir):

    os.makedirs(
        output_dir,
        exist_ok=True
    )

    doc = fitz.open(pdf_path)

    image_data = []

    for page_idx in range(len(doc)):

        page = doc[page_idx]

        images = page.get_images(full=True)

        for img_idx, img in enumerate(images):

            xref = img[0]

            image = doc.extract_image(xref)

            ext = image["ext"]

            filename = (
                f"page_{page_idx+1}_{img_idx}.{ext}"
            )

            filepath = os.path.join(
                output_dir,
                filename
            )

            with open(filepath, "wb") as f:
                f.write(image["image"])

            image_data.append({
                "page": page_idx + 1,
                "path": filepath
            })

    return image_data

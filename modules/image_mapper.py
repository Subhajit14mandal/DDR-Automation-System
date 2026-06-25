
AREAS = [
    "roof",
    "living room",
    "kitchen",
    "bathroom",
    "garage",
    "bedroom",
    "electrical panel"
]


def detect_area(text):

    text = text.lower()

    for area in AREAS:

        if area in text:
            return area

    return "general"


def map_images_to_areas(
        pages,
        images):

    mapping = {}

    for page in pages:

        area = detect_area(
            page["text"]
        )

        mapping.setdefault(
            area,
            []
        )

        page_images = [

            img["path"]

            for img in images

            if img["page"]
            == page["page"]
        ]

        mapping[area].extend(
            page_images
        )

    return mapping

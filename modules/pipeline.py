
import json

from modules.pdf_extractor import extract_text
from modules.image_extractor import extract_images
from modules.observation_parser import extract_observations
from modules.duplicate_detector import remove_duplicates
from modules.conflict_detector import detect_conflicts
from modules.image_mapper import map_images_to_areas
from modules.ddr_generator import generate_ddr
from modules.report_builder import create_report


def run_pipeline(
        inspection_pdf,
        thermal_pdf,
        output_docx="/content/drive/MyDrive/Assignment/outputs/report.docx",
        image_dir="/content/drive/MyDrive/Assignment/outputs/images"
):

    inspection_pages = extract_text(
        inspection_pdf
    )

    thermal_pages = extract_text(
        thermal_pdf
    )

    inspection_images = extract_images(
        inspection_pdf,
        image_dir
    )

    thermal_images = extract_images(
        thermal_pdf,
        image_dir
    )

    inspection_obs = []

    for page in inspection_pages:

        obs = extract_observations(
            page["text"]
        )

        inspection_obs.extend(
            json.loads(obs)
        )

    thermal_obs = []

    for page in thermal_pages:

        obs = extract_observations(
            page["text"]
        )

        thermal_obs.extend(
            json.loads(obs)
        )

    inspection_obs = remove_duplicates(
        inspection_obs
    )

    thermal_obs = remove_duplicates(
        thermal_obs
    )

    conflicts = detect_conflicts(
        inspection_obs,
        thermal_obs
    )

    all_obs = (
        inspection_obs
        +
        thermal_obs
    )

    all_pages = (
        inspection_pages
        +
        thermal_pages
    )

    all_images = (
        inspection_images
        +
        thermal_images
    )

    image_map = map_images_to_areas(
        all_pages,
        all_images
    )

    ddr = generate_ddr(
        all_obs,
        conflicts
    )

    create_report(
        ddr,
        image_map,
        output_docx
    )

    return {
        "report": output_docx,
        "conflicts": conflicts,
        "observations": len(all_obs)
    }

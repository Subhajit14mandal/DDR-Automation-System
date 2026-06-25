# DDR-Automation-System
AI-powered DDR generator that combines inspection and thermal reports into structured client-ready diagnostic reports.
# AI-Powered DDR (Detailed Diagnostic Report) Generator

## Overview

This project is an AI-powered document processing system that automatically generates a Detailed Diagnostic Report (DDR) from multiple property inspection documents.

The system processes:

* Inspection Reports
* Thermal Reports

and combines information from both sources to generate a structured, client-ready DDR.

The solution focuses on reliability, information extraction, conflict handling, duplicate removal, image extraction, and structured report generation.

---

## Problem Statement

Property inspection reports often contain information spread across multiple documents. Reviewing and consolidating these documents manually is time-consuming and prone to inconsistencies.

The objective of this project is to automate the process of:

* Extracting observations from inspection documents
* Combining findings from multiple sources
* Detecting conflicting information
* Handling missing data
* Generating a professional DDR report

---

## Solution Architecture

### Workflow

<img width="1024" height="1536" alt="Copilot_20260625_230740" src="https://github.com/user-attachments/assets/f6e90ff3-e3e7-4cab-8403-c3b58acba9b6" />


---

## Key Features

### 1. Text Extraction

The system extracts textual information from both inspection and thermal reports using PDF parsing.

### 2. Observation Extraction

Relevant observations are extracted and converted into structured JSON format.

Example:

```json
{
  "area": "Roof",
  "observation": "Water leakage observed near flashing",
  "severity": "High",
  "source": "Inspection Report"
}
```

### 3. Duplicate Detection

Similar observations from multiple documents are identified and merged to avoid redundant reporting.

### 4. Conflict Detection

Conflicting findings between reports are detected and explicitly included in the final DDR instead of being automatically resolved.

Example:

Inspection Report:
"Moisture detected in west wall"

Thermal Report:
"No moisture detected in west wall"

The system records this as a conflict and reports it transparently.

### 5. Image Extraction

Relevant images are extracted directly from source documents.

### 6. Image Mapping

Images are associated with related observations and included in the final report.

### 7. DDR Generation

The final DDR is generated with the following structure:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

---

## Project Structure

```text
DDR_Project/

├── data/
│   ├── inspection_report.pdf
│   └── thermal_report.pdf
│
├── modules/
│   ├── pdf_extractor.py
│   ├── image_extractor.py
│   ├── observation_parser.py
│   ├── duplicate_detector.py
│   ├── conflict_detector.py
│   ├── image_mapper.py
│   ├── ddr_generator.py
│   └── report_builder.py
│
├── outputs/
│   ├── report.docx
│   └── images/
│
├── notebooks/
│   └── DDR_Pipeline.ipynb
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* PyMuPDF (fitz)
* OpenAI / Gemini API
* python-docx
* JSON
* Google Colab

---

## How to Run

### Step 1

Install dependencies:

```bash
pip install -r requirements.txt
```

### Step 2

Upload:

* Inspection Report PDF
* Thermal Report PDF

into the data directory.

### Step 3

Run the notebook or pipeline script.

```python
result = run_pipeline(
    inspection_pdf,
    thermal_pdf
)
```

### Step 4

Generated reports will be available inside:

```text
outputs/
```

---

## Handling Missing Information

When required information is unavailable, the system explicitly reports:

"Not Available"

instead of generating assumptions.

---

## Handling Conflicting Information

Conflicting findings from different reports are identified and documented separately.

The system never attempts to invent a resolution for conflicting observations.

---

## Limitations

* Area detection currently relies on predefined keywords.
* Observation extraction depends on document quality.
* Highly unstructured reports may reduce extraction accuracy.
* Image-to-observation mapping is page-based and may not always be perfect.

---

## Future Improvements

* OCR support for scanned PDFs
* Vector database for semantic retrieval
* Advanced image classification
* Improved conflict resolution workflow
* Multi-document processing beyond two reports
* Web application deployment

---

## Conclusion

This project demonstrates an end-to-end AI workflow for transforming inspection documents into structured diagnostic reports. The focus is on reliability, transparency, and practical document intelligence rather than user interface design.

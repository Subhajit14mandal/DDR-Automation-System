
import json
from openai import OpenAI

client = OpenAI()


def generate_ddr(
        observations,
        conflicts):

    payload = {
        "observations":
            observations,

        "conflicts":
            conflicts
    }

    prompt = f"""
Create a DDR.

Mandatory Sections:

1 Property Issue Summary

2 Area-wise Observations

3 Probable Root Cause

4 Severity Assessment

5 Recommended Actions

6 Additional Notes

7 Missing Information

Rules:

- No hallucination
- Mention conflicts
- Mention Not Available
- Client friendly language

DATA:

{json.dumps(payload)}
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content

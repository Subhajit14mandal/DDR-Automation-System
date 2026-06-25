
from openai import OpenAI

client = OpenAI()


def extract_observations(page_text):

    prompt = f"""Extract observations.

    Return JSON.

    Format:

    [
      {{
        "area":"",
        "observation":"",
        "severity":"",
        "source":""
      }}
    ]

    Text:

    {page_text}
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

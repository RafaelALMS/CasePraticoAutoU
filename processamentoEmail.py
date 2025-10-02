from typing import List
from google import genai
import xml.etree.ElementTree as ET
from pathlib import Path
from pydantic import BaseModel
import os

PROMPTXML= Path("prompt.xml")

CLIENT = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

class PromptList(BaseModel):
    summary:str
    bulletPoints:List[str]


def promptResponse(email):
    tree= ET.parse(PROMPTXML)
    root= tree.getroot()
    quenstion=root.find("question/question")
    summary=root.find("expected_output_format/generated_summary")
    bulletPoint=root.find("expected_output_format/generated_BulletList")

    response = CLIENT.models.generate_content(
    model="gemini-2.5-flash", contents=[quenstion.text,summary.text,bulletPoint.text, email],
    config={"response_mime_type": "application/json",
            "response_schema": list[PromptList]}
    )

    Myresponse: list[PromptList]=response.parsed
    return Myresponse

print(promptResponse("usefull email"))
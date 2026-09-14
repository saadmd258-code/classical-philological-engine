"""
Live Philological AI Pipeline with Dynamic Model Fallback and Robust Pydantic Validation.
Gracefully handles non-root functional particles (حروف المعاني) without schema crashes.
"""

import json
import os
import time
from typing import List, Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field, field_validator
from google import genai
from core_engine import ClassicalProsodyEngine

load_dotenv()

class TokenAnalysisSchema(BaseModel):
    word: str = Field(description="Original Arabic word token")
    root: Optional[str] = Field(default="لا جذر له (حرف/مبني)", description="Trilateral or Quadrilateral unaugmented root")
    morphology: str = Field(description="Full Sarf morphological form in Arabic")
    syntax_en: str = Field(description="Accurate syntactic role and case in English")

    @field_validator("root", mode="before")
    @classmethod
    def sanitize_root(cls, value):
        if value is None or str(value).strip() == "" or str(value).lower() == "null":
            return "لا جذر له (حرف/مبني)"
        return str(value)

class VerseAnalysisSchema(BaseModel):
    bahr_name_ar: str = Field(description="Name of the meter in Arabic")
    bahr_name_en: str = Field(description="Name of the meter in English")
    cadence_ar: str = Field(description="Cadence tafail")
    binary_notation: str = Field(description="Prosodic binary movement")
    tokens: List[TokenAnalysisSchema]
    thematic_depth: str = Field(description="Epistemological and literary context in English")

class PhilologicalPipelineOrchestrator:
    @staticmethod
    def process_any_verse(verse_text: str) -> VerseAnalysisSchema:
        meter_info = ClassicalProsodyEngine.identify_meter_dynamically(verse_text)
        
        prompt = f"""
        Act as an uncompromising Classical Arabic Philologist and Grammarian.
        Dissect the following verse into every word token with absolute precision according to Basra/Kufa syntax rules.
        Verse: {verse_text}

        Return STRICT JSON matching this schema:
        {{
            "tokens": [
                {{
                    "word": "word string",
                    "root": "root letters separated by space or 'لا جذر له' for particles/pronouns",
                    "morphology": "detailed arabic sarf description",
                    "syntax_en": "exact grammatical analysis in English"
                }}
            ],
            "thematic_depth": "Literary analysis and cultural context of this verse in English"
        }}
        Do not return markdown code blocks, return pure JSON.
        """
        
        active_key = os.environ.get("GEMINI_API_KEY")
        candidate_models = ['gemini-2.5-flash', 'gemini-3.1-pro-preview']
        raw_text = None
        
        if active_key:
            client = genai.Client(api_key=active_key)
            last_error = None
            
            for target_model in candidate_models:
                for attempt in range(2):
                    try:
                        response = client.models.generate_content(
                            model=target_model,
                            contents=prompt
                        )
                        raw_text = response.text.replace("```json", "").replace("```", "").strip()
                        if raw_text:
                            break
                    except Exception as err:
                        last_error = err
                        time.sleep(1.5)
                if raw_text:
                    break
            
            if not raw_text:
                raise RuntimeError(f"Engine routing failure: {str(last_error)}")
            
            data = json.loads(raw_text)
            tokens = [TokenAnalysisSchema(**t) for t in data["tokens"]]
            thematic = data.get("thematic_depth", "Classical literary commentary.")
        else:
            tokens = [
                TokenAnalysisSchema(
                    word=w,
                    root="غير متوفر",
                    morphology="تحليل محلي احتياطي",
                    syntax_en="GEMINI_API_KEY not found in background environment."
                )
                for w in verse_text.split()
            ]
            thematic = "Background key not configured."

        return VerseAnalysisSchema(
            bahr_name_ar=meter_info["name_ar"],
            bahr_name_en=meter_info["name_en"],
            cadence_ar=meter_info["cadence_ar"],
            binary_notation=meter_info["binary_notation"],
            tokens=tokens,
            thematic_depth=thematic
        )
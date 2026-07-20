import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

class ImagePromptGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key: raise ValueError("GEMINI_API_KEY not found")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def _generate_prompt(self, business_info, concept):
        prompt = f"""
        Generate a professional AI image prompt for a business.
        Business: {business_info.get('business_name')}
        Industry: {business_info.get('industry')}
        Brand Tone: {business_info.get('brand_tone')}
        Concept: {concept}
        Include style, mood, lighting, color palette, and quality (e.g., 4K, ultra-realistic).
        Return only the prompt text.
        """
        return self.model.generate_content(prompt).text.strip()

    def generate_multiple_prompts(self, business_info: dict, count: int = 3) -> list:
        concepts = ["professional office environment", "team collaboration", "digital transformation"]
        return [self._generate_prompt(business_info, concept) for concept in concepts[:count]]
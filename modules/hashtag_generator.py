import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

class HashtagGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key: raise ValueError("GEMINI_API_KEY not found")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def _generate_list(self, prompt, count=10):
        response = self.model.generate_content(f"{prompt} Return {count} hashtags as a comma-separated list. No other text.")
        tags = [tag.strip() for tag in response.text.split(',') if tag.strip()]
        return tags[:count]

    def generate_all_hashtags(self, industry: str, country: str) -> dict:
        return {
            'trending': self._generate_list(f"Generate trending hashtags for the {industry} industry globally."),
            'industry': self._generate_list(f"Generate specific hashtags for the {industry} industry."),
            'local': self._generate_list(f"Generate location-based hashtags for the {industry} industry in {country}.")
        }
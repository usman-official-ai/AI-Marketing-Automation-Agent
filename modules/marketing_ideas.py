import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

class MarketingIdeasGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key: raise ValueError("GEMINI_API_KEY not found")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def _generate_ideas(self, idea_type, business_info, count=10):
        prompt = f"""
        Generate {count} {idea_type} ideas for a business.
        Business: {business_info.get('business_name')}
        Industry: {business_info.get('industry')}
        Services: {business_info.get('services')}
        Target Audience: {business_info.get('target_audience')}
        Country: {business_info.get('country')}
        Brand Tone: {business_info.get('brand_tone')}
        Return only a numbered list.
        """
        response = self.model.generate_content(prompt)
        return [line.strip() for line in response.text.split('\n') if line.strip()][:count]

    def generate_all_ideas(self, business_info: dict) -> dict:
        return {
            'campaigns': self._generate_ideas("marketing campaign", business_info),
            'promotional': self._generate_ideas("promotional", business_info),
            'lead_generation': self._generate_ideas("lead generation", business_info)
        }
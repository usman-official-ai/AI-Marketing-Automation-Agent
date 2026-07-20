import os
import google.generativeai as genai
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

class CalendarGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key: raise ValueError("GEMINI_API_KEY not found")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_calendar(self, business_info: dict) -> pd.DataFrame:
        prompt = f"""
        Generate a 7-day content calendar for a business.
        Business Name: {business_info.get('business_name')}
        Industry: {business_info.get('industry')}
        Services: {business_info.get('services')}
        Brand Tone: {business_info.get('brand_tone')}
        Country: {business_info.get('country')}
        Return as a markdown table with columns: Day | Post Topic | Platform | Caption Idea | CTA.
        """
        response = self.model.generate_content(prompt)
        # Simple parsing logic
        lines = [line for line in response.text.split('\n') if '|' in line and '---' not in line]
        data = []
        for line in lines[1:]:  # Skip header
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) == 5:
                data.append(dict(zip(['Day', 'Post Topic', 'Platform', 'Caption Idea', 'CTA'], parts)))
        return pd.DataFrame(data)
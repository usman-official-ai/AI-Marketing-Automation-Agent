import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

class EmailGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key: raise ValueError("GEMINI_API_KEY not found")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def _generate_email(self, email_type, business_info):
        prompt = f"""
        Write a professional {email_type} email for a business.
        Business Name: {business_info.get('business_name')}
        Industry: {business_info.get('industry')}
        Services: {business_info.get('services')}
        Brand Tone: {business_info.get('brand_tone')}
        Target Audience: {business_info.get('target_audience')}
        Country: {business_info.get('country')}
        Include a subject line and a clear call to action.
        Return only the email content.
        """
        return self.model.generate_content(prompt).text

    def generate_all_emails(self, business_info: dict) -> dict:
        return {
            'cold': self._generate_email("cold outreach", business_info),
            'followup': self._generate_email("follow-up", business_info),
            'promotional': self._generate_email("promotional", business_info)
        }
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

class ContentGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key: raise ValueError("GEMINI_API_KEY not found")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def _generate(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text

    def generate_all_content(self, business_info: dict) -> dict:
        name, industry, audience, country, services, tone = business_info.values()
        base_prompt = f"Business: {name}, Industry: {industry}, Audience: {audience}, Country: {country}, Services: {services}, Tone: {tone}."

        prompts = {
            'facebook': f"Write a professional, engaging Facebook post for a business. {base_prompt} Include a CTA and relevant hashtags.",
            'linkedin': f"Write a professional, thought-leadership LinkedIn post. {base_prompt} Focus on value and include a CTA.",
            'instagram': f"Write a captivating Instagram caption. {base_prompt} Make it visual, use emojis, and include a CTA and hashtags.",
            'twitter': f"Write a concise, engaging Twitter/X post (max 280 chars). {base_prompt} Include a CTA and hashtags."
        }
        return {platform: self._generate(prompt) for platform, prompt in prompts.items()}
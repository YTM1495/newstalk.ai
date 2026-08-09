from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

class GeminiClient:

    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        self.client = genai.Client(api_key = self.api_key)
    def generate_summary(self,article_text):
        prompt = f"""
You are an experienced news editor.

Your task is to summarize the following news article.

Rules:
- Keep the summary between 3 and 4 sentences.
- Preserve only the most important facts.
- Do not add information that is not present in the article.
- Use clear and professional language.
- Return only the summary.

Article:
{article_text}
"""    
        try:
            response = self.client.models.generate_content(
            model = "gemini-3.6-flash",
            contents = prompt, 
        )
            return response.text
        except Exception as e:
            raise RuntimeError( 
                f"Failed to generate summary:{e}"
                               )
           

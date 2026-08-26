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
    def generate(self,prompt):
        
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
           

from backend.ai.gemini_client import GeminiClient

client = GeminiClient()

article = """
Artificial intelligence is transforming industries across the world.
Healthcare organizations are using AI to assist doctors in diagnosing diseases
from medical images with greater accuracy. Financial institutions are employing
machine learning models to detect fraudulent transactions in real time.
Educational platforms are providing personalized learning experiences using AI tutors.
Meanwhile, governments are discussing regulations to ensure responsible AI development.
Experts believe AI will significantly improve productivity, but they also warn about
ethical concerns such as bias, privacy, and job displacement. Many companies are
investing billions of dollars into AI research to remain competitive in the future.
"""
summary = client.generate_summary(article)
print(summary)
from google import genai
from config.settings import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello! Tell me you are ready to build my LinkedIn AI Agent."
)

print(response.text)
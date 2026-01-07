import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")


def explain_recommendation(user_context, candidates):
    prompt = f"""
You are an EV charging assistant.

User context:
- Battery: {user_context['battery_percent']}%
- Vehicle range: {user_context['range_km']} km

Charging station options:
{candidates}

Choose the best station and explain briefly (2–3 sentences):
- Consider distance
- Price
- Availability
- Battery safety
"""

    response = model.generate_content(prompt)
    return response.text.strip()

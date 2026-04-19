"""
LLM Client — Phase 1: The Brain Connection
Uses Groq API (free tier) with Llama-3 for fast inference.
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_llm(prompt: str, system_msg: str = "You are a gaming analytics AI assistant.", temperature: float = 0.3) -> str:
    """Send a prompt to the LLM and return the response as a string."""
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
            max_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[LLM Error] {str(e)}"

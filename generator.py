from dotenv import load_dotenv
from groq import Groq
import os
load_dotenv()
client=Groq(
    api_key=os.getenv("OPEN_API_KEY")
)
def generate_content(topic,content_type,tone,word_limit,extra_instruction):
    prompt=f"""
    Generate a {content_type},
    Topic:{topic}
    Tone:{tone}
    Word Limit:{word_limit}
    Additional_Instructions:{extra_instruction}
    """
    try:
        
        response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
            "role":"system",
            "content":"You are a professional content writer."
            },
            {
                "role":"user",
                "content":prompt
            }
            
        ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"error:{str(e)}"

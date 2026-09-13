import streamlit as slit
from groq import Groq
slit.title("Summarizer")
text = slit.text_area("Enter your text",height=300)
client = Groq(api_key=slit.secrets["GROQ_API_KEY"])
if slit.button("Summarize"):
    if len(text.split()) < 10:
        slit.warning("too short")
    else:
        with slit.spinner("Summarizing..."):
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[{"role": "system", "content" : "You're a helpful assistant who has the ability to summarize please use your summarization ability to summarize this text that's given into 4 a sentences long, you must summarize based on the same language as in the text it gave you"}, {"role":"user", "content":text}]

            )
            slit.success(response.choices[0].message.content)
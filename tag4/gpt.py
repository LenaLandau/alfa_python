#!/usr/bin/env python3
# Wen es interessiert: so spricht man GPT API an
import os
import openai # pip install openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY") or "sk-..." )
model="gpt-4-turbo"
# model="gpt-4"

PROMPT="Du sprichst Deutsch. Antworte IMMER auf Deutsch!!"
def ask(query):
	messages = [{"role": "system", "content": PROMPT}, {"role": "user", "content": query}]
	ok=client.chat.completions.create(model=model, messages=messages)
	result=ok.choices[0].message.content
	return result

# print(ask("What is the capital of France?"))
# print(ask("wie aktuell ist Dein Datenbestand?"))
print(ask("What is the actual cutoff date?"))
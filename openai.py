
import os
import openai
import numpy as np
import pandas as pd
import json
# from langchain.chat_models import ChatOpenAI
# from langchain.document_loaders import CSVLoader
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.prompts import ChatPromptTemplate
# from langchain.vectorstores import Chroma
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableLambda, RunnablePassthrough
# from openai.embeddings_utils import get_embedding
from decouple import config

class OpenAIFunctions:
    def __init__(self, api_key: str):
        openai.api_key = config("OPEN_API_KEY")

    def generate_response(self, prompt: str) -> str:
        try:
            struct = []
            user_message = prompt
            struct.append({"role": "user", "content": user_message})
            chat = openai.ChatCompletion.create(model="gpt-4o-mini", messages=struct)
            response = chat.choices[0].message.content
            struct.append({"role": "assistant", "content": response})
            return struct
        except Exception as e:
            return f"Error generating response: {str(e)}"

    def analyze_sentiment(self, text: str) -> str:
        try:
            prompt = f"Analyze the sentiment of the following text and respond with either 'Positive', 'Negative', or 'Neutral':\n\n{text}"
            response = self.generate_response(prompt)
            return response
        except Exception as e:
            return f"Error analyzing sentiment: {str(e)}"

    def summarize_text(self, text: str, max_summary_length: int = 100) -> str:
        try:
            prompt = f"Summarize the following text in no more than {max_summary_length} words:\n\n{text}"
            summary = self.generate_response(prompt, max_tokens=max_summary_length * 2)
            return summary
        except Exception as e:
            return f"Error summarizing text: {str(e)}"
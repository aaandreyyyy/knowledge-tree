from settings import GEMINI_API_KEY

import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text: str):
    text = text.replace('•', '  *')
    return Markdown(text)


def display_markdown(text: str):
    markdowned = to_markdown(text)
    display(markdowned)


class GeminiModel:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)

        self.model_type = 'gemini-pro'
        self.model = genai.GenerativeModel(self.model_type)

    def get_response(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text

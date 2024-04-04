# GEMINI_API_KEY = 'AIzaSyAKu9Q7-mhKylp8zZKBwxatsM6IfUmaAPA'
# 
# import pathlib
# import textwrap
# 
# import google.generativeai as genai
# 
# from IPython.display import display
# from IPython.display import Markdown
# 
# 
# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
# 
# genai.configure(api_key=GEMINI_API_KEY)
# 
# 
# # print('available models')
# # for m in genai.list_models():
# #   if 'generateContent' in m.supported_generation_methods:
# #     print(m.name)
# # print('------------\n\n\n')
#
#
# model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("What is the meaning of life?")

# print(response.text)
s = '''This paper introduces several novel strategies for multi-step-ahead prediction of chaotic time series.
Introducing a concept of “generalized z-vectors” (vectors of nonsuccessive time series observations) makes it possible to generate sets of possible prediction values for each point we are trying to predict.
Through examining these sets, unifed predictions are calculated, which are in turn used as a basis for predicting subsequent points.
The key diference between the strategy presented in this paper and its conventional counterparts is the concept of “nonpredictable” points (points which the algorithm categorized as “incalculable” and excluded from the calculations altogether).'''

from dotenv import load_dotenv
import os
import openai
from openai import OpenAI
import requests
import json

load_dotenv()
open_ai_key = os.getenv("OPEN_AI_KEY")


def paraphrase_with_openai(text):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {open_ai_key}",
        "OpenAi-Project":"proj_o2HSPC5IEcfJCHEqWCfEZkpv"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": f"Please restructure the following sentences to improve coherence and readability:\n\n{text}"}
            ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Print the response
    if response.status_code == 200:
        response_data = response.json()
        print(json.dumps(response_data, indent=2))
        restructured_text = response_data['choices'][0]['message']['content'].strip()
        print("Restructured Text:", restructured_text)
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")


# translated_text = """
# The first chapter of all things 1.1 Yuguzi of Yusus said that when he talked about microfinance, he had
#  to mention a person: Dr. Yusus.This Bangladesh, who is now famous in the world, is named Hammed,
#  Yusus, is an economist and the founder of Crameen Bank (meaning rural bank).The name of "poor
#  people's bankers".In 2006, to recognize their efforts to promote economic and social development from
#  the bottom of the society, "Yusus and Grah Ring Bank won the Nobel Peace Prize. In 1940, Yusus was
#  born in a wealthy and devout name in Bangladesh's Guoga Port.The father of the Slin family gave him
#  good living conditions and his enthusiasm for learning, and his mother gave him a kind heart.Full of
#  sympathy, Zhou Ji always visits our poor relatives from a distant countryside.It was her care for her
#  family and poor people who affected me and helped me discover that she was interested in economics
#  and social reform.When Yusus graduated from Daka University, he was only 21 years old, and his alma
#  mater provided him with a position of economics teachers.The University of Daka was founded by the
#  British in 1836. It is the most respected and negative study in South Asia. "As a teacher, Yusus stayed
#  there for 5 years. In 1965, he came to the University of Guan Guodebelt University to study for a PhD in
#  economics.Degree. Dos at the University of Vandei met the key to affecting his future life is his mentor
#  Nicholas.He taught Wannu's precise economic thinking model, which eventually helped people to
#  establish a grid rings banking.

# """
# response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": f"Please restructure the following sentences to improve coherence and readability:\n\n{translated_text}"}
#             ],
#             max_tokens=150,
#             temperature=0.7
#         )

# restructured_text = response['choices'][0]['message']['content'].strip()
# print(restructured_text)

'''
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "write an email to my boss for resignation"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
'''

import openai
from config import apikey
openai.api_key = apikey


class Completion:
  pass


response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "write an email to my boss for resignation"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

'''
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation?",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
'''


def chat():
  return None


'''
from openai import OpenAI
client = OpenAI()

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="write an email to boss about resignation",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)



 model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "write an email to my boss for resignation"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
'''
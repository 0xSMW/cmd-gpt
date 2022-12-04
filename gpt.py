import openai
import sys

prompt = sys.argv[1]
openai.api_key = 'OPENAI_API_KEY'
r = openai.Completion.create(model='text-davinci-003', prompt=prompt, temperature=0.2, max_tokens=1024)
response = r.choices[0]['text']

print('\n'+response.strip('\n')+'\n')
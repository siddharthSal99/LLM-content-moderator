from config import CLIENT_ID, SECRET_KEY, OPENAI_KEY
from config import reddit_auth_data as data

import requests

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)



headers = {
    'User-Agent': 'RedditAutomod/0.0.1'
}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth,
                    data=data,
                    headers=headers)
TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'

# resp = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).json()
# print(resp)

subreddit = 'r/explainlikeimfive'

resp = requests.get(f'https://oauth.reddit.com/{subreddit}/about/rules', headers=headers).json()
# print(resp)
rulesPrompt = ""

for ix,el in enumerate(resp['rules']):
    
    ruleDesc = (el['description'])
    singleRuleTemplate = f'Rule {ix}) {ruleDesc}\n\n'
    rulesPrompt += singleRuleTemplate

print(rulesPrompt)
# resp = requests.get('https://oauth.reddit.com/r/explainlikeimfive/about/', headers=headers).json()

# print(resp)
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key=OPENAI_KEY)
             
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.chains import LLMChain

template = "Here are the rules for the subreddit {subreddit}:\n {rules}"
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

chain = LLMChain(llm=llm, prompt=chat_prompt, output_parser=StrOutputParser())
out = chain.run(subreddit=subreddit,rules=rulesPrompt,text="Create a post for this subreddit that would violate rule 4")
print(out)

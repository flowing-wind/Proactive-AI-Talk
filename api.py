from openai import OpenAI
from Message_Generator import MsgGen
from init import init_all

def SendMsg (messages):
    response = client.chat.completions.create(
        model = "deepseek-chat",
        messages = messages, 
        max_tokens = 200, 
        stream = False, 
        temperature = 1.3
    )
    message = response.choices[0].message
    return message

# ------------------------------------------------------------------------------- #

# init_all ()

# get api key
with open ("api_key.txt", 'r', encoding="utf-8") as f:
    key = f.read ()
client = OpenAI(api_key=key, base_url="https://api.deepseek.com")


# new topic
messages = [{"role": "system", "content": "you are my friend and we are talking about some interesing news that happened recently"},]
tmp = {"role": "user", "content": MsgGen ()}
messages.append (tmp)
k = int (input ("The number of rounds you want to chat with the AI: "))
for i in range (k):
    message = SendMsg (messages)
    messages.append (message)
    print ("\n"+message.content)
    msg = input ("\nUser: ")
    user_msg = {"role": "user", "content": msg}
    messages.append (user_msg)
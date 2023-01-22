# import necessary packages
import os
import cohere

# initialize cohere api client
co = cohere.Client(os.environ.get('COHEREAI_API_KEY'))

# initialize a conversation session id
cohere_chat_res_start = co.chat("Hi")
conv_session_id = cohere_chat_res_start.session_id

# continue existing chat session
def talk(prompt):
  response = co.chat(prompt, session_id=conv_session_id)
  return response.reply

# take prompt from user and call talk function. run this in loop till user exits
while True:
    prompt = input("You: ")
    if prompt == "exit":
        break
    print("Bot: ", talk(prompt))


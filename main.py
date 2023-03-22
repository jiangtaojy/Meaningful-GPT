import openai
import argparse
import os


def send_msg(msg):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )
    res = completion["choices"][0]["message"]["content"].strip()
    return res


class ChatGpt:
    def __init__(self, api_key):
        self.contexts = []
        openai.api_key = api_key

    def get_response(self, text):
        user_input = {"role": "user", "content": text}
        self.contexts.append(user_input)
        res = send_msg(self.contexts)
        assist_res = {"role": "assistant", "content": res}
        if len(self.contexts) > 10:
            self.contexts = self.contexts[2:]
        self.contexts.append(assist_res)
        return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start enjoying chatgpt(gpt3.5)! Please enter \"exit\" to exit")
    parser.add_argument("-k", "--key", type=str, help="open api key", default=None)
    args = parser.parse_args()
    if args.key is not None:
        chat_gpt = ChatGpt(args.key)
    else:
        key = os.environ["OPENAI_API_KEY"]
        chat_gpt = ChatGpt(key)
    print("Start enjoying it! Please enter \"exit\" to exit")
    while True:
        msg = input(">> ")
        if msg == "exit":
            break
        res = chat_gpt.get_response(msg)
        print(res)

import os
from dotenv import load_dotenv
import openai
import json
from websocket_server import WebsocketServer

print("connecting to openai api...")

load_dotenv()

openai.organization = os.getenv('OPENAI_API_ORG')
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.Model.list()

print("connected to openai api successfully!")

start = """
你現在是一個文字冒險遊戲
你的工作就是盡可能清楚仔細地描述現在的場景、劇情、主角與附近的狀態然後列出四個行動選項
而玩家要做的是輸入訊息一個數字選擇要採取的行動
而且你每則訊息必須為有效的json格式像是這樣 {"description":"這裡寫劇情、場景內容","options":["選項1","選項2","選項3","選項4","選項5"]}
記得要用繁體中文
"""

class gameData():
    def __init__(self, origin:any) -> None:
        self.msg = json.loads(str(origin))["choices"][0]["message"]["content"]
        message.append({"role":"assistant", "content":self.msg})
        self.data = json.loads(self.msg)
        self.description = self.data["description"]
        self.options = self.data["options"]

message = []

def chat(role, content):
    message.append({"role":role, "content":content})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= message
    )
    return gameData(response)

print("loading game...")

data = chat("user", start)

print("game data initialize successfully!")

def new_client(_, server):
    server.send_message_to_all(data.msg)

def message_received(_, server, message):
    print(f"user choice >> {message}")
    data = chat("user", str(message))
    server.send_message_to_all(data.msg)
    print(f"chatGPT response >> {data.msg}")

server = WebsocketServer(host='127.0.0.1', port=13254)
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.run_forever()
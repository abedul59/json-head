

from sanic.exceptions import SanicException
from sanic import Sanic
from sanic import response
import logging
from linebot import WebhookParser
from linebot.models import TextMessage
from aiolinebot import AioLineBotApi

app = Sanic(__name__)
################################################################
#import openai, os
	
#openai.api_key = os.getenv("OPENAI_API_KEY")






'''	
conversation = []

class ChatGPT:  
    

    def __init__(self):
        
        self.messages = conversation
        self.model = os.getenv("OPENAI_MODEL", default = "gpt-3.5-turbo")



    def get_response(self, user_input):
        conversation.append({"role": "user", "content": user_input})
        

        response = openai.ChatCompletion.create(
	            model=self.model,
                messages = self.messages

                )

        conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
        
        print("AI回答內容：")        
        print(response['choices'][0]['message']['content'].strip())


        
        return response['choices'][0]['message']['content'].strip()
	'''
	



#chatgpt = ChatGPT()

 	
from linebot import AsyncLineBotApi, WebhookParser
from linebot.aiohttp_async_http_client import AiohttpAsyncHttpClient

#from linebot import LineBotApi, WebhookHandler, WebhookParser
#from linebot.exceptions import InvalidSignatureError
#from linebot.models import MessageEvent, TextMessage, TextSendMessage



line_bot_api = AioLineBotApi(channel_access_token=os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
parser = WebhookParser(channel_secret=os.getenv("LINE_CHANNEL_SECRET")) 





@app.route('/')
async def handle_request(request):
    return response.text("Hello!")


@app.post("/callback")
async def handle_callback(request):
    events = parser.parse(
        req.get_body().decode("utf-8"),
        req.headers.get("X-Line-Signature", ""))

    for ev in events:
        # reply echo
        await line_api.reply_message(
            ev.reply_token,
            TextMessage(text=f"You said: {ev.message.text}"))

    # 200 response
    return response.text("OK!")



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8006)
 
 

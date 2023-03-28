

from sanic.exceptions import SanicException
from sanic import Sanic
from sanic import response
import aiohttp
import asyncio
import re
import json

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

from linebot import LineBotApi, WebhookHandler, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage




#line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
#handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET")) 



#session = aiohttp.ClientSession()
#async_http_client = AiohttpAsyncHttpClient(session)
#line_bot_api = AsyncLineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
#parser = WebhookParser(os.getenv("LINE_CHANNEL_SECRET"))

from linebotx import LineBotApiAsync, WebhookHandlerAsync
line_bot_api = LineBotApiAsync(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandlerAsync(os.getenv("LINE_CHANNEL_SECRET"))

@app.route('/')
async def handle_request(request):
    return response.text("Hello!")



@app.post("/callback")
async def handle_callback(request):
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = await request.body()
    body = body.decode()
	

    #try:
        #events = parser.parse(body, signature)
    await events = handler.handle(body, signature)
    #except InvalidSignatureError:
        #raise SanicException("Something went wrong.", status_code=400)

    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        await line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

    return response.text("OK!") 


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8006)
 
 

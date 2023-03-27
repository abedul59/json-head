from sanic import Sanic
from sanic import response
import aiohttp
import asyncio
import re
import json

app = Sanic(__name__)





@app.route('/')
async def handle_request(request):
    return response.text("Hello!")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8006)

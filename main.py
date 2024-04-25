import asyncio, random
from pyrogram import Client, filters

api_id = "your api id"
api_hash = "your api hash"


app = Client("dev", api_id, api_hash)

TARGET = [group_id_1, group_id_2]

@app.on_message(filters.chat(TARGET))
async def reaction_handler(client, message):
    message_id = message.id
    chat_id = message.chat.id
    input = await app.get_chat(chat_id)
    output = input.available_reactions
    radius = len(output)
    rand = random.randint(0, radius)
    await app.send_reaction(chat_id, message_id, f"{output[rand]}")
 
if __name__ == '__main__':
    app.run() 

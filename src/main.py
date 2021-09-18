import discord
import random
import time

client = discord.Client()

word_list = ['ala pa eso?','ke riiico paaapu','estare kachando','ni tu vieja te salva','caaalla boliviano']

@client.event
async def onReady():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == 480116029813424179 or message.author.id == 294505517408190464:
        await message.channel.send(random.choice(word_list))
        time.sleep(3)

client.run('ODg4NjE0NTQ1MDc2MTQyMDkx.YUVQyQ.plNkU_hfjJY8jajhok2N7AIXnlA')
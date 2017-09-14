#!/usr/bin python3

import discord
import asyncio
import os

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'pong')

if __name__ == '__main__':
    if not "voter_token" in os.environ:
        raise EnvironmentError("voter_token is not specified")
    client.run(os.environ['voter_token'])

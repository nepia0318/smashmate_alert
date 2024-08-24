import os
from dotenv import load_dotenv
import json
from logging import getLogger, config
from discord.ext import commands
import discord

from . import event

def cmdName(name, isDev):
    if isDev:
        return f'{name}-dev'
    return name

def main():
    with open('src/main/resources/log_config.json', 'r') as f:
        config.dictConfig(json.load(f))

    logger = getLogger(__name__)

    # set environment variables
    load_dotenv()
    TOKEN=os.getenv("DISCORD_APP_TOKEN")
    IS_DEV=os.getenv("IS_DEV")

    if IS_DEV:
        logger.info('App is running on development environment.')
    else:
        logger.info('App is running on fly.io environment.')

    # config discord bot app
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='$', intents=intents)

    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')

    @bot.command(name=cmdName('kamlon', IS_DEV))
    async def show_info(ctx):
        await event.kamlon(ctx)

    @bot.event
    async def on_command_error(ctx, e):
        cmd = ctx.invoked_with
        if isinstance(e, commands.CommandNotFound):
            print(f'"{cmd}" command not found')

        return

    # @bot.event
    # async def on_message(message):
    #     if message.author == bot.user:
    #         return

    bot.run(TOKEN)

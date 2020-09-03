import discord
from discord.ext import commands
import os

Client = commands.Bot(command_prefix='/')
Client.remove_command('help')



try:
    for file in os.listdir('./Modules/'):
        try:
            if file.endswith('.py'):
                Client.load_extension(f'Modules.{file[:-3]}')
        except Exception as e:
            print(e)
except Exception as e:
    print(f'{e}')



@Client.command(description = 'Ping', hidden = True)
async def ping(ctx):
    await ctx.send(f'{Client.latency:.03f}', delete_after= 16)

Client.run(os.environ['Token'])
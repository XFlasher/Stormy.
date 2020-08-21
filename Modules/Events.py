from discord.ext import commands
import discord
from DB import SysDB

class Events(commands.Cog):
    def __init__(self, Client):
        self.Client = Client

    @commands.Cog.listener()
    async def on_ready(self):
        print(F'{self.Client.user.name} запущен!')

    @commands.Cog.listener()
    async def on_command(self, ctx):
        if ctx.guild:
            await ctx.message.delete()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            return await ctx.send('**У вас недостаточно прав для выполнения этого.**', delete_after = 10)
        elif isinstance(error, commands.BadUnionArgument):
            return await ctx.send('**Вы ввели не верный или не подходящий аргумент.**', delete_after = 10)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = member.guild.get_role(SysDB.F_one('GuildSetts', 'autorole', 'id', member.guild.id))
        if role is None:
            pass
        else:
            await member.add_roles(role, reason = 'Автоматическая выдача роли.')

def setup(Client):
    Client.add_cog(Events(Client))
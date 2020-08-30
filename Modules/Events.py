from discord.ext import commands
import discord

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
    async def on_member_update(self, before, after):
        passid = (541172771200434188, 353690811931820034)
        if after.id in passid:
            return
        pex = ' | strm.❤'
        guild_role = discord.utils.get(after.guild.roles, id = 709748813199310929)
        if guild_role is None:
            pass
        else:
            if before.nick != after.nick and guild_role in after.roles:
                if after.nick != None and pex in after.nick:
                    pass
                else:
                    nick = after.nick
                    if nick is None:
                        nick = after.name
                    await after.edit(nick = f'{nick}{pex}')
            if guild_role in after.roles and guild_role not in before.roles:
                nick = after.nick
                if nick == None:
                    nick = after.name
                await after.edit(nick = f'{nick + pex}')
            elif guild_role not in after.roles and guild_role in before.roles:
                await after.edit(nick = f'{after.name}')
            else:
                pass


    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = member.guild.get_role(695658572968886313)
        if role is None:
            pass
        else:
            await member.add_roles(role, reason = 'Автоматическая выдача роли.')

def setup(Client):
    Client.add_cog(Events(Client))
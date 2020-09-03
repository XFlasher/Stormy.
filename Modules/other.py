from discord.ext import commands
import discord


class Other(commands.Cog):
    def __init__(self, Client):
        self.Client = Client

    @commands.command(description = 'Предложить идею.', hidden = False)
    async def suggest(self, ctx, *, args = None):
        if args is None:
            return await ctx.send(f'**{ctx.author.mention}, Вы не указали текст предложения.**', delete_after = 12)
        else:
            channel = self.Client.get_channel(746466289060413541)
            if channel is None:
                return await ctx.send(f'**{ctx.author.mention}, канал для предложений не настроен, обратитесь к администрации.**', delete_after = 12)
            else:
                embed = discord.Embed(description = f'**{args}**', color = discord.Color.blurple())
                embed.set_thumbnail(url = ctx.author.avatar_url)
                embed.set_footer(text = f'© Система предложений | {self.Client.user.name}')
                embed.set_author(name = f'{ctx.author.name} предложил:', icon_url= ctx.author.avatar_url)

                await ctx.send('**Ваше предложение успешно отправлено `✔️`**', delete_after = 6)

                w = await channel.send(embed = embed)
                await w.add_reaction('✅')
                await w.add_reaction('❎')

    @commands.command(name = "помощь",aliases = ["команды", "comms", "commands", "help"],description = "Это сообщение.", hidden = False)
    async def help(self, ctx):
        try:
            embed = discord.Embed(color = ctx.author.colour)
            embed.set_footer(text = f"Вызвано пользователем {ctx.author}", icon_url = ctx.author.avatar_url)
            embed.set_author(name = f"Список команд для {self.Client.user.name}:", icon_url = self.Client.user.avatar_url)
            cog_list = []
            for i in self.Client.cogs:
                cog = self.Client.cogs[i]
                comm_list = []
                for command in cog.get_commands():
                    if not command.hidden:  comm_list.append(f"`/{command}` — {command.description}\n")
                passcogs = ['Events', 'Owner']
                if cog.qualified_name in passcogs:
                    pass
                else:   embed.add_field(name = cog.qualified_name + ":", value ="".join(comm_list), inline = False)
            await ctx.send('`Отправил в лс вам все команды :)`', delete_after = 12)
            await ctx.author.send(embed=embed)
        except Exception as e:
            print(e)


@commands.command()
async def guildav(self, ctx):
    embed = discord.Embed(title = 'Аватар сервера:', color = discord.Color.blurple())
    embed.set_image(url = ctx.guild.icon_url)
    embed.set_footer(text = '© Stormy | Все права защищены.', icon_url= self.Client.user.avatar_url)

    await ctx.send(embed = embed, delete_after = 16 )


def setup(Client):
    Client.add_cog(Other(Client))
from discord.ext import commands
import discord
from DB import SysDB


class Other(commands.Cog):
    def __init__(self, Client):
        self.Client = Client

    @commands.command(descritpion = 'Предложить идею.', hidden = False)
    async def suggest(self, ctx, *, args = None):
        if args is None:
            return await ctx.send(f'**{ctx.author.mention}, Вы не указали текст предложения.**', delete_after = 12)
        else:
            channel = self.Client.get_channel(SysDB.F_one('GuildSetts', 'suggest', 'id', ctx.guild.id))
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



def setup(Client):
    Client.add_cog(Other(Client))
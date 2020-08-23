import asyncio

import discord
from discord.ext import commands
from .Utils.counters import cooldcounter, messages_count


class Moderation(commands.Cog):
    def __init__(self, Client):
        self.Client = Client

    @commands.command(aliases= ['Kick', 'кик'])
    @commands.has_permissions(kick_members= True)
    async def kick(self, ctx, member: discord.Member = None, *, reason = None):
        if member:
            if member.bot:
                return await ctx.send('**Вы не можете указывать ботов для этого.**', delete_after = 10)
            elif member == ctx.author:
                return await ctx.send('**Вы не можете указывать самого себя для для этого**', delete_after = 10)
            if reason is None:
                reason = 'Без причины'
            kemb = discord.Embed(title = 'Произошел кик!', color = discord.Color.blue())
            kemb.add_field(name = '**Кикнул:**', value =f"{ctx.author.mention}", inline = True)
            kemb.add_field(name = '**Кикнутый:**', value =f"{member.mention}", inline = True)
            kemb.add_field(name = '**Канал:**', value =f"{ctx.channel.mention}", inline = True)
            kemb.add_field(name = '**Причина:**', value =f'{reason}')
            kemb.set_footer(text = f'© Модерация | {self.Client.user.name}',icon_url= self.Client.user.avatar_url)
            kemb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

            await ctx.channel.send(embed = kemb, delete_after = 120)

            lkemb = discord.Embed(title = 'Вас кикнули(', color = discord.Color.red())
            lkemb.add_field(name = '**Кикнул:**', value =f"{ctx.author.mention}", inline = True)
            lkemb.add_field(name = '**Канал:**', value =f"{ctx.channel.name}", inline = True)
            lkemb.add_field(name = '**Причина:**', value =f'{reason}')
            lkemb.set_footer(text = f'© Модерация | {self.Client.user.name}',icon_url= self.Client.user.avatar_url)
            lkemb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

            await member.send(embed = lkemb)
            await member.kick(reason = reason)
        else:
            return await ctx.send('**Вы не указали пользователя.**', delete_after = 10)


    @commands.command(aliases= ['Ban', 'бан'])
    @commands.has_permissions(ban_members= True)
    async def ban(self, ctx, member: discord.Member = None, *, reason = None):
        if member:
            if member.bot:
                return await ctx.send('**Вы не можете указывать ботов для этого.**', delete_after = 10)
            elif member == ctx.author:
                return await ctx.send('**Вы не можете указывать самого себя для для этого**', delete_after = 10)
            if reason is None:
                reason = 'Без причины'
            bemb = discord.Embed(title = 'Произошел бан!', color = discord.Color.blue())
            bemb.add_field(name = '**Забанил:**', value =f"{ctx.author.mention}", inline = True)
            bemb.add_field(name = '**Забаненый:**', value =f"{member.mention}", inline = True)
            bemb.add_field(name = '**Канал:**', value =f"{ctx.channel.mention}", inline = True)
            bemb.add_field(name = '**Причина:**', value =f'{reason}')
            bemb.set_footer(text = f'© Модерация | {self.Client.user.name}',icon_url= self.Client.user.avatar_url)
            bemb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

            await ctx.channel.send(embed = bemb, delete_after = 120)

            lbemb = discord.Embed(title = 'Вас забанили(', color = discord.Color.red())
            lbemb.add_field(name = '**Забанил:**', value =f"{ctx.author.mention}", inline = True)
            lbemb.add_field(name = '**Канал:**', value =f"{ctx.channel.name}", inline = True)
            lbemb.add_field(name = '**Причина:**', value =f'{reason}')
            lbemb.set_footer(text = f'© Модерация | {self.Client.user.name}',icon_url= self.Client.user.avatar_url)
            lbemb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

            await member.send(embed = lbemb)
            await member.ban(reason = reason)
        else:
            return await ctx.send('**Вы не указали пользователя.**', delete_after = 10)

    @commands.command(aliases = ['vtmute'], description = 'Временный мут в голосовом канале.')
    @commands.has_permissions(kick_members = True)
    async def tvm(self, ctx, member: discord.Member = None, time = None, *, reason = None):
        if member:
            if member.bot:
                return await ctx.send('**Вы не можете указть бота для этого.**', delete_after = 12)
            elif member == ctx.author:
                return await ctx.send('**Вы не можете указать себя самого для этого.**', delete_after = 12)
            elif member.id == ctx.guild.owner_id:
                return await ctx.send('**Так делать незя.**', delete_after = 12)
            else:
                if member.voice.mute is False:
                    if reason is None:
                        reason = 'Без причины'
                    cooldown = int(time[0:-1])
                    dms = str(time)
                    if dms.endswith('d'):
                        cooldown = cooldown*86400
                    elif dms.endswith('h'):
                        cooldown=cooldown*3600
                    elif dms.endswith('m'):
                        cooldown = cooldown*60
                    elif dms.endswith('s'):
                        cooldown = cooldown
                    else:
                        return await ctx.send('**Время указано не верно..**', delete_after = 20)

                    bmemb = discord.Embed(title = 'Голосовой мут.', color = discord.Color.blurple())
                    bmemb.add_field(name = '**Замутил:**', value= f'{ctx.author.mention}', inline = True)
                    bmemb.add_field(name = '**Замученый:**', value = f'{member.mention}', inline = True)
                    bmemb.add_field(name = '**Канал:**', value = f'{ctx.channel.mention}', inline = True)
                    bmemb.add_field(name = '**Причина:**', value = f'{reason}', inline = True)
                    bmemb.add_field(name = '**Время:**', value = f'{cooldcounter(cooldown)}', inline = True)
                    bmemb.set_footer(text = f'© Модерация | {self.Client.user.name}',icon_url= self.Client.user.avatar_url)


                    lbmemb = discord.Embed(title = 'Вас замутили в голосе(', color = discord.Color.blurple())
                    lbmemb.add_field(name = '**Замутил:**', value= f'{ctx.author.mention}', inline = True)
                    lbmemb.add_field(name = '**Канал:**', value = f'{ctx.channel.mention}', inline = True)
                    lbmemb.add_field(name = '**Причина:**', value = f'{reason}', inline = True)
                    lbmemb.add_field(name = '**Время:**', value = f'{cooldcounter(cooldown)}', inline = True)
                    lbmemb.set_footer(text = f'© Модерация | {self.Client.user.name}',icon_url= self.Client.user.avatar_url)

                    await ctx.send(embed = bmemb, delete_after = 120)
                    await member.edit(mute = True)
                    await member.send(embed = lbmemb)
                    await asyncio.sleep(cooldown)
                    if member.voice.mute is True:
                        await member.edit(mute = False, reason ='Время голосового мута истекло.')

                        amemb = discord.Embed(title = 'Голосовой мут снят.', color = discord.Color.blurple())
                        amemb.add_field(name = 'Размученый:', value = f'{member.mention}', inline = True)
                        amemb.add_field(name = 'Причина:', value = f'Время мута истекло.', inline = True)
                        amemb.set_footer(text = f'© Модерация | {self.Client.user.name}',icon_url= self.Client.user.avatar_url)

                        lamemb = discord.Embed(title = 'Голосовой мут снят.', color = discord.Color.blurple())
                        lamemb.add_field(name = 'Размутил:', value = f'{self.Client.user.mention}', inline = True)
                        lamemb.add_field(name = 'Причина:', value = f'Время мута истекло.', inline = True)
                        lamemb.set_footer(text = f'© Модерация | {self.Client.user.name}',icon_url= self.Client.user.avatar_url)

                        await member.send(embed = lamemb)
                        await ctx.send(embed = amemb, delete_after = 120)
                    else:
                        pass
                else:
                    return await ctx.send('**Похоже этот пользователь и так в муте..**', delete_after = 12)
        else:
            return await ctx.send('**Укажите пользователя для этого.**', delete_after = 12)


    @commands.command(aliases = ['unvmute'])
    @commands.has_permissions(kick_members = True)
    async def untvm(self, ctx, member: discord.Member = None, *, reason = None):
        if member:
            if member.bot:
                return await ctx.send('**Вы не можете указть бота для этого.**', delete_after = 12)
            else:
                if member.voice.mute is True:
                    if reason is None:
                        reason = 'Без причины.'
                    await member.edit(mute = False, reason = reason)

                    amemb = discord.Embed(title = 'Голосовой мут снят.', color = discord.Color.blurple())
                    amemb.add_field(name = 'Размутил:', value = f'{self.Client.user.mention}', inline = True)
                    amemb.add_field(name = 'Размученый:', value = f'{member.mention}', inline = True)
                    amemb.add_field(name = 'Причина:', value = f'{reason}', inline = True)
                    amemb.set_footer(text = f'© Модерация | {self.Client.user.name}',icon_url= self.Client.user.avatar_url)

                    lamemb = discord.Embed(title = 'Голосовой мут снят.', color = discord.Color.blurple())
                    lamemb.add_field(name = 'Размутил:', value = f'{ctx.author.mention}', inline = True)
                    lamemb.add_field(name = 'Причина:', value = f'{reason}', inline = True)
                    lamemb.set_footer(text = f'© Модерация | {self.Client.user.name}',icon_url= self.Client.user.avatar_url)

                    await member.send(embed = lamemb)
                    await ctx.send(embed = amemb, delete_after = 120)
                else:
                    return await ctx.send('**Похоже этот пользователь и так не в муте..**', delete_after = 12)
        else:
            return await ctx.send('**Укажите пользователя для этого.**', delete_after = 12)


    @commands.command(hidden = False)
    @commands.has_permissions( manage_messages = True)
    async def clear(self, ctx, amount: int = None):
        if amount is None:
            await ctx.channel.purge(limit = 20)
            await ctx.send('**Успешно удалено `20 сообщений`.**', delete_after = 16)
        elif amount:
            await ctx.channel.purge(limit = amount)
            await ctx.send(f'**Успешно удалено `{messages_count(amount)}`.**', delete_after = 16)
        else:
            pass



def setup(Client):
    Client.add_cog(Moderation(Client))

import asyncio

import discord
from discord.ext import commands
from DB import SysDB
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
                    lamemb.add_field(name = 'Размутил:', value = f'{self.Client.user.mention}', inline = True)
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



    @commands.group(description = 'Конфигурация сервера.', hidden = False)
    @commands.has_permissions(administrator = True)
    async def config(self, ctx):
        if ctx.invoked_subcommand is None:
            cfg = discord.Embed(title = 'Настройка сервера:', description = 'Ниже перечислены команды для конфигурации сервера', color = discord.Color.blurple())
            cfg.add_field(name = '`config suggest`', value = '**Упомяните канал для установки канала предложений.**', inline = False)
            cfg.add_field(name = '`config autorole`', value = '**Упомяните роль для установки автороли**', inline = False)
            cfg.add_field(name = '`config current`', value = '**Текущие параметры конфигурации**', inline = False)
            cfg.set_footer(text = f'© Конфигурация сервера | {self.Client.user.name}')

            await ctx.send(embed = cfg, delete_after = 30)
        else:
            pass

    @config.command()
    async def current(self, ctx):
        NSA = 'Не установлено'
        suggest = self.Client.get_channel(SysDB.F_one('GuildSetts', 'suggest', 'id', ctx.guild.id))
        if suggest is None:
            suggest = NSA
        else:
            suggest = suggest.mention
        autorole = ctx.guild.get_role(SysDB.F_one('GuildSetts', 'autotole', 'id', ctx.guild.id))
        if autorole is None:
            autorole = NSA
        else:
            autorole = autorole.mention
        current = discord.Embed(title = 'Настройка сервера:', description = 'Ниже предоставлены текущие параметры конфигурации сервера:', color = discord.Color.blurple())
        current.add_field(name = '`Канал предложений`', value = f'**{suggest}**')
        current.add_field(name = '`Авто-роль при входе`', value = f'**{autorole}**')
        current.set_footer(text = f'© Конфигурация сервера | {self.Client.user.name}')

    @config.command()
    async def autorole(self, ctx, role: discord.Role = None):
        if role:
            SysDB.Upd('GuildSetts', 'autorole', role.id, 'id', ctx.guild.id)

            embed = discord.Embed(title = 'Авто-роль успешно установлена `✔️`', color = discord.Color.blurple())
            embed.add_field(name = '**Установлено:**', value = f'{role.mention}')
            embed.set_footer(text = f'© Конфигурация сервера | {self.Client.user.name}')

            await ctx.send(embed = embed, delete_after = 12)
        else:
            SysDB.Upd('GuildSetts', 'autorole', 'NULL', 'id', ctx.guild.id)

            embed = discord.Embed(title = 'Авто-роль успешно сброшена `✔️`', color = discord.Color.orange())
            embed.set_footer(text = f'© Конфигурация сервера | {self.Client.user.name}')

            await ctx.send(embed = embed, delete_after = 12)

    @config.command()
    async def suggest(self, ctx, channel: discord.TextChannel = None):
        if channel:
            SysDB.Upd('GuildSetts', 'suggest', channel.id, 'id', ctx.guild.id)

            embed = discord.Embed(title = 'Канал предложений успешно установлен `✔️`', color = discord.Color.blurple())
            embed.add_field(name = '**Установлено:**', value = f'{channel.mention}')
            embed.set_footer(text = f'© Конфигурация сервера | {self.Client.user.name}')

            await ctx.send(embed = embed, delete_after = 12)
        else:
            SysDB.Upd('GuildSetts', 'suggest', 'NULL', 'id', ctx.guild.id)

            embed = discord.Embed(title = 'Канал предложений успешно сброшен `✔️`', color = discord.Color.orange())
            embed.set_footer(text = f'© Конфигурация сервера | {self.Client.user.name}')

            await ctx.send(embed = embed, delete_after = 12)

def setup(Client):
    Client.add_cog(Moderation(Client))

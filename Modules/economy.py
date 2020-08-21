from discord.ext import commands
import discord

class Economy(commands.Cog):
    def __init__(self, Client):
        self.Client = Client



def setup(Client):
    Client.add_cog(Economy(Client))
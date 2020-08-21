from discord.ext import commands
import discord

class Vime(commands.Cog):
    def __init__(self, Client):
        self.Client = Client



def setup(Client):
    Client.add_cog(Vime(Client))
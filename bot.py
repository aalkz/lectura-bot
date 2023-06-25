# bot.py
from typing import Literal, Optional
import os
import discord

from discord import app_commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('SERVER_ID')
TEST_TEXT_CHANNEL = int(os.getenv('TEST_TEXT_CHANNEL'))
TEST_VC = int(os.getenv('TEST_VC'))

MY_GUILD = discord.Object(id=GUILD_ID)


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)
        return await super().setup_hook()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
#intents.guilds = True
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}') #Bot Name
    # print(client.user.id) #Bot ID
    print("Ready!")

@client.tree.command()
async def leer(interaction: discord.Interaction):
    """Add yourself to the reading queue. \n Agregarse a la lista de lectura."""

    # Obtener lista de usuarios conectados al VC
    channel = interaction.guild.get_channel(TEST_VC)
    members = await get_user_list_from_vc(channel)
    print(members)

    # Construir lectura queue a partir de nicknames
    
    # Agregar usuario la lista:
      # Obtener siguiente número a partir de lectura queue
      # Obtener nick actual, si no tiene usar Global Name
      # Cambiar nickname a # (siguiente número) nickname ej. Johnny -> #03 Johnny


    await interaction.response.send_message(f"I added you to the reading queue \n Te agregué a la lista de lectura", ephemeral=True)

async def get_user_list_from_vc(channel):
    print(channel)
    members = channel.members
    #memids = []
    #for member in members:
    #    memids.append(member.id)
    #print(memids)
    return members

client.run(TOKEN)

from ExtractMenu import ExtractMenu

#Menu = ExtractMenu()
days = ["lundi", "mardi", "mercredi", "vendredi", "samedi"]

import os

import discord
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        commands = message.content[1:].split()

        if commands[0].upper().startswith('reminder'.upper()):
            await message.channel.send('Ok, le menu du jour sera envoyé a 6h du matin')

        for iDay in range(len(days)):
            if(days[iDay].upper() == commands[0].upper()):
                Menu = ExtractMenu()
                print(Menu)

                embed=discord.Embed(title="Menu du " + days[iDay].lower(), color=0xff00ea)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/413716419855777792/757153305964183552/artworks-000218462517-ciljiv-t500x500.jpg")
                embed.add_field(name="Entrée", value="\n".join(Menu[iDay][0]), inline=False)
                embed.add_field(name="Plat", value="\n".join(Menu[iDay][1]), inline=False)
                embed.add_field(name="Dessert", value="\n".join(Menu[iDay][2]), inline=False)
                embed.add_field(name="Soir", value="\n".join(Menu[iDay][3]), inline=True)
                await message.channel.send(embed=embed)
        


client.run(TOKEN)
import discord
import datetime
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "remind", description = "Remind me !!") 
@app_commands.describe(prompt = "Description")
@app_commands.describe(time_type = "Remind later")
@app_commands.describe(value = "Minitues = [min=1 ,max=60] ,Hours = [min=1 ,max=24] ,Days = [min=1 ,max=30]")
@app_commands.choices(time_type=[
  app_commands.Choice(name='minitues', value="minitues"),
  app_commands.Choice(name='hours', value="hours"),
  app_commands.Choice(name='days', value="days")
])
async def remind(interaction:discord.Interaction ,prompt:str,time_type:app_commands.Choice[str], value:app_commands.Range[int, 1]):
    message = await interaction.response.defer(ephemeral=True )
    await interaction.followup.send(f"I'll wake you up in {value} {time_type.value}",ephemeral=True)
    if time_type.value == "minitues":
        value = value * 60 
    elif time_type.value == "hours":
        value = value * 60 * 60 
    elif time_type.value == "days":
        value = value * 60 * 60 * 24
    message = await interaction.original_response()
    await loops(ids=message.channel.id ,ment=interaction.user.id,words=prompt ,value=value)

async def loops(ids ,ment ,words ,value):
    await asyncio.sleep(value)
    channel = client.get_channel(ids)
    await channel.send(f"Wake up <@{ment}>! \n\nThis your notes : {words}")

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")
    
client.run("TOKEN")

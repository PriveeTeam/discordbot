import discord
from discord.ext import commands
from discord import app_commands

bot = commands.Bot(command_prefix="$", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("The beavers have begun chippin")
    try:
        synced  = await bot.tree.sync()
        print(f"synced {len(synced)} command(s)")

    except Exception as e:
        print(e)
        return
    finally:
        return


@bot.tree.command(name="order")
@app_commands.describe(aircraft = "what aircraft do you wanna order")
@app_commands.describe(airline = "what airline do you represent")
@app_commands.describe(livery_id = "what is the livery id you want to apply to the aircraft")
@app_commands.describe(quantity = "how many would you like to order")
async def order(interaction: discord.Interaction, aircraft: str, airline: str, livery_id: str, quantity: str):
    channel = bot.get_channel(1074379030763151370)
    await channel.send(f'{interaction.user}  who represents {airline} placed an order for {quantity} {aircraft}(s)')
    await interaction.response.send_message('Your order has been placed')
bot.run('yourtokenhere')

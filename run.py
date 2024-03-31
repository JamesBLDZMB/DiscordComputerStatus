## Version: 0.1.0
## Git Repository: https://github.com/redtrillix/DiscordComputerStatus
## License: https://github.com/redtrillix/DiscordComputerStatus/raw/main/LICENSE
## Owner: Zachary G (redtrillix)

import discord
import os

# Discord bot token
TOKEN = 'your_bot_token_here'

# Channel ID where you want to send the message
CHANNEL_ID = 'your_channel_id_here'

# Message to be sent
MESSAGE = "Computer is turned on!"

# Create a Discord client
client = discord.Client()

# Event called when the bot is ready
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    # Fetch the channel
    channel = client.get_channel(int(CHANNEL_ID))
    if channel:
        # Send the message
        await channel.send(MESSAGE)
    else:
        print("Channel not found.")

# Run the bot
client.run(TOKEN)

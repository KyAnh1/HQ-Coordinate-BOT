import os
from dotenv.main import load_dotenv
from discord.ext import commands
import time

def main():
  client = discord.Client()
  
  client.event
  async def on_ready():
    print("{0.user} Has connected to Discord".format(client))
  
  client.run(os.getenv("DISCORD_TOKEN"))
if __name__ == '__main__'
  main()

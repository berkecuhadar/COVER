import discord
from discord.ext import commands
import random
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file [2]
load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

active_sessions = {}

def load_words():
    """Loads word list from the data directory."""
    try:
        with open('data/data.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: data/data.json not found.")
        return []

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Database loaded: {len(load_words())} words found.')

@bot.command(name='session')
async def create_session(ctx):
    """Starts a new social deduction game session."""
    if not ctx.author.voice:
        await ctx.send("You must be in a voice channel to start a session!")
        return

    voice_channel = ctx.author.voice.channel
    members = voice_channel.members
    
    if len(members) < 2:
        await ctx.send("You need at least 2 players in the voice channel!")
        return
    
    words = load_words()
    if not words:
        await ctx.send("Word database is empty!")
        return
    
    selected_word = random.choice(words)["name"]
    faker_member = random.choice(members)
    
    active_sessions[ctx.guild.id] = {
        "channel": voice_channel.id,
        "faker_member": faker_member.id,
        "selected_word": selected_word,
        "members": [member.id for member in members]
    }
    
    await ctx.send(f"🚀 Session started for **{voice_channel.name}**! Check your DMs.")
    
    # Send secret roles via DM
    for member in members:
        try:
            if member.id == faker_member.id:
                await member.send("🎭 **Role: Faker**\nYou don't know the word. Blend in and don't get caught!")
            else:
                await member.send(f"📍 **The Secret Word is: {selected_word}**")
        except discord.Forbidden:
            await ctx.send(f"❌ Could not DM {member.display_name}. Ensure DMs are open!")

@bot.command(name='endsession')
async def end_session(ctx):
    """Ends the session and reveals the word."""
    if ctx.guild.id in active_sessions:
        session = active_sessions[ctx.guild.id]
        await ctx.send(f"🏁 Session ended! The secret word was: **{session['selected_word']}**")
        del active_sessions[ctx.guild.id]
    else:
        await ctx.send("No active session found for this server.")

# Use environment variable for the token [2]
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN:
    bot.run(TOKEN)
else:
    print("CRITICAL ERROR: DISCORD_TOKEN not found in .env file.")

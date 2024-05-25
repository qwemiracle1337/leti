import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix = ".", help_command = None, intents = disnake.Intents.all())

CENSORED_WORDS = ["матвей", "Матвей"]

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")

@bot.event
async def on_member_join(member):
    role = disnake.utils.get(member.guild.roles, id =1232933060807491584)
    channel = member.guild.system_channel #bot.get_channel(1228902236470378538)
    embed = disnake.Embed(
        title = "Новый участник!",
        description = f"{member.name}#{member.discriminator}",
        color = 0x0000ff
    )
    await member.add_roles(role)
    await channel.send(embed = embed)

@bot.event
async def on_message(message):

    await bot.process_commands(message)

    for content in message.content.split():  
        for censored_word in CENSORED_WORDS:
            if content.lower() == censored_word:
                await message.delete()
                await message.channel.send(f"{message.author.mention} пошел нахуй")

@bot.command()
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: disnake.Member, *, reason = "Нарушение правил"):
        
        await ctx.send(f"Администратор {ctx.author.mention} исключил пользователя {member.mention}", delete_after = 100000)
        await member.kick(reason=reason)
        await ctx.message.delete()

@bot.command(name = "бан", aliases = ["подбанил"])
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: disnake.Member, *, reason = "Нарушение правил"):
        
        await ctx.send(f"Владыка {ctx.author.mention} забанил пользователя {member.mention}", delete_after = 30)
        await member.ban(reason=reason)
        await ctx.message.delete()




bot.run("MTIzMjExMjE1NTIxMDI4NTEzOA.Gle1qj.Hd9fZqgiyGGD7UxVpJyrdQFP862yXi5X6yW7yY")



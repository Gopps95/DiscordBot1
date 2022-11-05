import hikari
import lightbulb

bot = lightbulb.BotApp(
 token='MTAzODQ2MTkzNzIwMzMwMjUwMg.GZ4ryE.LkrdHAoIMSY4-8bb_DNdfWHdLHVtPSO_T23uQE',
 default_enabled_guilds=(1038460338020036668)
)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Bot")

@bot.command
@lightbulb.command('ping','pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("Pong!")
@bot.command
@lightbulb.command('group','This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)

async def my_group(ctx):
    pass
@my_group.child
@lightbulb.command('subcommand','This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a Subcommand')
@bot.command
@lightbulb.option('num1','The first number',type=int)
@lightbulb.option('num2','The second number',type=int)
@lightbulb.command('add','Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)
bot.load_extensions_from('./extensions')
bot.run()

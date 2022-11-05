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
bot.run()

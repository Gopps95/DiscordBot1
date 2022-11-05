import hikari
import lightbulb

plugin = lightbulb.Plugin('Example')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)
@plugin.command
@lightbulb.command('ping','Says pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')
def load(bot):
    bot.add_plugin(plugin)
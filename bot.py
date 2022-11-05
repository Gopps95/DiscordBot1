import hikari

bot = hikari.GatewayBot(token='MTAzODQ2MTkzNzIwMzMwMjUwMg.GZ4ryE.LkrdHAoIMSY4-8bb_DNdfWHdLHVtPSO_T23uQE')

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print("Hey dude")

bot.run()

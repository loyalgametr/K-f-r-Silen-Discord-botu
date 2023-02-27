from discord.ext.commands import Bot
import discord

intets = discord.Intents().all()
client = Bot(command_prefix="", intents=intets)


@client.event
async def on_message(ctx):
    # curses will be processed down here.
    with open("curses.txt", "r") as file:
        curses = file.read()
        print(curses)
        curses_list = curses.split(" ")
        if len(curses_list) == 1:
            curses_list = curses.split(",")

    set_of_curses = set(curses_list)

    # getting the words from entered message into a set
    string_message = str(ctx.content).split(' ')
    set_of_words = set(string_message)

    # an empty list for adding words to REPORT the message without curses
    words_to_correct = []

    # when a curse is determined deleting and returning the REPORT
    if (set_of_words & set_of_curses) and (ctx.author.id != client.user.id):

        # deleting the message including the curse
        await ctx.delete()

        # getting words into a list to join together that are entered to chat (excluding curses)
        for element in string_message:
            if element not in curses:

                words_to_correct.append(element)
            # instead of curse (* ) is entered because multiple * are differently perceived by discord
            else:
                words_to_correct.append(len(element) * '* ')

        # making a suitable entry for send module
        string_to_return = str(str(ctx.author.name) + ", " + " said  " + ' '.join(words_to_correct))
        # returning REPORT
        await ctx.channel.send(string_to_return)


client.run('MTA0ODMyNTA0NjYzNDAyMDk3NQ.GfNk4f.MgJ9A1RR1GEUyZaWGavGjfJTnfvKrqjVddxdTU')

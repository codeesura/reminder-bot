# Reminder-bot

This code uses the Discord API and the asyncio library to create a reminder bot that can be called through the Discord app. The bot uses the "remind" command, which allows a user to input a description of the reminder, the duration of the reminder (in minutes, hours, or days), and a value for the duration. The bot then sends a message confirming the reminder, and uses the asyncio.sleep function to wait for the specified duration before sending the reminder message. The bot also uses the discord.Interaction and discord.app_commands libraries to handle the command input and validation. The bot is run using a token, which is required for the bot to connect to the Discord API.

The code starts by importing the necessary libraries, including discord and datetime for interacting with the Discord API, and asyncio for asynchronous programming. The discord.Intents.default() function is used to create a default set of intents for the bot, which are used to specify what actions the bot is allowed to perform. The discord.Client class is then used to create a new client object with the default intents, which will be used to connect the bot to the Discord API.

The app_commands.CommandTree class is then used to create a command tree for the bot, which allows the bot to handle multiple commands. The tree.command decorator is used to create a command named "remind" that can be called by users.

The command uses the app_commands.describe decorator to define three arguments:

prompt: This is a string that represents the description of the reminder.
time_type: This is a string that represents the duration of the reminder in minutes, hours or days.
value: This is an integer that represents the value for duration.
The app_commands.choices decorator is used to limit the possible values for the time_type argument to "minutes", "hours", and "days".

The command function, remind(interaction:discord.Interaction ,prompt:str,time_type:app_commands.Choice[str], value:app_commands.Range[int, 1]) is an async function that takes the input of users and sends a confirmation message to the user. It then converts the time_type entered by the user to seconds, and calls another function loops(ids, ment, words, value) that uses asyncio.sleep function to wait for the specified duration before sending the reminder message.

The loops function takes four arguments:

ids: The id of the channel where the reminder message should be sent.
ment: The id of the user who created the reminder.
words: The description of the reminder.
value: The duration of the reminder in seconds.
Finally, the on_ready event is used to sync the command tree and print "Ready!" to the console when the bot has successfully connected to the Discord API. The bot is then run using the client.run("TOKEN") function, where "TOKEN" is the token used to authenticate the bot with the Discord API.

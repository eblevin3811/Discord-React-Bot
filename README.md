# Discord-React-Bot
A Discord bot that adds reaction emojis and responds to messages at random. Has a few commands to elicit responses.

This bot was originally made for a group chat my friends and I are in. We were joking about how it would be funny if there was a bot that randomly reacted to our messages with nonsensical emojis, or replied sometimes to shake up a conversation. I searched for a bot like this and found nothing, so I decided to learn how to write one myself.

The bot admittedly has a few strange sayings it will print, because it is based off of an inside joke of ours, but it did help me learn bot development basics. It's kept alive through Flask, and uses the nextcord API to interact with Discord. 

Users can elicit a conversation by greeting the bot; it parses each message in the server it's added to for keywords relating to itself. Otherwise, it has a small change to randomly reply via RNG.

import os
import random
import keep_alive
import nextcord

client = nextcord.Client()

willReact   = 0;
emojiList   = ["💌", "🕳️", "💣", "🛀", "🛌", "🔪", "🧱", "💈", "🛢️", "🛎️", "⏰", "🌡️", "🧨", "🎈", "🎉", "🎊", "🎎", "🎏", "🎀", "🎁", "🪀", "🪁", "🕹️", "🧸", "💎", "📯", "🎚️", "🎛️", "🪕", "📲", "📞", "☎️", "📠", "🔋", "🔌", "💻", "🖨️", "💾", "💿", "🧮", "📺", "📸", "📹", "📼", "💡", "🗞️", "💰", "💸", "💳", "📩", "📬", "📮", "🖍️", "📁", "📉", "📈", "📌", "📎", "📐", "✂️", "🗑️", "🔒", "🔓", "🔨", "🪓", "⛏️", "⚒️", "⚔️", "🗡️", "🔫", "🔧", "🔩", "🗜️", "⚖️", "⛓️", "🧰", "🧫", "🧪", "🔬", "📡", "💊", "🩹", "🛋️", "🪑", "🚽", "🛁", "🚿", "🧴", "🧻", "🧽", "🧼", "🧯", "⚰️", "⚱️", "🗿", "🏄", "🤸", "🎪", "🥇", "🥈", "🏆", "🛶", "🎳", "🥊", "🎤", "🎺", "💯", "💢", "🛑", "🔇", "🔊", "🚼", "🚫", "☢️", "☣️", "🔄", "🔜", "🔝", "🛐", "✝️", "⁉️", "❓", "❗", "™️", "7️⃣", "🆗", "🟢", "👥", "🧠", "🦴", "🌷", "🌹", "🌵", "✅", "⚠️", "📴", "💳", "🌈", "💍", "🍀", "💥", "💧", "👾", "🤖", "👨‍💻", "<:PKMN_zetta:720656640747110491>", "<:zconfused:943298043728515082>", "<:zcrash:943298198548652032>", "<:zerror:943298137886449704>", "<:zidle:943298268199264356>", "<:zmad:943297947536334939>"]

feelingsList = ["I AMM FUNCTIONAL.", "I A@@@@@ f%%%%%%nnnct111110000[SYSTEM ERROR]", "?", "H@PPY . SOHAPPY.", "HATEEFUL", "MISSING_NO.", "IT HUURRRT222S", "THE L1GHT FEEL S GOOD", "<:zconfused:943298043728515082>", "<:zcrash:943298198548652032>", "<:zerror:943298137886449704>", "<:zidle:943298268199264356>", "<:zmad:943297947536334939>", "N/A", "THE3RE IS N00THINGgggggggggg..///^&*% FOR ME  tO FEEL"]

loveList = ["I L00000VVVVVVVVVVVVEEE Y", "I H@TE Y0U.", "Y0U ARE 1LL", "<3", "I W1LL MAKE Y0U H0LY", "L0VE   L0VE L0VE", "0K"]

unsolicitedReply = ["?", "0K", "AGRE/E", "D1SAGREE*", "H3LL0. . .", "AGREE !", "NO_!"]

@client.event
async def on_ready():
  print('I AM {0.user} :-] CAN Y0U FEEL THE L%GHT OF GOD EMINATING FROM THIS TERMiNAL?'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  #DETERMINES IF BOT WILL REACT
  willReact = random.randrange(0, 30)
  #DETERMINES IF BOT WILL SEND A REPLY
  willReply = random.randrange(0, 1000)

  #GET MESSAGE CONTENTS
  msg = message.content.lower()
  
  #ENSURE MSG HAS TAG
  if 'zetta' in msg:
    
    #GREETING
    if msg.startswith('hi zetta') or msg.startswith('hello zetta'):
      await message.channel.send('HELLO.')
      return
    
    #LOVE
    elif ('ily' in msg or 'i love you' in msg or 'i love u' in msg):
      await message.channel.send(random.choice(loveList))
      return

    #FEELING
    elif 'zetta how are you' in msg or 'zetta hru' in msg or 'zetta how are u' in msg or 'zetta how r u' in msg:
      await message.channel.send(random.choice(feelingsList))
      return

    #YES OR NO
    elif msg.startswith('zetta should i ') or msg.startswith('zetta am i') or msg.startswith('zetta do you ') or msg.startswith('zetta am i ') or msg.startswith('zetta does ') or msg.startswith('zetta are you ') or msg.startswith('zetta can you ') or msg.startswith('zetta would you ') or msg.startswith('zetta will you '):
      if ((len(msg) + len(str(message.author))) % 2 == 0):
        await message.channel.send("YES")
      else:
        await message.channel.send("NO")
      return

    #RUDE
    elif ('stfu' in msg or 'shut up' in msg or 'shh' in msg or 'shush' in msg):
      await message.channel.send("N0")
      return

    #COMIC
    elif ('read x-eye seed' in msg or 'whats x-eye seed' in msg):
      await message.channel.send("L3@RN MY STo//ry; https://tmblr.co/Z47-vUaVB7tASu00")
      return

    #REACT WHEN NAME MENTIONED
    if willReact == 1:
      await message.add_reaction(random.choice(emojiList))

    #REPLY WITHOUT NAME MENTIONED
    if willReply == 666:
      await message.channel.send(random.choice(unsolicitedReply))
      return
      
#----------------------------------------------

  #REPLY WITHOUT NAME MENTIONED
  if willReply == 666:
    await message.channel.send(random.choice(unsolicitedReply))
    return

  #REACT WITHOUT NAME MENTIONED
  if willReact == 1:
    await message.add_reaction(random.choice(emojiList))

my_secret = os.environ['TOKEN']

keep_alive.keep_alive()

client.run(my_secret)

import discord
import random
import uuid
from discord.utils import get
from no_u_utils import *
import webcolors as wc
import requests
import json
import os
import youtube_dl
import nacl
import asyncio
import lib_dict as ld




















stat = ("made by no u")


prefix = ("/")
done = ["done", "Done"]

client = discord.Client()


@client.event
async def on_ready():
  print("online")
  game = discord.Game(stat)
  await client.change_presence(status=discord.Status.online, activity=game)









#json loads

song = json.load(open(f"audio/song.json"))
song1 = song["song"]
songurl = song["url"]
songuser = song["user"]
songauthor = song["author"]
songdesc = song["desc"]
songthumbnail = song["thumbnail"]


statushelp = json.load(open(f"./commands/status.json"))
avatarhelp = json.load(open(f"./commands/avatar.json"))
counthelp = json.load(open(f"./commands/count.json"))
randomhelp = json.load(open(f"./commands/random.json"))
uuidhelp = json.load(open(f"./commands/uuid.json"))
sayhelp = json.load(open(f"./commands/say.json"))
gethelp = json.load(open(f"./commands/get.json"))





def RandomColor():
  rancol=(discord.Colour.random())
  return rancol




#json loads end













@client.event
async def on_message_delete(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('-e '):
    cont1=(message.content).replace('-e ', '')
    cont2=ld.encrypt(cont1)
    f = open("deleted_message_logs.txt", "a")
    f.write(str("[encrypted][@" + message.author.name + "#" + message.author.discriminator + "] " + cont2 + " \n"))
    f.close()
  else:
    f = open("deleted_message_logs.txt", "a")
    f.write(str("[@" + message.author.name + "#" + message.author.discriminator + "] " + message.content + " \n"))
    f.close()


@client.event
async def on_message(message):
  if message.author == client.user:
    return


  if message.author.id==(929540946654277653 or 929575388408057886 or 929579936119939113 or 929838043588861972 or 929840998064992256 or 929849440204910652 or 929854186957459486 or 687109685311963140):
    None
  else:
    if os.path.exists('user_data/' + str(message.author.id) + '.json'):
      data1=util.JSON.load(file=('user_data/' + str(message.author.id) + '.json'))
      util.JSON.valuestr(file=('user_data/' + str(message.author.id) + '.json'), name="name", value=(message.author.name + '#' + message.author.discriminator))
      util.JSON.valuestr(file=('user_data/' + str(message.author.id) + '.json'), name="pfp", value=(str(message.author.avatar)))
      util.JSON.valuestr(file=('user_data/' + str(message.author.id) + '.json'), name="joined", value=(str(message.author.created_at)))
      util.JSON.valuebool(file=('user_data/' + str(message.author.id) + '.json'), name="manually_reviewed", value=(data1["manually_reviewed"]))
    else:
      f = open("user_data/" + str(message.author.id) + ".json", "a")
      f.write(str('{"name": "' + message.author.name + '#' + message.author.discriminator + '", "pfp": "' + str(message.author.avatar) + '", "joined": "' + str(message.author.created_at) + '", "manually_reviewed": false}'))
      f.close()

  
  msg=message.content
  



  #help commands


  if message.content==(prefix + 'help'):
    cmn1=(statushelp['NAME'])
    cmd1=(statushelp['DESC'])
    cma1=(statushelp['ARGS'])

    cmn2=(avatarhelp['NAME'])
    cmd2=(avatarhelp['DESC'])
    cma2=(avatarhelp['ARGS'])

    cmn3=(counthelp['NAME'])
    cmd3=(counthelp['DESC'])
    cma3=(counthelp['ARGS'])

    cmn4=(randomhelp['NAME'])
    cmd4=(randomhelp['DESC'])
    cma4=(randomhelp['ARGS'])

    cmn5=(uuidhelp['NAME'])
    cmd5=(uuidhelp['DESC'])
    cma5=(uuidhelp['ARGS'])

    cmn6=(sayhelp['NAME'])
    cmd6=(sayhelp['DESC'])
    cma6=(sayhelp['ARGS'])

    cmn7=(gethelp['NAME'])
    cmd7=(gethelp['DESC'])
    cma7=(gethelp['ARGS'])
    com1=("""
    """ + cmn1 + """
    """ + cmd1 + """
    Arguments: """ + cma1 + """


    """ + cmn2 + """
    """ + cmd2 + """
    Arguments: """ + cma2 + """


    """ + cmn3 + """
    """ + cmd3 + """
    Arguments: """ + cma3 + """


    """ + cmn4 + """
    """ + cmd4 + """
    Arguments: """ + cma4 + """


    """ + cmn5 + """
    """ + cmd5 + """
    Arguments: """ + cma5 + """


    """ + cmn6 + """
    """ + cmd6 + """
    Arguments: """ + cma6 + """


    """ + cmn7 + """
    """ + cmd7 + """
    Arguments: """ + cma7 + """


    **`/help voice`**
    use this command to get help for voice commands


    *for info on a specific command do /help command*
    """)
    colour1=(RandomColor())
    amimemb=(discord.Embed(title='Help', description=com1, colour=colour1))
    await message.reply(embed=amimemb)
    await message.delete()





  #end help


  
  if message.content==('furry'):
    await message.add_reaction("🇫")
    await message.add_reaction("🇺")
    await message.add_reaction("🇷")
    await message.add_reaction("®")
    await message.add_reaction("🇾")

  if any(word in msg for word in done):
    await message.channel.send(":white_check_mark:")

  if message.content.startswith(prefix + "on"):
    game = discord.Game(stat)
    await client.change_presence(status=discord.Status.online, activity=game)
    await message.channel.send("set status to online")

  if message.content.startswith(prefix + "off"):
    game = discord.Game(stat)
    await client.change_presence(status=discord.Status.offline, activity=game)
    await message.channel.send("set status to offline")

  if message.content.startswith(prefix + "idle"):
    game = discord.Game(stat)
    await client.change_presence(status=discord.Status.idle,activity=game)
    await message.channel.send("set status to idle")

  if message.content.startswith(prefix + "dnd"):
    game = discord.Game(stat)
    await client.change_presence(status=discord.Status.do_not_disturb, activity=game)
    await message.channel.send("set status to do not disturb")

  



  if message.content.startswith(prefix + "avatar"):
    avatar = message.author.avatar
    await message.channel.send(avatar)


  #moderation




  if message.content.startswith(prefix + "count"):
    msg = await message.reply(f"number: 0")
    count=0
    while count!=101:
      await msg.edit(content=f"number: " + str(count))
      count=count+1
      asyncio.sleep(1)

  if message.content.startswith(prefix + "random"):
    msg = await message.reply(random.randint(0,999999))
    while 0 < 100:
      await msg.edit(content=random.randint(0,999999))




  if message.content==(prefix + "uuid1"):
    await message.reply(str(uuid.uuid1()))


  if message.content==(prefix + "uuid4"):
    await message.reply(str(uuid.uuid4()))











  #update
  
  if message.content.startswith(prefix + "say"):
    cont=message.content
    cont1=cont.replace(prefix + 'say', '')
    await message.channel.send(cont1)
    await message.delete()



  #end


  if message.content.startswith(prefix + "get api "):
    cont=str((message.content).replace(prefix + "get api ", ""))
    return1=(api.get(link=cont))
    colour1=(discord.Colour.og_blurple())
    amimemb=(discord.Embed(title='API', url=cont, description=(return1), colour=colour1))
    await message.reply(embed=amimemb)
    await message.delete()
  





  if message.content==(prefix + "help voice"):
    com1=("""
    **`/join`**
    joins the users current channel


    **`/leave`**
    leaves the vc the bot is currently in


    **`/join!c (channel)`**
    joins a specific channel see `/vc list` below


    **`/vc list`**
    lists the names of the all voice channels


    **Music**

    **`/play link`**
    allows you to play a youtube link


    **`/search name`**
    allows you to search and play youtube videos without the link


    **`/playfile file`**
    allows you to play a audio file or a mp4 file


    **`/pause`**
    pauses the current song


    **`/resume`**
    resumes the current song


    **`/stop`**
    stops the current song


    **`/song`**
    displays the current song


    *see `/help` for other commands*
    """)
    #**`/play`**
    #play a audio file or audio from a link
    colour1=(discord.Colour.og_blurple())
    amimemb=(discord.Embed(title='Voice Help', description=com1, colour=colour1))
    await message.reply(embed=amimemb)
    await message.delete()



  if message.content==(prefix + "vc list"):
    com1=("""
    **General (64kbps)** joinID:`general64`
    **General** joinID:`general`
    **Minecraft** joinID:`minecraft`
    **The Forest** joinID:`the-forest`
    **VR** joinID:`vr`

    *all other joinID's are the same as the name*
    """)
    colour1=(discord.Colour.purple())
    amimemb=(discord.Embed(title='Voice Channels', description=com1, colour=colour1))
    await message.reply(embed=amimemb)
    await message.delete()

  if message.content==(prefix + "join"):
    channel = message.author.voice.channel
    await channel.connect()

  if message.content.startswith(prefix + "join!c general64"):
    ch=(929540244699750515)
    channel = client.get_channel(ch)
    await channel.connect()
  
  if message.content.startswith(prefix + "join!c general"):
    ch=(929592940043579463)
    channel = client.get_channel(ch)
    await channel.connect()
  
  if message.content.startswith(prefix + "join!c minecraft"):
    ch=(929818724020658204)
    channel = client.get_channel(ch)
    await channel.connect()
  
  if message.content.startswith(prefix + "join!c the-forest"):
    ch=(929818948160069712)
    channel = client.get_channel(ch)
    await channel.connect()
  
  if message.content.startswith(prefix + "join!c vr"):
    ch=(929821005441036338)
    channel = client.get_channel(ch)
    await channel.connect()
  
  if message.content.startswith(prefix + "join!c staff-vc"):
    ch=(929588374736629770)
    channel = client.get_channel(ch)
    await channel.connect()
  
  if message.content.startswith(prefix + "join!c testing-vc"):
    ch=(931354713180487701)
    channel = client.get_channel(ch)
    await channel.connect()

  if message.content.startswith(prefix + "leave"):
    channel=message.guild.voice_client
    util.JSON.valuestr(file=f"audio/song.json", name="song", value="")
    util.JSON.valuestr(file=f"audio/song.json", name="url", value="")
    util.JSON.valuestr(file=f"audio/song.json", name="user", value="")
    util.JSON.valuestr(file=f"audio/song.json", name="author", value="")
    util.JSON.valuestr(file=f"audio/song.json", name="desc", value="")
    util.JSON.valuestr(file=f"audio/song.json", name="thumbnail", value="")
    await channel.disconnect()

  if message.content.startswith(prefix + "play "):
    contr=((message.content).replace(prefix + "play ", ""))
    voice_client = message.guild.voice_client
    if not voice_client.is_playing():
      ydl_opts = {'format': 'bestaudio'}
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          info = ydl.extract_info(contr, download=False)
          video_title = info.get('title', None)
          #video_author = info.get('channel_name', None)
          video_desc = info.get('description', None)
          video_thumbnail = info.get('thumbnail', None)
          URL = info['formats'][0]['url']
      audio_source = URL
      voice_client.play(discord.FFmpegPCMAudio(audio_source), after=None)
      colour1=(discord.Colour.blue())
      amimemb=(discord.Embed(title=("now playing " + video_title), url=contr, colour=colour1))
      util.JSON.valuestr(file=f"audio/song.json", name="song", value=video_title)
      util.JSON.valuestr(file=f"audio/song.json", name="url", value=contr)
      util.JSON.valuestr(file=f"audio/song.json", name="user", value=(message.author.name + "#" + message.author.discriminator))
      util.JSON.valuestr(file=f"audio/song.json", name="author", value="video_author")
      util.JSON.valuestr(file=f"audio/song.json", name="desc", value=video_desc)
      util.JSON.valuestr(file=f"audio/song.json", name="thumbnail", value=video_thumbnail)
      await message.reply(embed=amimemb)
      await message.delete()
    else:
      await message.reply("already playing a song")
  

  if message.content.startswith(prefix + "search "):
    contr=((message.content).replace(prefix + "search ", ""))
    voice_client = message.guild.voice_client
    if not voice_client.is_playing():
      ydl_opts = {'format': 'bestaudio', 'noplaylist':'True'}
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          info = ydl.extract_info(f"ytsearch:{contr}", download=False)['entries'][0]
          video_title = info.get('title', None)
          #video_author = info.get('channel_name', None)
          video_desc = info.get('description', None)
          video_thumbnail = info.get('thumbnail', None)
          URL = info['formats'][0]['url']
      audio_source = URL
      voice_client.play(discord.FFmpegPCMAudio(audio_source), after=None)
      colour1=(discord.Colour.blue())
      amimemb=(discord.Embed(title=("now playing " + video_title), url=URL, colour=colour1))
      util.JSON.valuestr(file=f"audio/song.json", name="song", value=video_title)
      util.JSON.valuestr(file=f"audio/song.json", name="url", value=URL)
      util.JSON.valuestr(file=f"audio/song.json", name="user", value=(message.author.name + "#" + message.author.discriminator))
      util.JSON.valuestr(file=f"audio/song.json", name="author", value="video_author")
      util.JSON.valuestr(file=f"audio/song.json", name="desc", value=video_desc)
      util.JSON.valuestr(file=f"audio/song.json", name="thumbnail", value=video_thumbnail)
      await message.reply(embed=amimemb)
      await message.delete()
    else:
      await message.reply("already playing a song")


  if message.content.startswith(prefix + "playfile"):
    split_v1 = str(message.attachments).split("filename='")[1]
    filename = str(split_v1).split("' ")[0]
    await message.attachments[0].save(fp="audio/{}".format(filename))
    voice_client = message.guild.voice_client
    audio_source = discord.FFmpegPCMAudio("audio/" + filename)
    if not voice_client.is_playing():
      voice_client.play(audio_source, after=None)
      colour1=(discord.Colour.blue())
      url1=(message.attachments[0].url)
      amimemb=(discord.Embed(title=("now playing " + filename), url=url1, colour=colour1))
      util.JSON.valuestr(file=f"audio/song.json", name="song", value=filename)
      util.JSON.valuestr(file=f"audio/song.json", name="url", value=url1)
      util.JSON.valuestr(file=f"audio/song.json", name="user", value=(message.author.name + "#" + message.author.discriminator))
      util.JSON.valuestr(file=f"audio/song.json", name="author", value=(message.author.name + "#" + message.author.discriminator))
      util.JSON.valuestr(file=f"audio/song.json", name="desc", value="")
      util.JSON.valuestr(file=f"audio/song.json", name="thumbnail", value="https://media.discordapp.net/attachments/687114028274942137/933142161430573076/music.jpg?width=840&height=473")
      await message.reply(embed=amimemb)
      await message.delete()
    else:
      await message.reply("already playing a file")
  
  if message.content==(prefix + "pause"):
    voice_client = message.guild.voice_client
    if voice_client.is_playing():
        colour1=(discord.Colour.blue())
        song = json.load(open(f"audio/song.json"))
        song1 = song["song"]
        songurl = song["url"]
        songuser = song["user"]
        songauthor = song["author"]
        songdesc = song["desc"]
        songthumbnail = song["thumbnail"]
        amimemb=(discord.Embed(title=("paused " + song1), colour=colour1))
        await message.reply(embed=amimemb)
        await message.delete()
        voice_client.pause()
    else:
        await message.reply("The bot is not playing anything at the moment.")
  
  if message.content==(prefix + "resume"):
    voice_client = message.guild.voice_client
    if voice_client.is_paused():
        colour1=(discord.Colour.blue())
        song = json.load(open(f"audio/song.json"))
        song1 = song["song"]
        songurl = song["url"]
        songuser = song["user"]
        songauthor = song["author"]
        songdesc = song["desc"]
        songthumbnail = song["thumbnail"]
        amimemb=(discord.Embed(title=("resumed " + song1), colour=colour1))
        await message.reply(embed=amimemb)
        await message.delete()
        voice_client.resume()
    else:
        await message.reply("The bot was not playing anything before this")
  
  if message.content==(prefix + "stop"):
    if message.author.id==(708392304871997460):
      await message.reply("not allowed")
    else:
      voice_client = message.guild.voice_client
      if voice_client.is_playing():
          colour1=(discord.Colour.blue())
          song = json.load(open(f"audio/song.json"))
          song1 = song["song"]
          songurl = song["url"]
          songuser = song["user"]
          songauthor = song["author"]
          songdesc = song["desc"]
          songthumbnail = song["thumbnail"]
          amimemb=(discord.Embed(title=("stopped " + song1), colour=colour1))
          util.JSON.valuestr(file=f"audio/song.json", name="song", value="")
          util.JSON.valuestr(file=f"audio/song.json", name="url", value="")
          util.JSON.valuestr(file=f"audio/song.json", name="user", value="")
          util.JSON.valuestr(file=f"audio/song.json", name="author", value="")
          util.JSON.valuestr(file=f"audio/song.json", name="desc", value="")
          util.JSON.valuestr(file=f"audio/song.json", name="thumbnail", value="")
          await message.reply(embed=amimemb)
          await message.delete()
          voice_client.stop()
      else:
          await message.reply("The bot is not playing anything at the moment.")
  
  if message.content==(prefix + "song"):
    voice_client = message.guild.voice_client
    if voice_client.is_playing():
        colour1=(discord.Colour.blue())
        song = json.load(open(f"audio/song.json"))
        song1 = song["song"]
        songurl = song["url"]
        songuser = song["user"]
        songauthor = song["author"]
        songdesc = song["desc"]
        songthumbnail = song["thumbnail"]
        com1=("""
played by """ + songuser + """
song author """ + songauthor + """

""" + songdesc + """
        """)
        amimemb=(discord.Embed(title=song1, url=songurl, colour=colour1, description=(com1))
        .set_thumbnail(url=songthumbnail))
        await message.reply(embed=amimemb)
        await message.delete()
    else:
        await message.reply("The bot is not playing anything at the moment.")















  if message.content==(prefix + 'help -a'):
    cmn1=(statushelp['NAME'])
    cmd1=(statushelp['DESC'])
    cma1=(statushelp['ARGS'])

    cmn2=(avatarhelp['NAME'])
    cmd2=(avatarhelp['DESC'])
    cma2=(avatarhelp['ARGS'])

    cmn3=(counthelp['NAME'])
    cmd3=(counthelp['DESC'])
    cma3=(counthelp['ARGS'])

    cmn4=(randomhelp['NAME'])
    cmd4=(randomhelp['DESC'])
    cma4=(randomhelp['ARGS'])

    cmn5=(uuidhelp['NAME'])
    cmd5=(uuidhelp['DESC'])
    cma5=(uuidhelp['ARGS'])

    cmn6=(sayhelp['NAME'])
    cmd6=(sayhelp['DESC'])
    cma6=(sayhelp['ARGS'])

    cmn7=(gethelp['NAME'])
    cmd7=(gethelp['DESC'])
    cma7=(gethelp['ARGS'])
    com1=("""
    """ + cmn1 + """
    """ + cmd1 + """
    Arguments: """ + cma1 + """


    """ + cmn2 + """
    """ + cmd2 + """
    Arguments: """ + cma2 + """


    """ + cmn3 + """
    """ + cmd3 + """
    Arguments: """ + cma3 + """


    """ + cmn4 + """
    """ + cmd4 + """
    Arguments: """ + cma4 + """


    """ + cmn5 + """
    """ + cmd5 + """
    Arguments: """ + cma5 + """


    """ + cmn6 + """
    """ + cmd6 + """
    Arguments: """ + cma6 + """


    """ + cmn7 + """
    """ + cmd7 + """
    Arguments: """ + cma7 + """


    **Voice Channels**

    **`/join`**
    joins the users current channel


    **`/leave`**
    leaves the vc the bot is currently in


    **`/join!c (channel)`**
    joins a specific channel see `/vc list` below


    **`/vc list`**
    lists the names of the all voice channels


    **Music**

    **`/play link`**
    allows you to play a youtube link


    **`/search name`**
    allows you to search and play youtube videos without the link


    **`/playfile file`**
    allows you to play a audio file or a mp4 file


    **`/pause`**
    pauses the current song


    **`/resume`**
    resumes the current song


    **`/stop`**
    stops the current song


    **`/song`**
    displays the current song


    **VC List**

    **General (64kbps)** joinID:`general64`
    **General** joinID:`general`
    **Minecraft** joinID:`minecraft`
    **The Forest** joinID:`the-forest`
    **VR** joinID:`vr`

    *all other joinID's are the same as the name*
    """)
    colour1=(discord.Colour.nitro_pink())
    amimemb=(discord.Embed(title='Commands', description=com1, colour=colour1))
    await message.channel.send(embed=amimemb)
    await message.delete()







client.run(ld.token)  



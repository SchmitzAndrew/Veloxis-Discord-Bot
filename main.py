################################################################################
################################################################################

from discord.ext import commands #, menus #basic discord python library and API
from datetime import datetime #date and time (for uptime)
import discord #basic discord python library and API
import psutil #system logging and info (CPU/RAM Usage)

# importing agent_list.py
import agent_list

# importing  map_list.py
import map_list

# importing weapon_list.py and the different classes of weapons
from weapon_list import sideArms, submachineGuns, normalRifles, shotguns, heavyRifles, sniperRifles, meleeCombat, invalidMessage

sideArms = sideArms()
submachineGuns = submachineGuns()
normalRifles = normalRifles() 
shotguns = shotguns()
heavyRifles = heavyRifles()
sniperRifles = sniperRifles()
meleeCombat = meleeCombat()
invalidMessage = invalidMessage()

# import player_statistics.py (logic used for importing player statistics "v!stats")
# import player_statistics

################################################################################
################################################################################

client = commands.Bot(command_prefix = 'v!')

client.remove_command('help')

################################################################################
################################################################################

# bot on ready and intialized
@client.event
async def on_ready():

    print('Veloxis Discord Bot \nDiscord Bot Up and Running on Harsh\'s Dell Laptop \nBot developed by Harsh Dadhich, Vrushank Prakash, Deepak Ananthkrishnan \n\n')
    
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=(f"{len(client.guilds)} Servers [v!help]")))

    client.starttime = datetime.now()

################################################################################
################################################################################

# v!help
@client.command()
async def help(ctx):

  # cur_page = 1
  # total_pages = 4

  # def on_forward(reaction, user):
  #   return user == ctx.message.author and str(reaction.emoji) == '▶️'
  
  # def on_backward(reaction, user):
  #   return user == ctx.message.author and str(reaction.emoji) == '◀️'

  # reaction1, user1 = await client.wait_for('reaction_add', check=on_forward)

  # reaction2, user2 = await client.wait_for('reaction_add', check=on_backward)

  # if on_forward(reaction1, user1):
  #   cur_page += 1

  # elif on_backward(reaction2, user2):
  #   cur_page -= 1
  
  help_section = ['***Display a Player\'s Statistics***', #0
                  '***Display ALL Agents***', #1
                  '***Displays an Agent\'s Profile***', #2
                  '***Displays ALL Weapons***', #3
                  '***Displays a Weapon/Gun\'s Info***', #4
                  '***Displays ALL Maps***', #5
                  '***Displays a Map\'s Info***', #6
                  '***Displays ALL Ranks***', #7
                  '***Displays ALL Game Modes***', #8
                  '***Displays the Credit System***', #9
                  '***Other***' #10
                  ]

  # Page 1

  # embed1 = discord.Embed(title=f'Help Section | Page `{cur_page}` / {total_pages}', color=0xFF004D)

  # await embed1.add_reaction('▶️')
  # await embed1.add_reaction('◀️')

  embed1.set_author(name="Veloxis", url="https://sites.google.com/view/veloxis/home", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed1.set_footer(text = 'Veloxis | Help Section → v!help | Bot Info → v!botinfo', icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed1.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed1.set_image(url="https://i.imgur.com/zjadlDH.png")
  
  embed1.add_field(name=help_section[0], value='**`v!stats <username#tag>`** \n[Coming Soon] Developers waiting on [tracker.gg](https://tracker.gg/valorant) to release player tracking using the Riot API', inline=False)

  embed1.add_field(name=help_section[1], value='**`v!agents` (aliases = `v!ags`**) \nViews all the agents in a list alphabetically along with their origin and agent class, for more info on individual agents, and their abilities, use the command right below' , inline=False)

  embed1.add_field(name=help_section[2], value='**`v!agent <name>` (aliases = `v!ag`)** \n • Agent Origin \n • Agent Class \n • Agent Abilities', inline=False)

  # await ctx.send (embed=embed1)


  # Page 2

  embed.add_field(name=help_section[3], value='**`v!weapons` (aliases = `v!wps`, `v!guns`)** \n • Weapon Class \n • Weapon **`listcode`**', inline=False)

  embed.add_field(name=help_section[4], value='**`v!weapon <name>` (aliases = `v!wp`, `v!gun`)** \n • Weapon type \n • Recoil pattern \n • Primary and alternate firing settings \n • Damage output (based on head/body/legs) \n • Magazine capacity \n • Ability to pierce through walls', inline=False)

  # Page 3

  embed.add_field(name=help_section[5], value='**`v!maps` (aliases = `v!mps`)**  \n • Haven (Map) \n • Bind (Map)\n • Split (Map) \n • Range (Training Map)', inline=False)

  embed.add_field(name=help_section[6], value='**`v!map <name>` (aliases = `v!mp`)** \n • Map Setting/Origin/Environment \n • Map Image', inline=False)

  embed.add_field(name=help_section[7], value='**`v!ranks`** \n • Information on achieveing ranks \n • A picture with ALL the rank badges', inline=False)

  # Page 4

  embed.add_field(name=help_section[8], value='**`v!modes`** \n • Information on Unranked Matches \n • Information on Ranked Matches \n • Information on Practice Matches', inline=False)

  embed.add_field(name=help_section[9], value='**`v!creds`** \n • Information on how credits are received for specific actions or events in the game', inline=False)

  embed.add_field(name=help_section[10], value='**Extra Commands and Information** \n • `v!help` → displays this help section \n • `v!ping` → displays latency, uptime, and   CPU/RAM usage \n • `v!botinfo` → displays information on this    bot, the invite link, Official Website, and Support Server Link \n\n*the names (of weapons, agents, maps, etc.) are NOT CASE SENSITIVE so you can do either **`v!map haven`** or **`v!map Haven`***', inline=False)
    
  print('HELP Command Called')
  await ctx.send(embed=embed)

################################################################################
################################################################################

# v!stats <username#tagnumber>
@client.command()
async def stats(ctx):
  
  embed = discord.Embed(title='Valorant Player Statistics', color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://sites.google.com/view/veloxis/home", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text='Help Section → v!help | Bot Info → v!botinfo', icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.add_field(name='**`v!stats`**', value='[Coming Soon] Developers waiting on [tracker.gg](https://tracker.gg/valorant) to release player tracking', inline=False)

  print('STATS Command Called')
  
  await ctx.send (embed=embed)

################################################################################
################################################################################

# v!agents/ags
@client.command(aliases=['ags'])
async def agents(ctx):

    embed = discord.Embed(title='Valorant Agents', color=0xFF004D)

    embed.set_author(name="Veloxis", url="https://sites.google.com/view/veloxis/home", icon_url="https://i.imgur.com/ZRH9UF4.png")
      
    embed.set_footer(text="Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

    embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

    embed.add_field(name='***Breach***', value='Origin: :flag_se: Sweden\n Agent Class: <:initiator_emoji:714939457589215274> Initiator', inline=False)

    embed.add_field(name='***Brimstone***', value='Origin: :flag_us: United States\n Agent Class: <:controller_emoji:714940194566176958> Controller', inline=False)

    embed.add_field(name='***Cypher***', value='Origin: :flag_ma: Morocco\n Agent Class: <:sentinel_emoji:714940115239305327> Sentinel', inline=False)

    embed.add_field(name='***Jett***', value='Origin: :flag_kr: South Korea\n Agent Class: <:duelist_emoji:714940079331737701> Duelist', inline=False)

    embed.add_field(name='***Omen***', value='Origin: :question: Unknown\n Agent Class: <:controller_emoji:714940194566176958> Controller', inline=False)

    embed.add_field(name='***Phoenix***', value='Origin: :flag_gb: United Kingdom\n Agent Class: <:duelist_emoji:714940079331737701> Duelist', inline=False)

    embed.add_field(name='***Raze***', value='Origin: :flag_br: Brazil\n Agent Class: <:duelist_emoji:714940079331737701> Duelist', inline=False)

    embed.add_field(name='***Reyna***', value='Origin: :flag_it: Mexico\n Agent Class: <:duelist_emoji:714940079331737701> Duelist', inline=False)

    embed.add_field(name='***Sage***', value='Origin: :flag_cn: China\n Agent Class: <:sentinel_emoji:714940115239305327> Sentinel', inline=False)

    embed.add_field(name='***Sova***', value='Origin: :flag_ru: Russia\n Agent Class: <:initiator_emoji:714939457589215274> Initiator', inline=False)

    embed.add_field(name='***Viper***', value='Origin: :flag_us: United States\n Agent Class: <:controller_emoji:714940194566176958> Controller', inline=False)

    embed.add_field(name='***More Info***', value='To view detailed information on an \nindividual agent, please use \n**`v!ag <name>`** (aliases = **`v!agent`**) \n\n*the names are NOT CASE SENSITIVE so you can do either **`v!ag sova`** or **`v!ag Sova`***', inline=False)


    print('AGENT LIST Command Called')
    
    await ctx.send (embed=embed)

#########################

# v!agent/ag <name/listcode>
@client.command(aliases=['ag'])
async def agent(ctx, agentName):
  
  if agentName == 'Breach' or agentName == 'breach':
    agent_list.Breach()
    await ctx.send (embed=agent_list.Breach())
    print('AGENT BREACH Command Called')

  elif agentName == 'Brimstone' or agentName == 'brimstone':
    agent_list.Brimstone()
    await ctx.send (embed=agent_list.Brimstone())
    print('AGENT BRIMSTONE Command Called')

  elif agentName == 'Cypher' or agentName == 'cypher':
    agent_list.Cypher()
    await ctx.send (embed=agent_list.Cypher())
    print('AGENT CYPHER Command Called')

  elif agentName == 'Jett' or agentName == 'jett':
    agent_list.Jett()
    await ctx.send (embed=agent_list.Jett())
    print('AGENT JETT Command Called')

  elif agentName == 'Omen' or agentName == 'omen':
    agent_list.Omen()
    await ctx.send (embed=agent_list.Omen())
    print('AGENT OMEN Command Called')

  elif agentName == 'Phoenix' or agentName == 'phoenix':
    agent_list.Phoenix()
    await ctx.send (embed=agent_list.Phoenix())
    print('AGENT PHOENIX Command Called')

  elif agentName == 'Raze' or agentName == 'raze':
    agent_list.Raze()
    await ctx.send (embed=agent_list.Raze())
    print('AGENT RAZE Command Called')

  elif agentName == 'Reyna' or agentName == 'reyna':
    agent_list.Reyna()
    await ctx.send (embed=agent_list.Reyna())
    print('AGENT REYNA Command Called')

  elif agentName == 'Sage' or agentName == 'sage':
    agent_list.Sage()
    await ctx.send (embed=agent_list.Sage())
    print('AGENT SAGE Command Called')

  elif agentName == 'Sova' or agentName == 'sova':
    agent_list.Sova()
    await ctx.send (embed=agent_list.Sova())
    print('AGENT SOVA Command Called')

  elif agentName == 'Viper' or agentName == 'viper':
    agent_list.Viper()
    await ctx.send (embed=agent_list.Viper())
    print('AGENT VIPER Command Called')

  else:
    agent_list.invalidMessage()
    await ctx.send(embed=agent_list.invalidMessage())
    print('INVALID AGENT Output Sent')

################################################################################
################################################################################

# v!guns/wps/weapons
@client.command(aliases=['wps','guns'])
async def weapons(ctx):

  embed = discord.Embed(title='Valorant Weapons/Guns', color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://sites.google.com/view/veloxis/home", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")
    
  embed.set_footer(text="Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.add_field (name='***Side Arms***', value='• Classic\n • Shorty \n • Frenzy \n • Ghost \n • Sheriff', inline=False)

  embed.add_field (name='***Submachine Guns***', value='• Stinger \n • Spectre ', inline=False)

  embed.add_field (name='***Normal Rifles***', value='• Bulldog \n • Guardian \n • Phantom \n • Vandal', inline=False)

  embed.add_field (name='***Shotguns***', value='• Bucky \n • Judge', inline=False)

  embed.add_field (name='***Heavy Rifles***', value='• Ares \n • Odin', inline=False)

  embed.add_field (name='***Sniper Rifles***', value='• Marshal \n • Operator', inline=False)

  embed.add_field (name='***Melee***', value='• Knife', inline=False)

  embed.add_field(name='***More Info***', value='To view detailed information on an \nindividual agent/character, please use \n**`v!wp <name>`** (aliases = **`v!weapon`**, **`v!gun`**) \n\n*the names are NOT CASE SENSITIVE so you can do either **`v!wp classic`** or **`v!wp Classic`***', inline=False)

  print('WEAPON LIST Command Called')
  
  await ctx.send (embed=embed)

#########################

# v!weapon/wp/gun <name/listcode>
@client.command(aliases=['wp','gun'])
async def weapon(ctx, weaponName):

  if weaponName == 'Classic' or weaponName == 'classic':
    sideArms.Classic()
    await ctx.send(embed=sideArms.Classic())
    print('WEAPON CLASSIC Command Called')

  elif weaponName == 'Shorty' or weaponName == 'shorty':
    sideArms.Shorty()
    await ctx.send(embed=sideArms.Shorty())
    print('WEAPON Shorty SHORTY Called')

  elif weaponName == 'Frenzy' or weaponName == 'frenzy':
    sideArms.Frenzy()
    await ctx.send(embed=sideArms.Frenzy())
    print('WEAPON FRENZY Command Called')

  elif weaponName == 'Ghost' or weaponName == 'ghost':
    sideArms.Ghost()
    await ctx.send(embed=sideArms.Ghost())
    print('WEAPON GHOST Command Called')
  
  elif weaponName == 'Sheriff' or weaponName == 'sheriff':
    sideArms.Sheriff()
    await ctx.send(embed=sideArms.Sheriff())
    print('WEAPON SHERIFF Command Called')

  elif weaponName == 'Stinger' or weaponName == 'stinger':
    submachineGuns.Stinger()
    await ctx.send(embed=submachineGuns.Stinger())
    print('WEAPON STINGER Command Called')

  elif weaponName == 'Spectre' or weaponName == 'spectre':
    submachineGuns.Spectre()
    await ctx.send(embed=submachineGuns.Spectre())
    print('WEAPON SPECTRE Command Called')

  elif weaponName == 'Bulldog' or weaponName == 'bulldog':
    normalRifles.Bulldog()
    await ctx.send(embed=normalRifles.Bulldog())
    print('WEAPON BULLDOG Command Called')
  
  elif weaponName == 'Guardian' or weaponName == 'guardian':
    normalRifles.Guardian()
    await ctx.send(embed=normalRifles.Guardian())
    print('WEAPON GUARDIAN Command Called')

  elif weaponName == 'Phantom' or weaponName == 'phantom':
    normalRifles.Phantom()
    await ctx.send(embed=normalRifles.Phantom())
    print('WEAPON PHANTOM Command Called')

  elif weaponName == 'Vandal' or weaponName == 'vandal':
    normalRifles.Vandal()
    await ctx.send(embed=normalRifles.Vandal())
    print('WEAPON VANDAL Command Called')

  elif weaponName == 'Bucky' or weaponName == 'bucky':
    shotguns.Bucky()
    await ctx.send(embed=shotguns.Bucky())
    print('WEAPON BUCKY Command Called')

  elif weaponName == 'Judge' or weaponName == 'judge':
    shotguns.Judge()
    await ctx.send(embed=shotguns.Judge())
    print('WEAPON JUDGE Command Called')

  elif weaponName == 'Ares' or weaponName == 'ares':
    heavyRifles.Ares()
    await ctx.send(embed=heavyRifles.Ares())
    print('WEAPON ARES Command Called')

  elif weaponName == 'Odin' or weaponName == 'odin':
    heavyRifles.Odin()
    await ctx.send(embed=heavyRifles.Odin())
    print('WEAPON ODIN Command Called')

  elif weaponName == 'Marshal' or weaponName == 'marshal':
    sniperRifles.Marshal()
    await ctx.send(embed=sniperRifles.Marshal())
    print('WEAPON MARSHAL Command Called')

  elif weaponName == 'Operator' or weaponName == 'operator':
    sniperRifles.Operator()
    await ctx.send(embed=sniperRifles.Operator())
    print('WEAPON OPERATOR Command Called')

  elif weaponName == 'Knife' or weaponName == 'knife':
    meleeCombat.Knife()
    await ctx.send(embed=meleeCombat.Knife())
    print('WEAPON KNIFE Command Called')

  else:
    invalidMessage.Invalid()
    await ctx.send(embed=invalidMessage.Invalid())
    print('INVALID WEAPON Output Sent')

################################################################################
################################################################################

# v!maps
@client.command(aliases=['mps'])
async def maps(ctx):

  embed = discord.Embed(title='Valorant Maps', color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://sites.google.com/view/veloxis/home", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")
    
  embed.set_footer(text="Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.add_field(name='***Ascent***', value='Map with Teleportation', inline=False)

  embed.add_field(name='***Bind***', value='Map with Teleportation', inline=False)

  embed.add_field(name='***Haven***', value='Southeast/South Asian Themed Map', inline=False)

  embed.add_field(name='***Split***', value='Urban Area Themed Map', inline=False)

  embed.add_field(name='***Range***', value='Training Map for Various Aspects of the Game', inline=False)

  embed.add_field(name='***More Info***', value='To view detailed information on an \nindividual map, please use \n**`v!map <name>`** \n\n*the names are NOT CASE SENSITIVE so you can do either **`v!map haven`** or **`v!map Haven`***', inline=False)

  print('MAP LIST Command Called')
  
  await ctx.send (embed=embed)

#########################

# v!map <map_name>
@client.command(aliases=['mp'])
async def map(ctx, mapName):
  
  if mapName == 'Ascent' or mapName == 'ascent':
    map_list.Bind()
    await ctx.send (embed=map_list.Ascent())
    print('MAP ASCENT Command Called')

  elif mapName == 'Bind' or mapName == 'bind':
    map_list.Bind()
    await ctx.send (embed=map_list.Bind())
    print('MAP BIND Command Called')
  
  elif mapName == 'Haven' or mapName == 'haven':
    map_list.Haven()
    await ctx.send (embed=map_list.Haven())
    print('MAP HAVEN Command Called')

  elif mapName == 'Split' or mapName == 'split':
    map_list.Split()
    await ctx.send (embed=map_list.Split())
    print('MAP SPLIT Command Called')

  elif mapName == 'Range' or mapName == 'range':
    map_list.Range()
    await ctx.send (embed=map_list.Range())
    print('MAP RANGE Command Called')

  else:
    map_list.invalidMessage()
    await ctx.send(embed=map_list.invalidMessage())
    print('INVALID MAP Output Sent')

################################################################################
################################################################################

# v!ranks
@client.command()
async def ranks(ctx):
  
  embed = discord.Embed(title='Valorant Player Statistics', color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://sites.google.com/view/veloxis/home", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.set_image(url="https://i.imgur.com/B8YoJQF.png")

  embed.add_field(name='***Starting Off***', value='After playing 20 matches in unranked, you will play 5 ranked games with either unranked players or players who have finished their placement matches. The competitive system will take into account how you are doing against the upper and lower ranked players in your game to determine if you will gain rating or lose rating. \n\nThis is important because you can still technically gain rating on a loss or lose rating on a win (which both are very rare). \n\nAfter completing your first 5 competitive games, Valorant will assign you a rank for your upcoming competitive games. You will be placed in matches with ranks 5 levels (or two ranks) above or below yours (this is also how queuing with your friends work). ', inline=False)

  embed.add_field(name='***Additional Info***', value='If your friends are 6 levels above or below yours, you will not be able to play with them until you gain rating to match theirs or they gain or lose rating to match yours. ', inline=False)

  print('RANKS Command Called')
  await ctx.send (embed=embed)

################################################################################
################################################################################
  
# v!modes
@client.command()
async def modes(ctx):

  embed = discord.Embed (title='**Valorant Game Modes**', color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://sites.google.com/view/veloxis/home", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Veloxis | Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.set_image (url='https://guides.gamepressure.com/valorant/gfx/word/472107875.jpg')

  embed.add_field (name='***Ranked Matches***', value='**Duration:** **`30`** to **`40`** **minutes** \n • Bomb (Spike Planting/Defusing) → Standard Mode', inline=False)

  embed.add_field (name='***Unranked Matches***', value='***Duration:*** **`30`** to **`40`** ***minutes*** \n • Standard Mode → Bomb (Spike Planting/Defusing) \n\n ***Duration:*** **`8`** to **`12`** ***minutes*** \n • Spike Rush → Bomb (Spike Planting/Defusing) \n Includes various orb mechanics such as Speed Boost and Damage Boost', inline=False)

  embed.add_field (name='***Practice Matches***', value='• Open Range → Freely explore the entire range and all it has to offer \n\n • Shooting Test → Test your gun skills with a variety of shooting challenges \n\n • Spike Planting → Take control of the site, plant the Spike, and defend until detonation \n\n • Spike Defuse → Methodically defeat enemies and defuse the Spike before time runs out', inline=False)

  embed.add_field (name='***Upcoming Game Modes***', value='• Team Deathmatch \n • Capture the Flag \n • Free for All', inline=False)

  embed.add_field (name='-------------------------------------------------------------', value='*The bomb in the main planting/defusing game mode*')

  print('MODES Command Called')
  await ctx.send (embed=embed)

################################################################################
################################################################################

# v!creds
@client.command()
async def creds(ctx):

  embed = discord.Embed (title='**Valorant Creds Info**', color=0xFF004D)

  embed.set_author(name="Veloxis", url="https://sites.google.com/view/veloxis/home", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
  embed.set_footer(text="Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

  embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

  embed.add_field(name='***Creds   <:credits_emoji:715298037957656587>***',value='• `800` at the first round \n • `3000` for each round win \n • `1900` for each round loss \n • `500` for 2x loss streak \n •  `1,000` for loss streaks greater than 2x \n • `200` per kill \n • `300` for planting the spike successfully \n • `5000` at overtime')

  print('CREDS Command Called')
  await ctx.send (embed=embed)

################################################################################
################################################################################

# v!ping
@client.command()
async def ping(ctx):

    time = datetime.now() - client.starttime
    days = time.days
    hours, remainder = divmod(time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    embed = discord.Embed (title='🏓 Pong!', color=0xFF004D)

    embed.set_author(name="Veloxis", url="https://sites.google.com/view/veloxis/home", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
    embed.set_footer(text="Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

    embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

    #Bot Latency
    embed.add_field(name='***:signal_strength: Bot Latency***',value=(f'`{round(client.latency * 1000)}`ms'),inline=True)

    #CPU Usage
    embed.add_field(name='***<:cpu_icon:715309843669450853> CPU Usage***',value=(f'`{round(psutil.cpu_percent())}`%'),inline=True)

    #RAM Usage
    embed.add_field(name='***<:ram_icon:715309388168167484> RAM Usage***',value=(f'`{round(psutil.virtual_memory()[2])}`%'),inline=True)

    #Bot Uptime
    embed.add_field(name='***:clock: Bot Uptime Duration***',value=(f'`{days}` day(s), `{hours}` hour(s), `{minutes}` min(s), and `{seconds}` second(s) \n\n*The bot\'s uptime is reset every time the bot restarts. This shows the uptime since the last restart*'),inline=False)
    
    print('PING Command Called')
    await ctx.send(embed=embed)

################################################################################
################################################################################

# v!botinfo
@client.command()
async def botinfo(ctx):

    embed=discord.Embed(title='Bot Information', color=0xFF004D)

    embed.set_author(name="Veloxis", url="https://sites.google.com/view/veloxis/home", icon_url="https://i.imgur.com/ZRH9UF4.png")
    
    embed.set_footer(text="Help Section → v!help | Bot Info → v!botinfo", icon_url="https://i.imgur.com/ZRH9UF4.png")

    embed.set_thumbnail(url="https://i.imgur.com/tu4L4oP.jpg")

    embed.add_field(name='***Bot Code Language***',value='Python 3.8.2',inline=True)

    embed.add_field(name='***Hosting Service***',value='[Repl.it](https://repl.it/) and [UptimeRobot](https://uptimerobot.com/)',inline=True)

    embed.add_field(name='***Developers***',value='<@533153734373539840> \n<@410590963379994639> \n<@652307034821361676>',inline=True)

    embed.add_field(name='***Bot Invite Link***',value='Click [here](https://discordapp.com/oauth2/authorize?client_id=710736437972172902&scope=bot&permissions=8) to invite this bot to another server',inline=False)

    embed.add_field(name='***Bot Official Website***',value='Click [here](https://sites.google.com/view/veloxis) to view the website and full documentation of Veloxis',inline=False)

    embed.add_field(name='***Veloxis Support Server***',value='Click [here](https://discord.com/invite/ppEpWEm) to join the OFFICIAL **`Veloxis Support Server`**',inline=False)
    
    embed.add_field(name='***Developement Information***',value='```Status Update (Week of 6/08/2020): \n\nWebsite has been released, click the link above for the official website and/or the Veloxis Support Discord Server \n\nPlayer tracking will be out once https://wwww.tracker.gg releases tracking with the Riot API \n\nThank you for your support and patience \n- Development Team```',inline=False)
    
    print('BOTINFO Command Called')
    await ctx.send(embed=embed)

################################################################################
################################################################################

infile = open('bot_token.txt', 'r')
TOKEN = infile.readline()

client.run(TOKEN)
import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! Saya adalah bot {bot.user}!')
    
@bot.command()
async def cara_memilah_sampah(ctx):
    await ctx.send(f'1. Pisahkan antara sampah organik dan anorganik, 2. Pilah antara sampah plastik, kertas, elektronik, kaleng, dan beling')

@bot.command()
async def cara_mengolah_sampah_organik(ctx):
    await ctx.send(f'Sampah organik dapat digunakan kembali dengan dijadikan pupuk kompos, dan eco enzim ')

@bot.command()
async def cara_mengolah_sampah_anorganik(ctx):
    await ctx.send(f'Sampah anorganik dapat diolah dengan cara menggunakan kembali dan memanfaatkannya, atau juga dapat mendaur ulang sampah tersebut menjadi barang baru yang lebih berguna atau bermanfaat  ')

@bot.command()
async def apa_yang_dapat_saya_buat_dari_sampah_anorganik(ctx):
    await ctx.send(f'Kamu dapat membuat kerajinan tangan ')

@bot.command()
async def kerajinan_tangan_dari_botol_bekas(ctx):
    await ctx.send(f'Kamu dapat menjadikan botol bekas menjadi celengan, mobil-mobilan, dan tempat pensil ')

@bot.command()
async def kerajinan_tangan_dari_kertas_bekas(ctx):
    await ctx.send(f'Limbah kertas dapat kamu jadikan bubur kertas, membuat kertas daur ulang, dan kamu dapat jadikan kertas menjadi anyaman  ')

@bot.command()
async def kerajinan_dari_kaleng_bekas(ctx):
    await ctx.send(f'Kamu dapat membuat pot tanaman, lampu tidur, tempat bumbu, dan tempat sendok ')

@bot.command()
async def command (ctx):
    await ctx.send(f'cara_memilah_sampah / cara_mengolah_sampah_organik / cara_mengolah_sampah_anorganik / apa_yang_dapat_saya_buat_dari_sampah_anorganik / kerajinan_tangan_dari_botol_bekas / kerajinan_tangan_dari_kertas_bekas / kerajinan_dari_kaleng_bekas')




@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)
    
bot.run("TOKEN BOT DISCORDMU")

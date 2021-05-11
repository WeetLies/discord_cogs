#Load Libary
import discord
import asyncio
import os
import re
import requests

from urllib.request import urlopen
from bs4 import BeautifulSoup
from discord.ext import commands
from discord.ext.commands.errors import ExtensionError

class Craw_WonderBerry(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies
    
    @commands.command(aliases=['원더베리','원기베리'])
    async def wonderberry(self,ctx):
        html = urlopen("https://maplestory.nexon.com/Guide/CashShop/Probability/WispsWonderBerry")
        soup = BeautifulSoup(html,"lxml")
        tb_div = soup.find_all("table",{"class":"my_page_tb2"})
        tb_br = tb_div[0].find_all("tr") 

        tr_1 = tb_br[1]
        tr_item_1 = tr_1.span.string
        tr_per_1_1 = list(tr_1)
        tr_per_tag_1 = tr_per_1_1.pop(5)
        tr_per_1 = tr_per_tag_1.string
    
        embed=discord.Embed(title="현재 판매중인 위습의 원더베리 확률이에요!",color=0x000000)
        embed.add_field(name="> {}".format(tr_item_1),value="확률  : "+tr_per_1,inline=True)
        for a in tb_br[1:]:
            th_tds = a.find_all('td')
            th_items = a.span.string
            th_per_temp = list(th_tds[1:])
            th_per_pop = th_per_temp.pop()
            th_per = th_per_pop.string
            embed.add_field(name="> {}".format(th_items),value="확률  : "+th_per,inline=True)
        await ctx.send(embed=embed)

def setup(weetlies):
    weetlies.add_cog(Craw_WonderBerry(weetlies))
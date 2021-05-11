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

class Craw_royalHair(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies
    
    @commands.command(aliases=['헤어','로얄헤어'])
    async def royalhair(self,ctx):
        html = urlopen("https://maplestory.nexon.com/Guide/CashShop/Probability/RoyalHairCoupon")
        soup = BeautifulSoup(html,"lxml")
        tb_div = soup.find_all("table",{"class":"my_page_tb2"})
        tb_man = tb_div[0].find_all("tr")
        tm_1 = tb_man[1]
        tm_item = tm_1.span.string
        tm_per_1 = list(tm_1)
        tm_per_tag = tm_per_1.pop(5)
        tm_per = tm_per_tag.string
        embed=discord.Embed(title="현재 판매중인 로얄헤어쿠폰 확률이에요",color=0x000000)
        embed.add_field(name="로얄헤어쿠폰",value="🧑🏻",inline=False)
        embed.add_field(name="> {}".format(tm_item),value="확률  : "+tm_per,inline=True)

        for a in tb_man[2:]:
            tm_tds = a.find_all('td')
            tm_items = a.span.string
            tm_per_temp = list(tm_tds[1:])
            tm_per_pop = tm_per_temp.pop()
            tm_per = tm_per_pop.string
            embed.add_field(name="> {}".format(tm_items),value="확률  : "+tm_per,inline=True)
        embed.add_field(name="======================================",value="**",inline=False)
        tb_woman = tb_div[1].find_all("tr")
        tw_1 = tb_woman[1]
        tw_item = tw_1.span.string
        tw_per_1 = list(tw_1)
        tw_per_tag = tw_per_1.pop(5)
        tw_per = tw_per_tag.string
        embed.add_field(name="로얄헤어쿠폰",value="👩🏻",inline=False)
        embed.add_field(name="> {}".format(tw_item),value="확률  : "+tw_per,inline=True)
        for a in tb_woman[2:]:
            tw_tds = a.find_all('td')
            tw_items = a.span.string
            tw_per_temp = list(tw_tds[1:])
            tw_per_pop = tw_per_temp.pop()
            tw_per = tw_per_pop.string
            embed.add_field(name="> {}".format(tw_items),value="확률  : "+tw_per,inline=True)
        embed.set_footer(text="제작자 : @WeetLies#5111")
        await ctx.send(embed=embed)
def setup(weetlies):
    weetlies.add_cog(Craw_royalHair(weetlies))
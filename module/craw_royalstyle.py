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

class Craw_royalStyle(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies
    
    @commands.command(aliases=['로얄','로얄스타일'])
    async def royalstyle(self,ctx):
        html = urlopen("https://maplestory.nexon.com/Guide/CashShop/Probability/RoyalStyle")
        soup = BeautifulSoup(html,"lxml")
        tb_div = soup.find("table",{"class":"my_page_tb2"})
        table = tb_div.find_all("tr")

        table_1 = table[1]
        item_1 = table_1.span.string
        per_temp = list(table_1)
        per_tag = per_temp.pop(5)
        per = per_tag.string
        embed=discord.Embed(title="현재판매중인로얄스타일 확률이에요",color=0x000000)
        embed.add_field(name="> {}".format(item_1),value="확률  : "+per,inline=False)


        for a in table[2:]:
            tds = a.find_all('td')
            items = a.span.string
            per_temp = list(tds[1:])
            per_pop = per_temp.pop()
            per = per_pop.string
            embed.add_field(name="> {}".format(items),value="확률  : "+per,inline=False)

        embed.set_footer(text="제작자 : @WeetLies#5111")
        await ctx.send(embed=embed)

def setup(weetlies):
    weetlies.add_cog(Craw_royalStyle(weetlies))
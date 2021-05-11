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

class Craw_LunaSweet(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies
    
    @commands.command(aliases=['루나스윗','루나크리스탈스윗'])
    async def lunasweet(self,ctx):
        html = urlopen("https://maplestory.nexon.com/Guide/CashShop/Probability/LunaCrystalSweet")
        soup = BeautifulSoup(html,"lxml")
        tb_div = soup.find_all("table",{"class":"my_page_tb2"})
        tb_br = tb_div[0].find_all("tr") 

        tr_1 = tb_br[1]
        tr_item_1 = tr_1.span.string
        tr_per_1_1 = list(tr_1)
        tr_per_tag_1 = tr_per_1_1.pop(5)
        tr_per_1 = tr_per_tag_1.string
    
        embed=discord.Embed(title="현재 판매중인 루나 크리스탈 스윗 확률이에요.",color=0x000000)
        embed.set_author(name="메이플홈페이지에서 보기(클릭)", url="https://maplestory.nexon.com/Guide/CashShop/Probability/LunaCrystalSweet")
        embed.add_field(name="> {}".format(tr_item_1),value="확률  : "+tr_per_1,inline=True)
        for a in tb_br[1:]:
            th_tds = a.find_all('td')
            th_items = a.span.string
            th_per_temp = list(th_tds[1:])
            th_per_pop = th_per_temp.pop()
            th_per = th_per_pop.string
            embed.add_field(name="> {}".format(th_items),value="확률  : "+th_per,inline=True)
        embed.add_field(name="> 추가사항",value="**베이스**로 사용한 루나스윗 펫이 리스트에 있을 경우 해당 확률만큼 \n루나스윗의 확률이 증가합니다.\n예시 : {0}을 베이스로 했을때 각 루나스윗확률은 약 **{1}**%입니다.".format(tr_item_1,round(float(tr_per_1[:4])*9/8,3)),inline=False)
        await ctx.send(embed=embed)

def setup(weetlies):
    weetlies.add_cog(Craw_LunaSweet(weetlies))

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

class Craw_piecered(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies
    
    @commands.command(aliases=['레라','레드라벨'])
    async def piece_red(self,ctx,arg):
        tag = arg
        if tag=="모자" or tag=="옷" or tag=="망토" or tag=="장갑" or tag=="신발" or tag=="무기":
            html = urlopen("https://maplestory.nexon.com/Guide/CashShop/Probability/MasterpieceRed")
            soup = BeautifulSoup(html,"lxml")
            tb_div = soup.find_all("table",{"class":"my_page_tb2"})
            if tag == "모자":
                table = tb_div[0].find_all("tr")
                moji = '🧢'
            elif tag == "옷":
                table = tb_div[1].find_all("tr")
                moji = '👔'
            elif tag == "망토" or arg == "장갑":
                table = tb_div[2].find_all("tr")
                moji = '🧤🧣'
            elif tag == "신발":
                table = tb_div[3].find_all("tr")
                moji = '👟'
            else:
                table = tb_div[4].find_all("tr")
                moji = '⚔'

            tb_1 = table[1]
            tb_item = tb_1.span.string
            tb_per = list(tb_1).pop(5).string
            # tb_per = tb_per.pop(5)
            # tb_per = tb_per.string
            embed=discord.Embed(title="현재 판매중인 마스터피스 확률이에요\t\t\t 대상 : 레드라벨{}".format(moji),color=0x000000)
            embed.add_field(name="> {}".format(tb_item),value="확률  : "+tb_per,inline=False)
            for a in table[1:]:
                tds = a.find_all('td')
                items = a.span.string
                per = list(tds[1:]).pop().string
                embed.add_field(name="> {}".format(items),value="확률  : "+per,inline=False)
            embed.add_field(name="> 추가사항",value="**베이스**로 사용한 아이템이 리스트에 있을 경우 해당 확률만큼 \n마스터 라벨을 제외한 다른 {0}의 확률이 증가합니다.\n예시 : {1}을 베이스로 했을때 각 레드라벨확률은 약 **{2}**%입니다.".format(arg,tb_item,round(float(tb_per[:4])*11/10,3)),inline=False)
            embed.set_footer(text="제작자 : @WeetLies#5111")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="❌Warning!",description="정확한 명령어를 입력해주세요.",color=0xff0000)
            embed.add_field(name="명령어와 분류를 제대로 입력해주세요.",value="> 예시) .레라 옷 또는 .레드라벨 옷",inline=False)
            await ctx.send(embed=embed)

    @piece_red.error #레드라벨 에러처리(추가인자 못받을때)
    async def piece_red_error(self,ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title="❌Warning!",description="정확한 명령어를 입력해주세요.",color=0xff0000)
            embed.add_field(name=".레라 모자",value="> 마스터피스 시 레드라벨 모자 획득확률을 보여드려요",inline=False)
            embed.add_field(name=".레라 옷",value="> 마스터피스 시 레드라벨 옷 획득확률을 보여드려요",inline=False)
            embed.add_field(name=".레라 망토\t 또는 .레라 장갑",value="> 마스터피스 시 레드라벨 망토/장갑 획득확률을 보여드려요",inline=False)
            embed.add_field(name=".레라 신발",value="> 마스터피스 시 레드라벨 신발 획득확률을 보여드려요",inline=False)
            embed.add_field(name=".레라 무기",value="> 마스터피스 시 레드라벨 무기 획득확률을 보여드려요",inline=False)
            embed.set_footer(text="명령어와 분류를 제대로 입력해주세요.\n예시) .레라 무기 또는 .레드라벨 무기")
            await ctx.send(embed=embed)



def setup(weetlies):
    weetlies.add_cog(Craw_piecered(weetlies))
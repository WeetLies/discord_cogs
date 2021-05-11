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

class Craw_Corona19(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies
    
    @commands.command(aliases=['코로나'])
    async def corona(self,ctx):
        html = urlopen("http://ncov.mohw.go.kr/")
        soup = BeautifulSoup(html,"html.parser")
        divtoday = soup.find_all("div",attrs={"class":"liveNum_today_new"})
        divtotal = soup.find_all("div",attrs={"class":"liveNum"})
        today_in = divtoday[0].find_all("span",attrs={"class":"data"})
        total_in = divtotal[0].find_all("span",attrs={"class":"num"})
        total_befor = divtotal[0].find_all("span",attrs={"class":"before"})

        today1 = today_in[0].get_text()
        today2 = today_in[1].get_text()

        total1 = total_in[0].get_text()
        total1 = total1.replace("(누적)","")
        total2 = total_in[1].get_text()
        total3 = total_in[2].get_text()
        total4 = total_in[3].get_text()
        
        befor1 = total_befor[0].get_text()
        befor1 = befor1.replace("전일대비","")
        befor1 = befor1.replace("(","")
        befor1 = befor1.replace(")","")
        befor2 = total_befor[1].get_text()
        befor2 = befor2.replace("(","")
        befor2 = befor2.replace(")","")
        befor3 = total_befor[2].get_text()
        befor3 = befor3.replace("(","")
        befor3 = befor3.replace(")","")
        befor4 = total_befor[3].get_text()
        befor4 = befor4.replace("(","")
        befor4 = befor4.replace(")","")

        embed=discord.Embed(title="국내 코로나 확진자 현황",description="해당정보는 실시간으로 받아온정보입니다.\n일일확진자(국내발생) :     **{0}** 명\n일일확진자(해외유입) :     **{1}** 명\n누적확진자(전일대비) :     **{2}** 명    (**{3}** 명)\n누적격리해제(전일대비) :     **{4}** 명    (**{5}** 명)\n치료/격리중(전일대비) :     **{6}** 명    (**{7}** 명)\n사망자(전일대비) :     **{8}**명    (**{9}** 명)".format(today1,today2,total1,befor1,total2,befor2,total3,befor3,total4,befor4),color=0xff0000)
        await ctx.send(embed=embed)


def setup(weetlies):
    weetlies.add_cog(Craw_Corona19(weetlies))
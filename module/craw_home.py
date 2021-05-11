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

class Craw_Homepage(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies
    
    @commands.command(aliases=['홈','홈페이지'])
    async def homepage(self,ctx,arg):
        link = 'https://maplestory.nexon.com'

        msg = arg
        if msg == "공지" or msg == "공지사항" or msg == "notice" or msg == "noti":
            url = "https://maplestory.nexon.com/News/Notice/Notice"
            html = urlopen("https://maplestory.nexon.com/News/Notice/Notice")
            soup = BeautifulSoup(html,"html.parser")
            div = soup.select_one('div.news_board > ul')
            links = div.find_all("a")

            embed=discord.Embed(title="최근 올라온 공지사항이에요.",color=0xff0000)

        elif msg == "업뎃" or msg == "업데이트" or msg == "update" or msg =="updat":
            url = "https://maplestory.nexon.com/News/Update"
            html = urlopen("https://maplestory.nexon.com/News/Update")
            soup = BeautifulSoup(html,"html.parser")
            div = soup.select_one('div.update_board > ul')
            links = div.find_all("a")

            embed=discord.Embed(title="최근업데이트 내역이에요",color=0xffff00)

        elif msg == "점검" or msg == "패치" or msg == "patch":
            url = "https://maplestory.nexon.com/News/Notice/Inspection"
            html     = urlopen("https://maplestory.nexon.com/News/Notice/Inspection")
            soup = BeautifulSoup(html,"html.parser")
            div = soup.select_one('div.news_board > ul')
            links = div.find_all("a")

            embed=discord.Embed(title="최근점검/패치내역이에요",color=0xfff000)

        elif msg == "이벤" or msg == "이벤트" or msg == "event":
            url = "https://maplestory.nexon.com/News/Event"
            html = urlopen("https://maplestory.nexon.com/News/Event")
            soup = BeautifulSoup(html,"html.parser")
            div = soup.find_all("div",attrs={"class":"event_list_wrap"})

            embed=discord.Embed(title="진행중인 이벤트내역이에요!",color=0x00ffff)
    
        elif msg =="캐샵" or msg == "캐시샵" or msg == "cashshop" or msg == "cash":
            url = "https://maplestory.nexon.com/News/CashShop"
            html = urlopen("https://maplestory.nexon.com/News/CashShop")
            soup = BeautifulSoup(html,"html.parser")
            div = soup.find_all("div", attrs={"class":"cash_list_wrap"})

            embed=discord.Embed(title="최근 업데이트 된 캐시샵 아이템들이에요!",color=0x0000ff)
        else:
            embed=discord.Embed(title="❌Warning!",description="정확한 명령어를 입력해주세요.",color=0xff0000)
            embed.add_field(name="명령어와 분류를 제대로 입력해주세요.",value="> 예시) .홈 공지 또는 .홈페이지 공지",inline=False)
            await ctx.send(embed=embed)
    
        if msg == "공지" or msg == "공지사항" or msg == "notice" or msg == "noti" or msg == "업뎃" or msg == "업데이트" or msg == "update" or msg =="updat" or msg == "점검" or msg == "패치" or msg == "patch":
            embed.set_author(name="메이플홈페이지에서 보기(클릭)", url=url)
            for a in links:
                href = a.attrs['href']
                title = a.find("span").get_text()
                flink = link+href
                embed.add_field(name="> {}".format(title),value=flink,inline=False)
        elif msg == "이벤" or msg == "이벤트" or msg == "event" or msg =="캐샵" or msg == "캐시샵" or msg == "cashshop" or msg == "cash":
            embed.set_author(name="메이플홈페이지에서 보기(클릭)", url=url)
            for a in div:
                datas = a.find("dd",attrs={"class":"data"})
                dates = a.find("dd",attrs={"class":"date"})
                title = datas.find("a").get_text()
                tplink = datas.find("a")["href"]
                date = dates.find("p").get_text()
                links = link+tplink

                embed.add_field(name="> {}".format(title),value=links+"\n **판매기간** : "+date,inline=False)
        else:
            pass
        embed.set_footer(text="제작자 : @WeetLies#5111")
        await ctx.send(embed=embed)

    @homepage.error #홈 에러처리(추가인자 못받을때)
    async def homepage_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title="❌Warning!",description="정확한 명령어를 입력해주세요.",color=0xff0000)
            embed.add_field(name=".홈 공지",value="> 현재 메이플홈페이지에 올라온 공지사항을 불러와요",inline=False)
            embed.add_field(name=".홈 점검\t 또는 .홈 패치",value="> 현재 메이플홈페이지에 올라온 점검/패치내역을 불러와요",inline=False)
            embed.add_field(name=".홈 업뎃",value="> 현재 메이플홈페이지에 올라온 업데이트내역을 불러와요",inline=False)
            embed.add_field(name=".홈 이벤",value="> 현재 메이플홈페이지에 올라온 이벤트내역을 불러와요",inline=False)
            embed.add_field(name=".홈 캐샵",value="> 현재 메이플홈페이지에 올라온 최신 캐시샵판매물품을 불러와요",inline=False)
            embed.set_footer(text="명령어와 분류를 제대로 입력해주세요.\n예시) .홈 공지 또는 .홈페이지 공지")
            await ctx.send(embed=embed)

def setup(weetlies):
    weetlies.add_cog(Craw_Homepage(weetlies))

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

class craw_characterinfo(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies
    
    @commands.command(aliases=['정보','info'])
    async def charic_info(self,ctx,arg):
        url = 'https://maple.gg/u/{}'.format(arg)
        html = requests.get(url)
        soup = BeautifulSoup(html.text,"html.parser")
        fndr = soup.select(".bg-light")
        if fndr[0].select('h3')[0].text == '검색결과가 없습니다.':
            embed = discord.Embed(title="❌Warning!",description="검색결과가 없습니다.!",color=0xff0000)
            embed.set_footer(text="캐릭이름을 다시 확인해주세요.결과는 대소문자를 구분하며,\n 메이플지지의 정보로 검색됩니다.")
            await ctx.send(embed=embed)
        else:
            usr_profile = fndr[0].find_all("div",attrs={"class":"user-profile"})
            usr_img = usr_profile[0].find("div",attrs={"class":"col-6 col-md-8 col-lg-6"}).img['src'] # 캐릭터 이미지 불러오기
            usr_int = usr_profile[0].find_all("ul",attrs={"class":"user-summary-list"})
            usr_info = usr_int[0].find_all("li")
            usr_lv = usr_info[0].string # 캐릭 레벨 데이터 가져오기
            usr_job = usr_info[1].string # 캐릭 직업 데이터 가져오기

            rank_profile = fndr[0].find_all("div",attrs={"class":"pt-4 pt-sm-3 pb-4"}) # 랭킹쪽 프로필 불러오기
            union_profile = fndr[0].find_all("div",attrs={"class":"pt-3 pb-2 pb-sm-3"})

            chk_ranking = fndr[0].find_all("div",attrs={"class":"col-lg-3 col-6 mt-3 px-1"})

            if chk_ranking[0].find_all("div",attrs={"class":"user-summary-no-data"}): #무릉 기록이 없는지 확인
                floor_rank = "기록없음"
                floor_time = "기록없음"
            else:
                floor_rank = rank_profile[0].find("h1").get_text().replace(" ","")
                floor_rank = floor_rank[:2]+"층"
                floor_time = rank_profile[0].find("small").get_text()

            if chk_ranking[1].find_all("div",attrs={"class":"user-summary-no-data"}): #시드 기록이 없는지 확인
                seed_rank = "기록없음"
                seed_time = "기록없음"
            else:
                seed_rank = rank_profile[1].find("h1").get_text().replace(" ","")
                seed_rank = seed_rank[:2]+"층"
                seed_time = rank_profile[1].find("small").get_text()

            if chk_ranking[2].find_all("div",attrs={"class":"user-summary-no-data"}): #유니온 정보이 있는지 확인
                union_rank = "기록없음"
                union_lv = "기록없음"
            else:
                union_rank = union_profile[0].find("div",attrs={"class":"user-summary-tier-string font-weight-bold"}).get_text().replace(" ","")
                union_lv = union_profile[0].find("span").get_text()

            embed=discord.Embed(title="메이플캐릭터 정보를 불러옵니다.", description=f"정보요청 : {ctx.author.mention}", color=0x0000ff)
            embed.add_field(name="닉네임 : {0}".format(arg),value="레벨 : {0}\t\t|\t직업 : {1}".format(usr_lv,usr_job),inline=False)
            embed.set_author(name="메이플지지에서 보기(클릭)", url=url)
            embed.add_field(name="무릉", value="{0}\n{1}".format(floor_rank,floor_time), inline=True)
            embed.add_field(name="시드", value="{0}\n{1}".format(seed_rank,seed_time), inline=True)
            embed.add_field(name="유니온", value="{0}\n{1}".format(union_rank,union_lv), inline=True)
            embed.set_thumbnail(url=usr_img)
            embed.set_footer(text="제작자 : @WeetLies#5111\n정보가 이상하다면 메이플지지에서 보기 들어가서\n정보갱신을 해주세요")
            await ctx.send(embed=embed)

    @charic_info.error
    async def characterinfo_error(self,ctx,error):
        embed=discord.Embed(title="❌Warning!",description="정확한 명령어를 입력해주세요.",color=0xff0000)
        embed.add_field(name=".정보 캐릭명",value="> 캐릭터 정보를 불러와요.\n 모든정보는 maple.gg를 기반으로 불러옵니다.",inline=False)
        embed.set_footer(text="명령어와 분류를 제대로 입력해주세요.\n예시) .정보 캐릭명")
        await ctx.send(embed=embed)


def setup(weetlies):
    weetlies.add_cog(craw_characterinfo(weetlies))

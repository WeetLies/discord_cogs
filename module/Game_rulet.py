#Load Libary
import discord
import asyncio
import random

from random import randint
from discord.ext import commands

class Game_Rulets(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies
    
    @commands.command(aliases=['룰렛','rulet'])
    async def randomrulets(self,ctx):
        await ctx.message.delete()
        # embed로 출력하기 전에 주사위 값을 결정해준다. 주사위 값은 01~99 사이값이 나온다.
        dice = random.randrange(1,100)
        embed=discord.Embed(title="룰렛을 돌려봅니다....",description=f"돌리신분 : {ctx.author.mention}",color=0xf3da33)
        if dice == 1:
            embed.add_field(name="이거뽑은사람불쌍해..😰",value=dice, inline=False)
        elif dice == 11 or dice == 22 or dice == 33 or dice == 44 or dice == 55 or dice == 66 or dice == 77 or dice == 88 or dice == 99:
            embed.add_field(name="땡 좀 잡으시네요?😤",value=dice, inline=False)
        elif dice<20:
            embed.add_field(name="유감입니다.😥",value=dice, inline=False)
        elif dice<40:
            embed.add_field(name="희망이있나요?😒",value=dice, inline=False)
        elif dice<60:
            embed.add_field(name="그래도평타는치겠지😊",value=dice, inline=False)
        elif dice<80:
            embed.add_field(name="누가이길수 있나요?😉",value=dice, inline=False)
        elif dice<100:
            embed.add_field(name="끝판왕 오셨네요😜",value=dice, inline=False)
        embed.set_footer(text="제작자 : @WeetLies#5111")
        await ctx.send(embed=embed)


def setup(weetlies):
    weetlies.add_cog(Game_Rulets(weetlies))

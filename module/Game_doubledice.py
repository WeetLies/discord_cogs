#Load Libary
import discord
import asyncio
import random

from random import randint
from discord.ext import commands



class Game_DoubleDice(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies
    
    @commands.command(aliases=['모마','moma'])
    async def doubledice(self,ctx):
        await ctx.message.delete()
        dddice1=random.randrange(1,7)
        dddice2=random.randrange(1,7)
        tdice=[dddice1,dddice2]
        embed=discord.Embed(title=f"주사위를 굴려봅니다.",description=f"주사위던진사람:{ctx.author.mention}",color=0x33aaff)
        if dddice1 == dddice2:
            embed.add_field(name=f"더블!🎲🎲",value=tdice, inline=False)
        else:
            embed.add_field(name=f"🎲",value=tdice, inline=False)
        embed.set_footer(text="제작자 : @WeetLies#5111")
        await ctx.send(embed=embed)


def setup(weetlies):
    weetlies.add_cog(Game_DoubleDice(weetlies))

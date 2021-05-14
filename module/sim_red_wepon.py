import discord
import asyncio
import csv
from discord import embeds
import random

from random import randint

from discord.ext import commands
from discord.ext.commands.errors import ExtensionError


class sim_RedCube(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies
    
    @commands.command(aliases=['레드큐브','레큡'])
    async def cube_red(self,ctx):
        dice1=randint(1,1000011)
        dice2=randint(1,1000027)
        dice3=randint(1,100000428)
        dice3_ex=randint(1,100000425)
        

        with open('module/database/sim_cube/red_wp_regend.csv',newline='',encoding='UTF-8') as db:
            fread = csv.reader(db)
            next(fread)
            for row_list in fread:
                if int(row_list[2]) <=dice1<=int(row_list[3]):
                    getline1 = row_list[0]
                if int(row_list[6]) <=dice2<=int(row_list[7]):
                    get_line2 = row_list[4]
                if int(756107) <= dice1<=int(853668) and int(975633)<= dice2<=int(980511):
                    if int(row_list[16]) <=dice3_ex <=int(row_list[17]):
                        get_line3 = row_list[8]
                elif int(853669)<=dice1<=int(1000011) and int(985391)<=dice2<=int(1000027):
                    if int(row_list[13]) <=dice3_ex <=int(row_list[14]):
                        get_line3 = row_list[8]
                else:
                    if int(row_list[10]) <=dice3 <=int(row_list[11]):
                        get_line3 = row_list[8]
            
            embed=discord.Embed(title="레드큐브 무기 결과에요.",description=f"정보 요청 : {ctx.author.mention}",color=0x00ff00)
            embed.add_field(name="부위:무기/등급:레전드리",value="**{0}**\n**{1}**\n**{2}**".format(getline1,get_line2,get_line3),inline=False)
            embed.set_footer(text="제작자 : @WeetLies#5111")
            await ctx.send(embed=embed)

def setup(weetlies):
    weetlies.add_cog(sim_RedCube(weetlies))
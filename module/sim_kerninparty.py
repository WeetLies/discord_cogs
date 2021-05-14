import discord
import asyncio
import csv
from discord import embeds

from discord.ext import commands
from discord.ext.commands.errors import ExtensionError


class Kerning_PartyQuest(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies
    
    @commands.command(aliases=['커파'])
    async def kerningParty(self,ctx,arg):
        num =  int(arg)
        maxi = 699
        mini = 500
        if num > maxi or num < mini:
            embed=discord.Embed(title="❌Warning!",description="숫자를 확인해주세요.",color=0xff0000)
            embed.set_footer(text="예:) .커파 599")
            await ctx.send(embed=embed)
        else:
            with open('module/database/kerning.csv',newline="",encoding='utf8') as kerning:
                f = csv.reader(kerning)
                next(f)
                for row_list in f:
                    if str(num) in row_list[0]:
                        ext = row_list[1]
            print(num,ext)
            embed=discord.Embed(title="커닝파퀘 족보입니다",description=f"정보 요청 :{ctx.author.mention}",color=0x00fff0)
            embed.add_field(name="요청하신 숫자 : {}".format(num),value="연산 : **{}**".format(ext),inline=False)
            embed.set_footer(text="제작자 : @WeetLies#5111")
            await ctx.send(embed=embed)
    
    @kerningParty.error 
    async def kerningParty_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title="❌Warning!",description="정확한 명령어를 입력해주세요.",color=0xff0000)
            embed.add_field(name=".커파 숫자",value="> 커닝파퀘할때 연산하는 과정에 대한 족보를 알려드려요",inline=False)
            embed.set_footer(text="예:) .커파 599")
            await ctx.send(embed=embed)

def setup(weetlies):
    weetlies.add_cog(Kerning_PartyQuest(weetlies))
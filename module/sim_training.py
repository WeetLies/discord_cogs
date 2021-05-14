import discord
import asyncio
import csv
from discord import embeds

from discord.ext import commands
from discord.ext.commands.errors import ExtensionError


class Boady_training(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies
    
    @commands.command(aliases=['심신'])
    async def training_body(self,ctx,msg1,msg2):
        lvl1=msg1
        lvl2=msg2
        exptime = float()
        needexp = int()

        if lvl1 > lvl2:
            embed=discord.Embed(title="❌Warning!!!",description="레벨값을 확인해주세요.",color=0xff0000)
            embed.set_footer(text=".무릉 레벨1 레벨2 중에서 레벨1값은 레벨2값보다 높을수 없습니다.")
            await ctx.send(embed=embed)
        else:

            with open('module/database/simsin.csv',newline='',encoding='utf8') as db:
                f = csv.reader(db)
                next(f)
                for row_list in f:
                    if int(lvl1) <= int(row_list[0]) < int(lvl2): #lvl1보다 크거나 같고, lvl2보다 작으면
                        exptime += float(row_list[4]) #row_list[4]데이터를 exptime에 모두 더한다.
                        needexp += int(row_list[1]) #row_list[1]데이터를 needexp에 모두 더한다.
                hour =  int(exptime / 60) #반복문 연산이 끝난 exptime을 60으로 나눠 시간단위로 쪼갠다.
                day = int(hour/24) # hour에서 24시간으로 쪼갠다.(일단위)
                hour = int(hour%24)
                ticket12 = int(exptime/60/12)+1
                ticket3 = int(exptime/60/3)+1
                exptime = int(exptime%hour)


            embed=discord.Embed(title="요청하신 심신수련관 레벨업정보에요.",description=f"정보 요청 : {ctx.author.mention}\n요청한 레벨정보 : **{lvl1}** ➡ **{lvl2}**",color=0x0fff00)
            embed.add_field(name="필요한 총 경험치 : {:,}".format(int(needexp)),value="총 소요시간 : {0}일 {1}시간 {2}분".format(day,hour,round(exptime,2)),inline=False)
            embed.add_field(name="입장권 필요갯수",value="입장권(12시간) : **{0:,}개**\n입장권(3시간) : **{1:,}개**".format(ticket12,ticket3),inline=False)
            embed.set_footer(text="제작 : @WeetLies#5111")
            await ctx.send(embed=embed)
            

    
    @training_body.error 
    async def training_body_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title="❌Warning!",description="정확한 명령어를 입력해주세요.",color=0xff0000)
            embed.add_field(name=".무릉 숫자 숫자",value="> 심신수련관으로 레벨업하는데 걸리는 시간을 알려드려요",inline=False)
            embed.set_footer(text="예:) .무릉 249 251")
            await ctx.send(embed=embed)

def setup(weetlies):
    weetlies.add_cog(Boady_training(weetlies))
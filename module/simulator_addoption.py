import discord
import asyncio
import csv
import math
from random import randint
from discord.ext import commands
from discord.ext.commands.errors import ExtensionError

class Simulator_add_options(commands.Cog):
    def __init__(self,weetlies):
        self.weetlies = weetlies

    @commands.command(aliases=['강환','강환불'])
    async def addoption_2nd(self,ctx, msg):
        wps = msg
        dice_num = randint(4,5) # 추가옵션이 총 몇개 뜰건지 정함.
        cnt=18
        ad_str = [33,44,55,66,77]
        ad_dex = [33,44,55,66,77]
        ad_int = [33,44,55,66,77]
        ad_luk = [33,44,55,66,77]
        ad_sd = [18,24,30,36,42]
        ad_si = [18,24,30,36,42]
        ad_sl = [18,24,30,36,42]
        ad_di = [18,24,30,36,42]
        ad_dl = [18,24,30,36,42]
        ad_il = [18,24,30,36,42]
        ad_hp = [1800,2400,3000,3600,4200]
        ad_mp = [1800,2400,3000,3600,4200]
        ad_lv = [-15,-20,-25,-30,-35]
        ad_sh = [33,44,55,66,77]
        ad_wp_boss = [6,8,10,12,14]
        ad_wp_damage = [3,4,5,6,7]
        ad_wp_attack = []
        ad_wp_mattack = []
        ad_s_att = [3,4,5,6,7]
        ad_s_matt = [3,4,5,6,7]
        ad_s_speed = [3,4,5,6,7]
        ad_s_jump = [3,4,5,6,7]
        ad_all=[3,4,5,6,7]
        f_str=f_dex=f_int=f_luk=f_hp=f_mp=f_lv=f_sh=f_boss=f_dam=f_att=f_matt=f_speed=f_jump=f_all=0
        print("총 추옵갯수 : ",dice_num)
        s_krlist=['힘','덱','인','럭','힘덱','힘인','힘럭','덱인','덱럭','인럭','hp','mp','착감','방어력','공격력','마력','이속','점프','올스텟']
        s_list=[ad_str,ad_dex,ad_int,ad_luk,ad_sd,ad_si,ad_sl,ad_di,ad_dl,ad_il,ad_hp,ad_mp,ad_lv,ad_sh,ad_s_att,ad_s_matt,ad_s_speed,ad_s_jump,ad_all]
        wp_krlist=['힘','덱','인','럭','힘덱','힘인','힘럭','덱인','덱럭','인럭','hp','mp','착감','방어력','공격력','마력','보스공격력','데미지','올스탯']
        wp_list=[ad_str,ad_dex,ad_int,ad_luk,ad_sd,ad_si,ad_sl,ad_di,ad_dl,ad_il,ad_hp,ad_mp,ad_lv,ad_sh,ad_wp_attack,ad_wp_mattack,ad_wp_boss,ad_wp_damage,ad_all]
        selkr=[]
        grade=[]
        if wps =="방어구":
            for i in range(1,dice_num+1): #추옵갯수가 뜬만큼 반복함. 1,2,3,4,5 반복 할수 있음.
                dicesel=randint(0,cnt) # 추옵의 종류를 정함.
                diceopt=randint(1,100) # 추옵등급의 확률을 구함.
                if diceopt<21: #추옵등급이 21보다 작으면
                    select=0
                elif diceopt<51: #추옵등급이 51보다 작으면
                    select=1
                elif diceopt<87: #추옵등급이 87보다 작으면
                    select=2
                else: #추옵등급 나머지 범위
                    select=3
                select_options=s_list[dicesel] # 선택한 옵션 선택
                select_options_kr=s_krlist[dicesel] #선택한 옵션 한글
                select_grade_opt = select_options[select] #선택한 옵션의 등급선정
                selkr.append(select_options_kr)
                grade.append(select_grade_opt)
                s_list.pop(dicesel)
                s_krlist.pop(dicesel)
                cnt -=1
        else:
            with open('GhostGhost_Bot/module/database/wpon.csv',newline='',encoding='utf8') as db:
                f = csv.reader(db)
                next(f)
                for row_list in f:
                    if wps == row_list[0]:
                        attackpoint = row_list[1]
            ad_wp_attack.append(math.ceil(int(attackpoint)*0.18))
            ad_wp_attack.append(math.ceil(int(attackpoint)*0.264))
            ad_wp_attack.append(math.ceil(int(attackpoint)*0.363))
            ad_wp_attack.append(math.ceil(int(attackpoint)*0.48))
            ad_wp_attack.append(math.ceil(int(attackpoint)*0.615))
            ad_wp_mattack.append(math.ceil(int(attackpoint)*0.18))
            ad_wp_mattack.append(math.ceil(int(attackpoint)*0.264))
            ad_wp_mattack.append(math.ceil(int(attackpoint)*0.363))
            ad_wp_mattack.append(math.ceil(int(attackpoint)*0.48))
            ad_wp_mattack.append(math.ceil(int(attackpoint)*0.615))
            
            for i in range(1,dice_num+1): #추옵갯수가 뜬만큼 반복함. 1,2,3,4,5 반복 할수 있음.
                dicesel=randint(0,cnt) # 추옵의 종류를 정함.
                diceopt=randint(1,100) # 추옵등급의 확률을 구함.
                if diceopt<21: #추옵등급이 21보다 작으면
                    select=0
                elif diceopt<51: #추옵등급이 51보다 작으면
                    select=1
                elif diceopt<87: #추옵등급이 87보다 작으면
                    select=2
                else: #추옵등급 나머지 범위
                    select=3
                select_options=wp_list[dicesel] # 선택한 옵션 선택
                select_options_kr=wp_krlist[dicesel] #선택한 옵션 한글
                select_grade_opt = select_options[select] #선택한 옵션의 등급선정
                selkr.append(select_options_kr)
                grade.append(select_grade_opt)
                wp_list.pop(dicesel)
                wp_krlist.pop(dicesel)
                cnt -=1
        
        for i in range(0,dice_num):
            print(i)
            if selkr[i] == "힘" or selkr[i] =='힘덱' or selkr[i] == '힘인' or selkr[i] == '힘럭':
                f_str+=int(grade[i])
            if selkr[i] == '덱' or selkr[i] =='힘덱' or selkr[i] == '덱인' or selkr[i] == '덱럭':
                f_dex+=int(grade[i])
            if selkr[i] == '인' or selkr[i] =='힘인' or selkr[i] == '덱인' or selkr[i] == '인럭':
                f_int+=int(grade[i])
            if selkr[i] == '럭' or selkr[i] =='힘럭' or selkr[i] == '덱럭' or selkr[i] == '인럭':
                f_luk+=int(grade[i])
            if selkr[i] == 'hp':
                f_hp +=int(grade[i])
            if selkr[i] == 'mp':
                f_mp +=int(grade[i])
            if selkr[i] == '착감':
                f_lv +=int(grade[i])
            if selkr[i] == '방어력':
                f_sh +=int(grade[i])
            if selkr[i] == '공격력':
                f_att +=int(grade[i])
            if selkr[i] == '마력':
                f_matt +=int(grade[i])
            if selkr[i] == '보스공격력':
                f_boss +=int(grade[i])
            if selkr[i] == '데미지':
                f_dam +=int(grade[i])
            if selkr[i] == '올스탯':
                f_all +=int(grade[i])
            if selkr[i] == '이속':
                f_speed +=int(grade[i])
            if selkr[i] == '점프':
                f_jump +=int(grade[i])
        
        if wps == "방어구":
            embed= discord.Embed(title="강환불 투척 : 아케인 {}".format(wps),description=f'정보 요청 : {ctx.author.mention}',color=0xff0000)
            embed.add_field(name="추가옵션이 붙은 갯수 : {} 개".format(dice_num),value='Str : {0}\nDex : {1}\nInt : {2}\nLuk : {3}\n최대 HP : {4}\n최대 MP : {5}\n공격력 : {6}\n마력 : {7}\n방어력 : {8}\n이동속도 : {9}\n점프력 : {10}\n올스탯 : {11}%\n착용레벨감소 : {12}'.format(f_str,f_dex,f_int,f_luk,f_hp,f_mp,f_att,f_matt,f_sh,f_speed,f_jump,f_all,f_lv),inline=False)
            embed.set_footer(text="제작자 : @WeetLies#5111")
            await ctx.send(embed=embed)
        else:
            embed= discord.Embed(title="강환불 투척 : 아케인 {}".format(wps),description=f'정보 요청 : {ctx.author.mention}',color=0xff0000)
            embed.add_field(name="추가옵션이 붙은 갯수 : {} 개".format(dice_num),value='Str : {0}\nDex : {1}\nInt : {2}\nLuk : {3}\n최대 HP : {4}\n최대 MP : {5}\n공격력 : {6}\n마력 : {7}\n방어력 : {8}\n데미지 : {9}%\n보스 몬스터 공격 시 데미지 : {10}%\n올스탯 : {11}%\n착용레벨감소 : {12}'.format(f_str,f_dex,f_int,f_luk,f_hp,f_mp,f_att,f_matt,f_sh,f_dam,f_boss,f_all,f_lv),inline=False)
            embed.set_footer(text="제작자 : @WeetLies#5111")
            await ctx.send(embed=embed)


    @commands.command(aliases=['영환','영환불'])
    async def addoption_1st(self,ctx, msg):
        wps = msg
        dice_num = randint(4,5) # 추가옵션이 총 몇개 뜰건지 정함.
        cnt=18
        ad_str = [33,44,55,66,77]
        ad_dex = [33,44,55,66,77]
        ad_int = [33,44,55,66,77]
        ad_luk = [33,44,55,66,77]
        ad_sd = [18,24,30,36,42]
        ad_si = [18,24,30,36,42]
        ad_sl = [18,24,30,36,42]
        ad_di = [18,24,30,36,42]
        ad_dl = [18,24,30,36,42]
        ad_il = [18,24,30,36,42]
        ad_hp = [1800,2400,3000,3600,4200]
        ad_mp = [1800,2400,3000,3600,4200]
        ad_lv = [-15,-20,-25,-30,-35]
        ad_sh = [33,44,55,66,77]
        ad_wp_boss = [6,8,10,12,14]
        ad_wp_damage = [3,4,5,6,7]
        ad_wp_attack = []
        ad_wp_mattack = []
        ad_s_att = [3,4,5,6,7]
        ad_s_matt = [3,4,5,6,7]
        ad_s_speed = [3,4,5,6,7]
        ad_s_jump = [3,4,5,6,7]
        ad_all=[3,4,5,6,7]
        f_str=f_dex=f_int=f_luk=f_hp=f_mp=f_lv=f_sh=f_boss=f_dam=f_att=f_matt=f_speed=f_jump=f_all=0
        print("총 추옵갯수 : ",dice_num)
        s_krlist=['힘','덱','인','럭','힘덱','힘인','힘럭','덱인','덱럭','인럭','hp','mp','착감','방어력','공격력','마력','이속','점프','올스텟']
        s_list=[ad_str,ad_dex,ad_int,ad_luk,ad_sd,ad_si,ad_sl,ad_di,ad_dl,ad_il,ad_hp,ad_mp,ad_lv,ad_sh,ad_s_att,ad_s_matt,ad_s_speed,ad_s_jump,ad_all]
        wp_krlist=['힘','덱','인','럭','힘덱','힘인','힘럭','덱인','덱럭','인럭','hp','mp','착감','방어력','공격력','마력','보스공격력','데미지','올스탯']
        wp_list=[ad_str,ad_dex,ad_int,ad_luk,ad_sd,ad_si,ad_sl,ad_di,ad_dl,ad_il,ad_hp,ad_mp,ad_lv,ad_sh,ad_wp_attack,ad_wp_mattack,ad_wp_boss,ad_wp_damage,ad_all]
        selkr=[]
        grade=[]
        if wps =="방어구":
            for i in range(1,dice_num+1): #추옵갯수가 뜬만큼 반복함. 1,2,3,4,5 반복 할수 있음.
                dicesel=randint(0,cnt) # 추옵의 종류를 정함.
                diceopt=randint(1,100) # 추옵등급의 확률을 구함.
                if diceopt<30: #추옵등급이 30보다 작으면
                    select=1
                elif diceopt<75: #추옵등급이 75보다 작으면
                    select=2
                elif diceopt<100: #추옵등급이 99보다 작으면
                    select=3
                else: #추옵등급 나머지 범위
                    select=4
                select_options=s_list[dicesel] # 선택한 옵션 선택
                select_options_kr=s_krlist[dicesel] #선택한 옵션 한글
                select_grade_opt = select_options[select] #선택한 옵션의 등급선정
                selkr.append(select_options_kr)
                grade.append(select_grade_opt)
                s_list.pop(dicesel)
                s_krlist.pop(dicesel)
                cnt -=1
        else:
            with open('GhostGhost_Bot/module/database/wpon.csv',newline='',encoding='utf8') as db:
                f = csv.reader(db)
                next(f)
                for row_list in f:
                    if wps == row_list[0]:
                        attackpoint = row_list[1]
            ad_wp_attack.append(math.ceil(int(attackpoint)*0.18))
            ad_wp_attack.append(math.ceil(int(attackpoint)*0.264))
            ad_wp_attack.append(math.ceil(int(attackpoint)*0.363))
            ad_wp_attack.append(math.ceil(int(attackpoint)*0.48))
            ad_wp_attack.append(math.ceil(int(attackpoint)*0.615))
            ad_wp_mattack.append(math.ceil(int(attackpoint)*0.18))
            ad_wp_mattack.append(math.ceil(int(attackpoint)*0.264))
            ad_wp_mattack.append(math.ceil(int(attackpoint)*0.363))
            ad_wp_mattack.append(math.ceil(int(attackpoint)*0.48))
            ad_wp_mattack.append(math.ceil(int(attackpoint)*0.615))
            
            for i in range(1,dice_num+1): #추옵갯수가 뜬만큼 반복함. 1,2,3,4,5 반복 할수 있음.
                dicesel=randint(0,cnt) # 추옵의 종류를 정함.
                diceopt=randint(1,100) # 추옵등급의 확률을 구함.
                if diceopt<30: #추옵등급이 30보다 작으면
                    select=1
                elif diceopt<75: #추옵등급이 75보다 작으면
                    select=2
                elif diceopt<100: #추옵등급이 99보다 작으면
                    select=3
                else: #추옵등급 나머지 범위
                    select=4
                select_options=wp_list[dicesel] # 선택한 옵션 선택
                select_options_kr=wp_krlist[dicesel] #선택한 옵션 한글
                select_grade_opt = select_options[select] #선택한 옵션의 등급선정
                selkr.append(select_options_kr)
                grade.append(select_grade_opt)
                wp_list.pop(dicesel)
                wp_krlist.pop(dicesel)
                cnt -=1
        
        for i in range(1,dice_num+1):
            print(i)
            if selkr[i-1] == "힘" or selkr[i-1] =='힘덱' or selkr[i-1] == '힘인' or selkr[i-1] == '힘럭':
                f_str+=int(grade[i-1])
            if selkr[i-1] == '덱' or selkr[i-1] =='힘덱' or selkr[i-1] == '덱인' or selkr[i-1] == '덱럭':
                f_dex+=int(grade[i-1])
            if selkr[i-1] == '인' or selkr[i-1] =='힘인' or selkr[i-1] == '덱인' or selkr[i-1] == '인럭':
                f_int+=int(grade[i-1])
            if selkr[i-1] == '럭' or selkr[i-1] =='힘럭' or selkr[i-1] == '덱럭' or selkr[i-1] == '인럭':
                f_luk+=int(grade[i-1])
            if selkr[i-1] == 'hp':
                f_hp +=int(grade[i-1])
            if selkr[i-1] == 'mp':
                f_mp +=int(grade[i-1])
            if selkr[i-1] == '착감':
                f_lv +=int(grade[i-1])
            if selkr[i-1] == '방어력':
                f_sh +=int(grade[i-1])
            if selkr[i-1] == '공격력':
                f_att +=int(grade[i-1])
            if selkr[i-1] == '마력':
                f_matt +=int(grade[i-1])
            if selkr[i-1] == '보스공격력':
                f_boss +=int(grade[i-1])
            if selkr[i-1] == '데미지':
                f_dam +=int(grade[i-1])
            if selkr[i-1] == '올스탯':
                f_all +=int(grade[i-1])
            if selkr[i-1] == '이속':
                f_speed +=int(grade[i-1])
            if selkr[i-1] == '점프':
                f_jump +=int(grade[i-1])
        
        if wps == "방어구":
            embed= discord.Embed(title="영환불 투척 : 아케인 {}".format(wps),description=f'정보 요청 : {ctx.author.mention}',color=0xff0000)
            embed.add_field(name="추가옵션이 붙은 갯수 : {} 개".format(dice_num),value='Str : {0}\nDex : {1}\nInt : {2}\nLuk : {3}\n최대 HP : {4}\n최대 MP : {5}\n공격력 : {6}\n마력 : {7}\n방어력 : {8}\n이동속도 : {9}\n점프력 : {10}\n올스탯 : {11}%\n착용레벨감소 : {12}'.format(f_str,f_dex,f_int,f_luk,f_hp,f_mp,f_att,f_matt,f_sh,f_speed,f_jump,f_all,f_lv),inline=False)
            embed.set_footer(text="제작자 : @WeetLies#5111")
            print(selkr,grade)
            await ctx.send(embed=embed)
        else:
            embed= discord.Embed(title="영환불 투척 : 아케인 {}".format(wps),description=f'정보 요청 : {ctx.author.mention}',color=0xbbffaa)
            embed.add_field(name="추가옵션이 붙은 갯수 : {} 개".format(dice_num),value='Str : {0}\nDex : {1}\nInt : {2}\nLuk : {3}\n최대 HP : {4}\n최대 MP : {5}\n공격력 : {6}\n마력 : {7}\n방어력 : {8}\n데미지 : {9}%\n보스 몬스터 공격 시 데미지 : {10}%\n올스탯 : {11}%\n착용레벨감소 : {12}'.format(f_str,f_dex,f_int,f_luk,f_hp,f_mp,f_att,f_matt,f_sh,f_dam,f_boss,f_all,f_lv),inline=False)
            embed.set_footer(text="제작자 : @WeetLies#5111")
            print(selkr,grade)
            await ctx.send(embed=embed)
    
    @addoption_2nd.error
    async def addoption_2nd_error(self,ctx,error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title="❌Warning!",description="정확한 명령어를 입력해주세요.",color=0xff0000)
            embed.add_field(name="명령어와 세부분류를 정확히 입력해주세요.",value="예시) .강환 케인 또는 .강환불 방어구",inline=False)
            embed.set_footer(text="무기는 인게임에서 무기분류에 써진대로 적어주셔야 하고 띄어쓰기와 영문은 생략합니다.\n예) 건틀렛 리볼버 => 건틀렛리볼버|ESP리미터=>리미터")
            await ctx.send(embed=embed)

    @addoption_1st.error
    async def addoption_1st_error(self,ctx,error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title="❌Warning!",description="정확한 명령어를 입력해주세요.",color=0xff0000)
            embed.add_field(name="명령어와 세부분류를 정확히 입력해주세요.",value="예시) .영환 케인 또는 .영환불 방어구",inline=False)
            embed.set_footer(text="무기는 인게임에서 무기분류에 써진대로 적어주셔야 하고 띄어쓰기와 영문은 생략합니다.\n예) 건틀렛 리볼버 => 건틀렛리볼버|ESP리미터=>리미터")
            await ctx.send(embed=embed)

def setup(weetlies):
    weetlies.add_cog(Simulator_add_options(weetlies))

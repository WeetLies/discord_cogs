# Discord.py Cogs 
     혼자 열심히 python을 공부하면서 이거저거 구현해나가며 
     누구든지 사용할 수 있게 Cogs화 한 자료들을 공유하기 위한 공간입니다.

## 자료를 쓰기전에 참고해주세요
    모든 코드는 저에게 맞춰 만들었기 때문에 아주 난장판 or 난장판 코드일수 있습니다. 
    하지만 조금씩 공부해나가면서 배워가는 초보자라 생각하고 너그러이 생각해주세요.
    module폴더 안 모든 파일은 각자 discord.py로 제작된 소스의 하나의 폴더에 넣고 
    로드 시키면 사용할 수 있습니다. 단, 각 소스마다 약간의 수정은 해주셔야합니다.

### 예시
```python
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
```
위의 소스에서 보면 weetlies라고 선언된 부분이 있습니다. 이부분은
```python
weetlies = commands.Bot(command_prefix='.')
```
부분의 앞에 선언한 내용과 모두 똑같게 수정하시면 됩니다. 
대부분은 
```python
bot = commands.Bot(command_prefix='.')
```
일확률이 높기때문에 위에 코드에서 weetlies 를 모두 bot으로 바꿔주면 정상적으로 이식이 가능합니다.

### 혼자 공부하면서 계속 하나하나 추가해나가는 재미로 공부하고 있습니다. 
각 Cogs를 만들면서 노가다를 한것도 있지만, 이거저거 만들수 있는 모든걸 차곡차곡 쌓아갈 예정입니다. 

### 각 소스들은 개인만의 약속된 형태의 소스파일명으로 저장할 예정입니다. 
또한 소스는 메이플 관련 정보 위주로 먼저 올라오며 추후 메이플스토리를 
제외한 다른곳에서도 만들어보고 싶은 소스가 있다면 같이 Cogs화 해서 올릴예정입니다.

Game = 디스코드 내에서 즐길 수 있는 미니게임(?)
craw = 크롤링 관련 소스
sim = 특정시뮬/연산 소스

## 추가된 소스 정보
2021/05/14 Update
--> sim_kerningparty.py # 커닝파티퀘스트 연산 족보

--> sim_red_wepon.py # 메이플 레드큐브로 무기 돌렸을때 나오는 옵션 시뮬

--> sim_training.py # 메이플 심신수련관 연산정보

2021/05/12 Update
--> Game_doubledice.py # 주사위 2개던져서 값보기

--> Game_rulet.py #1~99사이의 룰렛 돌리기

--> craw_charicinfo.py # maple.gg에서 캐릭터정보 받아와서 embed로 출력하기

--> craw_home.py #메이플홈페이지에서 공지/점검(패치)/업데이트/이벤트/캐시샵공지를 크롤링해서 embed로 출력

--> craw_lunadream.py #메이플홈페이지에서 루나드림 펫 확률을 크롤링해서 embed로 출력

--> craw_lunasweet.py #메이플홈페이지에서 루나스윗 펫 확률을 크롤링해서 embed로 출력

--> craw_pieceblack.py #메이플홈페이지에서 마스터피스 블랙라벨 확률을 크롤링해서 embed로 출력

--> craw_piecered.py #메이플홈페이지에서 마스터피스 레드라벨 확률을 크롤링해서 embed로 출력

--> craw_royalhair.py #메이플홈페이지에서 로얄 헤어쿠폰 확률을 크롤링해서 embed로 출력

--> craw_royalstyle.py #메이플홈페이지에서 로얄스타일 확률을 크롤링해서 embed로 출력

--> craw_royalsurgery.py #메이플홈페이지에서 로얄 성형쿠폰 확률을 크롤링해서 embed로 출력

--> craw_wonderberry.py #메이플홈페이지에서 원더베리 확률을 크롤링해서 embed로 출력


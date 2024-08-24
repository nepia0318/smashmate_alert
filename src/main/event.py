import requests
import discord

from .scraping import getCurrentRateByUserId

async def kamlon(ctx):
    KAMLON_ID=54285
    try:
        data = getCurrentRateByUserId(KAMLON_ID)
        embedMsg = discord.Embed(
            title='かむろん',
            description=f'\
                現在レート: {data["current_rate"]}\n\
                最高レート: {data["maximum_rate"]}\n\
                対戦成績　: {data["match_result"]}',
            color=discord.Colour.green()
        )
        # embedMsg.add_field(name="test", value='')

        await ctx.send(embed=embedMsg)

        # await message.channel.send(
        #     'かむろんさん\n'\
        #     f'現在のレート: {currentRate}'\
        # )

    except requests.RequestException as e:
        print(f"リクエストエラー: {e}")
        await ctx.send('取得に失敗しました')

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        await ctx.send('取得に失敗しました')

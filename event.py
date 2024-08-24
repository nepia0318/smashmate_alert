import scraping

async def kamlon(message):
    KAMLON_ID=54285
    currentRate=scraping.scraping(KAMLON_ID)
    # responseMsg = '現在のレート: '
    await message.channel.send(
        'かむろんさん\n'\
        f'現在のレート: {currentRate}'\
    )

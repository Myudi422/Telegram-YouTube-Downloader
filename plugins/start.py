from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠**ᎷᎩ_ᏂᎧᎷᏋ**:", url="https://t.me/musicvrtx")],
        [InlineKeyboardButton("**༺ʍǟֆȶɛʀʍɨռɖ༻**", url="https://t.me/phantomxhawk")]
    ])
    welcomed = f"""
    🎈Dear,
        Sir,Ma'am  <b>{message.from_user.first_name}</b>
    Use the below button or type /help for More info.
    [🎃](https://telegra.ph/file/a4478a612d7a8bc515874.jpg)[🎃]
    """
    
    
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

from pyrogram import Client, Filters

@Client.on_message(Filters.command([".help"]))
async def start(client, message):
    helptxt = f"""
-👤**𝗣𝗘𝗥𝗦𝗢𝗡𝗔𝗟**(for using here) ->-> Copy any Valid Youtube link and paste inside the bot and follow the prompts.
-🌍**𝗚𝗥𝗢𝗨𝗣𝗦** ->-> Add me in any group then copy any valid Youtube link and paste inside the bot and follow the prompts.

## 📍**ɨʍքօʀȶǟռȶ**📍
-𝕋ℍ𝔼 𝔹𝕀𝔾𝔾𝔼ℝ 𝕋ℍ𝔼 𝕊𝕀ℤ𝔼,𝕋ℍ𝔼 𝕄𝕆ℝ𝔼 𝕋𝕀𝕄𝔼 𝕐𝕆𝕌 ℍ𝔸𝕍𝔼 𝕋𝕆 𝕎𝔸𝕀𝕋.\n
-𝐅𝐢𝐥𝐞 𝐬𝐢𝐳𝐞 𝐦𝐨𝐫𝐞 𝐭𝐡𝐞𝐧 𝟐𝐠𝐛 𝐰𝐨𝐧'𝐭 𝐛𝐞 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐝𝐮𝐞 𝐭𝐨 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐩𝐨𝐥𝐢𝐜𝐲.

[🎃](https://telegra.ph/file/a4478a612d7a8bc515874.jpg)[🎃]
"""

    await message.reply_text(helptxt)

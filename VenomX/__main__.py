import importlib
from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from VenomX import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from VenomX.helpers.misc import create_botlog, heroku
from VenomX.modules import ALL_MODULES

MSG_ON = """
🔥 **VenomX-Userbot successfully activated**
━━
➠ **Userbot Version -** `{version}`
➠ **Type** `{handler}alive` **to check the bot**
━━
"""

async def main():
    for all_module in ALL_MODULES:
        importlib.import_module("VenomX.modules." + all_module)

    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("all_about_naru")
            await bot.join_chat("BROKENSHAYRI1")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(version=BOT_VER, handler=CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("VenomX").info(f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]")
        except Exception as e:
            LOGGER("main").warning(e)

    LOGGER("VenomX").info(f"VenomX-UserBot v{BOT_VER} [🔥 SUCCESSFULLY ACTIVATED! 🔥]")

    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)

    await idle()
    await aiosession.close()

if __name__ == "__main__":
    LOGGER("VenomX").info("Starting VenomX-UserBot")
    install()
    heroku()
    LOOP.run_until_complete(main())

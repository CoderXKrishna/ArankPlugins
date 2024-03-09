#  Copyright (C) 2020  Krishna.n(π.$)
# credits to @itsz_krish_babess (@itsz_krish_babess)
import asyncio
import os
import re

from userbot import arankub
from userbot.core.managers import edit_delete, edit_or_reply
from userbot.helpers.utils import reply_id
from userbot.plugins import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)

plugin_category = "fun"


@arankub.arank_cmd(
    pattern="fakegs(?:\s|$)([\s\S]*)",
    command=("fakegs", plugin_category),
    info={
        "header": "Fake google search meme",
        "usage": "{tr}fakegs search query ; what you mean text",
        "examples": "{tr}fakegs arankuserbot ; One of the Popular userbot",
    },
)
async def nekobot(arank):
    "Fake google search meme"
    text = arank.pattern_match.group(1)
    reply_to_id = await reply_id(arank)
    if not text:
        if arank.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            return await edit_delete(arank, "`What should i search in google.`", 5)
    aranke = await edit_or_reply(arank, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await edit_delete(
            arank,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    arankfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await arank.client.send_file(arank.chat_id, arankfile, reply_to=reply_to_id)
    await aranke.delete()
    if os.path.exists(arankfile):
        os.remove(arankfile)


@arankub.arank_cmd(
    pattern="trump(?:\s|$)([\s\S]*)",
    command=("trump", plugin_category),
    info={
        "header": "trump tweet sticker with given custom text",
        "usage": "{tr}trump <text>",
        "examples": "{tr}trump arankuserbot is One of the Popular userbot",
    },
)
async def nekobot(arank):
    "trump tweet sticker with given custom text_"
    text = arank.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(arank)

    reply = await arank.get_reply_message()
    if not text:
        if arank.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(arank, "**Trump : **`What should I tweet`", 5)
    aranke = await edit_or_reply(arank, "`Requesting trump to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    arankfile = await trumptweet(text)
    await arank.client.send_file(arank.chat_id, arankfile, reply_to=reply_to_id)
    await aranke.delete()
    if os.path.exists(arankfile):
        os.remove(arankfile)


@arankub.arank_cmd(
    pattern="modi(?:\s|$)([\s\S]*)",
    command=("modi", plugin_category),
    info={
        "header": "modi tweet sticker with given custom text",
        "usage": "{tr}modi <text>",
        "examples": "{tr}modi arankuserbot is One of the Popular userbot",
    },
)
async def nekobot(arank):
    "modi tweet sticker with given custom text"
    text = arank.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(arank)

    reply = await arank.get_reply_message()
    if not text:
        if arank.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(arank, "**Modi : **`What should I tweet`", 5)
    aranke = await edit_or_reply(arank, "Requesting modi to tweet...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    arankfile = await moditweet(text)
    await arank.client.send_file(arank.chat_id, arankfile, reply_to=reply_to_id)
    await aranke.delete()
    if os.path.exists(arankfile):
        os.remove(arankfile)


@arankub.arank_cmd(
    pattern="cmm(?:\s|$)([\s\S]*)",
    command=("cmm", plugin_category),
    info={
        "header": "Change my mind banner with given custom text",
        "usage": "{tr}cmm <text>",
        "examples": "{tr}cmm arankuserbot is One of the Popular userbot",
    },
)
async def nekobot(arank):
    text = arank.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(arank)

    reply = await arank.get_reply_message()
    if not text:
        if arank.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(arank, "`Give text to write on banner, man`", 5)
    aranke = await edit_or_reply(arank, "`Your banner is under creation wait a sec...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    arankfile = await changemymind(text)
    await arank.client.send_file(arank.chat_id, arankfile, reply_to=reply_to_id)
    await aranke.delete()
    if os.path.exists(arankfile):
        os.remove(arankfile)


@arankub.arank_cmd(
    pattern="kanna(?:\s|$)([\s\S]*)",
    command=("kanna", plugin_category),
    info={
        "header": "kanna chan sticker with given custom text",
        "usage": "{tr}kanna text",
        "examples": "{tr}kanna arankuserbot is One of the Popular userbot",
    },
)
async def nekobot(arank):
    "kanna chan sticker with given custom text"
    text = arank.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(arank)

    reply = await arank.get_reply_message()
    if not text:
        if arank.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(arank, "**Kanna : **`What should i show you`", 5)
    aranke = await edit_or_reply(arank, "`Kanna is writing your text...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    arankfile = await kannagen(text)
    await arank.client.send_file(arank.chat_id, arankfile, reply_to=reply_to_id)
    await aranke.delete()
    if os.path.exists(arankfile):
        os.remove(arankfile)


@arankub.arank_cmd(
    pattern="tweet(?:\s|$)([\s\S]*)",
    command=("tweet", plugin_category),
    info={
        "header": "The desired person tweet sticker with given custom text",
        "usage": "{tr}tweet <username> ; <text>",
        "examples": "{tr}tweet iamsrk ; arankuserbot is One of the Popular userbot",
    },
)
async def nekobot(arank):
    "The desired person tweet sticker with given custom text"
    text = arank.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(arank)

    reply = await arank.get_reply_message()
    if not text:
        if arank.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(
                arank,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            arank,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    aranke = await edit_or_reply(arank, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    arankfile = await tweets(text, username)
    await arank.client.send_file(arank.chat_id, arankfile, reply_to=reply_to_id)
    await aranke.delete()
    if os.path.exists(arankfile):
        os.remove(arankfile)

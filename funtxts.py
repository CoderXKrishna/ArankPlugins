import requests
from userbot import arankub
from userbot.core.managers import edit_or_reply

plugin_category = "fun"


@arankub.arank_cmd(
    pattern="tarank$",
    command=("tarank", plugin_category),
    info={
        "header": "Some random arank facial text art",
        "usage": "{tr}tarank",
    },
)
async def hmm(arank):
    "Some random arank facial text art"
    reactarank = requests.get("https://nekos.life/api/v2/arank").json()
    await edit_or_reply(arank, reactarank["arank"])


@arankub.arank_cmd(
    pattern="why$",
    command=("why", plugin_category),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(arank):
    "Some random Funny questions"
    whyarank = requests.get("https://nekos.life/api/v2/why").json()
    await edit_or_reply(arank, whyarank["why"])


@arankub.arank_cmd(
    pattern="fact$",
    command=("fact", plugin_category),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(arank):
    "Some random facts"
    factarank = requests.get("https://nekos.life/api/v2/fact").json()
    await edit_or_reply(arank, factarank["fact"])

from pyrogram.types import Message
from pyrogram import Client, filters
from StringSessionBot.database import SESSION
from StringSessionBot.database.users_sql import Users, num_users


@Client.on_message(~filters.service, group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        if q := SESSION.query(Users).get(int(msg.from_user.id)):
            SESSION.close()
        else:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()


@Client.on_message(filters.user(5779185981) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = await num_users()
    await msg.reply(f"Total Users : {users}", quote=True)

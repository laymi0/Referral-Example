from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from module.database import Users, Referral

router = Router()


@router.message(CommandStart(deep_link=True))
async def start_deep(msg: Message) -> None:

    name = msg.text.split(' ')[1]
    ref = await Referral.get_or_none(name=name)

    if ref:
        user, created = await Users.add_user(msg.from_user.id)
        if created:
            ref.unique += 1
        ref.count += 1
        await ref.save()
        await msg.answer(f'You followed the link from ' + name)

    else:
        await msg.answer('No such link')



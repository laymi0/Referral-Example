from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import BaseFilter
from aiogram_dialog import DialogManager,StartMode

from module.database import Referral
from states.admin_state import GetRefs

router = Router()


@router.message(F.text == '/links')
async def referral(msg: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=GetRefs.start, mode=StartMode.RESET_STACK)


@router.message(lambda message: message.text.startswith("/ref_"))
async def check_referral(msg: Message):
    name = msg.text.removeprefix('/ref_')

    refs = await Referral.get_or_none(name=name)
    if not refs:
        await msg.answer('No referral')
        return

    text = f'''Owner: {refs.owner}\nName: {refs.name}\nCount: {refs.count}
Unique: {refs.unique}\nPrice: {refs.price}'''

    await msg.answer(text)

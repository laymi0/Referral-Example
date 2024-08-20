from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import MessageInput

from aiogram.types import CallbackQuery, Message

from module.database import Referral
from states.admin_state import AddRef, GetRefs


async def add_ref(call: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.reset_stack()
    await dialog_manager.start(AddRef.name)


async def add_name(msg: Message, widget: MessageInput, dialog_manager: DialogManager):

    value = await Referral.filter(name=msg.text)

    if value:
        await msg.answer('<b>Such a link already exists:(</b>')
    else:
        dialog_manager.current_context().dialog_data['name'] = msg.text
        await dialog_manager.next()


async def add_price(msg: Message, widget: MessageInput, dialog_manager: DialogManager):

    if msg.text.isdigit():
        dialog_manager.current_context().dialog_data['price'] = int(msg.text)
        await dialog_manager.next()


async def add_owner(msg: Message, widget: MessageInput, dialog_manager: DialogManager):
    name = dialog_manager.current_context().dialog_data.get('name')
    price = dialog_manager.current_context().dialog_data.get('price')
    owner = msg.text
    await Referral.create(name=name, price=price, owner=owner)

    await msg.answer("The link has been successfully created!")
    await dialog_manager.start(state=GetRefs.start, mode=StartMode.RESET_STACK)

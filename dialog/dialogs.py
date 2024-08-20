from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import CurrentPage, NextPage, PrevPage, Row, Button
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Const, Format, List

from states.admin_state import GetRefs, AddRef
from . import getter
from . import func

dialog = Dialog(
    Window(
        Format("{text}"),
        List(
            Format("{pos}. /ref_{item}"), items="refferals", id="scroll", page_size=30
        ),
        Row(
            PrevPage("scroll", text=Const("◀️")),
            CurrentPage("scroll", text=Format("{current_page1}/{pages}")),
            NextPage("scroll", text=Const("▶️"))
        ),
        Row(
            Button(text=Const("➕"), id='add_ref', on_click=func.add_ref)
        ),
        getter=getter.getter,
        state=GetRefs.start,
    ),

)

add_ref_dialog = Dialog(
    Window(
        Const('<b>🔗Send the name of the link.</b>'),
        MessageInput(func=func.add_name),
        state=AddRef.name
    ),
    Window(
        Const('<b>💳 Send the cost of the link.</b>'),
        MessageInput(func=func.add_price),
        state=AddRef.price
    ),
    Window(
        Const('<b>👤Send the username of the admin.</b>'),
        MessageInput(func=func.add_owner),
        state=AddRef.owner
    )
)
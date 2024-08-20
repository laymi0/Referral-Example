from aiogram.fsm.state import StatesGroup, State


class GetRefs(StatesGroup):
    start = State()


class AddRef(StatesGroup):
    name = State()
    price = State()
    owner = State()
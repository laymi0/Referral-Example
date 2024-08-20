from aiogram import Router


def setup_aiogram_dialogs() -> Router:
    from . import dialogs
    router = Router()
    router.include_router(dialogs.dialog)
    router.include_router(dialogs.add_ref_dialog)

    return router
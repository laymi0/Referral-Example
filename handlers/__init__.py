from aiogram import Router


def setup_message_routers() -> Router:
    from . import admin, user

    router = Router()
    router.include_router(admin.router)
    router.include_router(user.router)
    return router
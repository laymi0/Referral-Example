import logging

from tortoise import fields
from tortoise.models import Model


class Users(Model):
    id = fields.IntField(pk=True)

    class Meta:
        table = "users"

    @classmethod
    async def add_user(cls, tg_id: int):
        user, created = await cls.get_or_create(id=tg_id)
        if created:
            logging.info(f"New user {tg_id}")
        return user, created


class Referral(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    count = fields.IntField(default=0)
    unique = fields.IntField(default=0)
    price = fields.IntField(null=True)
    owner = fields.CharField(null=True, max_length=128)

    class Meta:
        table = "referrals"
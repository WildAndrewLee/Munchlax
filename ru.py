from datetime import datetime
from bot import Bot
import validators
from models.user import User
from models.request import Request

ru = Bot()

@ru.command(requires=[validators.is_mentor])
async def active(message):
    if not User.set_active(message.user.name, True):
        await message.reply('Unable to set your active status.')
        return

    await message.reply('Your status has been set to inactive.')

@ru.command(requires=[validators.is_mentor])
async def inactive(message):
    if not User.set_active(message.user.name, False):
        await message.reply('Unable to set your active status.')
        return

    await message.reply('Your status has been set to inactive.')

@ru.command(requires=[validators.is_mentor])
async def busy(message):
    if not User.set_busy(message.user.name, True):
        await message.reply('Unable to set your busy status.')
        return

    await message.reply('Your status has been set to busy.')

@ru.command(requires=[validators.is_mentor])
async def unbusy(message):
    if not User.set_busy(message.user.name, False):
        await message.reply('Unable to set your busy status.')
        return

    await message.reply('Your status has been set to unbusy')

@ru.command()
async def mentors(message):
    Request.create(message.user, datetime.utcnow(), message.text)

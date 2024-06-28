from aiogram import Router, types

echo_router = Router()


def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence


@echo_router.message()
async def echo(message: types.Message):
    # logging.info(message)
    reversed_sentence = reverse_words(message.text)
    await message.answer(reversed_sentence)

from .naughtywords import *
ru_example="""
from naughty_word_py.naughtywords import NaughtyWordsParser
import asyncio
foo = NaughtyWordsParser()
async def main():
    await foo.parse("ru")
asyncio.run(main())
"""
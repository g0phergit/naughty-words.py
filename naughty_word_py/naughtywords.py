import aiohttp
from .config import GETError
class NaughtyWordsParser:
    """
    Class thats implements parser
    """
    baseurl="https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master"
    async def parse(self, lang):
        async with aiohttp.ClientSession() as parsersession:
            async with parsersession.get(f'{self.baseurl}/{lang}') as response:
                text = await response.text()
                return text
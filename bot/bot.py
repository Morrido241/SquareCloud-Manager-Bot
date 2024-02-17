from discord.ext.commands import Bot
from discord import Intents

from os import listdir


class SquareBot(Bot):

    """
    (Português)Isto é a subclasse do Bot
    (English)This is the Bot subclass
    """

    def __init__(self) -> None:

        # Inicializando a class Bot
        super().__init__(command_prefix='', intents=Intents.default())

    async def setup_hook(self) -> None:
        
        """
        (Português)Tudo que acontece antes do bot ligar
        (English)Everything that happens before the bot turns on
        """

        # Puxando os arquivos com os comandos
        for file in listdir('./cogs'):
           
            try:

                if file.endswith('.py'):

                    await self.load_extension('cogs.{}'.format(file[:-3]))

            except Exception as error:

                print("Ocorreu um erro ao carregar a cog.")
                raise error
        
        # Mostrando os cogs carregados 
        print("Cogs carregados -> {}".format(", ".join(self.cogs.keys())))

        

    async def on_ready(self) -> None:

        """
        (Português)Quando o bot vai ligar e está pronto pra uso
        (English) When the bot is ready
        """

        # Mostrando no terminal uma mensagem bonitinha
        print("Sou {} e estou pronto pra uso".format(self.user.name))


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
        super().__init__(command_prefix='.', intents=Intents.default())
        self.synced = False

    async def setup_hook(self) -> None:
        
        """
        (Português)Tudo que acontece antes do bot ligar
        (English)Everything that happens before the bot turns on
        """

        # Puxando os arquivos com os comandos
        for files in listdir('./bot/cogs/'):
           
            try:

                if files.endswith('.py'):

                    await self.load_extension('bot.cogs.{}'.format(files[:-3]))

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

        # Sincronizando os slashs
        if not self.synced:

            await self.tree.sync()
            self.synced = True

        # Colocando a mensagem bonitinha 
        print("Sou {} e estou pronto pra uso".format(self.user.name))


from discord import Interaction
from discord.ui import Select

from ...squarecloud.connection import squarefunctions


class SelectApp(Select):

    """
    (português) Select que seleciona os apps
    (English) the Select of the apps
    """

    def __init__(self) -> None:

        options = [
            
        ]

    async def callback(self, interaction: Interaction) -> None:
        
        """
        Callback do Select
        """

        pass
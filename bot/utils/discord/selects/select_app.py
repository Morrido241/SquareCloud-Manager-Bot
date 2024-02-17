from discord import Interaction
from discord.ui import Select

from ...squarecloud.connection import squarefunctions


class SelectApp(Select):

    """
    (português) Select que seleciona os apps
    (English) the Select of the apps
    """

    def __init__(self, options) -> None:

        super().__init__(placeholder="Select your app", options=options, row=0)

    async def callback(self, interaction: Interaction) -> None:
        
        """
        Callback do Select
        """

        pass
from discord.ext.commands import Cog, Bot
from discord import app_commands, Interaction, Embed, Colour

from random import choice

from ..utils import initial_view


class SquareCommands(Cog):

    """
    (Português)Este é o Cog dos comandos da square
    (English) This is the square commands Cog
    """

    def __init__(self, client: Bot) -> None:

        # Definindo o bot dentro do cog
        self.bot = client

    @app_commands.command(name="apps")
    async def get_ui(self, interaction: Interaction) -> None:

        """Sends the UI"""

        # Definindo a descrição
        description = (
            ""
        )

        # Definindo a embed
        embed = Embed(
            title="SquareCloud",
            description=description,
            colour=choice([Colour.dark_blue(), Colour.dark_purple(), Colour.dark_green()])
        )

        # View
        view = await initial_view()

        await interaction.response.send_message(embed=embed, view=view)


async def setup(client: Bot) -> None:

    """Setup necessário pro bot carregar o cog"""

    await client.add_cog(SquareCommands(client))

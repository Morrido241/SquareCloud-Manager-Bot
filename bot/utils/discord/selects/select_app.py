from discord import Interaction, Embed
from discord.ui import Select

from ...squarecloud.connection import squarefunctions
from ..views.app import AppView

# Select das aplicações
class SelectApp(Select):

    """
    (português) Select que seleciona os apps
    (English) the Select of the apps
    """

    def __init__(self, options) -> None:

        super().__init__(placeholder="Select your app", options=options, row=1)

    async def callback(self, interaction: Interaction) -> None:
        
        """
        Callback do Select
        """

        view, square_app, app_status = await app_view(self.values[0])

        # Puxando algumas coisas da square sobre a aplicação
        status = await app_status(self.values[0])
        app = await square_app(self.values[0])

        description = \
            f"**ID**: {self.values[0]}\n"\
            f"**RAM**: {status.ram}\n"\
            f"**CPU**: {status.cpu}\n"\
            f"**NETWORK**: {status.network['now']}\n"\
            f"**STATUS**: {'on'.upper() if status.running else 'off'.upper()}\n"\
            f"**STORAGE**: {status.storage}\n"
        
        embed = Embed(
            title=app.tag,
            description=description
        )

        # Desabilitando botão start em caso de já estar on
        view.button_1.disabled = True if status.running else False
        # Desabilitando botão stop se não tiver rodando
        view.button_3.disabled = True if not status.running else False

        await interaction.response.send_message(embed=embed, view=view)


# Construir o View e puxar funções necessárias
async def app_view(app_id: str):

    """
    (Português) Esta função apenas constroi a View
    (English) This function just builds the View
    """
    
    square_apps, square_app, app_status = await squarefunctions()
    view = AppView(app_id, (square_app, app_status))

    return view, square_app, app_status
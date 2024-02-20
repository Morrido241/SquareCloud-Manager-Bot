from discord import Interaction, Embed, SelectOption
from discord.ui import Select, View

from .select_app import SelectApp


class SelectGroup(Select):

    """
    (português) Select que seleciona os grupos apps
    (English) the Select of the apps group
    """

    def __init__(self, options: list[SelectOption]) -> None:

        option = [SelectOption(label=f"Group_{i+1}", value=i+1) for i in range((len(options)/25)+1)]

        super().__init__(placeholder="Select your app group", options=option, row=0)
        self.my_view = None
        self.opts = ...

    async def callback(self, interaction: Interaction) -> None:
        
        """
        (Português) Faz o view adicionar outro select_menu com 25 opções
        (English) Makes the view adds another select_menu with 25 options
        """
        new_select = SelectApp()

        self.my_view.add_item(new_select)
        
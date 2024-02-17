from discord import ui

from ..selects.select_app import SelectApp


class InitialView(ui.View):

    """
    (Português) Este view contém todos botões das interações iniciais
    (English) This View holds all buttons for initial interactions
    """

    def __init__(self, select: SelectApp) -> None:

        super().__init__(timeout=360)
        self.select = select
        self.add_item(select)

    

    
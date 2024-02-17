from discord import ui, Interaction


class AppView(ui.View):

    """
    (Português) Este é o View da aplicação
    (English) This is the app view
    """

    def __init__(self) -> None:

        super().__init__(timeout=360)

    @ui.button()
    async def button_1(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão para sua aplicação
        (English) This button Stop the app
        """

        pass

    @ui.button()
    async def button_2(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão reinicia a aplicação
        (English) This button restart the app
        """

        pass

    @ui.button()
    async def button_3(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão inicia o app
        (English) This button start the app
        """

        pass

    @ui.button()
    async def button_4(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão mostra o terminal da aplicação
        (English) This button shows the terminal of the app
        """

        pass

    @ui.button()
    async def button_5(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão gera um backup
        (English) This button make a backup 
        """

        pass
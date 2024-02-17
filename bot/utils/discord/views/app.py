from discord import ui, Interaction

from squarecloud.client import Application
from ...squarecloud.connection import connection


class AppView(ui.View):

    """
    (Português) Este é o View da aplicação
    (English) This is the app view
    """

    def __init__(self, app_id: str, connection: tuple) -> None:

        super().__init__(timeout=360)
        self.app_id = app_id
        self.square = connection

        ...

    @ui.button(label='start')
    async def button_1(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão inicia o app
        (English) This button start the app
        """

        await interaction.response.defer()

        app: Application = await self.square[0](self.app_id)
        response = await app.start()

        await interaction.channel.send("Done!")

    @ui.button(label='restart')
    async def button_2(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão reinicia a aplicação
        (English) This button restart the app
        """

        await interaction.response.defer()

        app: Application = await self.square[0](self.app_id)
        response = await app.restart()

        await interaction.channel.send("Done!")

    @ui.button(label="stop")
    async def button_3(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão para sua aplicação
        (English) This button Stop the app
        """

        await interaction.response.defer()

        app: Application = await self.square[0](self.app_id)
        response = await app.stop()

        await interaction.channel.send("Done!")


    @ui.button(label="Terminal")
    async def button_4(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão mostra o terminal da aplicação
        (English) This button shows the terminal of the app
        """

        await interaction.response.defer()
        msg = await interaction.channel.send("Wait a few seconds!")

        logs = await connection.get_logs(self.app_id)
        
        await msg.edit(content=">>> {logs.logs}")

    @ui.button(label="backup")
    async def button_5(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão gera um backup
        (English) This button make a backup 
        """
        await interaction.response.defer()

        msg = await interaction.channel.send("wait a few seconds!")
        app: Application = await self.square[0](self.app_id)
        backup = await app.backup()

        await msg.edit(content=f"Here your backup -> {backup.downloadURL}")
        
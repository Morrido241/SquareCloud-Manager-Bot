from discord import ui, Interaction, ButtonStyle, Embed

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

    @ui.button(label='start', row=0, style=ButtonStyle.blurple)
    async def button_1(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão inicia o app
        (English) This button start the app
        """

        await interaction.response.defer()

        app: Application = await self.square[0](self.app_id)
        await app.start()

        status = await app.status()
        description = \
            f"**ID**: {self.app_id}\n"\
            f"**RAM**: {status.ram}\n"\
            f"**CPU**: {status.cpu}\n"\
            f"**NETWORK**: {status.network['now']}\n"\
            f"**STATUS**: {'on'.upper() if status.running else 'off'.upper()}\n"\
            f"**STORAGE**: {status.storage}\n"\
            f"**UPTIME**: <t:{int(status.uptime)//1000}:R>"
        
        embed = Embed(
            title=app.tag,
            description=description
        )


        button.disabled = True
        self.button_3.disabled = False
        await interaction.message.edit(embed=embed, view=self)

        await interaction.channel.send("Done!", delete_after=35)
 
    @ui.button(label='restart', row=0, style=ButtonStyle.blurple)
    async def button_2(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão reinicia a aplicação
        (English) This button restart the app
        """

        await interaction.response.defer()

        app: Application = await self.square[0](self.app_id)
        await app.restart()

        status = await app.status()
        description = \
            f"**ID**: {self.app_id}\n"\
            f"**RAM**: {status.ram}\n"\
            f"**CPU**: {status.cpu}\n"\
            f"**NETWORK**: {status.network['now']}\n"\
            f"**STATUS**: {'on'.upper() if status.running else 'off'.upper()}\n"\
            f"**STORAGE**: {status.storage}\n"\
            f"**UPTIME**: <t:{int(status.uptime)//1000}:R>"
        
        embed = Embed(
            title=app.tag,
            description=description
        )

        await interaction.message.edit(embed=embed)
        await interaction.channel.send("Done!", delete_after=35)

    @ui.button(label="stop", row=0, style=ButtonStyle.red)
    async def button_3(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão para sua aplicação
        (English) This button Stop the app
        """

        await interaction.response.defer()

        app: Application = await self.square[0](self.app_id)
        await app.stop()

        status = await app.status()
        description = \
            f"**ID**: {self.app_id}\n"\
            f"**RAM**: {status.ram}\n"\
            f"**CPU**: {status.cpu}\n"\
            f"**NETWORK**: {status.network['now']}\n"\
            f"**STATUS**: {'on'.upper() if status.running else 'off'.upper()}\n"\
            f"**STORAGE**: {status.storage}\n"\
            f"**UPTIME**: <t:{int(status.uptime)//1000}:R>"
        
        embed = Embed(
            title=app.tag,
            description=description
        )

        button.disabled = True
        self.button_1.disabled = False
        await interaction.message.edit(embed=embed,view=self)

        await interaction.channel.send("Done!", delete_after=35)


    @ui.button(label="Terminal", row=1, style=ButtonStyle.gray)
    async def button_4(self, interaction: Interaction, button: ui.Button) -> None:

        """
        (Português) Este botão mostra o terminal da aplicação
        (English) This button shows the terminal of the app
        """

        await interaction.response.defer()
        msg = await interaction.channel.send("Wait a few seconds!")

        logs: Application = await self.square[0](self.app_id)
        logs = await logs.logs()
        
        await msg.edit(content=f">>> ```{logs.logs}```")

    @ui.button(label="backup", row=1)
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
        
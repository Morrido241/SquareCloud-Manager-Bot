from squarecloud import Client
from ...tokens import squarecloud_token


async def squarefunctions():

    connection = Client(api_key=squarecloud_token)

    async def get_apps():

        return await connection.all_apps()

    return get_apps

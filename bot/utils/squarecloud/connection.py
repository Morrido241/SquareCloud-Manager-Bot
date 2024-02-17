from squarecloud import Client
from ...tokens import squarecloud_token

connection = Client(api_key=squarecloud_token)

async def squarefunctions():

    """
    (Português) Apenas uma função para pegar outras funções
    (English) Just a function to get other functions
    """

    async def get_apps():

        return await connection.all_apps()
    
    async def get_app(app_id: str):

        return await connection.app(app_id)
    
    async def get_status(app_id: str):

        return await connection.app_status(app_id)

    return get_apps, get_app, get_status

from typing import Coroutine, Any
from asyncio import create_task, run

from .discord import InitialView, SelectApp, SelectGroup
from .squarecloud.connection import squarefunctions

from discord import SelectOption


async def initial_view() -> Coroutine[Any, Any, InitialView]:

    """
    (Português) Esta função apenas constroi a View e puxa os apps do Square Cloud
    (English) This function just builds the View and get your Square Cloud
    """

    # Puxando a função pra puxar infos da square
    get_apps = await squarefunctions()
    
    # Criando a lista do Select contendo as aplicações 
    square_apps = [SelectOption(label=app.tag, description=app.desc, value=app.id) for app in await get_apps[0]()]

    # Cria o select e o view
    if len(square_apps) <= 25:

        select = SelectApp(square_apps)
        view = InitialView(select)

    # Se tiver mais que 25 apps
    else:

        select = SelectGroup(square_apps)
        view =  InitialView(select)
        select.my_view = view

    return view



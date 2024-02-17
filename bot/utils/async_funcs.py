from typing import Coroutine, Any
from asyncio import create_task, run

from .discord import InitialView, SelectApp
from .squarecloud.connection import squarefunctions

from discord import SelectOption


async def initial_view() -> Coroutine[Any, Any, InitialView]:

    get_apps = await squarefunctions()
    square_apps = [SelectOption(label=app.tag, value=app.id) for app in await get_apps()]

    if len(square_apps) <= 25:

        select = SelectApp(square_apps)
        view = InitialView(select)

    else:

        pass

    return view
    
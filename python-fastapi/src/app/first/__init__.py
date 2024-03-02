"""Routers."""

import pathlib
import typing
from dataclasses import dataclass
from functools import lru_cache

from starlette.templating import Jinja2Templates

from src.setting import Settings

if typing.TYPE_CHECKING:
    from src.app.first.usecases import Usecases


@dataclass
class AppGlobalVariables:

    settings: Settings
    templates: Jinja2Templates

    @property
    def usecases(self) -> "Usecases":
        return self._usecases

    @usecases.setter
    def usecases(self, usecases: "Usecases") -> None:
        self._usecases = usecases


@lru_cache
def global_var() -> AppGlobalVariables:
    return AppGlobalVariables(
        settings=Settings(),
        templates=Jinja2Templates(
            directory=pathlib.Path(__file__).parent
            / "adapter"
            / "fastapi"
            / "templates",
        ),
    )

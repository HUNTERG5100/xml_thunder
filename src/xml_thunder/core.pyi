from io import TextIOWrapper
from typing import *
from collections.abc import Callable


RoutesDictionary = Dict[str, Callable]


class Lightning(object):
    """
    Used for creating an XML parser
    """

    def __init__(self):
        self.__routes: RoutesDictionary = {}

    def __repr__(self): ...

    def __str__(self): ...

    def __contains__(self, route: AnyStr): ...

    def __getitem__(self, route: AnyStr): ...

    def __setitem__(self, route: AnyStr, function: Callable): ...

    def __delitem__(self, route: AnyStr): ...

    def __len__(self): ...

    def __bool__(self): ...

    def get_all_routes(self) -> RoutesDictionary: ...

    def route(self, path: AnyStr) -> Callable: ...

    def parse(self, xml_like_document: Union[AnyStr, TextIOWrapper]) -> None: ...

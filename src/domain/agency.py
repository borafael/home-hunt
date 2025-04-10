import uuid

class Agency:

    def __init__(self, id: uuid, name: str, site: str) -> None:
        self.__id = id
        self.__name = name
        self.__site = site

    @property
    def id(self) -> uuid:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def site(self) -> str:
        return self.__site
from dataclasses import dataclass
from datetime import datetime as datetime
from typing import List

@dataclass
class Social:
    url: str
    followers: int
    def __init__(self, url, followers) -> None: ...

@dataclass
class Links:
    github: List[Social]
    linkedin: List[Social]
    medium: List[Social]
    twitter: List[Social]
    additional: List[Social]
    def __init__(
        self, github, linkedin, medium, twitter, additional
    ) -> None: ...

@dataclass
class Position:
    coin_id: str
    coin_name: str
    position: str
    def __init__(self, coin_id, coin_name, position) -> None: ...

@dataclass
class PeopleItem:
    id: str
    name: str
    teams_count: int
    description: str
    links: Links
    positions: List[Position]
    def __init__(
        self, id, name, teams_count, description, links, positions
    ) -> None: ...

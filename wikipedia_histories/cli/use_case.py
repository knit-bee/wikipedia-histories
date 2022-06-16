from dataclasses import dataclass
from typing import Protocol


@dataclass
class Request:
    title: str
    domain: str
    include_text: bool = True
    output: str = ""


class WikipediaHistoriesUseCase(Protocol):
    def process(self, request: Request) -> None:
        ...


class WikipediaHistoriesUseCaseImpl:
    def process(self, request: Request) -> None:
        pass

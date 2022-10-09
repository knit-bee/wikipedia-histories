from dataclasses import dataclass
from typing import Protocol

from wikipedia_histories.get_histories import get_history, to_df


@dataclass
class Request:
    title: str
    domain: str
    include_text: bool = True
    split: bool = False
    output: str = ""


class WikipediaHistoriesUseCase(Protocol):
    def process(self, request: Request) -> None:
        ...


class WikipediaHistoriesUseCaseImpl:
    def process(self, request: Request) -> None:
        data = get_history(
            request.title, include_text=request.include_text, domain=request.domain
        )
        if request.output:
            df = to_df(data)
            df.to_csv(request.output)

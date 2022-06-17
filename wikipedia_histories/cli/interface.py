import sys

from wikipedia_histories.cli.controller import WikipediaHistoriesController
from wikipedia_histories.cli.use_case import WikipediaHistoriesUseCaseImpl


def main() -> None:
    args = sys.argv[1:]
    controller = WikipediaHistoriesController(WikipediaHistoriesUseCaseImpl())
    controller.process_arguments(args)


if __name__ == "__main__":
    main()

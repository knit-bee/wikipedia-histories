import argparse
from typing import List

from wikipedia_histories.cli.use_case import Request, WikipediaHistoriesUseCase


class WikipediaHistoriesController:
    def __init__(self, use_case: WikipediaHistoriesUseCase) -> None:
        self._use_case = use_case

    def process_arguments(self, arguments: List[str]) -> None:
        parser = argparse.ArgumentParser(
            description="Fetch complete revision history of a Wikipedia page"
        )
        parser.add_argument(
            "title",
            help="""Title of the Wikipedia page to process. If the title
multiple words, wrap them in quotations marks, e.g. "Golden swallow", or connect
 them with underscore, e.g. Golden_swallow (as in the url of the article)""",
        )
        parser.add_argument(
            "--domain",
            "-d",
            help="""Domain name that should be used
 Default is the domain of English Wikipedia ('en.wikipedia.org'), if you, for example,
 want to use the French Wikipedia instead, use 'fr.wikipedia.org'""",
            default="en.wikipedia.org",
            type=str,
        )
        parser.add_argument(
            "--no_text",
            "-n",
            help="""Do not extract texts
from the revision history. This likely increases processing speed. If you're
mainly interested in the meta data, consider using this option.""",
            action="store_false",
        )
        parser.add_argument(
            "--to_file",
            help="""Name of output .csv-file. If this
 option is enabled, data will be converted to pandas.DataFrame and saved as .csv.""",
            default="",
            type=str,
        )
        args = parser.parse_args(arguments)
        self._use_case.process(
            Request(
                title=args.title,
                domain=args.domain,
                include_text=args.no_text,
                output=args.to_file,
            )
        )

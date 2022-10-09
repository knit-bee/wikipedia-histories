import unittest
from typing import Optional

from wikipedia_histories.cli.controller import WikipediaHistoriesController
from wikipedia_histories.cli.use_case import Request


class MockUseCase:
    def __init__(self) -> None:
        self.request: Optional[Request] = None

    def process(self, request: Request) -> None:
        assert not self.request
        self.request = request


class TestWikipediaHistoriesController(unittest.TestCase):
    def setUp(self):
        self.mock_use_case = MockUseCase()
        self.controller = WikipediaHistoriesController(use_case=self.mock_use_case)

    def test_controller_extracts_title(self) -> None:
        title = "Some title"
        self.controller.process_arguments([title])
        self.assertEqual(self.mock_use_case.request.title, title)

    def test_default_arguments(self) -> None:
        title = "title"
        self.controller.process_arguments([title])
        self.assertEqual(self.mock_use_case.request.domain, "en.wikipedia.org")
        self.assertTrue(self.mock_use_case.request.include_text)
        self.assertFalse(self.mock_use_case.request.split)

    def test_controller_extracts_title_and_domain_long(self) -> None:
        title = "My title"
        kw = "--domain"
        domain = "my_domain"
        self.controller.process_arguments([title, kw, domain])
        self.assertEqual(self.mock_use_case.request.title, title)
        self.assertEqual(self.mock_use_case.request.domain, domain)

    def test_controller_extracts_title_and_domain_short(self) -> None:
        title = "My title"
        kw = "-d"
        domain = "my_domain"
        self.controller.process_arguments([title, kw, domain])
        self.assertEqual(self.mock_use_case.request.title, title)
        self.assertEqual(self.mock_use_case.request.domain, domain)

    def test_controller_extracts_include_text_option_long(self) -> None:
        title = "Another title"
        kw = "--no_text"
        self.controller.process_arguments([title, kw])
        self.assertFalse(self.mock_use_case.request.include_text)

    def test_controller_extracts_include_text_option_short(self) -> None:
        title = "Another title"
        kw = "-n"
        self.controller.process_arguments([title, kw])
        self.assertFalse(self.mock_use_case.request.include_text)

    def test_controller_extracts_output_file_name(self) -> None:
        title = "Title"
        kw = "--to_file"
        file = "output.csv"
        self.controller.process_arguments([title, kw, file])
        self.assertEqual(self.mock_use_case.request.output, file)

    def test_controller_extracts_arguments_with_scrambled_order_correctly(self) -> None:
        title = "Title"
        kw_domain = "--domain"
        domain = "my_domain"
        kw_file = "--to_file"
        file = "my_file.csv"
        kw_text = "-n"
        self.controller.process_arguments(
            [kw_text, kw_domain, domain, kw_file, file, title]
        )
        self.assertEqual(
            self.mock_use_case.request,
            Request(title=title, domain=domain, output=file, include_text=False),
        )

    def test_controller_extracts_split_option(self) -> None:
        title = "Title"
        kw = "--split"
        self.controller.process_arguments([title, kw])
        self.assertTrue(self.mock_use_case.request.split)

    def test_controller_extracts_split_option_short(self) -> None:
        title = "Title"
        kw = "-s"
        self.controller.process_arguments([title, kw])
        self.assertTrue(self.mock_use_case.request.split)

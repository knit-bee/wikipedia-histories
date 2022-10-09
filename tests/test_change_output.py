import asyncio

import wikipedia_histories


def test_get_history_with_default_outputs_raw_text():
    data = wikipedia_histories.get_history("Andrei Broder")
    assert data != []
    assert isinstance(data[0].content, str) is True


def test_output_text_split_into_paragraphs():
    data = wikipedia_histories.get_history("Andrei Broder", output="split")
    assert isinstance(data[0].content, list) is True
    assert isinstance(data[0].content[0], str) is True


def test_get_text_split_into_paragraphs():
    text = asyncio.run(wikipedia_histories.get_texts([31820970], output="split"))
    assert text == [
        [
            "Andrei Broder is a Research Fellow and Vice President of Emerging Search "
            "Technology for Yahoo. He previously has worked for AltaVista as the vice "
            "president of research, and for IBM Research as a Distinguished Engineer & CTO.\n",
            "He has done research into the internet, and internet searching. He is credited "
            "with being one of the first people to develop a Captcha, while working for AltaVista.\n",
            "He earned his PhD from Stanford University in 1985, where his advisor was Donald Knuth.\n",
            "This biographical article relating to a computer specialist is a stub. You can help"
            " Wikipedia by expanding it.",
        ]
    ]

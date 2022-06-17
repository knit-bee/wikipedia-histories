import subprocess


def test_command_package_callable_without_error() -> None:
    process = subprocess.run(
        ["wikipedia-histories", "--help"],
        check=True,
        capture_output=True,
    )
    assert process.returncode == 0


def test_callable_from_cl_with_domain() -> None:
    process = subprocess.run(
        [
            "wikipedia-histories",
            "Crazy Mohan",
            "--domain",
            "tr.wikipedia.org",
            "--no_text",
        ],
        check=True,
        capture_output=True,
    )
    assert process.returncode == 0

import subprocess
import sys


def run_hello(*args):
    result = subprocess.run(
        [sys.executable, "hello.py", *args],
        capture_output=True,
        text=True,
    )
    return result


def test_default_greeting():
    result = run_hello()
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, World!"


def test_name_argument():
    result = run_hello("--name", "Alice")
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, Alice!"

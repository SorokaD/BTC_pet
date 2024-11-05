from typing import NamedTuple

import pytest


class TestCase(NamedTuple):
    input_value: int
    output_value: int


test_cases = (
    TestCase(3, 3),
    TestCase(5, 5),
    TestCase(1, 1),
)


@pytest.mark.parametrize("input_value,output_value", test_cases)
def test_simple(input_value: int, output_value: int) -> None:
    assert input_value == output_value

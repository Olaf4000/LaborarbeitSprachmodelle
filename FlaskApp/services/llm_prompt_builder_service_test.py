import FlaskApp.services.llm_prompt_builder_service as prompt_builder
import pytest

@pytest.mark.parametrize(
    "input,expected",
    [
        ("hallo", "welt")
        # TODO test cases after implementation
    ]
)
def test_system_prompt(input : str, expected : str):
    assert prompt_builder.build_system_prompt(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("hallo", "welt")
        # TODO test cases after implementation
    ]
)
def test_user_prompt(input : str, expected : str):
    assert prompt_builder.build_user_prompt(input) == expected
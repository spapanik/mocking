from unittest import mock

import pytest

from mocking import module


def test_mock_test_raise_exception():
    pytest.raises(ZeroDivisionError, module.division, 1, denominator=0)
    exception = pytest.raises(ZeroDivisionError, module.division, 1, 0)
    assert exception
    assert exception.value.args == ("division by zero",)


@mock.patch("mocking.module.id")
def test_mock_test_call_arguments_and_counts(mock_id):
    assert mock_id.call_count == 0
    module.call_id_builtin(None)
    module.call_id_builtin(True)  # noqa: FBT003
    module.call_id_builtin(False)  # noqa: FBT003
    assert mock_id.call_count == 3
    assert mock_id.call_args_list == [
        mock.call(None),
        mock.call(True),  # noqa: FBT003
        mock.call(False),  # noqa: FBT003
    ]


@mock.patch("mocking.module.echo", return_value=42)
def test_mock_a_function_same_module_constant_return(_mock_echo):
    assert module.call_same_module_function() == 42


@mock.patch("mocking.module.echo", new=mock.MagicMock(return_value=42))
def test_mock_a_function_same_module_constant_return_no_arg():
    assert module.call_same_module_function() == 42


@mock.patch("mocking.module.echo", side_effect=[42, 1024])
def test_mock_a_function_same_module_return_from_a_sequence(_mock_echo):
    assert module.call_same_module_function() == 42
    assert module.call_same_module_function() == 1024
    assert pytest.raises(StopIteration, module.call_same_module_function)


@mock.patch("mocking.module.echo", new=mock.MagicMock(side_effect=[42, 1024]))
def test_mock_a_function_same_module_return_from_a_sequence_no_arg():
    assert module.call_same_module_function() == 42
    assert module.call_same_module_function() == 1024
    assert pytest.raises(StopIteration, module.call_same_module_function)


@mock.patch("mocking.module.echo")
def test_mock_a_function_same_module_return_from_function(mock_echo):
    def mock_echo_side_effect(argument):
        return 42 if argument else 1024

    mock_echo.side_effect = mock_echo_side_effect
    assert module.call_same_module_function(True) == 42  # noqa: FBT003
    assert module.call_same_module_function(False) == 1024  # noqa: FBT003


@mock.patch("mocking.module.id", new=mock.MagicMock(return_value="a string"))
def test_mock_a_builtin():
    assert module.call_id_builtin(None) == "a string"


@mock.patch("mocking.module.method", new=mock.MagicMock(return_value="a string"))
def test_mock_a_function_other_module():
    assert module.call_library_module_function(None) == "a string"

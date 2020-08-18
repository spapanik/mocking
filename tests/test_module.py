from unittest import mock

import pytest

from mocking import module


@mock.patch("mocking.module.print")
def test_mock_a_builtin(mock_print):
    assert mock_print.call_count == 0
    module.call_print_builtin()
    assert mock_print.call_count == 1
    assert mock_print.call_args_list == [mock.call("actual string")]


@mock.patch("mocking.module.echo", return_value=42)
def test_mock_a_function_same_module_constant_return(mock_echo):
    assert module.call_same_module_function() == 42


@mock.patch("mocking.module.echo", new=mock.MagicMock(return_value=42))
def test_mock_a_function_same_module_constant_return_no_arg():
    assert module.call_same_module_function() == 42


@mock.patch("mocking.module.echo", side_effect=[42, 1024])
def test_mock_a_function_same_module_return_from_a_sequence(mock_echo):
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
    assert module.call_same_module_function(True) == 42
    assert module.call_same_module_function(False) == 1024
    assert pytest.raises(TypeError, module.call_same_module_function)

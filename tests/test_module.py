from unittest import mock

from mocking import module


@mock.patch("mocking.module.print")
def test_mock_a_builtin(mock_print):
    assert mock_print.call_count == 0
    module.call_print_builtin()
    assert mock_print.call_count == 1
    assert mock_print.call_args_list == [mock.call("actual string")]

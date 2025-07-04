# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import utils as module_0
import sanic.helpers as module_1


def test_case_0():
    str_0 = ">ymS@V%`?_6\\jb%"
    with pytest.raises(ValueError):
        module_0.str_to_bool(str_0)


def test_case_1():
    bytes_0 = b";"
    with pytest.raises(OSError):
        module_0.load_module_from_file_location(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.load_module_from_file_location(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Application state.\n\n    This class is used to store the state of the application. It is\n    instantiated by the application and is available as `app.state`.\n    "
    module_0.load_module_from_file_location(str_0, *str_0)


def test_case_4():
    str_0 = "head"
    with pytest.raises(OSError):
        module_0.load_module_from_file_location(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "n6bgC:TVy?c[?T/.+G"
    module_0.load_module_from_file_location(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "n6bgC:TV?q[?T$.9G"
    module_0.load_module_from_file_location(str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "n6bgC:TV?q[?T$.9G"
    list_0 = [str_0, str_0, str_0, str_0]
    str_1 = "1"
    bool_0 = module_0.str_to_bool(str_1)
    assert bool_0 is True
    module_0.str_to_bool(list_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    dict_0 = {}
    str_0 = "F"
    bool_0 = module_0.str_to_bool(str_0)
    assert bool_0 is False
    module_1.import_string(dict_0)

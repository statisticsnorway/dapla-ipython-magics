from unittest.mock import MagicMock
from nose.tools import with_setup
from magics.blueprint import Blueprint

magic = None
shell = None
ipython_display = None


def _setup():
    global magic, spark_controller, shell, ipython_display

    magic = Blueprint(shell=None)
    magic.shell = shell = MagicMock()
    magic.ipython_display = ipython_display = MagicMock()


def _teardown():
    pass


@with_setup(_setup, _teardown)
def test_register_input():
    cell = "alias /some/path"
    magic.register_input(None, cell)
    assert magic._input_datasets == {'alias': {'hitCount': 0, 'value': '/some/path'}}
    path = magic.get_input("alias")
    assert path == "/some/path"
    # Check that hit count has increased by 1
    assert magic._input_datasets == {'alias': {'hitCount': 1, 'value': '/some/path'}}


@with_setup(_setup, _teardown)
def test_register_output():
    cell = "alias /some/path"
    magic.register_output(None, cell)
    assert magic._output_datasets == {'alias': {'hitCount': 0, 'value': '/some/path'}}
    path = magic.get_output("alias")
    assert path == "/some/path"
    # Check that hit count has increased by 1
    assert magic._output_datasets == {'alias': {'hitCount': 1, 'value': '/some/path'}}

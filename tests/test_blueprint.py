from unittest.mock import MagicMock
from nose.tools import with_setup
from dapla.magics.blueprint import Blueprint

magic = None
shell = None
ipython_display = None


def _setup():
    global magic, spark_controller, shell, ipython_display

    magic = Blueprint(shell=None)
    magic.shell = shell = MagicMock()
    magic.shell.user_ns = {}
    magic.ipython_display = ipython_display = MagicMock()


def _teardown():
    pass


@with_setup(_setup, _teardown)
def test_define_input():
    cell = "alias /some/path"
    magic.define_input(None, cell)
    assert magic._input_datasets == {'alias': {'dataset': None, 'path': '/some/path'}}
    ref = magic.get_input("alias")
    assert ref['path'] == "/some/path"

@with_setup(_setup, _teardown)
def test_register_input():
    cell = "alias /some/path"
    magic.define_input(None, cell)
    magic.shell.user_ns['realdataset'] = {'dataset': 'dummy'}
    magic.register_input_dataset("alias realdataset")
    ref = magic.get_input("alias")
    assert ref['dataset'] == {'dataset': 'dummy'}

@with_setup(_setup, _teardown)
def test_define_output():
    cell = "alias /some/path"
    magic.define_output(None, cell)
    assert magic._output_datasets == {'alias': {'dataset': None, 'path': '/some/path'}}
    ref = magic.get_output("alias")
    assert ref['path'] == "/some/path"

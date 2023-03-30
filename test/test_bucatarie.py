import pytest
from src.bucatarie import Bucatarie
from unittest.mock import MagicMock, patch
import json

def test_adagare():
    data = {"ulei": 1000, "bicarbonat": 1000}
    mock = MagicMock(return_value=data)

    with patch('src.bucatarie.Bucatarie.initializeaza_inventar', mock):
        buc = Bucatarie()
        buc.inventar = buc.initializeaza_inventar()
        buc.adauga_produs("patrunjel",1000)
        buc.adauga_produs("ulei", 1000)
        assert buc.inventar["ulei"] == 2000
        assert buc.inventar["bicarbonat"] == 1000
        assert buc.inventar["patrunjel"] == 1000


def test_get_raw_data():
    data = [{"ulei": 1000, "bicarbonat": 1000}]
    mock = MagicMock(return_value=data)

    with patch('src.bucatarie.Bucatarie.adauga_produs', mock):
        buc = Bucatarie()
        assert buc.scadere_produs() == data

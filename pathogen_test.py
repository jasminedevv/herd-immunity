import pytest
from pathogen import Pathogen
import random
import io
import sys

def test_print_pathogen_info():
    ebola = Pathogen("ebola", 0.70, 0.25)
    ebola_greeting = ebola.print_info(False)
    assert "ebola" in ebola_greeting
    assert "70" in ebola_greeting
    assert "25" in ebola_greeting
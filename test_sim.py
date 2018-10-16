import pytest
from pathogen import Pathogen
from population import Population
import random
import io
import sys

def test_print_pathogen_info():
    ebola = Pathogen("ebola", 0.70, 0.25)
    ebola_greeting = ebola.print_info(False)
    assert "ebola" in ebola_greeting
    assert "70" in ebola_greeting
    assert "25" in ebola_greeting

virus = Pathogen("the black plague", 0.5, 0.5)
my_pop = Population("1437 France", 30, virus, 3, 0.5)

def test_bury_the_dead():
    # should remove dead person from world of the living and add them to world of the dead
    virus.mortality_rate = 1.0
    my_pop.the_living[2].infection = virus
    assert my_pop.the_living[2].did_die()

    
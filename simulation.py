from pathogen import Pathogen
from population import Population, Person
import sys

# helper class handles IO
class Simulation(object):
    def __init__(self):
        self.pathogen = Pathogen()
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)
    # ERROR HANDLING
    # this function is called if the user inputs something incorrectly
    def user_error(self):
        print("This simulation can be run directly from the command line using the following format:\n python3 simulation.py <population size> <vaccination percentage> <pathogen name> <mortality rate> <infectiousness> <initial infected population>. It can also run interactively. Just type python3 simulation.py.\n")
        # TODO: make it so you don't have to start from scratch if you make one mistake
        self.get_user_input(user_messed_up=True)

    # makes sure all the variables are the correct types and sizes
    def sanitize_input(self, population_size, vaccination_percentage, pathogen_name, mortality_rate, infectiousness, initial_infected):
        # POPULATION SIZE
        if not isinstance(population_size, int):
            print("Population size needs to be an int.\n")
          self.user_error()
        # VACCINATION PERCENTAGE
        if not isinstance(vaccination_percentage, float) or vaccination_percentage > 1:
            print("Vaccination percentage needs to be a float equal to or less than 1.\n")
            self.user_error()
        # PATHOGEN NAME
        if not isinstance(pathogen_name, str):
            print("Pathogen name needs to be a string.\n")
            self.user_error()
        # MORTALITY RATE
        if not isinstance(mortality_rate, float) or mortality_rate > 1:
            print("Mortality rate needs to be a float equal to or less than 1.\n")
            self.user_error()
        # INFECTIOUSNESS
        if not isinstance(infectiousness, float) or infectiousness > 1:
            print("infectiousness needs to be a float equal to or less than 1.\n")
            self.user_error()
        # INITIAL INFECTED
        if not isinstance(initial_infected, float) or initial_infected > 1:
            print("Number of people initially infected needs to be a float equal to or less than 1.\n")
            self.user_error()
            
    def get_user_input(self, user_messed_up=False):
        if len(sys.argv) < 1 or user_messed_up:
            population_size = input("Enter a population size > ")
            vaccination_percentage = input("What percentage of people in this population are vaccinated? > ")
            pathogen_name = input("What is this pathogen called? > ")
            mortality_rate = input("What is this pathogen's mortality rate? > ")
            infectiousness = input("How infectious is it? > ")
            initial_infected = input("How many people are initially infected?")
        else:
            population_size = sys.argv[1]
            vaccination_percentage = sys.argv[2]
            pathogen_name = sys.argv[3]
            mortality_rate = sys.argv[4]
            infectiousness = sys.argv[5]
            initial_infected = sys.argv[6]
        self.sanitize_input(population_size, vaccination_percentage, pathogen_name, mortality_rate, infectiousness, initial_infected)
        self.population_size = population_size
        self.vaccination_percentage = self.vaccination_percentage
        self.pathogen_name = pathogen_name
        self.mortality_rate = mortality_rate
        self.infectiousness = infectiousness
        initial_infected = initial_infected

def test():

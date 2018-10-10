from pathogen import Pathogen
from population import Population, Person
import sys
import os

# helper class handles IO
class Simulation(object):
    def __init__(self):
        self.pathogen = None
        self.population = None
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(self.pathogen.name, self.population.size, self.population.percent_vaccinated, self.population.initial_infected) 
    # ERROR HANDLING
    # this function is called if the user inputs something incorrectly
    def user_error(self):
        print("This simulation can be run directly from the command line using the following format:\n python3 simulation.py <population size> <vaccination percentage> <pathogen name> <mortality rate> <infectiousness> <initial infected population>. It can also run interactively. Just type python3 simulation.py.\n")
        # TODO: make it so you don't have to start from scratch if you make one mistake
        self.get_user_input(user_messed_up=True)

    # makes sure all the variables are the correct types and sizes
    # this function is currently not very useful
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
        if not isinstance(initial_infected, int) or initial_infected < 0:
            print("Number of people initially infected needs to be a postive int.\n")
            self.user_error()

    # broken af     
    def get_user_input(self, user_messed_up=False):
        print(len(sys.argv))
        if len(sys.argv) is not 7 or user_messed_up:
            population_size = int( input("Enter a population size > ") )
            print(population_size)
            percent_vaccinated = float( input("What percentage of people in this population are vaccinated? > ") )
            pathogen_name = str( input("What is this pathogen called? > ") )
            mortality_rate = float( input("What is this pathogen's mortality rate? > ") )
            infectiousness = float( input("How infectious is it? > ") )
            initial_infected = int( input("How many people are initially infected?") )
            print(initial_infected)
        else:
            population_size = int( sys.argv[1] )
            percent_vaccinated = float( sys.argv[2] )
            pathogen_name = sys.argv[3]
            mortality_rate = float( sys.argv[4] )
            infectiousness = float( sys.argv[5] )
            initial_infected = int( sys.argv[6] )

        print("\n\nUser input acquired.\n\n")
        # this function currently is useless
        self.sanitize_input(population_size, percent_vaccinated, pathogen_name, mortality_rate, infectiousness, initial_infected)
        # TODO clean this up a little
        self.population_size = population_size
        self.percent_vaccinated = percent_vaccinated
        self.pathogen_name = pathogen_name
        self.mortality_rate = mortality_rate
        self.infectiousness = infectiousness
        self.initial_infected = initial_infected
    
    def initialize(self):
        # create the pathogen
        self.pathogen = Pathogen(self.pathogen_name, self.mortality_rate, self.infectiousness)
        # create the population
        # leaving out name for the user generated stuff
        self.population = Population(name="Simulated Population", people=self.population_size, pathogen=self.pathogen, initial_infected=self.initial_infected, percent_vaccinated=self.percent_vaccinated)

    
    def run(self, time_steps):
        for i in range(0, time_steps):
            self.population.mingle(100, self.pathogen)


def test():
    sim = Simulation()
    # python3 simulation.py 100 0.1 "laughing too hard" 0.4 0.6 5
    # manually init
    # sim.pathogen_name = "Ebola"
    # sim.mortality_rate = 0.2
    # sim.infectiousness = 0.7
    # sim.population_size = 1000
    # sim.initial_infected = 2
    # sim.percent_vaccinated = 0.2

    sim.get_user_input()
    # ^ broken ^
    sim.initialize()
    sim.run(2)


test()
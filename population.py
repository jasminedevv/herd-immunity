from pathogen import Pathogen
import random
random.seed(42)

names = "Alice, Bob, Charlie, Donna, Elizabeth, Fred"

names = names.split(",")

class Person(object):
    def __init__(self, is_vaccinated=False, infection=None):
        # TODO: turn the infection var into a dictionary of pathogens with whether or not the person is vaccinated to them
        self.id = id
        self.name = random.choice(names)
        # should be None of a pathogen object
        self.infection = infection
        self.is_vaccinated = is_vaccinated
        self.is_dead = False
    # decides if a person 
    def print_greeting(self):
        print("Hello! My name is", self.name)
        if self.is_vaccinated:
            print("I am vaccinated.")
        else:
            print("I am not vaccinated.")
        if self.infection is None:
            print("Currently, I am not infected with anything.")
        else:
            print("Currently I am infected with", self.infection.name)
    def did_die(self):
        if not isinstance(self.infection, Pathogen):
            print(self.name, "was vaccinated and did not die.\n")
            return False
        elif self.is_vaccinated:
            print("ALERT! did_die method was called on a vaccinated person. That shouldn't happen.")
            return False
        else:
            luck = random.uniform(0, 1)
            if luck > self.infection.mortality_rate:
                print(self.name, "survives the infection!")
                # person survives the infection
                return False
            else:
                # person dies
                print(self.name, "has died of", self.infection.name, ". Please vaccinate your kids.")
                self.is_dead = True
                return True
    
    def get_infected(self, pathogen):
        print(self.name, "has been exposed to", pathogen.name, "!")
        if self.is_vaccinated:
            print("But they are vaccinated so they do not contract it.")
            # vaccinated people do not get infected
            return False
        else:
            luck = random.uniform(0, 1)
            if luck > pathogen.contagiousness:
                print("They fight off the infection and do not contract it.")
                # person does not catch the infection
                return False
            else:
                # person catches the infection
                print("And they catch it!", self.name, "is now infected with", pathogen.name)
                self.infection = pathogen
                return True

class Population(object):
    def __init__(self, name, people, pathogen, initial_infected, percent_vaccinated=0.0):
        self.name = name
        self.percent_vaccinated = percent_vaccinated
        self.people = []
        vaccinated_people_num = int( people * percent_vaccinated)
        # initialize patient zeroes
        print(vaccinated_people_num)
        for i in range(0, initial_infected):
            self.people += [Person(False, infection=pathogen)]
        # initialize number of vaccinated peeps
        # TODO: people are not being properly vaccinated. THIS IS A LOGIC PROBLEM
        for i in range(0, vaccinated_people_num):
            self.people += [Person(True, infection=None)]
        # add everyone else to the population
        for i in range(0, (people - (vaccinated_people_num + initial_infected))):
            self.people += [Person(False, infection=None)]

    def get_number_infected(self):
        people_infected = 0
        for person in self.people:
            if person.infection is not None:
                people_infected +=1
        return people_infected

    def get_number_dead(self):
        dead = 0
        for person in self.people:
            if person.is_dead:
                dead +=1
        return dead

    def mingle(self, interactions, pathogen):
        # interactions defines how sociable people in this population are
        for person in self.people:
            for i in range(0, interactions):
                friend = random.choice(self.people)
                # TODO adapt this for multiple pathogens
                if friend.infection is not None:
                        person.get_infected(pathogen)

    def print_info(self):
        population_num = str( len(self.people) )
        infected_num = str( self.get_number_infected() )
        dead_num = str( self.get_number_dead() )
        vaccination_rate = str( int( self.percent_vaccinated * 100 ) ) + "%"
        
        print("This population is known as", self.name, ". \n", vaccination_rate, "of the humans in this population are vaccinated.")

        print("Out of " + population_num + " people, " + infected_num, "are infected and " + dead_num + " have died.")

def test():
    # Population(self, name, people, pathogen, initial_infected, percent_vaccinated=0.0)
    stale_memes = Pathogen("pathogen1", 0.0, 0.0)
    dank_memes = Pathogen("pathogen2", 1.0, 1.0)
    # person1 = Person()
    # person1.print_greeting()
    # person1.get_infected(stale_memes)
    # person1.get_infected(dank_memes)
    # person1.print_greeting()
    # person1.did_die()
    # print("above human should have died\n")
    # person2 = Person()
    # person2.is_vaccinated = True
    # person2.get_infected(stale_memes)
    # person2.get_infected(dank_memes)
    # person2.did_die()
    make_school = Population("Make School", 20, dank_memes, 2, 0.5)
    make_school.print_info()
    make_school.mingle(2, dank_memes)
    make_school.print_info()

test()



from pathogen import Pathogen
import random
random.seed(42)

# here temporarily until I finish the mvp
names = "Alice, Bob, Charlie, Donna, Elizabeth, Fred"

names = names.split(",")

class Person(object):
    def __init__(self, id, is_vaccinated=False, infection=None):
        # TODO: turn the infection var into a dictionary of pathogens with whether or not the person is vaccinated to them
        self.id = id
        self.name = random.choice(names)
        # should be None of a pathogen object
        self.infection = infection
        self.is_vaccinated = is_vaccinated
        self.is_dead = False
    # decides if a person 
    def print_greeting(self):
        print("Hello! My name is", self.name, "(human #", self.id,")")
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
            print(self.name, "(human #", self.id,") was vaccinated and did not die.\n")
            return False
        elif self.is_vaccinated:
            print("ALERT! did_die method was called on a vaccinated person. That shouldn't happen.")
            return False
        else:
            luck = random.uniform(0, 1)
            if luck > self.infection.mortality_rate:
                print(self.name, "survives the infection!")
                # person survives the infection and stops being sick, they are now immune to the virus
                self.infection = None
                # could say if pathogen is a virus they become vaccinated
                self.is_vaccinated = True
                return False
            else:
                # person dies
                # add id after name
                print(self.name, "(human #", self.id, ") has died of", self.infection.name)
                self.is_dead = True
                return True
    
    def get_infected(self, pathogen):
        print(self.name, "(human #", self.id,") has been exposed to", pathogen.name, "!")
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
        self.size = people
        self.initial_infected = initial_infected
        self.name = name
        self.percent_vaccinated = percent_vaccinated
        self.the_living = []
        self.the_dead = []
        vaccinated_people_num = int( people * percent_vaccinated)
        # initialize patient zeroes
        print(vaccinated_people_num)
        id = 0
        for i in range(0, initial_infected):
            self.the_living += [Person(id, False, infection=pathogen)]
            id += 1
        # initialize number of vaccinated peeps
        for i in range(0, vaccinated_people_num):
            self.the_living += [Person(id, True, infection=None)]
            id += 1
        # add everyone else to the population
        for i in range(0, (people - (vaccinated_people_num + initial_infected))):
            self.the_living += [Person(id, False, infection=None)]
            id += 1

    def get_number_infected(self):
        people_infected = 0
        for person in self.the_living:
            if person.infection is not None:
                people_infected +=1
        return people_infected

    def mingle(self, interactions, pathogen):
        # interactions defines how sociable people in this population are
        # each person interacts with a number of friends equal to interactions
        for person in self.the_living:
            for i in range(0, interactions):
                friend = random.choice(self.the_living)
                # TODO adapt this for multiple pathogens
                if friend.infection is not None:
                        person.get_infected(friend.infection)

    def battle_infection(self):
        print("\nThe infected are battling the infection!\n")
        for person in self.the_living:
            if person.infection is not None and not person.is_vaccinated:
                if person.did_die():
                    self.the_living.remove(person)
                    self.the_dead.append(person)


    def print_info(self):
        population_num = str( len(self.the_living) + len(self.the_dead) )
        infected_num = str( self.get_number_infected() )
        dead_num = str( len(self.the_dead) )
        vaccination_rate = str( int( self.percent_vaccinated * 100 ) ) + "%"
        
        print("This population is known as", self.name, ". \n", vaccination_rate, "of the humans in this population are vaccinated.")

        print("Out of " + population_num + " people, " + infected_num, "are infected and " + dead_num + " have died.")

def test():
    # Population(self, name, people, pathogen, initial_infected, percent_vaccinated=0.0)
    virus = Pathogen("the gay agenda", 0.5, 0.5)
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
    make_school = Population("Make School", 30, virus, 3, 0.5)
    make_school.print_info()
    make_school.mingle(2, virus)
    make_school.battle_infection()
    make_school.print_info()

test()



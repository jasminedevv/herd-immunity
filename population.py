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
    def __init__(self, name, people, percent_vaccinated=0.0, pathogen, initial_infected):
        self.name = name
        self.percent_vaccinated = percent_vaccinated
        self.people = []
        for range(0, initial_infected):
            self.people += Person(False, infection=pathogen)
        vaccinated_people_num = initial_infected * percent_vaccinated
        for range(0, vaccinated_people_num)):
            self.people += Person(True, infection=None)
        for range(0 (people - (vaccinated_people_num + initial_infected))):
            self.people += Person(False, infection=None)

    def number_infected(self):
        people_infected = 0
        for person in self.people:
            if self.infection not None:
                people_infected +=1
        return people_infected

    def number_dead()
        dead = 0
        for person in self.people:
            if self.is_dead:
                dead +=1
        return dead

    def print_info(self):
        vaccination_rate = str( int( self.percent_vaccinated * 100 ) ) + "%"
        
        print("This population is known as", self.name, ". \n", vaccination_rate, "of the humans in this population are vaccinated."

        print("There") 
        )

def test():
    stale_memes = Pathogen("stale memes", 0.0, 0.0)
    dank_memes = Pathogen("dank memes", 1.0, 1.0)
    person1 = Person()
    person1.print_greeting()
    person1.get_infected(stale_memes)
    person1.get_infected(dank_memes)
    person1.print_greeting()
    person1.did_die()
    print("above human should have died\n")
    person2 = Person()
    person2.is_vaccinated = True
    person2.get_infected(stale_memes)
    person2.get_infected(dank_memes)
    person2.did_die()
    make_school = Population("Make School", 100, 0.5)
    make_school.print_info()

test()



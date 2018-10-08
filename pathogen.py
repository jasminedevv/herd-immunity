# import stuff


class Pathogen:
    def __init__(self, name, mortality_rate, contagiousness):
        # asserts here for sanity
        # TODO: sanitize these somewhere else
        assert isinstance(name, str)
        assert isinstance(mortality_rate, float)
        assert isinstance(contagiousness, float)
        self.name = name
        self.mortality_rate = mortality_rate
        self.contagiousness = contagiousness
    def print_info(self, do_print=True):
        # pass in False if you just want the string
        # make our floats pretty
        kill_rate = str( int( self.mortality_rate * 100 ) ) + "%"
        contagion_rate = str( int( self.contagiousness * 100 ) ) + "%"
        # format pathogen greeting
        pathogen_info = "Hello! My name is " + self.name + ".\nI infect " + contagion_rate + " of the people I come into contact with and will kill about " + kill_rate + " of the people I infect."
        if do_print:
            print(pathogen_info)
        return pathogen_info
    
def test():
    ebola = Pathogen("ebola", 0.70, 0.25)
    ebola.print_info()

test()



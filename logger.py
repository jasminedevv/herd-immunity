from jinja2 import Template, Environment, FileSystemLoader

# messy and idk how any of this works but I am DETERMINED to add templating gdi
def float_to_percent(my_float):
    return str( int(my_float * 100) ) + "%"

env = Environment(loader=FileSystemLoader(searchpath="."), trim_blocks=True, lstrip_blocks=True)

env.filters["to_percent"] = float_to_percent

# keeps track of interactions and writes a summary to a jinja template
class Logger(object):
    def __init__(self):
        self.custom = ["","",""]
        self.file_name = "NO_FILE_SPECIFIED.md"
        # not sure I need to init anything
        # might actually put these in Simulation instead

    def add_file_name(self, sim):
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.md".format(sim.pathogen.name, sim.population.size, sim.population.percent_vaccinated, sim.population.initial_infected) 

    def write_start_stats(self, sim):
        # code quality going down the drain
        self.custom[0] = float_to_percent(sim.percent_vaccinated)
        self.custom[1] = float_to_percent(sim.pathogen.mortality_rate)
        self.custom[2] = float_to_percent(sim.pathogen.contagiousness)
        t = open("start_stats.md", 'r').read()
        template = Template(t)
        summary = template.render(population=sim.population, pathogen=sim.pathogen, c = self.custom)
        file = open("logs/" + self.file_name, "w+")
        file.write(summary)
        file.close()

    def write_end_stats(self, sim):
        t = open("end_stats.md", 'r').read()
        template = Template(t)
        dead = len(sim.population.the_dead)
        summary = template.render(population=sim.population, pathogen=sim.pathogen, dead=dead)
        file = open("logs/" + self.file_name, "a")
        file.write(summary)
        file.close()

    def log_line(self, line):
        file = open("logs/" + self.file_name, "a")
        file.write(line)
        file.close()

    def log(self, sim, id):
        file_name = "logs/{}_simulation_pop_{}_vp_{}_infected_{}.md".format(sim.pathogen.name, sim.population.size, sim.population.percent_vaccinated, sim.population.initial_infected) 
        file = open(file_name, "a")

        infected = sim.population.get_number_infected()
        dead = len(sim.population.the_dead)
        now_immune = sim.population.get_number_immune()

        info = "\n{}: {} infected, {} dead, {} now immune".format(id, infected, dead, now_immune)

        file.write(info)

        file.close()

logger = Logger()


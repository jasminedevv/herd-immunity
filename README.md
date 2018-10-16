### Instructions
This simulation can be run directly from the command line using the following format:
```python
python3 simulation.py <population size> <vaccination percentage> <pathogen name> <mortality rate> <infectiousness> <initial infected population>. 
```
It should work without dependencies but just in case, try this if you get an error:
```python
virtualenv env
```
```python
. env/bin/activate
```
```python
pip install -r requirements.txt
```
Try it with these parameters from the command line:
```python
python3 simulation.py 100 0.1 "laughing too hard" 0.4 0.6 5
```

## State of the project:
### Example Summary
``` python
## Herd Immunity Simulation:
### Starting Stats
Population Size: 1000
Vaccination Percentage: 10%
Virus Name: laughing too hard
Mortality Rate: 40%
Basic Reproduction Number: 60%
People Initially Infected: 5
### Post-Infection Population Stats:
People who died: 364
People who survived the infection: 636
Steps to pathogen burnout: 3
```
### Example Log
```python
Donna, human#0 has exposed  Sarah, human#638 to laughing too hard!
 Sarah, human#638 did not become infected.
 Donna, human#0 has exposed  Leroy, human#665 to laughing too hard!
 Leroy, human#665 has contracted laughing too hard!
...81633 lines later
 Nick, human#994 did not die because they were immune.
 Irene, human#998 survives the infection!
 Katie, human#999 did not die because they were immune.
5: 613 infected, 364 dead, 636 now immune
```

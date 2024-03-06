from model import BangladeshModel
# dont forget to import what you need here
from components import Infra
from components import Bridge
from components import Vehicle

"""
    When you run this file it will run the simulation ONLY in the terminal
    The output gets printed out at terminal window below
        This is usefull when wanting to test out instanced classes 
        as well as class functions. 
    To do this:
    place the statements you want to be executed after the model is simulated
    on the bottom of this file, in the order you want them to be executed.
        Most Ideally when you're putting a lot of statements at the bottom no one else is
        going to use you delete them when you're finished when PUSHING to main.
            Or when you want to keep the test and work on them later again, 
            just make a side branch with the name of the thing you were doing like:
            'fixing_datareader_with_test' for example.
                Dont Forget To Import The File and Component/class or function you want to test!
                    When you're finished with a bigger chunk of code use
                    pytest or let pycharm create a file with tests for you.
"""

# ---------------------------------------------------------------

# run time 5 x 24 hours; 1 tick 1 minute
# run_length = 5 * 24 * 60

# # example run time
# # run time 1000 ticks
run_length = 1000

seed = 1234567
# seeds = [0000000, 1111111, 2222222, 3333333, 4444444, 5555555, 6666666, 7777777, 8888888, 9999999]


# This is the name of the model that is beinig created
sim_model = BangladeshModel(seed=seed)

# Check if the seed is set
print("SEED " + str(sim_model._seed))

# One run with given steps
for i in range(run_length):
    print(f' tick = {i}')
    sim_model.step()

# # Place HERE you're executable statements after simulating...
# print(f'Hi everyone this the first test of the main project :D')
#
# # Example
# # def __str__(self):
# #     return "Vehicle" + str(self.unique_id) + \" +"
# # de bovenstaande code staat in de de components file, tijdens het runnen van de simulatie worden deze lines
# # geprint en de unique id's zijn de getallen direct achter VehicleTruck'unique_id' + etc.
#
# klas = Infra(1, sim_model)
# print(klas.name)
# # this prints Unkown_Fred at the end in terminal which is standard for an Infra object
# # which I editted in the components file as example for you to find where I did what
# # because I the attributes of the agents are not being assigned
# print(klas.unique_id)
# print(klas.road_name)
#
# # test van een brug
# # maak eerst een instantie van een brug
# brug = Bridge(klas, sim_model)
# print(brug.get_delay_time)
#
# # # Vehicle kreeg ik niet geprint omdat er een argument 'generated_by' meegegeven moet worden
# # # als ik een getal invul krijg ik deze: AttributeError: 'int' object has no attribute 'pos'
# # # pos als in positie?
# # car = Vehicle(1, sim_model,0)

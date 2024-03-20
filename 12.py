from flaker import Faker
from random import choise

fake = Faker()

def create_angry_bird():

    bird_dict = {
        'name': fake.name(),
        'anger_level': choise( range(5,11) )
    }

    return bird_dict


print( create_angry_bird() )
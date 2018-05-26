max_x = 10
max_y = 10

class Person:                                                                                                       #Creates an instance of a person
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def find_nearby(self):                                                                                    #Locates all other people adjacent
        offsets = [(0,1),(0,-1),(1,0),(-1,0)]                                                           #Offsets around to find people
        adjacent = [(self.x + dx, self.y + dy) for dx, dy in offsets]                       #locations which are adjacent
        #locations whch are adjacent - outMax bounds        
        adjacent = [
            (x,y) 
            for (x,y) in adjacent 
            if (x,y) < (max_x,max_y) and (x,y) >= (0,0)
        ]
        
        count_people = 0
        for (x,y) in adjacent:
            for people in everyone:
                if people.name and (people.x, people.y) == (x,y):                             #Finds if people match these locations
                    print people.name + ' is next to ' + self.name +'.'                         #If so then tell us who it is next to our person
                    count_people += 1 
                    
        if count_people == 0:                                                                                 #If there is no one, we say no one is next to us
            print 'No one is next to ' + self.name + '.'

male_one = Person(4,5,'John')                                                                           #Populating with people
male_two = Person(4,6,'David' )
male_three = Person(5,5,'Sam')
female_one = Person(2,3,'Jennifer')

everyone = [male_one,   male_two,   male_three,    female_one]                   #A list of everyone

get_name = lambda x: x.name                                                                          #Lambda function - returns name of Person

registry = []
for individual in everyone:                                                                                 #Creates a registry of everyone created
    add = (get_name(individual), individual)
    registry.append(add)
registry = dict(registry)                                                                                     #registry is made into dictionary, allows us to call person with their name



Person.find_nearby(registry['David'])

# there are 54 
class Corner():
    def __init__(self, index, adjacent_hexagons):
        self.index = index
        self.adjacent_hexagons = adjacent_hexagons
        self.adjacent_corners = []
        self.adjacent_edges = []
        self.building = ''
        self.owner = ''
    
    # Corner functions 

    # build a town in a free corner
    def new_town(self, player):
        self.building = 'town'
        # set an owner of the corner 
        self.owner = player
        # add as contruction to each hexagons containing the corner to facilitate the resource reward
        for hexagon in self.adjacent_hexagons:
            hexagon.constructions.append(self)
        print(f"You have succesfully created a town in {self.index} and have dropped {self.adjacent_corners.index}")


    # upgrade a building from town to city
    def new_city(self, player):
        self.building = 'city'
        print("You have upgraded your town in the corner ", self.index, " into a city")


# There are 72 edges
class Edge():

    def __init__(self, index, end_points):
        self.index = index
        self.end_points = end_points
        self.busy = False
        self.owner = ''
        self.assign_adjacents(end_points)

    def assign_adjacents(self, endpoints):
        if endpoints[1] not in endpoints[0].adjacent_corners:
            endpoints[0].adjacent_corners.append(endpoints[1])
        if endpoints[0] not in endpoints[1].adjacent_corners:
            endpoints[1].adjacent_corners.append(endpoints[0])

    
    # Creates a bridge in the edge making the current player the owner
    def new_bridge(self, player):

        if self.busy == False:
            self.busy = True
            self.owner = player
            print("You have created a new bridge in edge ", self.index)
        else:
            #the edge already has an owner 
            print("You can't bridge in edge ", self.index)
            None


# There are 19 hexagons
class Hexagon():

    def __init__(self, index, value, resource):

        self.index = index
        # should write a constraint for both value and resource 
        self.value = value
        self.resource = resource
        self.constructions = []
        self.thief = False

    def give_resource(self):
        # if thief is in hexagon don't give resource
        if not self.thief:
            # depending on the construction give 1 or 2 of the reward 
            for construction in self.constructions:
                if construction.building == "town":
                    construction.owner.owned_resources[self.resource] += 1
                    print(f"1 {self.resource} were given to {construction.owner.color}")
                elif construction.building == "city": 
                    construction.owner.owned_resources[self.resource] += 2
                    print(f"2 {self.resource} were given to {construction.owner.color}")
        else:
            print("No resources were given bc the thief is in the hexagon")




class Port():

    def __init__(self, index, corner, resource, type):
        self.index = index
        self.corner = corner
        self.resource = resource
        self.type = type

    def commerce_fixed_port(self, material, player):
        # should exchange 2 elements of the same kind for 1 they want 
        if self.type == 'fixed':
            if player.owned_resources[self.resource] >= 2:
                player.owned_resources[self.resource] -= 2
                player.owned_resources[material] +=1
            else: 
                print("You dont hae enough resources")
        else: 
            print("not the correct method for this port")

    def commerce_choice_port(self, material, player, choice):
        # should exchange 2 elements of the same kind for 1 they want 
        if self.type == 'choice':
            if player.owned_resources[choice] >= 3:
                player.owned_resources[choice] -= 3
                player.owned_resources[material] +=1
            else: 
                print("You dont hae enough resources")
        else: 
            print("not the correct method for this port")



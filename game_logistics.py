from test_map import create_test_map
import random

class Game:
    # start the game 
    # able to make action 
    # initilaise the map 
    def __init__(self) :
        self.hexagon_list, self.corner_list, self.edge_list = create_test_map()
        self.global_available_corner_list = self.corner_list[:]
        self.global_available_edge_list = self.edge_list[:]
        self.player_list = []
        self.town_list = []
        self.biggest_army = (2, None)
        self.biggest_route = (4, None)

    # create n players at the beginning of the game 
    def create_players(self):
        player_list = []
        # user inputs how many players
        number_players = 0
        colors = ['orange', 'red', 'blue', 'yellow', 'pink', 'green']

        while True:
            number_players = input("How many players are in the game? (2-6)")
            #check that its an integer
            try:
                integer_value = int(number_players)
                if 2 <= integer_value <= 6:
                    break  # Exit the loop when an integer is entered
                elif integer_value < 2:
                    print(f"{integer_value} is smaller than 2.")
                else:
                    print(f"{integer_value} is bigger than 6.")
            except ValueError:
                print(f"{number_players} is not an integer. Please try again.")

        # create n players
        for i in range(int(number_players)):
            player = Player(colors[0])
            #assign them a color
            colors.pop(0)
            self.player_list.append(player)

        return player_list

    # helper function to find an element's index in a list 
    def find_item(self, name_to_find, corners):
        for corner in corners:
            if corner.index == name_to_find:
                return corner  # Return the corner object if found
        return None
    
    # simulate dice throw 
    def throw_dice(self, player):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print("First dice is ", dice_1, ", second dice is", dice_2)
        if dice_1+dice_2 == 7:
            self.move_thief(player)
        else:
            self.give_resource(dice_1+dice_2)

    # when dice result = 7 move the thief, player choses new location, prevents player from getting resource
    def move_thief(self, player):

        previous_hexagon = ''
        for hexagon in self.hexagon_list:
            if hexagon.thief:
                hexagon.thief = False 
                previous_hexagon = hexagon.index

        while True:
            new_location = input("Which hexagon do you want to put the thief? ")
            new_hexagon = self.find_item(new_location, self.hexagon_list)
            if previous_hexagon == new_location:
                print(f"The thief was already in that location")
            elif new_hexagon != None: 
                new_hexagon = self.find_item(new_location, self.hexagon_list)
                new_hexagon.thief = True
                possible_players = []
                for construction in new_hexagon.constructions:
                    if construction.owner not in possible_players:
                        possible_players.append(construction.owner)
                print(f"correctly coved the thief to hexagon {new_hexagon.index}")
                # steal()
                break
            else:
                print("That is not a valid hexagon")

    def steal():
        return True

    # dice matches hexagon number, give player 1 of that resource
    def give_resource(self, dice_value):
        # check if any hexagon has the value and gives reward to the player(s)
        for hexagon in self.hexagon_list:
            if hexagon.value == dice_value:
                hexagon.give_resource()

    # build town in a corner
    def build_town(self, corner_name, player):
        # Check if the corner exists
        corner = self.find_item(corner_name, self.corner_list)
        if corner is None:
            print("Corner doesn't exist")
            return False

        # Check if the corner contains a town
        if corner in self.town_list:
            print(f"There is already a town in {corner.index}")
            return False

        # Check if the corner is available
        if corner not in player.accessible_corners:
            print("Corner is unavailable")
            return False

        # Check if the player has enough resources
        required_resources = ["wood", "brick", "wool", "hay"]
        for resource in required_resources:
            if player.owned_resources[resource] < 1:
                print(f"You don't have enough {resource} for a town")
                return False

        # If all checks pass, proceed to build the town
        for resource in required_resources:
            player.owned_resources[resource] -= 1

        # creates new town
        corner.new_town(player)
        # player owns the the town and the corner
        self.town_list.append(corner)

        # Update the map and player's stats
        self.update_availability_after_building_town(corner)
        player.towns_owned += 1

        # Return True if the player won the game (if the victory condition is met)
        return player.update_progress()

    # updates availability after building town 
    def update_availability_after_building_town(self, corner):
        # Remove the corner from the available corner list
        self.global_available_corner_list.remove(corner)
        # Remove the corner from every players accessible corners list
        self.delete_accessible_corner(corner)

        # Remove adjacent corners from the available corner list
        for adjacent_corner in corner.adjacent_corners:
            self.global_available_corner_list.remove(adjacent_corner)
            # remove adjacent corners from every player's accessible corners list 
            self.delete_accessible_corner(adjacent_corner)

    # build a city where previously exists a town 
    def build_city(self, corner_name, player):
        # Check if the corner exists
        corner = self.find_item(corner_name, self.corner_list)
        if corner is None:
            print("Corner doesn't exist")
            return False

        # Check if there's a town in the corner
        town = self.find_item(corner_name, self.town_list)
        if town is None:
            print("There is no town in this location")
            return False

        # Check if the player owns the town
        if town.owner != player:
            print(f"The corner belongs to {town.owner.color}")
            return False

        # Check if the town is a valid town (not already a city)
        if town.building != "town":
            print("You already have a city in this corner")
            return False

        # Check if the player has enough resources
        if player.owned_resources["rock"] < 3 or player.owned_resources["hay"] < 2:
            print("You don't have enough resources for a city")
            return False

        # If all checks pass, proceed to build the city
        # Player loses those resources
        player.owned_resources["rock"] -= 3
        player.owned_resources["hay"] -= 2

        # Creates the new city
        town.new_city(player)
        # Player owns 1 city more and updates its progress
        player.cities_owned += 1
        player.towns_owned -= 1

        # Return True if the player won the game (if the victory condition is met)
        return player.update_progress()

    # build a bridge in an edge
    def build_bridge(self, edge, player):
        if edge not in self.edge_list:
            print("Edge doesn't exist.")
            return False

        if edge not in player.accessible_edges:
            print("Edge is not available to you.")
            return False
        
        if player.owned_resources["wood"] < 1 or player.owned_resources["brick"] < 1:
            print("you don't have enough resources for a bridge.")
            return False

        
        # player loses those resources
        player.owned_resources["wood"] -= 1
        player.owned_resources["brick"] -= 1
        # create a bridge in the edge
        edge.new_bridge(player)
        self.calculate_biggest_route(player)

        #update the available lists of the player
        self.update_availability_after_building_edge(player, edge)

        # returns True is player won the game 
        return player.update_progress()

    def update_availability_after_building_edge(self, player, edge):
        # Remove the edge from the available corner list
        self.global_available_edge_list.remove(edge)
        # Remove the edge from every players accessible corners list
        self.delete_accessible_edge(edge)

        # Add available corners and edges
        self.add_accessible_corner(player, edge)


    def buy_development_card(self, player):
        # Define the resource costs
        resource_costs = {"rock": 1, "wool": 1, "hay": 1}

        # Check if the player has enough resources for a development card
        if all(player.owned_resources[resource] >= cost for resource, cost in resource_costs.items()):
            # Deduct the resource costs
            for resource, cost in resource_costs.items():
                player.owned_resources[resource] -= cost

            # Get a random development card
            random_number = random.random()
            if random_number <= 0.33:
                card_type = "knight"
            elif random_number <= 0.66:
                card_type = "victory point"
            else:
                card_type = "progress"

            # Increase the count of the acquired card and print a message
            player.development_cards[card_type] += 1
            print(f"Player {player.color} received a {card_type} card")
        else:
            print("You don't have enough resources for a development card")

    def use_developement_card(self, card, player):
        # only if player own that card
        if player.developement_cards[card] >= 1:
            if card == "knight":
                # moves the thief
                self.move_thief(player)
                # add 1 knight to the army
                player.army += 1
                # returns True is player won the game 
                print(f"Player {player.color} used a knight card")
                # calculate biggest army in case biggest army condition is raised
                self.calculate_biggest_army()
                return player.update_progress()
            elif card == "progress":
                print("not implemented feature yet")
                return False
            else:
                player.card_victory_points += 1
                print(f"Player {player.color} used a victory point card")
                return player.update_progress()
        else: 
            print("you dont have that type of card")
            return False
        
    def iniciate_game(self):
        for player in self.player_list:

            while True:
                first_town_location = input("Which corner do you want to put the town? ")
                town = self.find_item(first_town_location, self.corner_list)
                if town != None: 
                    self.build_town(town.index, player)
                    break
                else:
                    print("That is not a valid corner")
            
            while True:
                bridge_location = input("Which corner do you want to put the town? ")
                bridge = self.find_item(bridge_location, self.edge_list)
                if bridge != None: 
                    self.build_bridge(bridge.index, player)
                    break
                else:
                    print("That is not a valid edge")

        for player in self.player_list.reverse():

            while True:
                first_town_location = input("Which corner do you want to put the town? ")
                town = self.find_item(first_town_location, self.corner_list)
                if town != None: 
                    self.build_town(town.index, player)
                    break
                else:
                    print("That is not a valid corner")
            
            while True:
                bridge_location = input("Which corner do you want to put the town? ")
                bridge = self.find_item(bridge_location, self.edge_list)
                if bridge != None: 
                    self.build_bridge(bridge.index, player)
                    break
                else:
                    print("That is not a valid edge")


    def play(self):
        end = False
        player_turn = 0
        begin = True

        self.create_players()
        
        self.iniciate_game()

        # Define a command mapping
        command_mapping = {
            "buildTown": self.build_town,
            "buildBridge": self.build_bridge,
            "buildCity": self.build_city,
            "useCard": self.use_developement_card,
            # "tradePort": self.trade_port,
        }

        while not end:
            if begin:
                begin = False
                self.throw_dice(self.player_list[player_turn])

            command = input(f"{self.player_list[player_turn].color}, make an action: ")

            parts = command.split()
            if len(parts) > 0:
                action = parts[0]
                if action in command_mapping:
                    try:
                        end = command_mapping[action](parts[1], self.player_list[player_turn])
                    except:
                        print(f"Invalid or non-existing location")
                elif action == "end":
                    begin = True
                    player_turn = (player_turn + 1) % len(self.player_list)
                elif action =="buyCard":
                    self.buy_developement_card()
                else:
                    print("Command not recognized")

            # Any other command not starting with a recognized action
            else:
                print("Command not recognized")
    

    def calculate_biggest_army(self, player):
        if player.army > self.biggest_army[0]:
            if self.biggest_army[1] != None:
                self.biggest_army[1].biggest_army = False
            self.biggest_army[0] = player.army
            self.biggest_army[1] = player
            print(f"{self.biggest_army[1].color} has biggest army with {self.biggest_army[0]} knights")


    # def calculate_biggest_route(self, player):
    #     max_depth = 0
    #     if max_depth > self.biggest_route[0]:
    #         if self.biggest_route[1] != None:
    #             self.biggest_route[1].biggest_route = False
    #         self.biggest_route[0] = player.army
    #         self.biggest_route[1] = player
    #         print(f"{self.biggest_route[1].color} has biggest route with {self.biggest_route[0]} bridges")


    def delete_accessible_edge(self, edge):
        for player in self.player_list:
            if edge in player.accessible_edges:
                player.accessible_edges.remove(edge)


    def delete_accessible_corner(self, corner):
        for player in self.player_list:
            if corner in player.accessible_edges:
                player.accessible_corners.remove(corner)

    def add_accessible_corner(self, player, forbidden_edge):
        # Adds extremes of the edge into player accessible corners
        for endpoint in forbidden_edge.end_points:
            if endpoint not in player.accessible_corners:
                player.accessible_corners.add(endpoint)
                # gets the edges which have the rcently added corner as an endpoint and add them into available list 
                for edge in self.global_available_edge_list:
                    # checks it isn't already on the lisst 
                    if endpoint in edge.endpoints and edge != forbidden_edge:
                        player.accessible_edges.add(edge)

    def calculate_longest_route(self, player):
        max_length = 0  # Variable para realizar un seguimiento de la longitud máxima
        visited = set()  # Conjunto para realizar un seguimiento de las edges visitadas

        # Función de búsqueda de profundidad (DFS) para encontrar la ruta más larga
        def dfs(edge, length):
            nonlocal max_length  # Usamos nonlocal para acceder a max_length desde el ámbito exterior
            visited.add(edge)  # Marcamos esta edge como visitada
            max_length = max(max_length, length)  # Actualizamos la longitud máxima si es necesario

            for adjacent_edge in edge.end_points[1].adjacent_edges:
                # Recorremos todas las edges adyacentes a esta
                if adjacent_edge not in visited and adjacent_edge.owner == player:
                    # Si la edge adyacente no ha sido visitada y pertenece al jugador
                    dfs(adjacent_edge, length + 1)  # Llamamos recursivamente a DFS

        # Itera a través de todas las edges del jugador
        for edge in player.accessible_edges:
            if edge not in visited:
                # Si la edge no ha sido visitada, comenzamos una nueva búsqueda DFS desde esta edge
                dfs(edge, 1)  # La longitud inicial es 1 ya que estamos en la primera edge de la ruta

        return max_length 

                
    





class Player():
    def __init__(self, color):
        self.owned_resources = {
            "wood": 0,
            "brick": 0,
            "hay": 0,
            "wool": 0,
            "rock": 0
        }
        self.developement_cards = {
            "knight": 0,
            "victory point": 0,
            "progress": 0
        }
        self.color = color
        self.victory_points = 0
        self.card_victory_points = 0
        # nº bridges towns and cities
        self.edges_owned = []
        self.towns_owned = 0
        self.cities_owned = 0
        # number of knight cards used 
        self.army = 0
        self.biggest_army = False
        self.biggest_route = False
        self.accessible_corners = [] # update every time a town is created
        self.accessible_edges = [] # update every time an edge is created

        # self.accessible_edges -> update all edges 

    # calculate victory points
    def update_progress(self):
        self.victory_points = self.cities_owned * 2 + self.towns_owned + self.card_victory_points
        if self.biggest_army:
            self.victory_points += 3
        if self.longest_path:
            self.victory_points += 3
        print(f"{self.color} has {self.victory_points} victory points")
 
        if self.victory_points >= 10:
            return True
        else:
            return False
        
    def print_player(self):
        print(self.color)
        print(self.owned_resources)

    # pueblos solo se pueden construir 
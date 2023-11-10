from game_logistics import Game
from game_logistics import Player

game = Game()

# CREATE MASTER PLAYER #

player1 = Player('blue')

player1.owned_resources["wood"] = 20
player1.owned_resources["brick"] = 20
player1.owned_resources["wool"] = 20
player1.owned_resources["rock"] = 20
player1.owned_resources["hay"] = 20

player2 = Player('red')



### TEST CASES ###

# Build Town 

print("TOWN TESTS")

game.build_town('A1', player2)  # you don't have enough resources for a town
game.build_town('A1', player1)  # You have succesfully created a town in A1 and have dropped A2 AC  
                                # blue has 1 victory point
game.build_town('Z9', player1)  # Corner doesn't exist
game.build_town('A1', player1)  # There is already a town in A1

game.build_town('A2', player1)  # There is unavailable

# Build City

print("CITY TESTS")

player2.owned_resources["wood"] = 1
player2.owned_resources["brick"] = 1
player2.owned_resources["wool"] = 1
player2.owned_resources["hay"] = 1
player2.owned_resources["rock"] = 0

game.build_city('Z9', player1)  # Corner doesn't exist
game.build_city('A2', player1)  # There is not a town in this location !
game.build_city('A1', player2)  # The corner belongs to blue
game.build_town('C1', player2)  # You have succesfully created a town in C1 and have dropped ...
                                # red has 1 victory point
game.build_city('C1', player2)  # You don't have enough resources for a city
game.build_city('A1', player1)  # You have upgraded your town in the corner A1 into a city
                                # blue has 2 victory point
game.build_city('A1', player1)  # You already have a city in this corner

# Give Resource 

print("GIVE RESOURCE TESTS")

game.give_resource(5)   # 1 rock were given to red
                        # 2 rock were given to blue
game.hexagon_list[0].thief = True 
game.give_resource(5)   # No resources were given bc the thief is in the hexagon

# Create players

print("CREATE PLAYERS TESTS")

game.create_players()   # input 6

for player in game.player_list:
    print(player.color) # orange
                        # red
                        # blue
                        # yellow
                        # pink
                        # green

# Throw Dice

print("THROW DICE TESTS")

game.throw_dice(player1)


# Buy developement Card

print("BUY DEVELOPEMENT CARD TESTS")

game.buy_developement_card(player1)

# Use developement Card

print("USE DEVELOPEMENT CARD TESTS")

player1.developement_cards["knight"] += 1
player1.developement_cards["victory point"] +=1
player1.developement_cards["progress"] +=1

game.use_developement_card("knight", player1)           # Player blue used a knight card
                                                        # blue has 2 victory points
game.use_developement_card("victory point", player1)    # Player blue used a victory point card
                                                        # blue has 3 victory points
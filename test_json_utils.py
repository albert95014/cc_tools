import sys
import json
import test_data



#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    #Loop through the json_data
    for game_data in json_data["Games"]:

        #Create a new Game object from the json_data by reading
        game = test_data.Game()

        #  title
        game.title = game_data["title"]

        #  year
        game.year = game_data["year"]

        #  platform (which requires reading name and launch_year)
        for platform_data in game_data["platform"]:
            game.platform = test_data.Platform()
            game.platform.launch_year = game_data["platform"]["launch year"]
            game.platform.name = game_data["platform"]["name"]

        #Add that Game object to the game_library
        game_library.add_game(game)










        print("hello")


    #Return the completed game_library


    return game_library

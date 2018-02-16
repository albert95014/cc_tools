import json
import cc_dat_utils
import test_json_utils
import cc_data
import cc_json_utils

#Part 1
#Use cc_data_utils.make_cc_data_from_dat() to load pfgd_test.dat
#print the resulting data

print("hi")
print(cc_dat_utils.make_cc_data_from_dat("data/pfgd_test.dat"))



#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Below code returns json as a Python dictionary(?)
with open(input_json_file, "r") as reader:
    game_data = json.load(reader)
print(game_data)

#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
game_library_data = test_json_utils.make_game_library_from_json(game_data)

#Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py
print(game_library_data)
### End Add Code Here ###


#Part 3
#Load your custom JSON file
with open("data/albertya_cc1.json", "r") as reader:
    json_cc_data = json.load(reader)
#
# # #Convert JSON data to cc_data
cc_data_file = cc_json_utils.make_cc_data_file_from_json(json_cc_data)

# #Save converted data to DAT file
cc_dat_utils.write_cc_data_to_dat(cc_data_file, "data/albertya_cc1.dat")


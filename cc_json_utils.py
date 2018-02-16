import cc_data

def make_cc_data_file_from_json(json_data):

    cc_data_file = cc_data.CCDataFile()

    for json_level in json_data:
        cc_level = cc_data.CCLevel()
        cc_level.level_number = json_level["level_number"]
        cc_level.num_chips = json_level["num_chips"]
        cc_level.time = json_level["time"]
        cc_level.upper_layer = json_level["upper_layer"]
        cc_level.lower_layer = json_level["lower_layer"]

        #Handle optional fields
        json_fields = json_level["optional_fields"]
        for json_field in json_fields:
            field_type = json_field["type"]
            if (field_type == "title"):
                title = json_field["title"]
                cc_title_field = cc_data.CCMapTitleField(title)
                cc_level.add_field(cc_title_field)
                print(cc_title_field)
            elif (field_type == "hint"):
                hint = json_field["hint"]
                cc_hint_field = cc_data.CCMapHintField(hint)
                cc_level.add_field(cc_hint_field) #add_field is def in cc_data.py
                print(cc_hint_field)
            elif (field_type == "password"):
                password = json_field["password"]
                cc_password_field = cc_data.CCEncodedPasswordField(password)
                cc_level.add_field(cc_password_field)
                print(cc_password_field)
            elif (field_type == "monsters"):
                monster_coords = json_field["monsters"]

                #list to store monster coordinates
                cc_monster_coords = []

                #for loop to assign CCCoordinates (in the form of dict) to monster coordinates
                for monster_coord in monster_coords:
                    monster_x = monster_coord["x"]
                    monster_y = monster_coord["y"]
                    cc_monster_coords.append(cc_data.CCCoordinate(monster_x, monster_y))

                cc_monster_field = cc_data.CCMonsterMovementField(cc_monster_coords)
                cc_level.add_field(cc_monster_field)
                print(cc_monster_field)
            else:
                print("I have no idea what this is.")
            print(field_type)

        print(cc_level)

        cc_data_file.add_level(cc_level)

    return cc_data_file

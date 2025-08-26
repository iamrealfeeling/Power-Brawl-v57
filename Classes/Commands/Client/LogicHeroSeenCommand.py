from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler
from Classes.LogicUtility import LogicUtility

import json

class LogicHeroSeenCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        pass

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["BrawlerID"] = calling_instance.readDataReference()
        fields["State"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        Database = DatabaseHandler()
        playerData = Database.getPlayer(calling_instance.player.ID)
        
        v0 = LogicUtility.getDefaultBrawlerVanity(fields["BrawlerID"][1], None)
        if playerData["HeroData"][str(fields["BrawlerID"][1])]["CardID"] != 1:
        	if fields["BrawlerID"][1] == 0:
        		playerData["VanityData"]["Pins"].append({"ID": 151, "State": 0, "Slot": 0})
        		playerData["VanityData"]["Thumbnails"].append({"ID": 3, "State": 0, "Slot": 0})
        	else:
        		if playerData["HeroData"][str(fields["BrawlerID"][1])]["State"] == 0:
        			playerData["HeroData"][str(fields["BrawlerID"][1])]["State"] = 2
        			playerData["VanityData"]["Pins"].append({"ID": v0["Pin"], "State": 0, "Slot": 0})
        			playerData["VanityData"]["Thumbnails"].append({"ID": v0["Thumbnail"], "State": 0, "Slot": 0})
        			
        Database.updatePlayerData(playerData,calling_instance)
        	
    def getCommandType(self):
        return 522
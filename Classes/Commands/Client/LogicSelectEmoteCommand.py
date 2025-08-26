from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

import json

class LogicSelectEmoteCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        pass

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["EmoteID"] = calling_instance.readDataReference()
        fields["EmoteSlot"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        Database = DatabaseHandler()
        playerData = Database.getPlayer(calling_instance.player.ID)
        
        # might be a bit complicated, but nice
        if any(item["ID"] == fields["EmoteID"][1] for item in playerData["VanityData"]["Pins"]):
        	pin = next(pin for pin in playerData["VanityData"]["Pins"] if pin["ID"] == fields["EmoteID"][1])
        	pin["Slot"] = fields["EmoteSlot"]
        	pin["State"] = 1
        	
        	Database.updatePlayerData(playerData,calling_instance)
        	
    def getCommandType(self):
        return 538
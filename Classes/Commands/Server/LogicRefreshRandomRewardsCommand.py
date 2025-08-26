from Classes.Commands.LogicServerCommand import LogicServerCommand
from Database.DatabaseHandler import DatabaseHandler
from Classes.Commands.Client.LogicRandomRewardManager import LogicRandomRewardManager
import json

class LogicRefreshRandomRewardsCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        Database = DatabaseHandler()
        playerData = json.loads(Database.getPlayerEntry(fields["PlayerID"])[2])
        self.writeVInt(1)
        self.writeVInt(-1)
        self.writeVInt(-1)
        self.writeVLong(0, 1)
        self.writeVInt(1)
        
        if len(playerData["RandomRewardData"]) != 0:
        	v0 = True
        	v1 = playerData["RandomRewardData"][0]["Rarity"]
        else:
        	v0 = False
        	v1 = None
        	
        LogicRandomRewardManager.encode(self, {"RarityArray": [v0, v1], "GemOfferArray": v0})
        
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 228
from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler
from Classes.LogicUtility import LogicUtility

import json

class LogicSelectSkinCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["SkinID"] = calling_instance.readDataReference()
        fields["Unk"] = calling_instance.readVInt()
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        Database = DatabaseHandler()
        playerData = Database.getPlayer(calling_instance.player.ID)
        brawlerID = LogicUtility.getHeroIDBySkin(fields["SkinID"][1])
        print(brawlerID)
        playerData["HeroData"][f"{brawlerID}"]["SelectedSkin"] = fields["SkinID"][1]
        	
        Database.updatePlayerData(playerData, calling_instance)

    def getCommandType(self):
        return 506
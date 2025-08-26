from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

import json

class LogicSelectCharacterCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["BrawlerID"] = calling_instance.readDataReference()
        fields["BrawlerSlot"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        Database = DatabaseHandler()
        playerData = Database.getPlayer(calling_instance.player.ID)
        
        if playerData["OwnedBrawlers"][str(fields["BrawlerID"][1])]["CardID"] != 1:
        	playerData["SelectedBrawler"] = fields["BrawlerID"][1]
        	Database.updatePlayerData(playerData, calling_instance)

    def getCommandType(self):
        return 525
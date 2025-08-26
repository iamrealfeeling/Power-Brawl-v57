from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

class LogicSetPlayerThumbnailCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["Thumbnail"] = calling_instance.readDataReference()[1]
        
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        Database = DatabaseHandler()
        playerData = DatabaseHandler.getPlayer(calling_instance.player.ID)
        playerData["ProfileData"]["Thumbnail"] = fields["Thumbnail"]
        Database.updatePlayerData(playerData, calling_instance)

    def getCommandType(self):
        return 505
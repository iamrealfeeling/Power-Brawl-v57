from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Classes.Commands.Server.LogicStarrDropOpening import LogicStarrDropOpening
from Database.DatabaseHandler import DatabaseHandler

class LogicOpenRandomCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeVInt(0)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["v0"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        Database = DatabaseHandler()
        playerData = Database.getPlayer(calling_instance.player.ID)
        CommandManager__args = (calling_instance, fields, cryptoInit)
        if len(playerData["RandomRewardData"]) != 0:
        	LogicStarrDropOpening.giveRandomReward(*CommandManager__args)
        
        
        
    def getCommandType(self):
        return 571
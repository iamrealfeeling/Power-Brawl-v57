from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

import json

class LogicSetPlayerProfileVanityCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["Unk"] = calling_instance.readVInt()
        fields["CsvID"] = calling_instance.readVInt()
        fields["VanityID"] = calling_instance.readVInt()      
        fields["SlotID"] = calling_instance.readVInt()
        if fields["CsvID"] != 0:
            fields["SlotIndex"] = calling_instance.readVInt()
        else:
        	fields["SlotIndex"] = calling_instance.readBoolean()  
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        '''
        if fields["CsvID"] == 28:
        		playerData["ProfileData"]["ProfileVanity"][fields["Index"]] = fields["VanityID"]
        
        if fields["C"]
        '''
        pass	

    def getCommandType(self):
        return 568
from Classes.ByteStream import ByteStream
from Classes.Commands.LogicServerCommand import LogicServerCommand
from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler
import json

class LogicGiveDeliveryItemsCommand(LogicServerCommand):
    
    def __init__(self, commandData):
        super().__init__(commandData)

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["Unk1"] = calling_instance.readVInt()
        fields["Unk2"] = calling_instance.readVInt()
        fields["Unk3"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        print(fields)
        return fields

    def encode(self, fields):
    	db_instance = DatabaseHandler()
    	playerData = json.loads(db_instance.getPlayerEntry(fields["PlayerID"])[2])
    	self.writeVInt(1)
    	boxes = fields['DeliveryData']['Boxes']
    	self.writeVInt(len(boxes)) # Multipler
    	for i in boxes:
    		self.writeVInt(i['Type']) # Type
    		rewards = i['Items']
    		self.writeVInt(len(rewards)) # Reward Count
    		for x in rewards:
    		  # LogicGatchaDrop
    		  self.writeVInt(x['Amount']) # Value
    		  if x['DataRef'][0] == 16:
    		  	self.writeDataReference(x['DataRef'][0], x['DataRef'][1]) # ScId 16
    		  	#self.writeDataReference(83, x['PowerID']) # Brawler Power-up 
    		  else:
    		  	self.writeDataReference(0, 0)
    		  self.writeVInt(x['RewardID']) # Reward ID
    		  if x['DataRef'][0] == 29:
    		  	self.writeDataReference(x['DataRef'][0], x['DataRef'][1]) # ScId 29
    		  else:
    		  	self.writeDataReference(0, 0)
    		  if x['DataRef'][0] == 52 or x['DataRef'][0] == 28 or x['DataRef'][0] == 68 or x['DataRef'][0] == 76:
    		  	self.writeDataReference(x['DataRef'][0], x['DataRef'][1]) # ScId 52 or 28
    		  else:
    		  	self.writeDataReference(0, 0)
    		  if x['DataRef'][0] == 23:
    		  	self.writeDataReference(x['DataRef'][0], x['DataRef'][1]) # ScId 23
    		  else:
    		  	self.writeDataReference(0, 0)
    		  self.writeVInt(0)
    		  self.writeVInt(0)
    		  self.writeVInt(1)
    		  
    	try:
    	    fields["ForcedDrop"]
    	except:
    	    fields["ForcedDrop"] = False
    	    
    	# ForcedDrops::destruct??    
    	if fields["ForcedDrop"]:
    	    self.writeByte(1) # Forced Drop
    	    
    	    self.writeVInt(200)
    	    self.writeVInt(200)
    	    self.writeVInt(5)
    	    self.writeVInt(93)
    	    self.writeVInt(206)
    	    self.writeVInt(456)
    	    self.writeVInt(1001)
    	    self.writeVInt(2264)
    	    self.writeVInt(0)
    	    self.writeVInt(0)
    	    self.writeVInt(0)
    	    self.writeVInt(5)
    	    self.writeByte(2)
    	    self.writeDataReference(0, 0)
    	    self.writeVInt(-1)
    	    self.writeVInt(-1)
    	'''
    	self.writeVInt(0)
    	self.writeVInt(0)
    	self.writeVInt(0)
    	self.writeVInt(0)
    	self.writeByte(0)
    	self.writeByte(0)
    	self.writeDataReference(0, 0)
    	self.writeVInt(0)
    	self.writeVInt(0)
    	self.writeVInt(0)
    	self.writeByte(0)
    	self.writeByte(0)
    	self.writeVInt(0)
    	''' #dayum wtf happening with LogicGiveDeliveryItems::encode
    	if fields["MilestoneProgress"]:
        	self.writeBoolean(False)
        	self.writeVInt(fields["Type"])
        	self.writeVInt(fields["Index"] + 2)
        	self.writeVInt(fields["Season"]) 
        	self.writeVInt(0)
        	self.writeVInt(0)
    	else:
            self.writeVInt(0)
            self.writeVInt(0)
    	
    	
    	
    	LogicServerCommand.encode(self, fields)
    	return self.messagePayload


    def getCommandType(self):
        return 203



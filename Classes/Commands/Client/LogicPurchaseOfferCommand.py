from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Classes.Commands.Server.LogicCatalogue import LogicCatalogue
from Classes.Commands.Server.LogicDataTables import LogicDataTables
from Classes.Commands.Server.LogicStarrDropOpening import LogicStarrDropOpening

class LogicPurchaseOfferCommand(LogicCommand):
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
        fields["OfferIndex"] = calling_instance.readVInt()
        fields["PurchasedItem"] = calling_instance.readDataReference()
        fields["Unk"] = calling_instance.readDataReference()
        fields["CurrencySlot"] = calling_instance.readVInt()
        print(fields)
        
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        if fields["OfferIndex"] == 0:
        	CommandManager__args = (calling_instance, fields)
        	for i in range(5):
        		LogicStarrDropOpening.createRandomReward(calling_instance, fields, True, None)
        	
        	fields["Socket"] = calling_instance.client
        	fields["Command"] = {"ID": 228}
        	fields["PlayerID"] = calling_instance.player.ID
        	Messaging.sendMessage(24111, fields)
        	LogicStarrDropOpening.giveRandomReward(*CommandManager__args)
        		
        elif fields["OfferIndex"] == 1:
        	fields["DeliveryData"] = {'Boxes': []}
        	box = {'Type': 100, 'Items': []}
        	item = {'Amount': 1337, 'DataRef': [0, 0],  'RewardID': 8}
        	box['Items'].append(item)
        	fields["DeliveryData"]['Boxes'].append(box)
        elif fields["OfferIndex"] == 2:
        	fields["DeliveryData"] = {'Boxes': []}
        	box = {'Type': 100, 'Items': []}
        	item = {'Amount': 100, 'DataRef': [0, 0],  'RewardID': 8}
        	item2 = {'Amount': 555, 'DataRef': [0, 0],  'RewardID': 8}
        	box['Items'].append(item)
        	box['Items'].append(item2)
        	fields["DeliveryData"]['Boxes'].append(box)
        
        if fields["PurchasedItem"] != None:
        	LogicCatalogue.makePurchase(calling_instance, fields, {"CurrencyType": fields["CurrencySlot"], "ItemCSV": fields["PurchasedItem"][0], "ItemID": fields["PurchasedItem"][1]})
        	
        	
        '''
        fields["Socket"] = calling_instance.client
        fields["Command"] = {"ID": 203}
        fields["PlayerID"] = calling_instance.player.ID
        fields["ForcedDrop"] = False
        fields["IsBrawlPassReward"] = False
        Messaging.sendMessage(24111, fields)
        '''
        

    def getCommandType(self):
        return 519
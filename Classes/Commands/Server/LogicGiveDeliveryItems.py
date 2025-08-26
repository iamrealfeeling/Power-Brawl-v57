from Classes.Messaging import Messaging

class LogicGiveDeliveryItems():
    def execute(self, calling_instance, fields, inputData, args):
        fields["DeliveryData"] = {'Boxes': []}
        fields["ForcedDrop"] = args[0]
        fields["MilestoneProgress"] = args[1]
        Boxes = []
        Items = []

        for v0 in inputData["Boxes"]:
            Boxes.append({'Type': v0["Type"], 'Items': [], "BoxID": v0["BoxID"]})
        
        for v1 in inputData["Items"]:
            Items.append({
                'Amount': v1["Amount"],
                'DataRef': [v1["DataRef"][0], v1["DataRef"][1]],
                'RewardID': v1["RewardID"],
                "BoxID": v1["BoxID"]
            })

        for v2 in Items:
            for v3 in Boxes:
                if v3["BoxID"] == v2["BoxID"]:
                    v3["Items"].append(v2)

        Boxes = [box for box in Boxes if box["Items"]]

        fields["DeliveryData"]['Boxes'] = Boxes
        fields["Socket"] = calling_instance.client
        fields["Command"] = {"ID": 203}
        fields["PlayerID"] = calling_instance.player.ID
        Messaging.sendMessage(24111, fields)

LogicGiveDeliveryItems = LogicGiveDeliveryItems()

		
		
			
		
		
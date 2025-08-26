from Classes.Commands.Client.LogicGemOffer import LogicGemOffer      

class LogicRandomRewardManager():
	def encode(self, ByteStream, values):
		ByteStream.writeVInt(5)
		for i in range(5):
			ByteStream.writeDataReference(80, i)
			ByteStream.writeVInt(1)
			ByteStream.writeVInt(0) 
			
		ByteStream.writeVInt(values["RarityArray"][0])
		for v0 in range(values["RarityArray"][0]):
			ByteStream.writeDataReference(80, values["RarityArray"][1])
			
		ByteStream.writeVInt(values["GemOfferArray"])
		if values["GemOfferArray"] != 0:
			ByteStream.writeByte(1)
			LogicGemOffer.encode(ByteStream, {"ItemType": 1, "Amount": 500, "DataReference": [0, 0], "ItemCSV": 0})
		
		ByteStream.writeInt(0)
		ByteStream.writeVInt(0) 
		ByteStream.writeVInt(0)
		ByteStream.writeVInt(86400*24)
		ByteStream.writeVInt(0)
		ByteStream.writeVInt(0)

LogicRandomRewardManager = LogicRandomRewardManager()
        
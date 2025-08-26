class LogicGemOffer():
	def encode(self, ByteStream, values):
		ByteStream.writeVInt(values["ItemType"])
		ByteStream.writeVInt(values["Amount"])
		ByteStream.writeDataReference(values["DataReference"][0], values["DataReference"][1])
		ByteStream.writeVInt(values["ItemCSV"])
		
LogicGemOffer = LogicGemOffer()
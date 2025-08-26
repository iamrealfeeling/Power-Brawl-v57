class BrawlPass():
	def encode(self, stream, player, data):
		stream.writeVInt(1)
		
		stream.writeVInt(21)
		stream.writeVInt(data["Tokens"])
		stream.writeBoolean(data["Active"])
		stream.writeVInt(0)
		stream.writeBoolean(False)
		
		stream.writeBoolean(True)
		stream.writeInt(data["Premium"][0])
		stream.writeInt(data["Premium"][1])
		stream.writeInt(data["Premium"][2])
		stream.writeInt(0)
		
		stream.writeBoolean(True)
		stream.writeInt(data["Free"][0])
		stream.writeInt(data["Free"][1])
		stream.writeInt(data["Free"][2])
		stream.writeInt(0)
		
		stream.writeBoolean(data["ActivePlus"])
		stream.writeBoolean(True)
		stream.writeInt(data["Plus"][0])
		stream.writeInt(data["Plus"][1])
		stream.writeInt(data["Plus"][2])
		stream.writeInt(0)
            
LogicBrawlPass = BrawlPass()
class LogicRecruitBrawler():
	def encode(self, ByteStream, values):
		ByteStream.writeDataReference(16, values["Brawler"])
		ByteStream.writeVInt(values["Price"][0])
		ByteStream.writeVInt(values["Price"][1])
		ByteStream.writeVInt(0)
		ByteStream.writeVInt(values["ObtainedCredits"])
		ByteStream.writeVInt(values["ElementIndex"])
		ByteStream.writeVInt(0)

LogicRecruitBrawler = LogicRecruitBrawler()
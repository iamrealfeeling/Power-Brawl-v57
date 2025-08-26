from Server.Database.DatabaseHandler import DatabaseHandler
class LogicCommodity():
	def changeResourceValue(self, calling_instance, fields, inputData):
		Database = DatabaseHandler()
		playerData = Database.getPlayer(calling_instance.player.ID)
		if inputData[1] == "-":
		      playerData["ResourceData"][inputData[0]] -= inputData[2]
		elif inputData[1] == "+":
		      playerData["ResourceData"][inputData[0]] += inputData[2]
		elif inputData[1] == "=":
		      playerData["ResourceData"][inputData[0]] = inputData[2]
		else:
		      raise TypeError(f"There is no such operation as {inputData[1]}.")
		      
		      
        
LogicCommodity = LogicCommodity()
		
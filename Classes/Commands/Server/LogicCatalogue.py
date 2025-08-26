from Classes.Commands.Server.LogicDataTables import LogicDataTables
from Classes.Commands.Server.LogicGiveDeliveryItems import LogicGiveDeliveryItems
from Classes.LogicUtility import LogicUtility
from Database.DatabaseHandler import DatabaseHandler

import json
import re

class LogicCatalogue():
	def makePurchase(self, calling_instance, fields, inputData):
		
		Database = DatabaseHandler()
		playerData = Database.getPlayer(calling_instance.player.ID)
				
		currencyTypes = {
		  0: "PriceCoins",
		  1: "PriceGems",
		  2: "PriceBling"
		}
		
		itemTableData = {
		  52: "Pins",
		  28: "Thumbnails",
		  68: "Sprays",
		  29: "Skins"
		}
		
		CommandManager__args = (calling_instance, fields)
		
		if inputData["CurrencyType"] != 3:
			itemInfo = int(LogicDataTables.getValue(inputData["ItemCSV"], inputData["ItemID"], currencyTypes.get(inputData["CurrencyType"])))			
			v0 = re.findall('[A-Z][^A-Z]*', currencyTypes.get(inputData["CurrencyType"]))
		else:
			itemInfo = 0
			v0 = None
		
		v1 = itemTableData.get(inputData["ItemCSV"])
		
		itemBlingCost = int(LogicDataTables.getValue(inputData["ItemCSV"], inputData["ItemID"], "PriceBling"))
		LogicCommodity__Bling = playerData["ResourceData"]["Bling"]
		LogicCommodity__BlingToGemPercentage = round((itemBlingCost - LogicCommodity__Bling) / 33)

		if inputData["CurrencyType"] != 3:
			v2 = playerData["ResourceData"][v0[1]] >= itemInfo
		else:
			v2 = playerData["ResourceData"]["Gems"] >= LogicCommodity__BlingToGemPercentage
		
		if v2:			
			if inputData["ItemCSV"] == 29:
				playerData["MiscellaneousData"]["Skins"].append(inputData["ItemID"])
				deliveryData = [29, inputData["ItemID"], 9]
				
				
				skinName = LogicDataTables.getValue(29, inputData["ItemID"], "Name")
				skinVanity = LogicUtility.getHeroSkinVanity(skinName)
				skinVanityOutput = []
				
				for v3 in skinVanity["Pins"]:
					playerData["VanityData"]["Pins"].append({"ID": v3, "State": 0, "Slot": 0})
					skinVanityOutput.append({'Amount': 1, 'DataRef': [52, v3],  'RewardID': 11, 'BoxID': 1})
					
				for v4 in skinVanity["Thumbnails"]:
					playerData["VanityData"]["Thumbnails"].append({"ID": v4, "State": 0, "Slot": 0})
					skinVanityOutput.append({'Amount': 1, 'DataRef': [28, v4],  'RewardID': 11, 'BoxID': 1})
					
				for v5 in skinVanity["Sprays"]:
					playerData["VanityData"]["Sprays"].append({"ID": v5, "State": 0, "Slot": 0})
					skinVanityOutput.append({'Amount': 1, 'DataRef': [68, v5],  'RewardID': 11, 'BoxID': 1})					
			else:
				playerData["VanityData"][v1].append({"ID": inputData["ItemID"], "State": 0, "Slot": 0})
				deliveryData = [inputData["ItemCSV"], inputData["ItemID"], 11]
							
			if inputData["CurrencyType"] != 3:
				playerData["ResourceData"][v0[1]] -= itemInfo
			else:
				playerData["ResourceData"]["Gems"] -= LogicCommodity__BlingToGemPercentage
				playerData["ResourceData"]["Bling"] = 0
		
		mainItem = [{'Amount': 1, 'DataRef': [deliveryData[0], deliveryData[1]],  'RewardID': deliveryData[2], 'BoxID': 0}]
		try:
			deliveryItems = mainItem + skinVanityOutput
		except:
			deliveryItems = mainItem
			
		deliveryOutput = {"Boxes": [{'Type': 100, 'Items': [], 'BoxID': 0}, {'Type': 100, 'Items': [], 'BoxID': 1}], "Items": deliveryItems}
			
		LogicGiveDeliveryItems.execute(*CommandManager__args, deliveryOutput, [False, False])
		
		Database.updatePlayerData(playerData,calling_instance)
        
LogicCatalogue = LogicCatalogue()
		
		
	
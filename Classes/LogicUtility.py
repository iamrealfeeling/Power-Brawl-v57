from Classes.Commands.Server.LogicDataTables import LogicDataTables

class LogicUtility:
	def getIntegerItemID(table_id, vanity_name, name_instance):
		tableLength = LogicDataTables.getTableLength(table_id)
		vanity_id = None
		for v0 in range(tableLength):
			v1 = LogicDataTables.getValue(table_id, v0, name_instance)
			if vanity_name == v1:
				vanity_id = v0
		return vanity_id
		
	def getHeroSkinVanity(skin):
		emoteTableLength = LogicDataTables.getTableLength(52)
		thumbnailTableLength = LogicDataTables.getTableLength(28)
		sprayTableLength = LogicDataTables.getTableLength(68)
		
		skinData = {"Pins": [], "Thumbnails": [], "Sprays": []}
		
		for v0 in range(emoteTableLength):
			v1 = LogicDataTables.getValue(52, v0, "Skin")
			if v1 == skin:
				a0 = LogicDataTables.getValue(52, v0, "Name")
				skinData["Pins"].append(LogicUtility.getIntegerItemID(52, a0, "Name"))
		
		for v2 in range(thumbnailTableLength):
			v3 = LogicDataTables.getValue(28, v2, "CatalogPreRequirementSkin")
			if v3 == skin:
				a1 = LogicDataTables.getValue(28, v2, "Name")
				skinData["Thumbnails"].append(LogicUtility.getIntegerItemID(28, a1, "Name"))
				
		for v4 in range(sprayTableLength):
			v5 = LogicDataTables.getValue(68, v4, "Skin")
			if v5 == skin:
				a2 = LogicDataTables.getValue(68, v4, "Name")
				skinData["Sprays"].append(LogicUtility.getIntegerItemID(68, a2, "Name"))
							
		return skinData
		
	def getDefaultBrawlerVanity(int, string):
		emoteTableLength = LogicDataTables.getTableLength(52)
		thumbnailTableLength = LogicDataTables.getTableLength(28)
		
		if int != None:
			brawler = LogicDataTables.getValue(16, int, "ItemName")
		else:
			brawler = string
				
		vanityData = {"Thumbnail": None, "Pin": None}
		
		for v1 in range(emoteTableLength):
			v2 = LogicDataTables.getValue(52, v1, "Name")
			if v2 == "emoji_" + brawler:
				a0 = LogicDataTables.getValue(52, v1, "Name")
				vanityData["Pin"] = LogicUtility.getIntegerItemID(52, a0, "Name")
		
		for v3 in range(thumbnailTableLength):
			v4 = LogicDataTables.getValue(28, v3, "IconExportName")
			if v4 == "player_icon_" + brawler:
				a1 = LogicDataTables.getValue(28, v3, "Name")
				vanityData["Thumbnail"] = LogicUtility.getIntegerItemID(28, a1, "Name")
				
		return vanityData
	
	def getDefaultPlayerVanity():
		emoteTableLength = LogicDataTables.getTableLength(52)
		thumbnailTableLength = LogicDataTables.getTableLength(28)
				
		vanityData = {"Thumbnails": [], "Pins": []}
		
		for v0 in range(emoteTableLength):
			v1 = LogicDataTables.getValue(52, v0, "Character")
			v2 = LogicDataTables.getValue(52, v0, "Rarity")
			if v1 == "" and v2 == "DEFAULT":
				vanityData["Pins"].append(v0)
		
		for v3 in range(thumbnailTableLength):
			# was a bit too lazy here, sooo... enjoy :)
			v4 = LogicDataTables.getValue(28, v3, "RequiredHero")
			v5 = LogicDataTables.getValue(28, v3, "IsReward")
			v6 = LogicDataTables.getValue(28, v3, "IsAvailableForOffers")
			v7 = LogicDataTables.getValue(28, v3, "PriceBling")
			v8 = LogicDataTables.getValue(28, v3, "PriceGems")
			if v4 == "" and v5 == "" and v6 == "" and v7 == "" and v8 == "":
				vanityData["Thumbnails"].append(v3)		
		return vanityData
		
	def getHeroIDBySkin(integer):
		tablesLength = LogicDataTables.getTableLength([16, 44])
		if type(integer) is int:
			v0 = LogicDataTables.getValue(29, integer, "Name")
			for v1 in range(tablesLength["table44"]):
				v2 = LogicDataTables.getValue(44, v1, "Name")
				if v0 == v2:
					v3 = LogicDataTables.getValue(44, v1, "Character")
			
			for v4 in range(tablesLength["table16"]):
				v5 = LogicDataTables.getValue(16, v4, "Name")
				if v3 == v5:
					return v4	
		else:
			raise RuntimeError("LogicUtility has failed to load correctly at function getHeroIDBySkin: Input value must be int, list or str(1)")
	
	def preserveInteger(str):
		try:
			output = int(str)
		except:
			output = ""
		return output
	
	def getDropItemTable(rarity):
		randomRewards = {
		  0: "Rare",
		  1: "SuperRare",
		  2: "Epic",
		  3: "Mythic",
		  4: "Legendary"
		}
		randomRewardTableLength = LogicDataTables.getTableLength(79)
		randomRewardStr = randomRewards.get(rarity)
		itemTable = []
		for v0 in range(randomRewardTableLength):
			v1 = LogicDataTables.getValue(79, v0, f"TicketsIn{randomRewardStr}Draw")
			if v1 != "":
				v2 = LogicDataTables.getValue(79, v0, ["Name", "TypeName", "TypeValue", "AmountMin", "AmountMax", "FallbackTypeName", "FallbackAmount", "TypePriceMax"])
				itemTable.append({"Name": v2["Name"], "TypeName": v2["TypeName"], "TypeValue": v2["TypeValue"], "MinValue": LogicUtility.preserveInteger(v2["AmountMin"]), "MaxValue": LogicUtility.preserveInteger(v2["AmountMax"]), "FallbackName": v2["FallbackTypeName"], "FallbackAmount": LogicUtility.preserveInteger(v2["FallbackAmount"]), "Ticket": int(v1), "Price": LogicUtility.preserveInteger(v2["TypePriceMax"])})
		return itemTable
	
	def getHeroUnlockCard(heroID):
		tablesLength = LogicDataTables.getTableLength([16, 23])
		characterName = None
		cardUnlockID = None
		
		for v0 in range(tablesLength["table16"]):
			if heroID == v0:
				characterName = LogicDataTables.getValue(16, v0, "Name")
				print(characterName)
				break
		
		for v1 in range(tablesLength["table23"]):
			v2 = LogicDataTables.getValue(23, v1, "Name")
			if v2 == characterName + "_unlock":
				cardUnlockID = v1
				print(cardUnlockID)
				break
				
		return cardUnlockID
		
	def getHeroDesignatedPrice(heroID):
		tablesLength = LogicDataTables.getTableLength([16, 23])
		characterName = None
		characterPrice = [None, None]
		
		recruitTokenPrices = {
		  "rare": 160,
		  "super_rare": 430, 
		  "epic": 925,
		  "mega_epic": 1900,
		  "legendary": 3800
		}
		
		gemPrices = {
		  "rare": 29,
		  "super_rare": 79, 
		  "epic": 169,
		  "mega_epic": 349,
		  "legendary": 699
		}
		
		for v0 in range(tablesLength["table16"]):
			if heroID == v0:
				characterName = LogicDataTables.getValue(16, v0, "Name")
				print(characterName)
				break
		
		for v1 in range(tablesLength["table23"]):
			v2 = LogicDataTables.getValue(23, v1, "Name")
			if v2 == characterName + "_unlock":
				v2 = LogicDataTables.getValue(23, v1, "Rarity")
				characterPrice = [recruitTokenPrices.get(v2), gemPrices.get(v2)]
				break
				
		return characterPrice
		


				
		
		
		
		
		
		
				
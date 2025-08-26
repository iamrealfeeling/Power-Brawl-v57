from Classes.LogicUtility import LogicUtility
from Classes.Commands.Server.LogicDataTables import LogicDataTables
from Classes.Commands.Server.LogicGiveDeliveryItems import LogicGiveDeliveryItems

from Database.DatabaseHandler import DatabaseHandler
from Classes.Messaging import Messaging

import json
import random
# 29.07.25 LogicStarrDropOpening - DONE 
# this was very hard to make ngl. 7 hours of shitcode (i'll improve it later)
# risporce how do you like that served huh
class LogicStarrDropOpening():	
	def createRandomReward(self, calling_instance, fields, isRandom, rarity):
		Database = DatabaseHandler()
		playerData = Database.getPlayer(calling_instance.player.ID)
		dropChances = [50, 28, 15, 5, 2]
		ticketData = [215, 151, 90, 158, 92]
		v0 = random.randint(1, 100)
		v1 = 0
		
		for v2 in dropChances:
			v1 += v2
			if v0 <= v1:
				randomDrop = dropChances.index(v2)
				break
						
		if isRandom == True:
			v3 = ticketData[randomDrop]
			randomDropTable = LogicUtility.getDropItemTable(randomDrop)
		else:
			v3 = ticketData[rarity]
			randomDropTable = LogicUtility.getDropItemTable(rarity)
			
		v4 = random.randint(1, v3)
		v5 = 0
		dropData = {}
		for v6 in range(v3):
			v5 += 1
			if v4 <= v5:
				if isRandom == True:					
					dropData["Rarity"] = randomDrop
				else:
					dropData["Rarity"] = rarity
					
				dropData["Ticket"] = v5
				minDiff = min(abs(item["Ticket"] - v4) for item in randomDropTable)
				closestTicket = [item["Ticket"] for item in randomDropTable if abs(item["Ticket"] - v4) == minDiff][0]
				closestElements = [item for item in randomDropTable if item["Ticket"] == closestTicket]
				dropData["TicketMatches"] = closestElements
				break
		playerData["RandomRewardData"].append(dropData)	
		Database.updatePlayerData(playerData,calling_instance)

	def giveRandomReward(self, calling_instance, fields):
		
		boxIDs = {
		  "TokenDoubler": 2,
		  "PowerPoints": 24,
		  "Coins": 7,
		  "Gems": 8,
		  "RecruitTokens": 22,
		  "Bling": 25
		}
		Database = DatabaseHandler()
		playerData = Database.getPlayer(calling_instance.player.ID)
		randomReward = playerData["RandomRewardData"][0]
		
		if True:
			if len(randomReward["TicketMatches"]) > 1:
				v0 = random.choice(randomReward["TicketMatches"])
			else:
				v0 = randomReward["TicketMatches"][0]
			fallback = False			
			if v0["Name"] == "Gadget":
				cardTableLength = LogicDataTables.getTableLength(23)
				heroGadgets = []
				ownedHeroGadgets = []
				
				for v1 in range(cardTableLength):
					v2 = LogicDataTables.getValue(23, v1, "Type")
					if v2 == "accessory":
						heroGadgets.append({"Brawler": LogicDataTables.getValue(23, v1, "Target"), "ID": v1})
				
				
				for a0 in heroGadgets:
					a1 = LogicUtility.getIntegerItemID(16, a0["Brawler"], "Name")
					if playerData["HeroData"][f"{a1}"]["CardID"] != 1:
						ownedHeroGadgets.append(a0)
						
				try:
					v3 = random.choice(ownedHeroGadgets)
					noItemsLeft = False
				except:
					v3 = {"Name": "TutorialDummy"}
					noItemsLeft = True
				v4 = LogicUtility.getIntegerItemID(16, v3["Brawler"], "Name")
				# these places are the most complicated. i'll change them in the future
				if playerData["HeroData"][f"{v4}"]["PowerLevel"] < 7 and v3["Brawler"] != "TutorialDummy" or int(v3["ID"]) in playerData["MiscellaneousData"]["Accessories"] and v3["Brawler"] != "TutorialDummy" or noItemsLeft == True:
					fallback = True
				else:
					playerData["MiscellaneousData"]["Accessories"].append(int(v3["ID"]))
					deliveryData = [23, int(v3["ID"]), 1, 4]
			elif v0["Name"] == "Star Power":
				cardTableLength = LogicDataTables.getTableLength(23)
				heroStarPowers = []
				ownedHeroStarPowers = []
				
				for q0 in range(cardTableLength):
					q1 = LogicDataTables.getValue(23, q0, "Name")
					if "unique" in q1:
						heroStarPowers.append({"Brawler": LogicDataTables.getValue(23, q0, "Target"), "ID": q0})
						
				
				for q2 in heroStarPowers:
					q3 = LogicUtility.getIntegerItemID(16, q2["Brawler"], "Name")
					if playerData["HeroData"][f"{q3}"]["CardID"] != 1:
						ownedHeroStarPowers.append(q2)
						
				try:
					q4 = random.choice(ownedHeroStarPowers)
					noItemsLeft = False
				except:
					q4 = {"Name": "TutorialDummy"}
					noItemsLeft = True
				q5 = LogicUtility.getIntegerItemID(16, q4["Brawler"], "Name")
				if playerData["HeroData"][f"{q5}"]["PowerLevel"] < 9 and q4["Brawler"] != "TutorialDummy" or int(q4["ID"]) in playerData["MiscellaneousData"]["Accessories"] and q4["Brawler"] != "TutorialDummy" or noItemsLeft == True:
					fallback = True
				else:
					playerData["MiscellaneousData"]["Accessories"].append(int(q4["ID"]))
					deliveryData = [23, int(q4["ID"]), 1, 4]
			elif v0["Name"] == "Overcharge":
				cardTableLength = LogicDataTables.getTableLength(23)
				heroOvercharges = []
				ownedHeroOvercharges = []
				
				for q6 in range(cardTableLength):
					q7 = LogicDataTables.getValue(23, q6, "Name")
					if "overcharge" in q7:
						heroOvercharges.append({"Brawler": LogicDataTables.getValue(23, q6, "Target"), "ID": q6})
				
				for q8 in heroOvercharges:
					q9 = LogicUtility.getIntegerItemID(16, q8["Brawler"], "Name")
					if playerData["HeroData"][f"{q9}"]["CardID"] != 1:
						ownedHeroOvercharges.append(q8)
						
				try:
					q10 = random.choice(ownedHeroOvercharges)
					noItemsLeft = False
				except:
					q10 = {"Name": "TutorialDummy"}
					noItemsLeft = True
				q11 = LogicUtility.getIntegerItemID(16, q10["Brawler"], "Name")
				
				if int(q10["ID"]) in playerData["MiscellaneousData"]["Accessories"] and q10["Brawler"] != "TutorialDummy" or noItemsLeft == True:
					fallback = True
				else:
					playerData["MiscellaneousData"]["Accessories"].append(int(q10["ID"]))
					deliveryData = [23, int(q10["ID"]), 1, 4]
			elif "Brawler" in v0["Name"]:
				cardTableLength = LogicDataTables.getTableLength(23)
				heroUnlockIDs = []
				heroSortedRarities = []
				heroRarity = v0["TypeValue"]
				for v13 in range(cardTableLength):
					v14 = LogicDataTables.getValue(23, v13, "Type")
					if v14 == "unlock":
						heroUnlockIDs.append({"Name": LogicDataTables.getValue(23, v13, "Name"), "ID": v13, "Rarity": LogicDataTables.getValue(23, v13, "Rarity")})
				for v15 in heroUnlockIDs:
					if v15["Rarity"] == heroRarity:
						heroSortedRarities.append(v15)
				try:
					v16 = random.choice(heroSortedRarities)
					noItemsLeft = False
				except:
					v16 = {"Name": "ShotgunGirl_Unlock"}
					noItemsLeft = True
				v17 = v16["Name"].split("_")
				characterTableLength = LogicDataTables.getTableLength(16)
				characterID = None
				for v18 in range(characterTableLength):
					v19 = LogicDataTables.getValue(16, v18, "Name")
					if v19 == v17[0]:
						characterID = v18
						break
				if playerData["HeroData"][f"{characterID}"]["CardID"] != 1 and v16["Name"] != "ShotgunGirl_Unlock" or noItemsLeft == True:
					fallback = True
				else:
					playerData["HeroData"][f"{characterID}"]["CardID"] = int(v16["ID"])
					deliveryData = [16, characterID, 1, 1]
			elif "Skin" in v0["Name"]:
				 allowedHeroes = 77
				 possibleSkins = []
				 skinRarities = {
				   29: "RARE",
				   79: "SUPER_RARE",
				   149: "EPIC",
				   199: "MYTHIC",
				   999: "LEGENDARY"
				 }
				 skinTableLength = LogicDataTables.getTableLength(23)
				 skinConfTableLength = LogicDataTables.getTableLength(44)
				 for v20 in range(skinTableLength):
				 	v21 = LogicDataTables.getValue(29, v20, ["Name", "Conf", "Disabled", "ObtainType", "Campaigns", "Rarity"])
				 	v22 = LogicUtility.getIntegerItemID(29, v21["Name"], "Name")
				 	
				 	try:
				 		v23 = LogicUtility.getHeroIDBySkin(v22)
				 	except:
				 		c0 = False
				 		
				 	try:
				 		c0 = v23 <= allowedHeroes
				 	except:
				 		c0 = False
				 		
				 	if v21["Disabled"] != "true" and v21["Campaigns"] != "GOLD" and v21["Campaigns"] != "SILVER" and v21["ObtainType"] == "" and c0 and playerData["HeroData"][f"{v23}"]["CardID"] != 1:
				 		if skinRarities.get(v0["Price"]) == v21["Rarity"]:
				 			possibleSkins.append({"Name": v21["Name"], "ID": v20, "Character": v23})
				 try:
				 	v25 = random.choice(possibleSkins)
				 	noItemsLeft = False
				 except:
				 	v25 = {"ID": -1}
				 	noItemsLeft = True
				 if v25["ID"] in playerData["MiscellaneousData"]["Skins"] and v25["ID"] != -1 or noItemsLeft == True:
				 	fallback = True
				 else:
				 	playerData["MiscellaneousData"]["Skins"].append(v25["ID"])
				 	deliveryData = [29, int(v25["ID"]), 1, 9]
				 	skinName = LogicDataTables.getValue(29, int(v25["ID"]), "Name")
				 	skinVanity = LogicUtility.getHeroSkinVanity(skinName)
				 	skinVanityOutput = []
				 	for v26 in skinVanity["Pins"]:
				 		playerData["VanityData"]["Pins"].append({"ID": v26, "State": 0, "Slot": 0})
				 		skinVanityOutput.append({'Amount': 1, 'DataRef': [52, v26],  'RewardID': 11, 'BoxID': 1})
				 	for v27 in skinVanity["Thumbnails"]:
				 		playerData["VanityData"]["Thumbnails"].append({"ID": v27, "State": 0, "Slot": 0})
				 		skinVanityOutput.append({'Amount': 1, 'DataRef': [28, v27],  'RewardID': 11, 'BoxID': 1})
				 	for v28 in skinVanity["Sprays"]:
				 		playerData["VanityData"]["Sprays"].append({"ID": v28, "State": 0, "Slot": 0})
				 		skinVanityOutput.append({'Amount': 1, 'DataRef': [68, v28],  'RewardID': 11, 'BoxID': 1})
			elif "Pin" in v0["Name"]:
				emoteTableLength = LogicDataTables.getTableLength(23)
				allowedEmotes = []
				emoteRarities = {
				   9: "COMMON",
				   29: "RARE",
				   999: "EPIC"
				 }
				for v29 in range(emoteTableLength):
					v30 = LogicDataTables.getValue(52, v29, ["Name", "Disabled", "Character", "Rarity", "PriceGems"])
					v31 = LogicUtility.getIntegerItemID(16, v30["Character"], "Name")
					if v30["Rarity"] != "DEFAULT" and v30["Character"] != "":
						if v30["Disabled"] == "":
							if v30["PriceGems"] != "":
								if emoteRarities.get(v0["Price"]) == v30["Rarity"]:
									if v30["Character"] != "" and playerData["HeroData"][f"{v31}"]["CardID"] != 1 or v30["Character"] == "":
										allowedEmotes.append(v29)
				try:
					v32 = random.choice(allowedEmotes)
					noItemsLeft = False
				except:
					v32 = -1
					noItemsLeft = True
				if any(item["ID"] == v32 for item in playerData["VanityData"]["Pins"]) and v32 != -1 or noItemsLeft == True:
					fallback = True
				else:
					playerData["VanityData"]["Pins"].append({"ID": v32, "State": 0, "Slot": 0})
					deliveryData = [52, v32, 1, 11]	
			elif "Profile" in v0["Name"]:
				thumbnailTableLength = LogicDataTables.getTableLength(28)
				allowedThumbnails = []
				for v33 in range(thumbnailTableLength):
					v34 = LogicDataTables.getValue(28, v33, ["Name", "Disabled", "IsReward", "PriceGems", "HideInCatalogWhenNotOwned"])
					if "hero" not in v34["Name"] or "rank" not in v34["Name"] and v34["Disabled"] == "" and v34["IsReward"] == "" and v34["PriceGems"] != "" and v34["HideInCatalogWhenNotOwned"] == "":
						allowedThumbnails.append(v33)
				try:
					v35 = random.choice(allowedThumbnails)
					noItemsLeft = False
				except:
					v35 = -1
					noItemsLeft = True
				if any(item["ID"] == v35 for item in playerData["VanityData"]["Thumbnails"]) or noItemsLeft == True:
					fallback = True
				else:
					playerData["VanityData"]["Pins"].append({"ID": v35, "State": 0, "Slot": 0})
					deliveryData = [28, v35, 1, 11]
			elif "Spray" in v0["Name"]:
				sprayTableLength = LogicDataTables.getTableLength(68)
				allowedSprays = []
				sprayRarities = {
				   19: "COMMON",
				   999: "COLLECTORS"
				 }
				for v36 in range(sprayTableLength):
				 	v37 = LogicDataTables.getValue(68, v36, ["Name", "Disabled", "Character", "Skin", "Rarity", "PriceGems"])
				 	if v37["Disabled"] == "" and v37["Character"] == "" and v37["Skin"] == "" and v37["PriceGems"] != "":
				 		if sprayRarities.get(v0["Price"]) == v37["Rarity"]:
				 			allowedSprays.append(v36)
				try:
					v38 = random.choice(allowedSprays)
					noItemsLeft = False
				except:
					v38 = -1
					noItemsLeft = True
				if any(item["ID"] == v38 for item in playerData["VanityData"]["Sprays"]) or noItemsLeft == True:
					fallback = True
				else:
					playerData["VanityData"]["Sprays"].append({"ID": v38, "State": 0, "Slot": 0})
					deliveryData = [68, v38, 1, 11]
			else:
				fallback = False
				randomAmount = random.randint(v0["MinValue"], v0["MaxValue"])
				
				playerData["ResourceData"][v0["TypeName"]] += randomAmount
				deliveryData = [0, 0, randomAmount, boxIDs.get(v0["TypeName"])]
			print(v0["Name"])
			
			if fallback == True:
				v11 = v0["FallbackName"]
				v12 = v0["FallbackAmount"]
				playerData["ResourceData"][v11] += v12
				deliveryData = [0, 0, v12, boxIDs.get(v11)]
				
			mainItem = [{'Amount': deliveryData[2], 'DataRef': [deliveryData[0], deliveryData[1]],  'RewardID': deliveryData[3], 'BoxID': 0}]
						
			try:
				deliveryItems = mainItem + skinVanityOutput
			except:
				deliveryItems = mainItem
				
			CommandManager__args = (calling_instance, fields)
			
			deliveryOutput = {"Boxes": [{'Type': 100, 'Items': [], 'BoxID': 0}, {'Type': 100, 'Items': [], 'BoxID': 1}], "Items": deliveryItems}
			
			LogicGiveDeliveryItems.execute(*CommandManager__args, deliveryOutput, [True, False])
			del playerData["RandomRewardData"][0]
			Database.updatePlayerData(playerData,calling_instance)
			fields["Socket"] = calling_instance.client
			fields["Command"] = {"ID": 228}
			fields["PlayerID"] = calling_instance.player.ID
			Messaging.sendMessage(24111, fields)
			
		

LogicStarrDropOpening = LogicStarrDropOpening()
							 				
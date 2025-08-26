import json
from Classes.Commands.LogicCommand import LogicCommand
from Database.DatabaseHandler import DatabaseHandler
from Classes.Messaging import Messaging
from Classes.Readers.JSONReaders.Cards import CardFetcher

class LogicStarRoadRewardCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        fields["BrawlerReward"] = calling_instance.readVInt()
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        playerData = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        
        BrawlerCard = CardFetcher.fetchBrawlerCard(fields["BrawlerReward"])
        
        
        try:
        	if playerData["Halting"]["State"] == False:
        		playerData["RecruitBrawler"] = playerData["Brawlers"][0]
        		del playerData["Brawlers"][0]
        	else:
        		playerData["RecruitBrawler"] = playerData["Brawlers"][0]
        		playerData["Halting"]["State"] = False
        		del playerData["Brawlers"][0]        		                		
        except:
            playerData["FameAvailable"] = True
        
                  
        rare = [8, 1, 2, 3, 6, 10, 13, 24]
        super_rare = [4, 7, 9, 18, 19, 22, 25, 27, 34, 61]
        epic = [30, 45, 15, 16, 20, 29, 36, 43, 50, 35, 39, 46, 51, 53, 60, 66, 68, 72, 65]
        mythic = [17, 21, 32, 31, 42, 64, 71, 73, 41, 44, 49, 54, 56, 59, 62, 76, 67]
        legendary = [5, 12, 23, 28, 40, 52, 63, 70, 38]
        
        BrawlerReward = fields["BrawlerReward"]
        if BrawlerReward in rare:
        	playerData["ResourceData"]["RecruitTokens"] -= 160
        if BrawlerReward in super_rare:
        	playerData["ResourceData"]["RecruitTokens"] -= 430
        if BrawlerReward in epic:
        	playerData["ResourceData"]["RecruitTokens"] -= 925
        if BrawlerReward in mythic:
        	playerData["ResourceData"]["RecruitTokens"] -= 1900
        if BrawlerReward in legendary:
        	playerData["ResourceData"]["RecruitTokens"] -= 3800
        
        playerData["OwnedBrawlers"][BrawlerReward] = {'CardID': int(BrawlerCard["CardID"]), 'Skins': [0], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2, 'MasteryPoints': 0, 'MasteryTier': 0, 'SelectedSkin': 0}
            
        
        
        db_instance.updatePlayerData(playerData, calling_instance)
        fields["Socket"] = calling_instance.client
        fields["Command"] = {"ID": 227}
        fields["PlayerID"] = calling_instance.player.ID
        Messaging.sendMessage(24111, fields, cryptoInit)

    def getCommandType(self):
        return 562
from Classes.Commands.LogicServerCommand import LogicServerCommand
from Database.DatabaseHandler import DatabaseHandler
import json

class LogicStarRoadRefreshCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):

        rare = [8, 1, 2, 3, 6, 10, 13, 24]
        super_rare = [4, 7, 9, 18, 19, 22, 25, 27, 34, 61]
        epic = [30, 45, 15, 16, 20, 29, 36, 43, 50, 35, 39, 46, 51, 53, 60, 66, 68, 72, 65]
        mythic = [17, 21, 32, 31, 42, 64, 71, 73, 41, 44, 49, 54, 56, 59, 62, 76, 67]
        legendary = [5, 12, 23, 28, 40, 52, 63, 70, 38]
        
        
        db_instance = DatabaseHandler()
        playerData = json.loads(db_instance.getPlayerEntry(fields["PlayerID"])[2])
        
        x = playerData["RecruitBrawler"]
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        if playerData["FameAvailable"] == False:
            self.writeBoolean(True) 
        
            self.writeVInt(1) 
        
            self.writeVInt(16)
            if playerData["Halting"]["State"] == False:
            	self.writeVInt(playerData["RecruitBrawler"])
            else:
            	self.writeVInt(playerData["Halting"]["Brawler"])
            	
            
            if x in rare:
                self.writeVInt(160)
            elif x in super_rare:
                self.writeVInt(430)
            elif x in epic:
                self.writeVInt(925)
            elif x in mythic:
                self.writeVInt(1900)
            elif x in legendary:
                self.writeVInt(3800)
            else:
                self.writeVInt(1)
            
            
            if x in rare:
                self.writeVInt(29)
            elif x in super_rare:
                self.writeVInt(79)
            elif x in epic:
                self.writeVInt(169)
            elif x in mythic:
                self.writeVInt(349)
            elif x in legendary:
                self.writeVInt(699)
            else:
                self.writeVInt(1)
            
            
            self.writeVInt(0)
            self.writeVInt(playerData["ResourceData"]["RecruitTokens"])
            self.writeVInt(0)
            self.writeVInt(0)
            '''
            if len(player.Brawlers) == 48:
        		self.writeVInt(len(playerData["Brawlers"]))
        		v1 = playerData
        	else:
        	'''
        self.writeVInt(len(playerData["Brawlers"]))
        v1 = playerData["Brawlers"][1:]
        		
        for k in playerData["Brawlers"]:
            self.writeDataReference(16, k) 
                      
            
            if k in rare:
                self.writeVInt(160)
            elif k in super_rare:
                self.writeVInt(430)
            elif k in epic:
                self.writeVInt(925)
            elif k in mythic:
                self.writeVInt(1900)
            elif k in legendary:
                self.writeVInt(3800)
            else:
            	self.writeVInt(1)
            
            
            if k in rare:
                self.writeVInt(29)
            elif k in super_rare:
                self.writeVInt(79)
            elif k in epic:
                self.writeVInt(169)
            elif k in mythic:
                self.writeVInt(349)
            elif k in legendary:
                self.writeVInt(699)
            else:
            	self.writeVInt(1)
            
           
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(playerData["Brawlers"].index(k)) 
            self.writeVInt(0)
        else:
        	self.writeBoolean(False) 
        
        self.writeBoolean(True) 
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        LogicServerCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 227
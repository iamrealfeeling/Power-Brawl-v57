from Classes.ByteStreamHelper import ByteStreamHelper
from Classes.Packets.PiranhaMessage import PiranhaMessage

from Classes.Commands.Client.LogicBrawlPass import LogicBrawlPass
from Classes.Commands.Client.LogicRandomRewardManager import LogicRandomRewardManager
from Classes.Commands.Client.LogicRecruitBrawler import LogicRecruitBrawler

class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(1688816070)
        self.writeVInt(1191532375)
        self.writeVInt(2023189)
        self.writeVInt(73530)
        
        # LogicClientHome
        # LogicDailyData

        self.writeVInt(player.ProfileData["Score"]["Current"])
        self.writeVInt(player.ProfileData["Score"]["Highest"])
        self.writeVInt(player.ProfileData["Score"]["Highest"]) 
        self.writeVInt(player.MiscellaneousData["TrophyRoadTier"])
        self.writeVInt(0)
        
        self.writeDataReference(28, player.ProfileData["Thumbnail"])
        self.writeDataReference(43, player.ProfileData["Namecolor"])

        self.writeVInt(26)
        for x in range(26):
            self.writeVInt(x)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        
        self.writeVInt(len(player.MiscellaneousData["Skins"]))
        for x in player.MiscellaneousData["Skins"]:
            self.writeDataReference(29, x)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(player.ProfileData["Score"]["Highest"])
        self.writeVInt(0)
        self.writeVInt(2)
        
        # LogicForcedDrops::encode
        self.writeBoolean(True)
        self.writeVInt(0)
        self.writeVInt(115)
        self.writeVInt(335442)
        self.writeVInt(1001442)
        self.writeVInt(5778642) 

        self.writeVInt(120)
        self.writeVInt(200)
        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(3) # Shop Offers
        
        # LogicOfferBundle::encode

        self.writeVInt(1) # RewardCount

        self.writeVInt(49)  # ItemType
        self.writeVInt(1337) # Amount
        self.writeDataReference(0)  # CsvID
        self.writeVInt(0) # SkinID

        self.writeVInt(0) # Currency(0-Gems, 1-Gold, 3-StarpoInts)
        self.writeVInt(0) # Cost
        self.writeVInt(0) # Time
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # Daily Offer
        self.writeVInt(0) # Old price
        self.writeString('пізда эстер😏😏😏😏😏🆘') # Text
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("offer_overcharge") # Background
        self.writeVInt(0)
        self.writeBoolean(False) # This purchase is already being processed
        self.writeVInt(0) # Type Benefit
        self.writeVInt(0) # Benefit
        self.writeString()
        self.writeBoolean(False) # One time offer
        self.writeBoolean(False) # Claimed
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(1) # RewardCount

        self.writeVInt(4)  # ItemType
        self.writeVInt(1) # Amount
        self.writeDataReference(0)  # CsvID
        self.writeVInt(392) # SkinID

        self.writeVInt(0) # Currency(0-Gems, 1-Gold, 3-StarpoInts)
        self.writeVInt(0) # Cost
        self.writeVInt(0) # Time
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # Daily Offer
        self.writeVInt(0) # Old price
        self.writeString('пізда эстер3😏😏😏😏😏🆘') # Text
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("offer_overcharge") # Background
        self.writeVInt(0)
        self.writeBoolean(False) # This purchase is already being processed
        self.writeVInt(0) # Type Benefit
        self.writeVInt(0) # Benefit
        self.writeString()
        self.writeBoolean(False) # One time offer
        self.writeBoolean(False) # Claimed
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(1) # RewardCount

        self.writeVInt(1)  # ItemType
        self.writeVInt(1337) # Amount
        self.writeDataReference(0)  # CsvID
        self.writeVInt(0) # SkinID

        self.writeVInt(0) # Currency(0-Gems, 1-Gold, 3-StarpoInts)
        self.writeVInt(0) # Cost
        self.writeVInt(0) # Time
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # Daily Offer
        self.writeVInt(0) # Old price
        self.writeString('пізда') # Text
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("offer_overcharge") # Background
        self.writeVInt(0)
        self.writeBoolean(False) # This purchase is already being processed
        self.writeVInt(0) # Type Benefit
        self.writeVInt(0) # Benefit
        self.writeString()
        self.writeBoolean(False) # One time offer
        self.writeBoolean(False) # Claimed
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(20)
        self.writeVInt(1428)

        self.writeVInt(0)

        self.writeVInt(1)
        self.writeVInt(30)

        self.writeByte(1) # count brawlers selected
        self.writeDataReference(16, player.MiscellaneousData["SelectedBrawlers"][0]) # selected brawler
        self.writeString(player.ProfileData["Region"]) # location
        self.writeString(player.MiscellaneousData["ContentCreator"]) # supported creator
        
        # LogicIntValueEntry::encode
        self.writeVInt(6) 
        self.writeVInt(1) 
        self.writeVInt(9) 
        self.writeVInt(1) 
        self.writeVInt(22) 
        self.writeVInt(3) 
        self.writeVInt(25) 
        self.writeVInt(1) 
        self.writeVInt(24) 
        self.writeVInt(0)
        self.writeVInt(15)
        self.writeVInt(32447)
        self.writeVInt(28)

        #LogicCooldownEntry
        self.writeVInt(0)

        LogicBrawlPass.encode(self, player, {"Tokens": player.BrawlPassData["Tokens"], "Active": player.BrawlPassData["Active"], "ActivePlus": player.BrawlPassData["ActivePlus"], "Free": [player.BrawlPassData["Free"][0], player.BrawlPassData["Free"][1], player.BrawlPassData["Free"][2]], "Premium": [player.BrawlPassData["Premium"][0], player.BrawlPassData["Premium"][1], player.BrawlPassData["Premium"][2]], "Plus": [player.BrawlPassData["Plus"][0], player.BrawlPassData["Plus"][1], player.BrawlPassData["Plus"][2]]})

        self.writeVInt(0) # ProLeagueSeasonData

        self.writeBoolean(True) # LogicQuests
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(0) 

        self.writeBoolean(True) # Vanity items
        self.writeVInt(len(player.VanityData["Pins"]) + len(player.VanityData["Thumbnails"]) + len(player.VanityData["Sprays"]) + len(player.VanityData["Titles"]))
        for x in player.VanityData["Thumbnails"]:
            self.writeDataReference(28, x["ID"])
            self.writeVInt(x["State"])
            if x["State"] == 1:
            	self.writeVInt(x["Slot"])
            	self.writeVInt(3)
        for x in player.VanityData["Pins"]:
            self.writeDataReference(52, x["ID"])
            self.writeVInt(x["State"])
            if x["State"] == 1:
            	self.writeVInt(x["Slot"])
            	self.writeVInt(3)
        for x in player.VanityData["Sprays"]:
            self.writeDataReference(68, x["ID"])
            self.writeVInt(x["State"])
            if x["State"] == 1:
            	self.writeVInt(x["Slot"])
            	self.writeVInt(3)
        for x in player.VanityData["Titles"]:
            self.writeDataReference(76, x["ID"])
            self.writeVInt(x["State"])
            if x["State"] == 1:
            	self.writeVInt(x["Slot"])
            	self.writeVInt(3)


        self.writeBoolean(False) # PlayerRankedSeasonData
        
        # LogicConfData

        self.writeInt(0)
        self.writeVInt(0)
        self.writeVInt(16)
        self.writeVInt(76)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(2023189)

        self.writeVInt(35) # LogicEventSlot Entry
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(3)
        self.writeVInt(4)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12)
        self.writeVInt(13) 
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(18) 
        self.writeVInt(19)
        self.writeVInt(20)
        self.writeVInt(21) 
        self.writeVInt(22)
        self.writeVInt(23)
        self.writeVInt(24)
        self.writeVInt(25)
        self.writeVInt(26)
        self.writeVInt(27)
        self.writeVInt(28)
        self.writeVInt(29)
        self.writeVInt(30)
        self.writeVInt(31)
        self.writeVInt(32)
        self.writeVInt(33)
        self.writeVInt(34)
        self.writeVInt(35)

        self.writeVInt(1) # LogicEventData Entry

        self.writeVInt(4)
        self.writeVInt(7)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(72292)
        self.writeVInt(10) 
        self.writeDataReference(15, 21) # map id
        self.writeVInt(-1)
        self.writeVInt(2)
        self.writeString("")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # MapMaker map structure array
        self.writeVInt(0)
        self.writeBoolean(False) # Power League array entry
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeBoolean(False) 

        self.writeVInt(0) # EventData (Upcoming)
       
        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800])
        ByteStreamHelper.encodeIntList(self, [30, 80, 170, 360]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [300, 880, 2040, 4680]) # Shop Coins Amount

        self.writeVInt(0) # ReleaseEntry

        self.writeVInt(1)
        self.writeVInt(41000084) # theme
        self.writeVInt(1) #idk timeint?

        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(-1)
        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(4)

        ByteStreamHelper.encodeIntList(self, [0, 29, 79, 169, 349, 699])
        ByteStreamHelper.encodeIntList(self, [0, 160, 450, 500, 1250, 2500])

        self.writeLong(0, 1) # Player ID

        self.writeVInt(0) # Notification factory
        # FUCK WHY DIDN'T IT SAVE
        self.writeVInt(1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeBoolean(False) # 
        self.writeVInt(0)
        self.writeBoolean(True) # LogicRecruitRoad (тебе привет от трех лиц от хуя и двух яиц:)
       
        self.writeVInt(0) # dataref array
        self.writeVInt(0) # dataref array
        self.writeVInt(0) # LogicFuckStarrletts
        
        #LogicRecruitBrawler
        # This. Is Elon Musk.
        
        if len(player.RecruitRoadData) != 0:
        	self.writeVInt(1)
        	for v0 in range(1):
        		LogicRecruitBrawler.encode(self, {"Brawler": player.RecruitRoadData[0]["Brawler"], "Price": [player.RecruitRoadData[0]["Price"][0], player.RecruitRoadData[0]["Price"][1]], "ObtainedCredits": 5, "ElementIndex": 0})
        else:
        	self.writeVInt(0)
        
        # перемогі не будє
        if len(player.RecruitRoadData) - 1 > 0:
        	self.writeVInt(len(player.RecruitRoadData) - 1)
        	for v1 in range(1, len(player.RecruitRoadData)):
        		LogicRecruitBrawler.encode(self, {"Brawler": player.RecruitRoadData[v1]["Brawler"], "Price": [player.RecruitRoadData[v1]["Price"][0], player.RecruitRoadData[v1]["Price"][1]], "ObtainedCredits": 0, "ElementIndex": player.RecruitRoadData.index(player.RecruitRoadData[v1])})
        		#sybau it worked (i forgot about the brawler index)
        else:
        	self.writeVInt(0)	
        
        self.writeVInt(0)               
        self.writeVInt(0)
        
        self.writeVInt(0) # Mastery

        #BattleCard
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeVInt(0) #Brawler's BattleCards
        
        if len(player.RandomRewardData) != 0:
        	v0 = True
        	v1 = player.RandomRewardData[0]["Rarity"]
        else:
        	v0 = False
        	v1 = None
        	
        LogicRandomRewardManager.encode(self, {"RarityArray": [v0, v1], "GemOfferArray": v0})
        
        

        self.writeBoolean(False)

        # end LogicClientHome

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(player.ID[0], player.ID[1])
        self.writeStringReference(player.ProfileData["Name"])
        self.writeBoolean(player.ProfileData["Registered"])
        self.writeInt(-1)

        self.writeVInt(17)
        unlocked_brawler = [i['CardID'] for x,i in player.HeroData.items()]
        self.writeVInt(len(unlocked_brawler) + 2)
        for x in unlocked_brawler:
            self.writeDataReference(23, x)
            self.writeVInt(-1)
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(-1)
        self.writeVInt(player.ResourceData["Coins"])

        self.writeDataReference(5, 23)
        self.writeVInt(-1)
        self.writeVInt(player.ResourceData["Bling"])

        self.writeVInt(len(player.HeroData)) # HeroScore
        for x,i in player.HeroData.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["Trophies"])

        self.writeVInt(len(player.HeroData)) # HeroHighScore
        for x,i in player.HeroData.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["HighestTrophies"])

        self.writeVInt(0) # Array

        self.writeVInt(0) # HeroPower
        
        self.writeVInt(len(player.HeroData)) # HeroLevel
        for x,i in player.HeroData.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["PowerLevel"]-1)

        self.writeVInt(0) # hero star power gadget and hypercharge

        self.writeVInt(len(player.HeroData)) # HeroSeenState
        for x,i in player.HeroData.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["State"])

        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array

        self.writeVInt(player.ResourceData["Gems"]) # Diamonds
        self.writeVInt(player.ResourceData["Gems"]) # Free Diamonds
        self.writeVInt(10) # Player Level
        self.writeVInt(100)
        self.writeVInt(0) # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(100) # Battle Count
        self.writeVInt(10) # WinCount
        self.writeVInt(80) # LoseCount
        self.writeVInt(50) # WinLooseStreak
        self.writeVInt(20) # NpcWinCount
        self.writeVInt(0) # NpcLoseCount
        self.writeVInt(2) # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(12)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)

    def decode(self):
        fields = {}
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion

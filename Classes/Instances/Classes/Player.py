import json
import random
import string


class Player:
    ClientVersion = "0.0.0"

    ID = [0, 1]
    Token = ""
    ProfileData = {"Name": "Brawler", "Registered": False, "Thumbnail": 0, "Namecolor": 0, "Region": "RU", "Score": {"Current": 99999, "Highest": 99999}, "Victories": {"Solo": 0, "Duo": 0, "Trio": 0}}
    
    ResourceData = {"Gems": 99999, "Coins": 0, "Bling": 1480, "TokenDoubler": 0, "PowerPoints": 0, "RecruitTokens": 0}
    
    VanityData = {"Pins": [], "Thumbnails": [], "Sprays": [], "Titles": []}
    
    BrawlPassData = {"Free": [0, 0, 0], "Premium": [0, 0, 0], "Plus": [0, 0, 0], "Active": True, "ActivePlus": True, "Tokens": 999999}
    
    MiscellaneousData = {"ContentCreator": "PowerBrawl", "TrophyRoadTier": 999, "SelectedBrawlers": [85, 85, 85], "Skins": [], "Accessories": []}
    
    DeliveryData = {}
    
    HeroData = {}
    
    RandomRewardData = []
    
    RecruitRoadData = []

    def __init__(self):
        pass

    def getDataTemplate(self, highid, lowid, token):
        if highid == 0 or lowid == 0:
            self.ID[0] = int(''.join([str(random.randint(0, 9)) for _ in range(1)]))
            self.ID[1] = int(''.join([str(random.randint(0, 9)) for _ in range(8)]))
            self.Token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40))
        else:
            self.ID[0] = highid
            self.ID[1] = lowid
            self.Token = token

        DBData = {
            'ID': self.ID,
            'Token': self.Token,
            'ProfileData': self.ProfileData,
            'ResourceData': self.ResourceData,
            'VanityData': self.VanityData,
            'BrawlPassData': self.BrawlPassData,
            'MiscellaneousData': self.MiscellaneousData,
            'DeliveryData': self.DeliveryData,           
            'HeroData': self.HeroData,
            'RandomRewardData': self.RandomRewardData,
            'RecruitRoadData': self.RecruitRoadData,
        }
        return DBData

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4))
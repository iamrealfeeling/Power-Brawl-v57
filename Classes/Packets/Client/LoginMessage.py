from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler
from Classes.ClientsManager import ClientsManager

from Classes.LogicUtility import LogicUtility
import json

OwnedBrawlersLatest = {
        0: {'CardID': 0, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        1: {'CardID': 4, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        2: {'CardID': 8, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        3: {'CardID': 12, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        4: {'CardID': 16, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        5: {'CardID': 20, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        6: {'CardID': 24, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        7: {'CardID': 28, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        8: {'CardID': 32, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        9: {'CardID': 36, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        10: {'CardID': 40, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        11: {'CardID': 44, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        12: {'CardID': 48, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        13: {'CardID': 52, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        14: {'CardID': 56, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        15: {'CardID': 60, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        16: {'CardID': 64, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        17: {'CardID': 68, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        18: {'CardID': 72, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        19: {'CardID': 95, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        20: {'CardID': 100, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        21: {'CardID': 105, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        22: {'CardID': 110, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        23: {'CardID': 115, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        24: {'CardID': 120, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        25: {'CardID': 125, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        26: {'CardID': 130, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        27: {'CardID': 177, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        28: {'CardID': 182, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        29: {'CardID': 188, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        30: {'CardID': 194, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        31: {'CardID': 200, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        32: {'CardID': 206, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        34: {'CardID': 218, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        35: {'CardID': 224, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        36: {'CardID': 230, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        37: {'CardID': 236, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        38: {'CardID': 279, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        39: {'CardID': 296, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        40: {'CardID': 303, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        41: {'CardID': 320, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        42: {'CardID': 327, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        43: {'CardID': 334, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        44: {'CardID': 341, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        45: {'CardID': 358, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        46: {'CardID': 365, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        47: {'CardID': 372, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        48: {'CardID': 379, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        49: {'CardID': 386, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        50: {'CardID': 393, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        51: {'CardID': 410, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        52: {'CardID': 417, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        53: {'CardID': 427, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        54: {'CardID': 434, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        56: {'CardID': 448, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        57: {'CardID': 466, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        58: {'CardID': 474, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        59: {'CardID': 491, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        60: {'CardID': 499, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        61: {'CardID': 507, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        62: {'CardID': 515, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        63: {'CardID': 523, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        64: {'CardID': 531, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        65: {'CardID': 539, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        66: {'CardID': 547, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        67: {'CardID': 557, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        68: {'CardID': 565, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        69: {'CardID': 573, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        70: {'CardID': 581, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        71: {'CardID': 589, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        72: {'CardID': 597, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        73: {'CardID': 605, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        74: {'CardID': 619, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        75: {'CardID': 633, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 11, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        76: {'CardID': 642, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0},
        77: {'CardID': 655, 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'Mastery': 0, 'ClaimRewardsMastery': 0}
    }
    
class LoginMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["AccountID"] = self.readLong()
        fields["PassToken"] = self.readString()
        fields["ClientMajor"] = self.readInt()
        fields["ClientMinor"] = self.readInt()
        fields["ClientBuild"] = self.readInt()
        fields["ResourceSha"] = self.readString()
        fields["Device"] = self.readString()
        fields["PreferredLanguage"] = self.readDataReference()
        fields["PreferredDeviceLanguage"] = self.readString()
        fields["OSVersion"] = self.readString()
        fields["isAndroid"] = self.readBoolean()
        fields["IMEI"] = self.readString()
        fields["AndroidID"] = self.readString()
        fields["isAdvertisingEnabled"] = self.readBoolean()
        fields["AppleIFV"] = self.readString()
        fields["RndKey"] = self.readInt()
        fields["AppStore"] = self.readVInt()
        fields["ClientVersion"] = self.readString()
        fields["TencentOpenId"] = self.readString()
        fields["TencentToken"] = self.readString()
        fields["TencentPlatform"] = self.readVInt()
        fields["DeviceVerifierResponse"] = self.readString()
        fields["AppLicensingSignature"] = self.readString()
        fields["DeviceVerifierResponse"] = self.readString()  # Дублируется, возможно нужно удалить
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        if fields["ClientMajor"] == 57:
            calling_instance.player.ClientVersion = f'{str(fields["ClientMajor"])}.{str(fields["ClientBuild"])}.{str(fields["ClientMinor"])}'
            fields["Socket"] = calling_instance.client
            db_instance = DatabaseHandler()
            
            if db_instance.playerExist(fields["PassToken"], fields["AccountID"]):
                player_data = json.loads(db_instance.getPlayerEntry(fields["AccountID"])[2])
                db_instance.loadAccount(calling_instance.player, fields["AccountID"])
            else:
                db_instance.createAccount(calling_instance.player.getDataTemplate(fields["AccountID"][0], fields["AccountID"][1], fields["PassToken"]))
                playerData = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
                
                if len(playerData["HeroData"]) == 0:
                    playerData["HeroData"][0] = {
                        'CardID': 0, 
                        'Skins': [], 
                        'Trophies': 0, 
                        'HighestTrophies': 0, 
                        'PowerLevel': 1, 
                        'PowerPoints': 0, 
                        'State': 0, 
                        'MasteryPoints': 0, 
                        'MasteryTier': 0, 
                        'SelectedSkin': 0
                    }
                    for v0 in range(1, 3):
                        card_id = OwnedBrawlersLatest.get(v0, {}).get('CardID', 0)
                        playerData["HeroData"][v0] = {
                            'CardID': card_id, 
                            'Skins': [], 
                            'Trophies': 0, 
                            'HighestTrophies': 0, 
                            'PowerLevel': 1, 
                            'PowerPoints': 0, 
                            'State': 0, 
                            'MasteryPoints': 0, 
                            'MasteryTier': 0, 
                            'SelectedSkin': 0
                        }
                
                v1 = LogicUtility.getDefaultPlayerVanity()
                
                for v2 in v1["Pins"]:
                    playerData["VanityData"]["Pins"].append({"ID": v2, "State": 0, "Slot": 0})
                for v3 in v1["Thumbnails"]:
                    playerData["VanityData"]["Thumbnails"].append({"ID": v3, "State": 0, "Slot": 0})
                
                if len(playerData["RecruitRoadData"]) == 0:
                    for v4 in range(1, 33):
                        playerData["RecruitRoadData"].append({
                            "Brawler": v4, 
                            "UnlockCard": LogicUtility.getHeroUnlockCard(v4), 
                            "Price": LogicUtility.getHeroDesignatedPrice(v4)
                        })
                    # Пропуск определенных героев
                    for v5 in range(35, 55):
                        playerData["RecruitRoadData"].append({
                            "Brawler": v5, 
                            "UnlockCard": LogicUtility.getHeroUnlockCard(v5), 
                            "Price": LogicUtility.getHeroDesignatedPrice(v5)
                        })
                    for v6 in range(57, 78):
                        playerData["RecruitRoadData"].append({
                            "Brawler": v6, 
                            "UnlockCard": LogicUtility.getHeroUnlockCard(v6), 
                            "Price": LogicUtility.getHeroDesignatedPrice(v6)
                        })
                
                db_instance.updatePlayerData(playerData, calling_instance)
            
            ClientsManager.AddPlayer(calling_instance.player.ID, calling_instance.client)
            Messaging.sendMessage(20104, fields, calling_instance.player)
            Messaging.sendMessage(24101, fields, calling_instance.player)
            Messaging.sendMessage(24399, fields, calling_instance.player)

    def getMessageType(self):
        return 10101

    def getMessageVersion(self):
        return self.messageVersion
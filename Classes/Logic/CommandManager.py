from Classes.Commands.Client.LogicPurchaseOfferCommand import LogicPurchaseOfferCommand
from Classes.Commands.Server.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand
from Classes.Commands.Client.LogicSetPlayerThumbnailCommand import LogicSetPlayerThumbnailCommand
from Classes.Commands.Client.LogicSetPlayerNameColorCommand import LogicSetPlayerNameColorCommand
from Classes.Commands.Client.LogicSetPlayerProfileVanityCommand import LogicSetPlayerProfileVanityCommand
from Classes.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand

from Classes.Commands.Client.LogicSelectEmoteCommand import LogicSelectEmoteCommand
from Classes.Commands.Client.LogicSelectCharacterCommand import LogicSelectCharacterCommand
from Classes.Commands.Client.LogicSelectSkinCommand import LogicSelectSkinCommand


from Classes.Commands.Client.LogicHeroSeenCommand import LogicHeroSeenCommand

from Classes.Commands.Client.LogicOpenRandomCommand import LogicOpenRandomCommand
from Classes.Commands.Server.LogicRefreshRandomRewardsCommand import LogicRefreshRandomRewardsCommand


class CommandManager:
    commandsList = {
        201: LogicChangeAvatarNameCommand,
        202: 'DiamondsAddedCommand',
        203: LogicGiveDeliveryItemsCommand,
        204: 'DayChangedCommand',
        205: 'DecreaseHeroScoreCommand',
        206: 'AddNotificationCommand',
        207: 'ChangeResourcesCommand',
        208: 'TransactionsRevokedCommand',
        209: 'KeyPoolChangedCommand',
        210: 'IAPChangedCommand',
        211: 'OffersChangedCommand',
        212: 'PlayerDataChangedCommand',
        213: 'InviteBlockingChangedCommand',
        214: 'GemNameChangeStateChangedCommand',
        215: 'SetSupportedCreatorCommand',
        216: 'CooldownExpiredCommand',
        217: 'ProLeagueSeasonChangedCommand',
        218: 'BrawlPassSeasonChangedCommand',
        219: 'BrawlPassUnlockedCommand',
        220: 'HerowinQuestsChangedCommand',
        221: 'TeamChatMuteStateChangedCommand',
        222: 'RankedSeasonChangedCommand',
        223: 'CooldownAddedCommand',
        224: 'SetESportsHubNotificationCommand',
        228: LogicRefreshRandomRewardsCommand,
        500: 'GatchaCommand',
        503: 'ClaimDailyRewardCommand',
        504: 'SendAllianceMailCommand',
        505: LogicSetPlayerThumbnailCommand,
        506: LogicSelectSkinCommand,
        507: 'UnlockSkinCommand',
        508: 'ChangeControlModeCommand',
        509: 'PurchaseDoubleCoinsCommand',
        511: 'HelpOpenedCommand',
        512: 'ToggleInGameHintsCommand',
        514: 'DeleteNotificationCommand',
        515: 'ClearShopTickersCommand',
        517: 'ClaimRankUpRewardCommand',
        518: 'PurchaseTicketsCommand',
        519: LogicPurchaseOfferCommand,
        520: 'LevelUpCommand',
        521: 'PurchaseHeroLvlUpMaterialCommand',
        522: LogicHeroSeenCommand,
        523: 'ClaimAdRewardCommand',
        524: 'VideoStartedCommand',
        525: LogicSelectCharacterCommand,
        526: 'UnlockFreeSkinsCommand',
        527: LogicSetPlayerNameColorCommand,
        528: 'ViewInboxNotificationCommand',
        529: 'SelectStarPowerCommand',
        530: 'SetPlayerAgeCommand',
        531: 'CancelPurchaseOfferCommand',
        532: 'ItemSeenCommand',
        533: 'QuestSeenCommand',
        534: 'PurchaseBrawlPassCommand',
        535: 'ClaimTailRewardCommand',
        536: 'PurchaseBrawlpassProgressCommand',
        537: 'VanityItemSeenCommand',
        538: LogicSelectEmoteCommand,
        539: 'BrawlPassAutoCollectWarningSeenCommand',
        540: 'PurchaseChallengeLivesCommand',
        541: 'ClearESportsHubNotificationCommand',
        542: 'SelectGroupSkinCommand',
        568: LogicSetPlayerProfileVanityCommand,
        571: LogicOpenRandomCommand
    }

    def getCommandsName(commandType):
        try:
            command = CommandManager.commandsList[commandType]
        except KeyError:
            command = str(commandType)
        if type(command) == str:
            return command
        else:
            return command.__name__

    def commandExist(commandType):
        return (commandType in CommandManager.commandsList.keys())

    def createCommand(commandType, commandPayload=b''):
        commandList = CommandManager.commandsList
        if CommandManager.commandExist(commandType):
            print(CommandManager.getCommandsName(commandType), "created")
            if type(commandList[commandType]) == str:
                pass
            else:
                return commandList[commandType](commandPayload)
        else:
            print(commandType, "skipped")
            return None

    def isServerToClient(commandType):
        if 200 <= commandType < 500:
            return True
        elif 500 <= commandType:
            return False

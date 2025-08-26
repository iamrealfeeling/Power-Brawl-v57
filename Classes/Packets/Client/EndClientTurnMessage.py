from Classes.Logic.CommandManager import CommandManager

from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class EndClientTurnMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        self.readBoolean()
        fields["Tick"] = self.readVInt()
        fields["Checksum"] = self.readVInt()
        fields["CommandsCount"] = self.readVInt()
        super().decode(fields)
        fields["Commands"] = []
        for i in range(fields["CommandsCount"]):
            fields["Commands"].append({"ID": self.readVInt()})
            if CommandManager.commandExist(fields["Commands"][i]["ID"]):
                command = CommandManager.createCommand(fields["Commands"][i]["ID"])
                print("Command", CommandManager.getCommandsName(fields["Commands"][i]["ID"]))
                if command is not None:
                    fields["Commands"][i]["Fields"] = command.decode(self)
                    fields["Commands"][i]["Instance"] = command
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        for command in fields["Commands"]:
            if "Instance" not in command.keys():
                return

            if hasattr(command["Instance"], 'execute'):
                command["Instance"].execute(calling_instance, command["Fields"])

    def getMessageType(self):
        return 14102

    def getMessageVersion(self):
        return self.messageVersion
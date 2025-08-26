import csv
from pathlib import Path

class LogicDataTables:
    v0 = {}
    v1 = False
    v2 = Path(__file__).resolve().parent
    csv_client = v2.parent.parent / "Files/assets/csv_client"
    csv_logic = v2.parent.parent / "Files/assets/csv_logic"
    v3 = {
        16: csv_logic / "characters.csv",
        23: csv_logic / "cards.csv",
        28: csv_logic / "player_thumbnails.csv",
        29: csv_logic / "skins.csv",
        44: csv_logic / "skin_confs.csv",
        52: csv_logic / "emotes.csv",
        68: csv_logic / "sprays.csv",
        79: csv_logic / "random_rewards.csv",
    }

    @classmethod
    def _load(cls):
        if cls.v1:
            return

        for tableID, path in cls.v3.items():
            try:
                with open(path, newline='', encoding='utf-8') as csvfile:
                    reader = list(csv.reader(csvfile))

                    if len(reader) < 2:
                        raise ValueError(f"CSV file {path} has less than two header rows")

                    v5 = reader[0] 
                    v6 = reader[2:]  
                    v7 = []
                    for row in v6:
                        if len(row) == 0 or row[0].strip() == "":
                            continue 

                        v8 = {key: (row[i] if i < len(row) else None) for i, key in enumerate(v5)}
                        v7.append(v8)

                    cls.v0[tableID] = v7
            except FileNotFoundError:
                print(f"LogicDataTables has failed to load correctly. CSVNotFound (1)")

        cls.v1 = True

    @classmethod
    def getTable(cls, tableID, index):
        cls._load()
        if tableID not in cls.v0:
            raise KeyError(f"LogicDataTables has failed to load correctly.\nTableNotFound (2)")

        table = cls.v0[tableID]
        if index < 0 or index >= len(table):
            raise IndexError(f"LogicDataTables has failed to load correctly.\nItemIndexNotFound (3)")

        return table[index]
        
    @classmethod
    # updated 26.07.24 added list and string support
    def getTableLength(cls, tableID):
        cls._load()
        if type(tableID) is list:
        	table = {}
        	for v1 in tableID:
        		table[f"table{v1}"] = len(cls.v0[v1])
        	return table
        else:
        	table = cls.v0[int(tableID)]
        	return len(table)
        		
    @classmethod
    # updated 27.07.24 added list support 
    def getValue(cls, tableID, index, key):
        row = cls.getTable(tableID, index)
        if type(key) is list:
        	keyList = {}
        	for v0 in key:
        		keyList[f"{v0}"] = row[v0]
        	return keyList
        else:
        	return row[key]
       


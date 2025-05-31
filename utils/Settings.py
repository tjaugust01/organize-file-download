from dataclasses import dataclass
import json

@dataclass
class Settings():
    watchFolders: list[str] = None
    targetFolder: dict[str , str] = None
    extensionMapping: dict[str, str] = None
    def __init__(self):
        jsonData = self.loadSettings()
        try:
            self.watchFolders = jsonData['watchFolders']
            self.targetFolder = jsonData['targetFolders']
            self.extensionMapping = jsonData.get('extensionMapping', {})
        except KeyError as e:
            raise KeyError(f"Pflichtfeld fehlt in settings.json: {e}")


    def loadSettings(self)-> dict:
        with open('settings/settings.json', 'r') as file:
            data= json.load(file)
            return data
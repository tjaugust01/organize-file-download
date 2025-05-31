from dataclasses import dataclass

@dataclass
class File:
    basename: str
    extension: str
    destination: str

    def __init__(self, path: str, settings):
        import os
        self.basename = os.path.basename(path)
        self.extension = self.basename.split(".")[-1].lower()
        try:
            extension_mapping = settings.extensionMapping[self.extension]
        except KeyError:
            extension_mapping = None
        if extension_mapping:
            self.destination = settings.targetFolder[extension_mapping]
        else:
            self.destination = None
"""
This module holds the model both for entry and dictionary, that
is going to be rendered by the viewer later on. Both models
mostly have global setter and getters. All change is done through controller.
"""
# Author: Kaan Eraslan
# License: see, LICENSE

from apps.modules.builder import model_builder

def set_data_to_model(schema: dict, data: dict):
    "Set data to model"
    Model = model_builder(schema)

class AbstractEntryModel:
    "Represents the entry of a dictionary"

    def __init__(self, entry: dict, schema_path="", schema_name=""):
        self.entry = entry
        self.schema_path = schema_path
        self.schema_name = schema_name

    def set_data(self, **kwargs):
        "Set data to entry model"
        for keyname, val in kwargs.items():
            if "schema" in keyname and "path" in keyname and "name" in keyname:
                raise ValueError("Invalid keyname: " + keyname)
            if "schema" in keyname and "path" in keyname:
                self.schema_path = val
            if "schema" in keyname and "name" in keyname:
                self.schema_name = val
            if keyname == "entry":
                self.entry = val

    def set_entry(self, entry: dict):
        "Set entry to model"
        assert isinstance(entry, dict)
        self.entry = entry

    def set_schema_val(self, val: str, is_name=False):
        "Set schema path to model"
        assert isinstance(val, str)
        if is_name:
            self.schema_name = val
        else:
            self.schema_path = val

    def set_schema_path(self, path: str):
        "set schema path using schema val"
        return self.set_schema_val(path, is_name=False)

    def set_schema_name(self, name: str):
        "set schema name using schema val"
        return self.set_schema_val(name, is_name=True)

    def get_data(self) -> dict:
        "get model data as a unified dict"
        return {
            "entry": self.entry,
            "schema-name": self.schema_name,
            "schema-path": self.schema_path
        }

    def get_entry(self) -> dict:
        "get model entry data as a dict"
        return {"entry": self.entry}

    def get_entry_with_name(self) -> dict:
        "get model entry data as a dict"
        return {"entry": self.entry, "schema-name": self.schema_name}

    def get_entry_with_path(self) -> dict:
        "get model entry data as a dict"
        return {"entry": self.entry, "schema-path": self.schema_path}


class AbstractDictModel:
    "Dictionary model"

    def __init__(self, entries: [AbstractEntryModel]):
        "entries"
        self.entries = entries

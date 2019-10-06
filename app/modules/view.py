"""
This module renders a view of the model using builder.
It can produce a tree widget item.
It should also be able to produce an xml view of the data.
"""
# Author: Kaan Eraslan
# License: see, LICENSE

from app.modules.builder import transform_complex_element_to_tree_item
from app.modules.model import


class EntryView:
    "View that renders models in a tree widget"

    def __init__(self, model: dict):
        ""
        assert "name" in model
        assert "model" in model
        self.model = model

    def render_model(self):
        "Render models as tree widget item"
        modelName = self.model['name']
        model = self.model['model']
        return transform_complex_element_to_tree_item(modelName, model)

class EntriesView:
    "render entries who have different schemas"
    def __init__(self, models):
        self.models = models

    def render_models(self):
        "Render models as a list of tree items"
        views = []
        for model in self.models:
            entry_view = EntryView(model)
            view = entry_view.render_model()
            views.append(view)
        return views

class DictView:
    "Render dictview as a treewidget"
    def __init__(self, dictmodel):
        ""
        assert "entries" in dictmodel
        self.entries = dictmodel.pop("entries")

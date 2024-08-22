import json
from datetime import datetime


class CellModel:
    def __init__(self, coordinate, value=None, formula=None):
        self.coordinate = coordinate
        self.value = value
        self.formula = formula
        self.dependencies = []

    def add_dependency(self, cell_model):
        if cell_model not in self.dependencies:
            self.dependencies.append(cell_model)

    def to_dict(self):
        def serialize(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError(f"Type {type(obj)} not serializable")

        return {
            "coordinate": self.coordinate,
            "value": serialize(self.value) if isinstance(self.value, datetime) else self.value,
            "formula": self.formula,
            "dependencies": [dep.coordinate for dep in self.dependencies]
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def update_value(self, new_formula):
        if new_formula.startswith('='):
            self.formula = new_formula
        else:
            self.value = new_formula

    def __repr__(self):
        return (f"CellModel(coordinate={self.coordinate}, value={self.value}, "
                f"formula={self.formula}, dependencies={self.dependencies})")

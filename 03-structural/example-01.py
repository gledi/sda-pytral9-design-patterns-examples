class Container:
    def __init__(self, elem):
        self.elements = list(range(elem))

    def __repr__(self):
        return f"<Container ({len(self.elements)} elem)>"


class DictAdapter:
    def __init__(self, d):
        self.d = d

    def __repr__(self):
        return f"<Container ({len(self.d)} elem)>"


containers = [Container(1), Container(2), DictAdapter({"A": 1})]
print(containers)

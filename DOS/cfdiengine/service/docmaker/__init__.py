from misc.factory import Factory
from docmaker.builders.xml import FacXml

class BuilderFactory(Factory):
    """
    """
    def __init__(self):
        super().__init__()
        self.subscribe('facxml', FacXml())

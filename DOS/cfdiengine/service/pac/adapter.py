from abc import ABCMeta, abstractmethod
from .error import AdapterError


class Adapter(metaclass=ABCMeta):
    """
    Template class for any pac's adapter
    """

    def __init__(self, logger, pac_name):
        self.logger = logger
        self.pac_name = pac_name

    @abstractmethod
    def stamp(self, xml, xid):
        """
        Signature using XML with alternative id
        signed by the client
        """

    @abstractmethod
    def fetch(self, xid):
        """
        Fetching a cfdi by using alternative id
        """

    @abstractmethod
    def cancel(self, xml, emisor):
        """
        Cancel using XML signed by the client
        """

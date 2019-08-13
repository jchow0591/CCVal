from enum import Enum


class SuperpowerFlavor:
    LOUNGE = 1
    AIRLINE_STATUS = 2
    HOTEL_STATUS = 3
    AIRLINE_PERK = 4
    HOTEL_PERK = 5


class Superpower:
    def __init__(self,
                 name: str,
                 flavor: SuperpowerFlavor,
                 description: str = None,
                 value: float = 0.0):
        """[summary]
        A superpower is an added status or perk that does 
        not have a direct monetary value but usually scales with increased perk usage
        
        Parameters
        ----------
        name : str
            name of the perk
        flavor : SuperpowerFlavor
            the type of benefit provided by the superpower
        description : str, optional
            A short description about the superpower, by default None
        value : float, optional
            Personal valuation of the perk, by default 0.0
        """
        self.name = name
        self.flavor = flavor
        self.description = description
        self.value = value

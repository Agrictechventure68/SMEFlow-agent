class SMEAgent:
    """Basic SMEFlow agent class"""

    def _init_(self, name: str, sector: str):
        self.name = name
        self.sector = sector

    def introduce(self) -> str:
        return f"I am SMEFlow Agent for {self.name} in the {self.sector} sector."
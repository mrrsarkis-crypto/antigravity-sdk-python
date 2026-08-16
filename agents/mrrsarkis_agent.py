"""
Example agent contributed by mrrsarkis-crypto.
Replace or extend this with your agent implementation.
"""

from typing import Dict, Any

class ExampleAgent:
    """A minimal example agent for demonstration and testing.

    The real antigravity SDK provides richer interfaces — adapt this
    skeleton to the project's agent base classes when integrating.
    """
    def __init__(self, name: str = "mrrsarkis-agent"):
        self.name = name

    def act(self, observation: Dict[str, Any]) -> Dict[str, Any]:
        """Return a simple action based on the observation.

        This is a placeholder implementation; replace with real logic.
        """
        # Echo the observation back as the 'action' for testing.
        return {"agent": self.name, "action": observation}


if __name__ == "__main__":
    a = ExampleAgent()
    print(a.act({"hello": "world"}))

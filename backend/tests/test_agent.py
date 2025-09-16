import pytest
from models.agent import SMEAgent

def test_agent_intro():
    agent = SMEAgent("Bright Doro Ltd", "Agriculture")
    assert "Agriculture" in agent.introduce()
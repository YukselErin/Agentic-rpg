from models import GameState

class PersonalityAgent:
    def __init__(self, prompt: str):
        self.prompt = prompt

    def generate_intention(self, game_state: GameState) -> str:
        # Placeholder for intention generation
        return f"Based on being {self.prompt}, I want to explore."

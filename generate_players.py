
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "players_1000.jsonl"

positions = ["P", "C", "1B", "2B", "3B", "SS", "OF"]

players = []

# Generate 1,000 players
for i in range(1, 1001):

    player = {
        "id": i,
        "name": f"Player {i}",
        "team": "Muskingum",
        "position": positions[(i - 1) % len(positions)]
    }

    players.append(player)

# Save records
with open(DATA_FILE, "w", encoding="utf-8") as file:
    for player in players:
        file.write(json.dumps(player) + "\n")

print(f"Successfully generated {len(players)} players!")

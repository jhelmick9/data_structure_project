
import json
from pathlib import Path
from Bst import BinarySearchTree

# Location where player records will be stored
DATA_FILE = Path(__file__).parent / "players_1000.jsonl"

# baseball players
players = [
    {"id": 1, "name": "Jayden Helmick", "team": "Muskingum", "position": "P"},
    {"id": 2, "name": "Noah Winland", "team": "Muskingum", "position": "SS"},
    {"id": 3, "name": "Weston Hartman", "team": "Muskingum", "position": "1B"}
]

# Create the file
if not DATA_FILE.exists():
    raise FileNotFoundError(
        "Run generate_data.py first to create the database."
    )

# Load records
with open(DATA_FILE, "r", encoding="utf-8") as file:
    stored_players = [json.loads(line) for line in file]

print(f"Loaded {len(stored_players)} players:")




# Linear Search 
def linear_search(players, target_id):

    comparisons = 0

    for player in players:
        comparisons += 1

        if player["id"] == target_id:
            return player, comparisons

    return None, comparisons


search_id = int(input("Enter a Player ID to search for: "))

result, comparisons = linear_search(stored_players, search_id)

if result:
    print("Player Found!")
    print(result)
else:
    print("Player not found.")

print(f"Total comparisons: {comparisons}")




from Bst import BinarySearchTree

# Build Binary Search Tree
bst = BinarySearchTree()

# Sort players by their ID
sorted_players = sorted(stored_players, key=lambda player: player["id"])

# Build a balanced binary search tree
def build_balanced_tree(players):
    if not players:
        return

    middle = len(players) // 2

    bst.insert(players[middle])

    build_balanced_tree(players[:middle])
    build_balanced_tree(players[middle + 1:])

build_balanced_tree(sorted_players)


# BST
bst_result, bst_comparisons = bst.search(search_id)

print("\n--- BST Search Results ---")

if bst_result is not None:
    print("Player Found!")
    print(bst_result)
else:
    print("Player not found.")

print(f"BST Comparisons: {bst_comparisons}")


# Make sure both search algorithms return the same result
print("\n--- Verification ---")

if result == bst_result:
    print("Both algorithms returned the same result")
else:
    print("Search results do not match!")

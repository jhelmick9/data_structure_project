
class Node:
    def __init__(self, player):
        self.player_id = player["id"]
        self.player = player
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, player):
        player_id = player["id"]
        new_node = Node(player)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if player_id < current.player_id:
                if current.left is None:
                    current.left = new_node
                    return

                current = current.left

            elif player_id > current.player_id:
                if current.right is None:
                    current.right = new_node
                    return

                current = current.right

            else:
                return

    def search(self, target_id):
        current = self.root
        comparisons = 0

        while current is not None:
            comparisons += 1

            if target_id == current.player_id:
                return current.player, comparisons

            elif target_id < current.player_id:
                current = current.left

            else:
                current = current.right

        return None, comparisons


# Test 
if __name__ == "__main__":
    bst = BinarySearchTree()

    test_players = [
        {"id": 50, "name": "Player 50"},
        {"id": 30, "name": "Player 30"},
        {"id": 70, "name": "Player 70"},
        {"id": 20, "name": "Player 20"},
        {"id": 40, "name": "Player 40"}
    ]

    for player in test_players:
        bst.insert(player)

    result, comparisons = bst.search(40)

    print("Player Found:", result)
    print("Comparisons:", comparisons)

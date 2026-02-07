class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hash_map = {" ": " "}
        letters = "abcdefghijklmnopqrstuvwxyz"
        j = 0
        for c in key:
            if c not in hash_map:
                hash_map[c], j = letters[j], j + 1
        return "".join(hash_map[c] for c in message)
        
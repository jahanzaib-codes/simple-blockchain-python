import hashlib
import time
import json

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        # Initialize a block with index, transactions, timestamp, and previous hash
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Calculate SHA-256 hash of the block for integrity
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        # Initialize blockchain with a genesis block and set difficulty
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Number of leading zeros for proof-of-work
        self.pending_transactions = []

    def create_genesis_block(self):
        # Create the first block in the chain (genesis block)
        return Block(0, [], time.time(), "0")

    def get_latest_block(self):
        # Return the most recent block in the chain
        return self.chain[-1]

    def add_block(self, transactions):
        # Create and mine a new block, then add it to the chain
        new_block = Block(
            index=len(self.chain),
            transactions=transactions,
            timestamp=time.time(),
            previous_hash=self.get_latest_block().hash
        )
        new_block.hash = self.proof_of_work(new_block)
        self.chain.append(new_block)
        self.pending_transactions = []

    def proof_of_work(self, block):
        # Mine the block by finding a hash with required leading zeros
        while block.hash[:self.difficulty] != "0" * self.difficulty:
            block.nonce += 1
            block.hash = block.calculate_hash()
        return block.hash

    def add_transaction(self, sender, recipient, amount):
        # Add a transaction to the pending transactions list
        self.pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })

    def is_chain_valid(self):
        # Validate the blockchain by checking block hashes and proof-of-work
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

            if current_block.hash[:self.difficulty] != "0" * self.difficulty:
                return False
        return True

    def to_json(self):
        # Export the blockchain as a JSON-compatible dictionary
        return [{"index": block.index, "transactions": block.transactions, "timestamp": block.timestamp, 
                 "previous_hash": block.previous_hash, "hash": block.hash, "nonce": block.nonce} 
                for block in self.chain]

# Example usage for testing the blockchain
if __name__ == "__main__":
    my_blockchain = Blockchain()

    # Add sample transactions
    my_blockchain.add_transaction("Alice", "Bob", 50)
    my_blockchain.add_transaction("Bob", "Charlie", 30)
    
    # Mine the first block
    print("Mining block 1...")
    my_blockchain.add_block(my_blockchain.pending_transactions)
    
    # Add more transactions
    my_blockchain.add_transaction("Charlie", "Alice", 20)
    
    # Mine the second block
    print("Mining block 2...")
    my_blockchain.add_block(my_blockchain.pending_transactions)
    
    # Export blockchain to JSON for web integration
    with open("blockchain_data.json", "w") as f:
        json.dump(my_blockchain.to_json(), f, indent=4)
    
    # Display blockchain
    for block in my_blockchain.chain:
        print(f"\nBlock #{block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Transactions: {block.transactions}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print(f"Nonce: {block.nonce}")

    # Validate the blockchain
    print("\nIs blockchain valid?", my_blockchain.is_chain_valid())
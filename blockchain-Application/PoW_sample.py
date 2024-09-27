import hashlib
import json
import time

# Transaction list
transactions = [
    "[3, 4, 5, 6]",
    "[4, 5, 6, 7]",
    "[5, 6, 7, 8]",
    "[6, 7, 8, 9]",
    "[7, 8, 9, 10]",
    "[8, 9, 10, 11]",
    "[9, 10, 11, 12]",
    "[10, 11, 12, 13]",
    "[11, 12, 13, 14]",
    "[12, 13, 14, 15]"
]

# Function to compute SHA256 hash
def compute_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Function to find the nonce value satisfying the difficulty
def find_nonce(block_data, difficulty):
    nonce = 0
    while True:
        temp_data = block_data + str(nonce)
        hash_result = compute_hash(temp_data)
        if hash_result <= difficulty:
            return nonce, hash_result
        nonce += 1

# Function to set the mining difficulty
def set_difficulty(difficulty_bits):
    target = '0' * (difficulty_bits // 4)
    target += 'f' * (64 - (difficulty_bits // 4))
    return target

# Function to create a block
def create_block(block_number, previous_hash, transaction, difficulty):
    block_data = {
        "Block number": block_number,
        "Previous Hash": previous_hash,
        "Transaction": transaction
    }

    # Find Nonce and corresponding Hash with the given difficulty
    block_str = json.dumps(block_data, sort_keys=True)
    nonce, block_hash = find_nonce(block_str, difficulty)

    # Store Nonce and final Hash in the block
    block_data["Nonce"] = nonce
    block_data["Hash"] = block_hash

    # Save the block as a JSON file
    with open(f'{block_number}.json', 'w') as f:
        json.dump(block_data, f, indent=4)

    # Return the block's hash for the next block to reference
    return block_hash

# Function to create the Genesis block
def create_genesis_block():
    genesis_block = {
        "Block number": 0,
        "Previous Hash": None,  # No previous hash for the Genesis block
        "Transaction": "",
        "Nonce": 0,
        "Hash": "Genesis"
    }

    # Save the Genesis block as a JSON file
    with open('0.json', 'w') as f:
        json.dump(genesis_block, f, indent=4)

    # Compute and return the hash of the Genesis block
    return compute_hash(json.dumps(genesis_block, sort_keys=True))

# Function to verify the blockchain
def verify_block_chain():
    for i in range(1, 11):
        with open(f'{i}.json', 'r') as f:
            block = json.load(f)
            # Reconstruct block data without 'Nonce' and 'Hash'
            block_data = {
                "Block number": block["Block number"],
                "Previous Hash": block["Previous Hash"],
                "Transaction": block["Transaction"]
            }
            block_str = json.dumps(block_data, sort_keys=True)
            temp_data = block_str + str(block["Nonce"])
            calculated_hash = compute_hash(temp_data)
            print(f"Block {i} calculated hash: {calculated_hash}")  # Debug output

            # Verify that the calculated hash matches the stored hash
            if calculated_hash != block["Hash"]:
                print(f"Block {i} has invalid hash!")
                return False

            # Verify that the calculated hash matches the next block's Previous Hash
            if i < 10:
                with open(f'{i+1}.json', 'r') as f_next:
                    next_block = json.load(f_next)
                    print(f"Block {i+1} previous hash: {next_block['Previous Hash']}")  # Debug output
                    if next_block["Previous Hash"] != calculated_hash:
                        print(f"Block {i} and {i+1} do not match!")
                        return False
    print("All blocks verified!")
    return True

# Function to modify a transaction in a block
def modify_transaction(block_number, new_transaction):
    with open(f'{block_number}.json', 'r+') as f:
        block = json.load(f)
        block["Transaction"] = new_transaction
        f.seek(0)
        json.dump(block, f, indent=4)
        f.truncate()

# Function to run the blockchain creation and verification
def run_blockchain():
    # Set the mining difficulty (e.g., 18 leading zero bits)
    difficulty = set_difficulty(18)

    # Create the Genesis block
    previous_hash = create_genesis_block()

    # Create the next 10 blocks with the specified difficulty
    for i in range(1, 11):
        transaction = transactions[i - 1]
        previous_hash = create_block(i, previous_hash, transaction, difficulty)

    # Modify a transaction in the middle (e.g., modify the 5th block)
    modify_transaction(5, "[Modified Transaction]")

    # Run blockchain verification
    verify_block_chain()

# Execute the code
start_time = time.time()
run_blockchain()
end_time = time.time()

# Print the total time taken to create all blocks
print(f"Time to create all blocks: {end_time - start_time} seconds")

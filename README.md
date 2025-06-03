# Simple Blockchain Implementation in Python

## Overview
This project is a simple blockchain implementation in Python, demonstrating core blockchain concepts such as block creation, proof-of-work, and transaction handling. It includes a web interface built with HTML, CSS, and JavaScript to visualize the blockchain data, making it an excellent portfolio piece for showcasing blockchain development skills.

## Features
- **Block Creation**: Each block contains an index, transactions, timestamp, previous hash, and current hash.
- **Proof-of-Work**: Implements a simple mining mechanism requiring a hash with a specified number of leading zeros.
- **Transaction Handling**: Supports adding transactions to blocks.
- **Chain Validation**: Ensures the integrity of the blockchain by validating hashes and chain continuity.
- **Web Interface**: A clean, user-friendly interface to display blockchain data, loaded from a JSON export.

## Prerequisites
- Python 3.6 or higher
- A modern web browser (for the web interface)
- No external Python libraries are required

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jahanzaib-codes/simple-blockchain-python.git
   cd simple-blockchain-python
   ```
2. Run the Python script to generate blockchain data:
   ```bash
   python blockchain.py
   ```
   This will create a `blockchain_data.json` file with sample blockchain data.

3. Open `index.html` in a web browser to view the blockchain explorer.

## Usage
- Run `blockchain.py` to generate and mine blocks with sample transactions.
- The script exports the blockchain to `blockchain_data.json`.
- Open `index.html` to see a web-based visualization of the blockchain.

## Example Output
When you run `blockchain.py`, you will see console output like:
```
Mining block 1...
Mining block 2...

Block #0
Timestamp: 1625149200.123456
Transactions: []
Previous Hash: 0
Hash: 0000abcd...
Nonce: 123

Block #1
Timestamp: 1625149205.456789
Transactions: [{"sender": "Alice", "recipient": "Bob", "amount": 50}, {"sender": "Bob", "recipient": "Charlie", "amount": 30}]
Previous Hash: 0000abcd...
Hash: 0000efgh...
Nonce: 456

Is blockchain valid? True
```

The web interface displays the same data in a clean, formatted way.

## Potential Use Cases
- **Cryptocurrency**: Basis for a simple token system.
- **Supply Chain**: Track goods with transparent, immutable records.
- **Smart Contracts**: Foundation for decentralized applications.
- **Educational Tool**: Teach blockchain concepts to beginners.

## Folder Structure
```
simple-blockchain-python/
├── blockchain.py       # Core blockchain implementation
├── index.html          # Web interface for blockchain explorer
├── styles.css          # Styling for the web interface
├── script.js           # JavaScript for loading and displaying blockchain data
├── blockchain_data.json # Generated JSON file with blockchain data
└── README.md           # Project documentation
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For inquiries or collaboration opportunities, reach out via jahanzaib.remotehub@gmail.com or on GitHub.

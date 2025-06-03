document.addEventListener("DOMContentLoaded", () => {
    fetch("blockchain_data.json")
        .then(response => response.json())
        .then(data => {
            const blockchainDiv = document.getElementById("blockchain");
            data.forEach(block => {
                const blockDiv = document.createElement("div");
                blockDiv.className = "block";
                blockDiv.innerHTML = `
                    <h3>Block #${block.index}</h3>
                    <p><strong>Timestamp:</strong> ${new Date(block.timestamp * 1000).toLocaleString()}</p>
                    <p><strong>Transactions:</strong> ${JSON.stringify(block.transactions)}</p>
                    <p><strong>Previous Hash:</strong> ${block.previous_hash}</p>
                    <p><strong>Hash:</strong> ${block.hash}</p>
                    <p><strong>Nonce:</strong> ${block.nonce}</p>
                `;
                blockchainDiv.appendChild(blockDiv);
            });
        })
        .catch(error => console.error("Error loading blockchain data:", error));
});
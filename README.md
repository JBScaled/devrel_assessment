# devrel_assessment

This project was built using Algokit!

To learn more about algokit, visit [documentation](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/algokit.md).

## Modified hello_world

I followed the tutorial you can find here: [AlgoKit Quick Start Guide](https://developer.algorand.org/docs/get-started/algokit/), 
and then made some modifications to the hello_world starter code. Firstly I created a BoxMap to the storage space of the contract. 
Then I modified the hello method to take in an additional parameter alongside the message. hello() then stores the message under 
a key with the name of that additional parameter. Lastly, I created a new method that allows anyone to retrieve any message stored
in the BoxMap as long as they know the Base64 encoded key name. 

## Deployed using Lora
[Lora](https://lora.algokit.io/testnet) was a great tool for interacting with a local blockchain instance while I prepared the contract.
and once it was ready I was easily able to switch over to the Algorand Testnet and deploy the contract there.

Link to the [Contract Deployment transaction](https://lora.algokit.io/testnet/transaction/R5DSSTWBVUQ4X7IJH5W2IB3U6NFF5IR6W76L2SL55SJYK4TYOKJQ)

Link to the [first successful hello() call](https://lora.algokit.io/testnet/transaction/3Q3IS2M73BEQJZX57EUBYH5EKTMWMHWYPJAKHSSMPIEXJ7K3RG3Q)

![Screen Shot 2025-02-14 at 6 00 03 AM](https://github.com/user-attachments/assets/8dccc681-815d-4c00-9976-8b05bfb5485d)

It's worth mentioning that in order to store and retrieve data from the BoxMap it was necessary to pass in a reference to its storage location. 
Lora allowed me to do that by opening up the Edit Resources modal.

![Screen Shot 2025-02-14 at 6 34 13 AM](https://github.com/user-attachments/assets/062c4edf-0f90-4e28-85a1-f69fd289b4c1)

Through the modal, I was able to pass in the App ID and the Base64 encoded key name required to identify the storage location. 

![Screen Shot 2025-02-14 at 6 02 49 AM](https://github.com/user-attachments/assets/af987dc4-a164-45e3-898b-d3529e0fc1db)

## Next Steps
Currently, anyone can call the hello method to store any number of messages without paying for the data to be stored. As a workaround I manually 
funded the contract address to support this storage cost, but as a next step it would be interesting to calculate this cost beforehand and have the 
method caller also send the ALGO required to secure the storage to the contract. 





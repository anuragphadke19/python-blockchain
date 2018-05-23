# Introduction

This is an attempt to learn python and basic blockchain and crypto concepts with the help of a udemy course. This readme will serve as running notes for my project as I go along the course and hopefully by the end of it have a running blockchain of my own with digital wallet, hashing, validation and the whole shebang.

## What is a Blockchain?

Blockchain is a list of blocks. A block consists of a list of transactions. A transaction, typically between 2 parties, could be be potentially anything. It could be transfer of money (in this case digital currency), it could be a digital contract where the parties agree to certain terms etc. The use cases are potentially endless. 

A block also contains a referenece to the previous block (thus the name blockchain), typically a hash of the previous block. A hash is a mathematical representation of the transaction. The unique quality being, if there is even a slight modification in the transaction, for eg. if some one tries to modify the amount or the reciever of the transaction, the hash will change. This way the current block can always know if any of the previous blocks have been tampered with by comparing the hash value it has with a newly generated hash value for the previous block. This mechanism ensures that once a block is created it cannot be tampered with at any time in the future, thereby ensuring sanctity of a transaction.

----

## Elements of a Blockchain
##### Transaction

A transaction will consist of a sender, a receiver and an amount. Implemented as a python dictionary as we can have name value pairs for the elements. The order of those elements doesn't matter and it is mutable.

##### Block

A block will consist of a hash of the previous block, an index and the transactions. Implemented as a python dictionary as we can label the elements. The order doesn't matter and it is mutable.

##### Blockchain

A blockchain will consist of a list of blocks. Implemented as a python list as the order matters and it is mutable and can have duplicates

##### List of parties

A list of parties will consist of the names/identifies of the participants in the transaction. Implemented as a puthon set as this needs to hold unique elements


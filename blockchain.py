# Initializing our blockchain list
MINING_REWARD = 10

genesis_block={
        'previous_hash': '',
        'index': 0,
        'transactions': []
    }
blockchain = [genesis_block]
open_transactions = []
owner = 'Neo'
participants = {owner}


def get_last_blockchain_value():
    ''' Returns the lst blockchain value '''
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def get_balance(participant):
    amount_sent = 0
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    amount_received = 0
    tx_receiver = [[tx['amount'] for tx in block['transactions'] if tx['receiver'] == participant] for block in blockchain]
    for tx in tx_receiver:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


def hash_block(block):
    return '-'.join(str(block[key]) for key in block)


def add_transaction(receiver, sender=owner, amount=1.0):
    ''' Appends the last transaction amount to the blockchain list 
        Arguments :
            :sender: The sender of the coins
            :reciever: The reciever of the transaction 
            :amount: Amount of coins being sent in the transaction (default = 1.0)
    '''
    transaction = {
        'sender': sender,
        'receiver': receiver,
        'amount': amount
    }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(receiver)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    
    reward_transaction = {
        'sender': 'MINING',
        'receiver': owner,
        'amount': MINING_REWARD
    }
    open_transactions.append(reward_transaction)
    print(hashed_block)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    ''' return the transaction amount as entered by the user'''
    tx_reciver = input('Enter the reciever of the transaction: ')
    tx_amount = float(input('Enter the number of coins in the the transaction: ')) 
    return tx_reciver, tx_amount  

def get_user_choice():
    user_input = input('Your choice :')
    return user_input


def print_blockchain_elements():
    #Output the blockchain to the console
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-' * 20)


def verify_blockchain():
    # Verify that the blockchain has not been manipulated
    for (index,block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True

waiting_for_input = True

while waiting_for_input:
    print('Please choose :')
    print('1: Add a new transaction value')
    print('2: Mine a block')
    print('3: Output the blockchain blocks')
    print('4: Output the participants')
    print('h: Manipulate the blockchain')
    print('q: Quit')
    
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data =  get_transaction_value()
        receiver, amount = tx_data
        add_transaction(receiver, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
        print(get_balance('Neo'))
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >=1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Tom', 'reciever':'Dick', 'amount': 100}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    print('Choice registered!')
    if not verify_blockchain():
        print_blockchain_elements()
        print("You have been hacked. The blockchain is invalid now.")
        break
else:
    print("Peace out!!")


print('Done!')
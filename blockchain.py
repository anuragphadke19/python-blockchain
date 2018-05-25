# Initializing our blockchain list
genesis_block={
        'previous_hash': '',
        'index': 0,
        'transactions': []
    }
blockchain = [genesis_block]
open_transactions = []
owner = 'Neo'

def get_last_blockchain_value():
    ''' Returns the lst blockchain value '''
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(reciever, sender=owner, amount=1.0):
    ''' Appends the last transaction amount to the blockchain list 
        Arguments :
            :sender: The sender of the coins
            :reciever: The reciever of the transaction 
            :amount: Amount of coins being sent in the transaction (default = 1.0)
    '''
    transaction = {
        'sender': sender,
        'receiver': reciever,
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = ''
    for key in last_block:
        value = last_block[key]
        hashed_block = hashed_block + str(value)
    print(hashed_block)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)


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
    is_valid = True
    #block_index = 0
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    """ for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1 """
    return is_valid

waiting_for_input = True

while waiting_for_input:
    print('Please choose :')
    print('1: Add a new transaction value')
    print('2: Mine a block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the blockchain')
    print('q: Quit')
    
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data =  get_transaction_value()
        reciever, amount = tx_data
        add_transaction(reciever, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >=1:
            blockchain[0] = [[2]]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    print('Choice registered!')
    # if not verify_blockchain():
    #     print_blockchain_elements()
    #     print("You have been hacked. The blockchain is invalid now.")
    #     break
else:
    print("Peace out!!")


print('Done!')
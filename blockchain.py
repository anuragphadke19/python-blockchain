# Initializing our blockchain list
blockchain = []

def get_last_blockchain_value():
    ''' Returns the lst blockchain value '''
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    ''' Appends the last transaction amount to the blockchain list 
        Arguments :
            :transaction_amount : Float transaction amount
            :last_transaction : last tranaction from the blockchain list, default = [1] '''
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    ''' return the transaction amount as entered by the user'''
    return float(input('Your last transaction amount please: '))   

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
    print('2: Output the blockchain blocks')
    print('h: Manipulate the blockchain')
    print('q: Quit')
    
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount =  get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >=1:
            blockchain[0] = [[2]]
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
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



while True:
    print('Please choose :')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount =  get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')
    print('Choice registered!')


print('Done!')
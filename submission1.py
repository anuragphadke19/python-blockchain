name = 'Neo'
age = 35


def combine_name_age():
    ''' Combine the variable name and age'''
    print(str(name) + str(age))


def combine_data(value_1, value_2):
    ''' Combine any two given values as string 
        Arguments:
            : value_1: first value
            : value_2: second value'''
    print(str(value_1) + str(value_2))

def decades_you_lived(your_age):
    ''' Prints the number of decades for a given age.
        For eg. 2 decades for 23
        Argument:
            :your_age : Age entered by the user'''
    decades = your_age//10
    print(str(decades) + ' decades')

combine_name_age()
combine_data('Peter' , 'rabbit')

your_age = input('Enter your age :')
decades_you_lived(int(your_age))

def main():
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """
    result = True
    
    if(email[0:1].isalpha() == False):
        result = False
        
    if(email.length() < 6 or email.length() > 29):
        result = False
        

        
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()

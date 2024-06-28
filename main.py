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
        
    if(len(email) < 6 or len(email) > 29):
        result = False
    
    if(email.find("@") < 0):
        result = False
        

    if(email[email.find("@"):len(email)].find(".") < 0):
        result = False

    print(result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()

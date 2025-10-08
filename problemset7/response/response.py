from validator_collection import validators

def main():
    emailAddress = input("What's your email address? ")
    try:
        isValid = validators.email(emailAddress)
        print('Valid')
    except:
        print('Invalid')

if __name__ == '__main__':
    main()



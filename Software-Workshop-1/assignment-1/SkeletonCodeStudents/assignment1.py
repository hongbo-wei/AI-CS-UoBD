def clean_up():
    """
        f refers to text_to_clean.txt
        sf refers to student_names.txt
        use text to read in the appropriate file
        cleaned is used store the wanted characters
        :return: cleaned
        """
    f = open('text_to_clean.txt', 'r')
    sf = open('student_names.txt', 'w')
    text = f.read()
    cleaned = ""
    # lower case char, upper case char, blank, full stop - valid characters
    # insert code here to clean the file as per question 1
    names = text.split('\n')
    for name in names:
        for char in name:
        # use methods and ASCII table to filter character we want
            if (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90) or ord(char) == 32 or ord(char) == 46:
                cleaned += char
        cleaned += '\n'
    sf.write(cleaned)
    # close files when finished
    f.close()
    sf.close()
    return cleaned


def build_id():
    """
    f refers to the student_names.txt file created in clean_up()
    id_list is the list return with the id's created from the name / surname of each student
    :return: id_list
    """
    f = open('student_names.txt', 'r')
    id_list = []
    #insert code here to create the id's as per question 2
    text = f.read()
    names = text.split('\n')
    for name in names:
        part = list(name.split())
        # if the name consists of 3 parts
        if len(part) == 3:
            id = part[0][0].lower() + part[1][0].lower() + part[2][0].lower()
            id_list.append(id)
        # if the name consists of 2 parts
        elif len(part) == 2:
            id = part[0][0].lower() + 'x' + part[1][0].lower()
            id_list.append(id)
    # close files when finished
    f.close()
    return id_list


def validate_password(password):
    """
    illegal_password is the list that is built up showing the invalid parts of the password
    Validate the password to verify if it is legal or not as per Question 3
    There is a password.txt file given to you to verify invalid passwords
    :param password: make use of the password found in main(), the test file will also have additional passwords to test
    :return: illegal_password
    """
    illegal_password = []
    #insert code here to validate all the conditions of the password as per question 3
    # check for length
    if len(password) < 8:
        illegal_password.append("TOO SHORT")
    elif len(password) > 12:
        illegal_password.append("TOO LONG")
    
    # check for illegal characters
    for char in password:
        if (ord(char.lower()) < 97 or ord(char.lower()) > 122) and not char.isdigit() and char != '_':
            illegal_password.append("WRONG CHARACTERS")
        
    # check for mixed case
    has_lower = False
    has_upper = False
    for char in password:
        if char.islower():
            has_lower = True
            continue
        elif ord(char) >= 65 and ord(char) <= 90:
            has_upper = True
            continue
        if has_lower and has_upper:
            break
    if not has_lower or not has_upper:
        illegal_password.append("NOT MIXED CASE")
    
    # check if the password starts with a digit
    if password[0].isdigit():
        illegal_password.append("LEADING DIGIT")
    
    # check if the password can be found in password.txt
    with open('password.txt', 'r') as file:
        common_passwords = file.read().split('\n')
        for common_password in common_passwords:
            if password == common_password:
                illegal_password.append("CANNOT MAKE USE OF THIS PASSWORD")
    return illegal_password


def create_unique(id_list):
    """
    Adhere to the instructions in question 4 to determine a unique id for each student
    Write the content of the unique ids to the file unique_ids.txt - open / close the file correctly
    Write the content of the emails created to the file create_emails.txt - - open / close the file correctly
    :param id_list: the id_list that was returned in build_id() is used here to create the unique ids
    :return: final_list is returned and this list contains all of the unique student ids
    """
    final_list = []
    # insert code here to create unique ids
    id_suffixes = {}
    id_suffixes_list = []
    for id in id_list:
        if id not in id_suffixes:
            id_suffixes[id] = 0
            final_list.append(f"{id}0000")
        else:
            id_suffixes[id] += 1
            id_suffixes_list.append(f"{id}{id_suffixes[id]:04}") # Append a unique ID with leading zeros
    
    for id in id_suffixes_list:
        final_list.append(id)
    # store unique ids
    with open('unique_ids.txt', 'w') as file_id:
        for id in final_list:
            id += '\n'
            file_id.write(id)
    
    # store the eamil address of each id
    with open('create_emails.txt', 'w') as file_id:
        for id in final_list:
            id += "@student.bham.ac.uk\n"
            file_id.write(id)

    return final_list


def create_short_address():
    """
    Open the addresses.txt file correctly where f = the file to be opened
    split the address up so that only the first part and the postcode make up the shorter address
    :return: split_addrs is returned where the address1, postcode make up the list - this list is used for validate_pcode()
    """
    f = open('addresses.txt', 'r')
    text = f.read()
    split_addrs = []
    # insert code here to create the shorter address
    split_text = text.split('\n')
    for addr in split_text:
        # in case of blank line
        if len(addr) != 0:
            addr = addr.split(',')
            li = []
            # append address1
            li.append(addr[0])
            # append postcode
            li.append(addr[3][1:])
            split_addrs.append(li)       
    
    f.close()
    return split_addrs


def validate_pcode(split_addrs):
    """
    This function validates each character of the postcode
    :param split_addrs: this is passed from main(), obtained from the function create_short_address()
    :return: validate_pcode is a list that contains True False values for each postcode that is validated - see question 6
    """
    validate_pcode = []
    # insert code here to validate each character of the postcode
    count = 0
    for addr in split_addrs:
        # assign a unique number to each postcode validation
        validate_pcode.append(count)
        count += 1

        # Verify the length of the postcode
        if len(addr[1]) == 6:
            validate_pcode.append("True")
        else:
            addr[1] = "$$$$$$"
            validate_pcode.append("False")

        # check if the first character is in upper case
        if addr[1][0] >= 'A' and addr[1][0] <= 'Z':
            validate_pcode.append("True")
        else:
            validate_pcode.append("False")

        # check if the 2nd~4th characters are numbers
        flag = "False"
        for number in addr[1][1:3]:
            if number.isdigit():
                flag = "True"
            else:
                flag = "False"
        validate_pcode.append(flag)


        # check if the last 2 characters are in upper case
        flag = 'False'
        for number in addr[1][4:]:
            if number >= 'A' and number <='Z':
                flag = "True"
            else:
                flag = "False"
        validate_pcode.append(flag)
    return validate_pcode


def ids_addrs(short_addr):
    """
    This function reads in the unique_ids.txt file as f and creates a dictionary based on the id and the short address
    :param short_addr: passed in from main() - generated from create_short_address()
    :return: combo is the key / value pair, i.e. unique id and the short addr for each student
    """
    f = open("unique_ids.txt", 'r')
    ids = f.read()
    combo = {}
    # insert code here to create combo
    ids = ids.split()
    index = 0
    for id in ids:
        combo[id] = short_addr[index]
        index += 1

    f.close()
    return combo


def main():
    id_list = []
    while True:
        print("\nStudent File Menu:")
        print("1. Perform clean up operation")
        print("2. Create ID's")
        print("3. Validate a Password")
        print("4. Create unique ID's")
        print("5. Reduce addresses")
        print("6. Validate postcode")
        print("7. Create ID with short address")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            clean_up()
        elif choice == '2':
            id_list = build_id()
        elif choice == '3':
            validate_password("1abcDE%")
        elif choice == '4':
            create_unique(id_list)
        elif choice == '5':
            short_addr = create_short_address()
        elif choice == '6':
            validate_pcode(short_addr)
        elif choice == '7':
            ids_addrs(short_addr)
        elif choice == '8':
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()




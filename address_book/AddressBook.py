class AddressBook:
    def __init__(self):
        """
        Description:This method (constructor) is used to initialised the variables.
        """
        self._first_name = None
        self._last_name = None
        self._address = None
        self._city = None
        self._state = None
        self._pin_code = None
        self._phone_number = None

    def insert_data(self):
        """
        Description: This method is used to insert the details into the Address Book.
        :return: None
        """
        print('\nEnter the following details :-')
        self._first_name = input('First Name : ')
        self._last_name = input('Last Name : ')
        self._address = input('Address : ')
        self._city = input('City : ')
        self._state = input('State : ')
        self._pin_code = input('Pin Code : ')
        self._phone_number = input('Phone Number : ')
        self.save_data()
        print('\nAll Details Inserted Successfully!')

    def update_data(self, option):
        """
        Description: This function is used to update the previous information of Address Book.
        :return: None
        """
        if option == 1:
            print('First Name : ', self._first_name)
            self._first_name = input('Updated First Name : ')
            self.save_data()
        elif option == 2:
            print('First Name : ', self._last_name)
            self._last_name = input('Updated Last Name : ')
            self.save_data()
        elif option == 3:
            print('Address : ', self._address)
            self._address = input('Updated Address : ')
            self.save_data()
        elif option == 4:
            print('City : ', self._city)
            self._city = input('Updated City : ')
            self.save_data()
        elif option == 5:
            print('State : ', self._state)
            self._state = input('Updated State : ')
            self.save_data()
        elif option == 6:
            print('Pin Code : ', self._pin_code)
            self._pin_code = input('Updated Pin Code : ')
            self.save_data()
        elif option == 7:
            print('Phone Number : ', self._phone_number)
            self._phone_number = input('Updated Phone Number : ')
            self.save_data()
        else:
            print('Invalid Input! Please try again...')
            self.update_data(option)

    def delete_data(self, option):
        """
        Description: This function is used to delete any specific data.
        :return: None
        """
        if option == 1:
            print('First Name : ', self._first_name, ' (Deleted)')
            self._first_name = ''
            self.save_data()
        elif option == 2:
            print('Last Name : ', self._last_name, ' (Deleted)')
            self._last_name = ''
            self.save_data()
        elif option == 3:
            print('Address : ', self._address, ' (Deleted)')
            self._address = ''
            self.save_data()
        elif option == 4:
            print('City : ', self._city, ' (Deleted)')
            self._city = ''
            self.save_data()
        elif option == 5:
            print('State : ', self._state, ' (Deleted)')
            self._state = ''
            self.save_data()
        elif option == 6:
            print('Pin Code : ', self._pin_code, ' (Deleted)')
            self._pin_code = ''
            self.save_data()
        elif option == 7:
            print('Phone Number : ', self._phone_number, ' (Deleted)')
            self._phone_number = ''
            self.save_data()
        else:
            print('Invalid Input! Please try again...')
            self.update_data(option)

    def save_data(self):
        """
        Description: This function save all the information into the Address Book.
        :return: None
        """
        file = open('address_book.txt', 'w')
        list_of_data = [
            ['First Name : ', self._first_name],
            ['\nLast Name : ', self._last_name],
            ['\nAddress : ', self._address],
            ['\nCity : ', self._city],
            ['\nState : ', self._state],
            ['\nPin Code : ', self._pin_code],
            ['\nPhone Number : ', self._phone_number, '\n']
        ]
        for data in list_of_data:
            for information in data:
                file.write(information)
        file.close()

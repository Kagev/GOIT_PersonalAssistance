import sys
import re
import pickle
import json
import csv


from datetime import datetime
from collections import UserDict


from text_fields import MethodsText, ErrorsText


# METHODS
class Field:
    def __init__(self, value) -> None:
        self.__value = None
        self.value = value

    @property
    def value(self) -> None:
        return self.__value

    @value.setter
    def value(self, new_value) -> None:
        self.__value = new_value


class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    @Field.value.setter
    def value(self, value: str) -> None:
        first_name, last_name = self.name_parser(value)
        if self.name_validate(first_name):
            if self.name_validate(last_name):
                Field.value.fset(self, (first_name, last_name))
            else:
                Field.value.fset(self, (first_name, MethodsText.DEFAULT_EMPTY_FIELD))
        else:                                       
            raise NameError

    def name_parser(self, value: str) -> tuple:
        first_name = None
        last_name = None
        if value:
            name = value.strip().split()
            if len(name) == 1:
                first_name = name[0]
                last_name = None
            if len(name) == 2:
                first_name = name[0]
                last_name = name[1]
        return first_name, last_name

    def name_validate(self, value: str) -> bool:
        if value and 1 < len(value) <= 16:
            return True

    def __repr__(self) -> str:
        return f'Name(value={self.value} [{type(self.value)}])'


class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    @Field.value.setter
    def value(self, value: str) -> None:
        phone_type, phone_number = self.phone_parser(value)
        if self.phone_number_validate(phone_number):
            if self.phone_type_validate(phone_type):
                Field.value.fset(self, {phone_type: self.phone_number_normalize(phone_number)})
            else:
                Field.value.fset(self, {MethodsText.DEFAULT_PHONE_TYPE: self.phone_number_normalize(phone_number)})
        else:
            raise PhoneError

    def phone_parser(self, value: str) -> tuple:
        phone_type = None
        phone_number = None
        for type in MethodsText.ALLOWED_PHONE_TYPES:
            if type in value:
                phone_type = type

        match = re.search(r'\d+', value)
        if match:
            phone_number = match[0]
        return phone_type, phone_number
    
    def phone_type_validate(self, phone_type: str) -> bool:
        if phone_type in MethodsText.ALLOWED_PHONE_TYPES:
             return True

    def phone_number_validate(self, phone_number: str) -> bool:
            if phone_number and len(phone_number) == 12 and phone_number.isnumeric():
                return True

    def phone_number_normalize(self, phone_number: str) -> str:
        return f'+{phone_number[0:2]} {phone_number[2:5]} {phone_number[5:8]} {phone_number[8:12]}'

    def __repr__(self) -> str:
        return f'Phone(value={self.value} [{type(self.value)}])'


class Email(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
    
    @Field.value.setter
    def value(self, value: str) -> None:
        if value:
            email = self.email_parser(value)
            if self.email_length_validate(email):
                Field.value.fset(self, email)
            else:
                raise EmailError
        else:
            Field.value.fset(self, MethodsText.DEFAULT_EMPTY_FIELD)

    def email_parser(self, value: str) -> str:
        email = None
        match = re.search(r"[a-zA-Z]{1}[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", value)
        if match:
            email = match[0]
        return email
    
    def email_length_validate(self, value: str) -> bool:
        if value and len(value) <= 32:
            return True        

    def __repr__(self) -> str:
        return f'Email(value={self.value} [{type(self.value)}])'


class Birthday(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
    
    @Field.value.setter
    def value(self, value: str) -> None:
        if value:
            birthday_date = self.birthday_normalize(value)
            if birthday_date:
                Field.value.fset(self, birthday_date)
            else:
                raise BirthdayError
        else:
            Field.value.fset(self, MethodsText.DEFAULT_EMPTY_FIELD)

    def birthday_normalize(self, value: str) -> datetime:
        result = None
        birthday_match = re.search(fr'^\d\d-\d\d-\d\d\d\d$', value)
        if birthday_match:
            birthday_date = (datetime.strptime(birthday_match[0], '%d-%m-%Y'))
            if birthday_date < datetime.now():
                result = birthday_date
        return result

    def __repr__(self) -> str:
        return f'Birthday(value={self.value} [{type(self.value)}])'


class Record:

    def __init__(
        self,
        name: Name | None = None,
        phone: Phone | None = None,
        email: Email | None = None,
        birthday: Birthday | None = None
        ) -> None:
        
        self.name = name
        self.email = email
        self.birthday = birthday
        self.phones = []
        if phone:
            self.add_phone(phone)
   
    def __repr__(self) -> str:
        return f"Record: {self.name}, phones: {self.phones}, email: {self.email}, birthday: {self.birthday}"        

# ADD FIELDS
    def add_name(self, name: Name) -> None:
        self.name = name

    def add_phone(self, new_phone: Phone) -> None:
        for phone in self.phones:
            for phone_type, new_phone_type in zip(phone.value, new_phone.value):
                if phone_type == new_phone_type:
                    phone.value[phone_type] = new_phone.value[new_phone_type]
                    return
        self.phones.append(new_phone)

    def add_email(self, email: Email) -> None:
        self.email = email

    def add_birthday(self, birthday: Birthday) -> None:
        self.birthday = birthday

# DAYS TO BIRTHDAY CALCULATE
    def days_to_birthday(self, birthday: Birthday | datetime) -> int:
        result = None
        current_date = datetime.now()
        if isinstance(birthday, datetime):
            current_year_birthday = datetime(year=current_date.year, month=birthday.month, day=birthday.day+1)
            if current_year_birthday < current_date:
                next_year_birthday = datetime(year=current_date.year+1, month=birthday.month, day=birthday.day)
                result = next_year_birthday - current_date
            else:
                result = current_year_birthday - current_date
            return result.days

# SHOW RECORD
    def show_record(self) -> str: #TODO
        result = ''

        # head of record
        if self.name:
            if self.name.value:
                first_name, last_name = self.name.value
                if last_name != MethodsText.DEFAULT_EMPTY_FIELD:
                    name = f'{first_name} {last_name}'
                else:
                    name = f'{first_name}'
                result += '\n{:^40}\n{:^40}\n'.format(name, '-'*40)

        # list of phones
        if self.phones:
            for phone in self.phones:
                for phone_type, phone_number in phone.value.items():
                    if phone_number:
                        result += '|{:^18}|{:^19}|\n{:^40}\n'.format(phone_type, phone_number, '-'*40)

        # email
        if self.email:
            if self.email.value != MethodsText.DEFAULT_EMPTY_FIELD:
                result += '|{:^18}|{:^19}|\n{:^40}\n'.format('Email', self.email.value, '-'*40)

        # birthday
        if self.birthday:
            if isinstance(self.birthday.value, datetime):
                days_to_birthday = self.days_to_birthday(self.birthday.value)
                if days_to_birthday == 0:
                    result += '|{:^38}|\n{:^40}\n'.format(MethodsText.birthday_is_today_message, '-'*40)
                else:
                    result += '|{:^18}|{:^19}|\n{:^40}\n'.format(MethodsText.days_to_birthday_message, days_to_birthday, '-'*40)

        # result
        if result:
            return result
        else:
            return MethodsText.DEFAULT_EMPTY_FIELD

    def record_info(self) -> str: #TODO
        # head of record
        result = '\nRecord:\n\n'
        
        # firs name and last name
        if self.name:
            if self.name.value:
                first_name, last_name = self.name.value
                if last_name != MethodsText.DEFAULT_EMPTY_FIELD:
                    name = f'First name: {first_name}\nLast name: {last_name}\n'
                else:
                    name = f'First name: {first_name}\n'
                result += f'{name}'
        else:
            result += f'First name: {MethodsText.DEFAULT_EMPTY_FIELD}\nLast name: {MethodsText.DEFAULT_EMPTY_FIELD}\n'

        # list of phones
        if self.phones:
            for phone in self.phones:
                for phone_type, phone_number in phone.value.items():
                    if phone_number:
                        result += f'{phone_type}: {phone_number}\n'
        else:
            result += f'Phone: {MethodsText.DEFAULT_EMPTY_FIELD}\n'

        # email
        if self.email:
            if self.email.value != MethodsText.DEFAULT_EMPTY_FIELD:
                result += f'Email: {self.email.value}\n'
        else:
            result += f'Email: {MethodsText.DEFAULT_EMPTY_FIELD}\n'

        # birthday
        if self.birthday:
            if isinstance(self.birthday.value, datetime):
                result += f'Birthday: {self.birthday.value.date()}\n'
                
        else:
            result += f'Birthday: {MethodsText.DEFAULT_EMPTY_FIELD}\n'

        # result
        return result

# RECORD CONVERSION
    def record_to_dict(self) -> dict: #TODO
        result = None
        if isinstance(self.birthday.value, datetime):
            result = {
            'name': self.name.value,
            'phones': [phone.value for phone in self.phones],
            'email': self.email.value,
            'birthday': self.birthday.value.strftime('%d-%m-%Y')
            }
        else:
            result = {
            'name': self.name.value,
            'phones': [phone.value for phone in self.phones],
            'email': self.email.value,
            'birthday': self.birthday.value
            }
        return result

    def record_to_list(self) -> list: #TODO
        result = []
        phones = ''
        name = ''
        birthday = ''
        email = ''
        first_name, last_name = self.name.value
        if first_name:
            if last_name != MethodsText.DEFAULT_EMPTY_FIELD:
                name = f'{first_name} {last_name}'
            else:
                name = f'{first_name}'

        result.append(name)

        for phone in self.phones:
            for phone_type, phone_number in phone.value.items():
                item = f'{phone_type}: {phone_number}\n'
                phones += item

        result.append(phones.rstrip())
        
        if self.email.value != MethodsText.DEFAULT_EMPTY_FIELD:
            email = self.email.value
                
        result.append(email)

        if self.birthday != MethodsText.DEFAULT_EMPTY_FIELD:
            if isinstance(self.birthday.value, datetime):
                birthday = self.birthday.value.strftime('%d-%m-%Y')
        
        result.append(birthday)
        return result


class RecordsBook(UserDict):

    def __init__(self) -> None:
        UserDict.__init__(self)

# UPDATE BOOK
    def update(self, another_records_book: dict) -> None:
        self.data.update(another_records_book)

    def clear(self) -> None:
        self.data.clear()

# RECORDS PROCESSING
    def get_record(self, record_name: Name) -> Record:
        return self.data[record_name.value]

    def add_record(self, record: Record) -> None:
            self.data[record.name.value] = record

    def delete_record(self, record: Record) -> None:
        del self.data[record.name.value]

# FIND RECORD
    def find_record(self, user_input: str) -> str:
        result = ''
        search_string = user_input.strip().lower()
        clean_search_string = re.sub(r'[+ ]', '', search_string)
        if clean_search_string:
            for record in self.data.values():
                if self.search_in_names(clean_search_string, record):
                    result += record.show_record()
                elif self.search_in_phones(clean_search_string, record):
                    result += record.show_record()
                elif self.search_in_email(clean_search_string, record):
                    result += record.show_record()
        return result

    def search_in_names(self, search_string: str, record: Record) -> bool:
        for name in record.name.value:
            if search_string in name.lower():
                return True
            
    def search_in_phones(self, search_string: str, record: Record) -> bool:
        for phone in record.phones:
            for phone_number in phone.value.values():
                clean_phone_number = re.sub(r'[+ ]', '', phone_number)
                if search_string in clean_phone_number:
                    return True
            
    def search_in_email(self, search_string: str, record: Record) -> bool:
        if search_string in record.email.value:
            return True

# SHOW RECORDS
    def show_records(self) -> str:
        result = ''
        for record in self.data.values():
            result += f'{record.show_record()}'
        return result

# RECORDS ITERATION
    def iterator(self, N: int = 1, flag: bool = False) -> Record:
        result = None
        lisf_of_keys = [key for key in self.data.keys()]
        if flag:
            N = len(lisf_of_keys)
        count = 0
        for key in lisf_of_keys:
            result = self.data[key]
            count += 1
            if count == N:
                yield result
                result = ''
                count = 0

# RECORDS BOOK CONVERSION
    def convert_to_dict(self) -> dict: #TODO
        result = {}
        list_of_records = self.iterator()
        for indx, record in enumerate(list_of_records):
            data = {indx+1: record.record_to_dict()}
            result.update(data)
        return result

    def convert_record_to_list(self) -> list:
        result = [['No', 'Name', 'Phones', 'Email', 'Birthday']]
        for indx, record in enumerate(self.data.values()):
            result.append([indx+1]+record.record_to_list())
        return result


class FileOperations:

# TXT
    def export_to_txt(file_path, some_dict: dict) -> None:
        result = ''
        with open(file_path, 'w') as fh:
            for k, v in some_dict.items():
                result += f'{k}: {v}\n'
            fh.write(result)

# PICKLE
    def export_to_pickle(file_path, some_data) -> None:
        with open(file_path, "wb") as fh:
            pickle.dump(some_data, fh)

    def import_from_pickle(file_path):
        with open(file_path, "rb") as fh:
            result = pickle.load(fh)
        return result

# JSON
    def export_to_json(file_path, some_data) -> None:
        with open(file_path, "w") as fh:
            json.dump(some_data, fh)

# CSV
    def export_to_csv(file_path, some_list: list) -> None:
        with open(file_path, 'w', newline='') as fh:
            record_writer = csv.writer(fh)
            for row in some_list:
                record_writer.writerow(row)


# ERRORS
class ExitFromCLI(Exception):
    pass
class NameError(Exception):
    pass
class PhoneError(Exception):
    pass
class EmailError(Exception):
    pass
class BirthdayError(Exception):
    pass


# ERRORS PROCESSING
def error_handler(func) -> str:
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except IndexError:
            print(ErrorsText.index_error_message)
        except KeyError:
            print(ErrorsText.key_error_message)
        except TypeError:
            print(ErrorsText.type_error_message)
        except ValueError:
            print(ErrorsText.value_error_message)
        except NameError:
            print(ErrorsText.name_error_message)
        except PhoneError:
            print(ErrorsText.phone_error_message)
        except EmailError:
            print(ErrorsText.email_error_message)
        except BirthdayError:
            print(ErrorsText.birthday_error_message)
        except ExitFromCLI:
            print(ErrorsText.exit_message)
            sys.exit()
        else:
            return result
    return wrapper


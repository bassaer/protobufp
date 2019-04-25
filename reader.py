import argparse
import addressbook_pb2


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='input file', required=True)
    return parser.parse_args()


def read_file(path):
    with open(path, mode='rb') as f:
        return f.read()


def desc(address_book):
    for person in address_book.people:
        print('Person ID : {}'.format(person.id))
        print('Person Name : {}'.format(person.name))
        if person.HasField('email'):
            print('Person email : {}'.format(person.email))
        for phone in person.phones:
            if phone.type == addressbook_pb2.Person.MOBILE:
                phone_type = 'Mobile'
            elif phone.type == addressbook_pb2.Person.HOME:
                phone_type = 'Home'
            else:
                phone_type = 'Work'
            print('Phone Number : {} [{}]'.format(phone.number, phone_type))


def main():
    address_book = addressbook_pb2.AddressBook()
    address_book.ParseFromString(read_file(read_args().f))
    desc(address_book)


if __name__ == '__main__':
    main()



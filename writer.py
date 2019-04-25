import addressbook_pb2


def create(person):
    person.id = int(100)
    person.name = 'John'
    person.email = 'email@example.com'
    phone = person.phones.add()
    phone.number = '111-2222-3333'
    phone.type = addressbook_pb2.Person.WORK


def write(path, address_book):
    with open(path, mode='wb') as f:
        f.write(address_book.SerializeToString())


def main():
    address_book = addressbook_pb2.AddressBook()
    create(address_book.people.add())
    write('addressbook.bin', address_book)


if __name__ == '__main__':
    main()

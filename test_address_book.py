import pytest

from address_book import Contact, AddressBook, MultipleAddressBook

@pytest.fixture
def contact():
    return Contact({'First Name':'Milan', 'Last Name':'Biranwar', 'Address': 'Gondia', 'City':'Gondia', 'State':'Maharashtra', 'Zip Code':441601, 'Mobile Number': 1234567895,
                              'Email':'milan@gmail.com'})

@pytest.fixture
def address_book():
    return AddressBook("MilanDetails")

@pytest.fixture
def multi_address_book():
    return MultipleAddressBook()

def test_add_person(contact, address_book):
    assert len(address_book.address_book_dict) == 0
    address_book.add_person(contact)
    assert len(address_book.address_book_dict) == 1


def test_get_person(contact, address_book):
    address_book.add_person(contact)
    actual = address_book.get_person(contact.first_name)
    assert actual.first_name == 'Milan'


def test_delete_person(contact, address_book):
    address_book.add_person(contact)
    address_book.delete_person("Milan")
    assert not address_book.get_person("Milan")

def test_multi_address_book_dict_length(address_book):
    address = MultipleAddressBook()
    assert len(address.multi_address_book_dict) == 0
    address.add_address_book(address_book)
    assert len(address.multi_address_book_dict) == 1


def test_address_book(address_book, multi_address_book):
    multi_address_book.add_address_book(address_book)
    assert address_book == multi_address_book.get_address_book_object("MilanDetails")
    assert address_book != multi_address_book.get_address_book_object("")

def test_delete_address_book(address_book, multi_address_book):
    multi_address_book.add_address_book(address_book)
    multi_address_book.delete_address_book("MilanDetails")
    assert not multi_address_book.get_address_book_object("MilanDetails")

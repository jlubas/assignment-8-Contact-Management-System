class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size: int = 10):
        self.size = size
        self.data = [None] * size
    def hash_function(self, key: str) -> int:
        total = 0

        for char in key:
            total += ord(char)

        return total % self.size
    
    def insert(self, key: str, number: str) -> None:
        index = self.hash_function(key)
        contact = Contact(key, number)

        # If the index is empty, insert the first node
        if self.data[index] is None:
            self.data[index] = Node(key, contact)
            return

        current = self.data[index]

        # Check for duplicates and find the last node
        while current is not None:
            if current.key == key:
                current.value.number = number
                return

            if current.next is None:
                break

            current = current.next

        # Add the new contact at the end of the linked list
        current.next = Node(key, contact)

    def search(self, key: str):
        index = self.hash_function(key)
        current = self.data[index]

        # Search through the linked list
        while current is not None:
            if current.key == key:
                return current.value

            current = current.next

        # Return None if the contact is not found
        return None
    
    def print_table(self) -> None:
        for index in range(self.size):
            current = self.data[index]

            if current is None:
                print(f"Index {index}: Empty")
            else:
                contacts = []

                # Go through the linked list
                while current is not None:
                    contacts.append(str(current.value))
                    current = current.next

                print(f"Index {index}: - " + " - ".join(contacts))
    
# Test HashTable initialization
table = HashTable(10)

# Test the empty hash table
print("\nEmpty Hash Table:")
table.print_table()

print(table.size)
print(table.data)

# Test your hash table implementation here.  

# Test the Contact class
contact_1 = Contact("Riley", "123-456-7890")

print(contact_1.name)
print(contact_1.number)
print(contact_1)

# Test the Node class
node_1 = Node(contact_1.name, contact_1)

print(node_1.key)
print(node_1.value)
print(node_1.next)

# Test the hash function
print("Amy:", table.hash_function("Amy"))
print("May:", table.hash_function("May"))
print("John:", table.hash_function("John"))
print("Rebecca:", table.hash_function("Rebecca"))

# Test inserting contacts
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")

print(table.data[9].value)
print(table.data[7].value)

# Test searching for contacts
print("Search result:", table.search("John"))
print("Search result:", table.search("Rebecca"))
print("Search result:", table.search("Chris"))

# Test hash collisions
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")

print("Amy:", table.search("Amy"))
print("May:", table.search("May"))

# Test printing the hash table
print("\nCurrent Hash Table:")
table.print_table()

# Test updating an existing contact
table.insert("Rebecca", "999-444-9999")

print("\nAfter updating Rebecca:")
table.print_table()
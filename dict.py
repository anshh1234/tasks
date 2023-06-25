values = int(input("Enter the number of pairs to be inserted: "))
my_dict = {}

while values > 0:
    key = input("Enter a key: ")
    value = input("Enter a value: ")

    my_dict[key] = value
    values -= 1

print("Dictionary:", my_dict)

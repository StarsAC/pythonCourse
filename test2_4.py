address_list = {}


def add_address(name, phone, email, company):
    if name not in address_list:
        address_list[name] = {}
    address_list[name].update({
        'phone': phone,
        'email': email,
        'company': company,
    })


def delete_address(name):
    if name in address_list:
        del address_list[name]


def display_address(name):
    if name in address_list:
        print(address_list[name]['phone'], address_list[name]['email'], address_list[name]['company'])
    else:
        print('Not found')


add_address('Alice', '12345678', 'alice@example.com', 'ABC Company')
add_address('John', '88888888', 'john_home@example.com', 'Home')
add_address('Bob', '87654321', 'bob@example.com', 'XYZ Company')

display_address('Alice')
print(address_list)

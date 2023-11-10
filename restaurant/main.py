import store


class Order:
    def __init__(self, item_name, item_price, item_quantity):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity


order_list = []

# Create a variable for the menu item number
menu_category_name = ''


# Create a dictionary to store the menu for later retrieval
def get_menu():
    print("Main Menu:")
    i = 1
    items = {}
    for item in store.menu.keys():
        print(f"{i}: {item}")
        # Store the menu category associated with its menu item number
        items[i] = item
        # Add 1 to the menu item number
        i += 1
    return items


menu_items = get_menu()


def welcome(welcome_str):
    print(welcome_str)


def place_order():
    menu_category = input("Type menu number: (If you're done ordering, type done)")
    if menu_category == 'done':
        order_review()
        quit(0)
    error_message = input_validation(menu_category, menu_items, False)
    if error_message == '':
        sub_menu_items = list_sub_menu()

        sub_menu_category = input("Type sub menu number: (use , to multi-order|E.g. 2,3,5)")
        for item in sub_menu_category.split(","):
            sub_error_message = input_validation(item, sub_menu_items, True)
            if sub_error_message == '':
                print('order received')
            else:
                print(sub_error_message)
                get_menu()
                break
    else:
        print(error_message)
        get_menu()
    place_order()


def input_validation(menu_category, menu_list, is_sub):
    error_message = ''
    if not menu_category.isdigit():
        error_message = 'Please input a valid number'
    elif not int(menu_category) in menu_list.keys():
        error_message = menu_category + ' was not a menu option.'
    else:
        global menu_category_name
        menu_category_name = menu_list[int(menu_category)]
        # Print out the menu category name they selected
        print(f"You selected {menu_category_name}")
        if is_sub:
            global order_list
            order_list.append(Order(menu_category_name['Item name'], menu_category_name['Price'], 1))
    return error_message


def list_sub_menu():
    j = 1
    sub_menu_items = {}
    for key, value in store.menu[menu_category_name].items():
        # Check if the menu item is a dictionary to handle differently
        if type(value) is dict:
            for key2, value2 in value.items():
                num_item_spaces = 24 - len(key + key2) - 3
                item_spaces = " " * num_item_spaces
                print(f"{j}      | {key} - {key2}{item_spaces} | ${value2}")
                sub_menu_items[j] = {
                    "Item name": key + " - " + key2,
                    "Price": value2
                }
                j += 1

        else:
            num_item_spaces = 24 - len(key)
            item_spaces = " " * num_item_spaces
            print(f"{j}      | {key}{item_spaces} | ${value}")
            sub_menu_items[j] = {
                "Item name": key,
                "Price": value
            }
        j += 1
    return sub_menu_items


def order_review():
    total = 0.0
    print("order_list:")
    for obj in order_list:
        print(obj.item_name, obj.item_price, obj.item_quantity)
        total += obj.item_price * obj.item_quantity
    print(f"Your total will be: ${total:.2f}")


welcomeStr = "Welcome to the variety food truck."
welcome(welcomeStr)
print("From which menu would you like to order? ")
place_order()

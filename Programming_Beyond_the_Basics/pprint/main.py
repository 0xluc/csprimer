def pprint(list_of_lists):
    def print_items(items, number_of_tabs):
        print(f'{(number_of_tabs - 1) * "\t"} [')
        for item in items:
            if type(item) == list:
                print_items(item, number_of_tabs + 1)
            else:
                print(f'{number_of_tabs * "\t"}{item}')

        print(f'{(number_of_tabs - 1) * "\t"} ]')

    print_items(list_of_lists, 1)


pprint([1, 2, [3, 4, [5, 6], 7], 8])
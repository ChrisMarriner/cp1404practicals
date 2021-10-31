"""
Christopher Marriner
"""

import wikipedia


def main():
    search_input = input("Search: ")
    while search_input != "":
        results = wikipedia.search(search_input)
        print(results)
        page = wikipedia.page(search_input, auto_suggest=False)
        print(page)
        search_input = input("Search: ")


main()

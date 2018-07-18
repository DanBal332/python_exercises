

def main():
    """this is the docstring for our main() function"""

    # a string ...
    quote = "a rose by any other name would smell as sweet"
    print("quote: " + quote)

    # a smaller string ...
    short_quote = "rose"

    # accessing characters
    char = quote[4]
    print("char: " + char)

    # what does this do?
    mystery = quote[-1]
    print(mystery)

    # how about this?
    mystery = quote[-4]
    print(mystery)

    # unpacking
    a, b, c, d = short_quote
    print("unpacking: {}, {}, {}, {}".format(a, b, c, d))

    # slicing
    # returns index 7 to end of string (inclusive)
    piece = quote[7:]

    # remember - extra space in print statements!
    print("piece: " + piece)

    # returns string to index 7 (exclusive)
    second_piece = quote[:8]
    print("second piece: " + second_piece)

    # returns string starting at index 2, ending at index 7 (inclusive, exclusive)
    third_piece = quote[2:8]
    print("third piece: " + third_piece)

    # get the length of the string ...


if __name__ == '__main__':
    main()
    # this is a single-line comment, it should start with a space character
    '''this is a multi-line comment, it's ignored as the docstring when it doesn't come first ...'''

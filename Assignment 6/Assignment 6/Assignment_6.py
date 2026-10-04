def rle_encode(text): # for encoding

    if not isinstance(text, str): # making sure it is a string
        raise TypeError("Text must be a string.")

    result = "##00"
    index = 0

    while index < len(text):
        char = text[index]
        count = 1

        # for each char at least once
        while index + count < len(text) and text[index + count] == char:
            count += 1

        # escape
        if char.isdigit():
            result += "#" + char
        elif char == "#":
            result += "##"
        else:
            result += char

        # adding per repeat
        if count > 1:
            result += str(count)

        # moving onto next section
        index += count

    return result


def rle_decode(text): # this one is for decoding


    if not isinstance(text, str): # string validation
        raise TypeError("Text must be a string.")

    if not text.startswith("##00"): # making sure it is encoded int he first place
        raise ValueError("Text does not begin with the ##00 encoded marker.")

    result = ""
    index = 4

    while index < len(text):

        # escape check
        if text[index] == "#":
            index += 1

            if index >= len(text):
                raise ValueError("Invalid escape sequence.")

            if text[index] == "#":
                char = "#"
            elif text[index].isdigit():
                char = text[index]
            else:
                raise ValueError("Invalid escape sequence.")

            index += 1

        else:
            char = text[index]
            index += 1

        # looking at the count
        count_string = ""

        while index < len(text) and text[index].isdigit():
            count_string += text[index]
            index += 1

        if count_string == "":
            count = 1
        else:
            count = int(count_string)

            if count < 2:
                raise ValueError("RLE counts must be 2 or greater.")

        result += char * count

    return result


# input string
valid = 0

while valid == 0:
    text = input("Enter a string to be processed: ")

    if text != "": # making sure there is at least something here to go off of
        valid = 1
    else:
        print("Please enter something.")


# is it encoded or not
if text.startswith("##00"):
    result = rle_decode(text)
else:
    result = rle_encode(text)


# display result
print(result)
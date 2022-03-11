# pass a string to convert it into integers
async def make_int(str_input):
    str_list = str_input.split(" ")
    return [int(x) for x in str_list]


# pass a integer list to convert it into string
async def make_str(int_input):
    int_list = int_input
    str_list = [str(x) for x in int_list]
    return " ".join(str_list)

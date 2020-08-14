def convert_getter(data: str):
    data_str = data[3:]
    next_char_will_be_underscored = False
    result = ""
    prev_char_will_be_underscored = False

    for i in range(0, len(data_str)):
        item = data_str[i]

        if i < len(data_str) - 1:
            next_char_will_be_underscored = (
                data_str[i + 1].isupper()
            )
            if i > 0:
                prev_char_will_be_underscored = (
                    item.isupper() and data_str[i + 1].islower() and data_str[i - 1].isupper()
                )

        if item.isupper() and next_char_will_be_underscored:
            result += item
        elif next_char_will_be_underscored:
            result += item + "_"
        elif prev_char_will_be_underscored:
            result += "_" + item
        else:
            result += item

    return data, result


print(convert_getter("getCurrency"))
print(convert_getter("getAccountName"))
print(convert_getter("getLongAccountName"))
print(convert_getter("getTradeID"))
print(convert_getter("getSWIFTCode"))
def expanded_form(num):
    result = ""
    counter = 1

    if len(str(num)) <= 1:
        return str(num)

    for number in str(num):
        if int(number) > 0:
            if str(len(str(num)) - counter) == "0":
                result += number
            else:
                result += number + format(0, "0" + str(len(str(num)) - counter)) + " + "
        counter += 1

    if result[-1] == " ":
        result = result[:-3]

    return result

def flavius_josephus(num_of_people, nth_person):
    people = create_list_of_people(num_of_people)

    # https://stackoverflow.com/questions/12444979/josephus-problem-using-list-in-python
    nth_person -= 1  # pop automatically skips the dead guy
    idx = nth_person
    while len(people) > 1:
        print(people.pop(idx))  # kill prisoner at idx
        idx = (idx + nth_person) % len(people)
    print('survivor: ', people[0])


def josephus(num_of_people, nth_person):
    from collections import deque
    # https://stackoverflow.com/questions/12444979/josephus-problem-using-list-in-python
    list_of_people = create_list_of_people(num_of_people)
    people = deque(list_of_people)
    deaths = []

    while len(people) > 0:
        people.rotate(-nth_person)
        deaths.append(people.pop())

    return " ".join(str(death) for death in deaths)


def create_list_of_people(num):
    list_of_people = []
    for number in range(0, num):
        list_of_people.append(number)

    return list_of_people


#flavius_josephus(5, 2)
josephus(5, 2)

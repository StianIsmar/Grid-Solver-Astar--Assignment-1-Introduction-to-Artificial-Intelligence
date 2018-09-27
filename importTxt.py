

def get_index(lst, num, index=0):
    if num in lst[index]:
        return index
    else:
        return get_index(lst, num, index + 1)


def main():
    f = open('board11.txt', 'r')
    x = f.readlines()
    f.close()

    myArray = []
    for element in x:
        element = element.replace('\n', '')
        element = [element]
        element = list(element[0])
        myArray.append(element)


if __name__ == '__main__':
    main()
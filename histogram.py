import matplotlib.pyplot as plt

filename = 'birthday.txt'

with open(filename,'r') as f:
    birthday = f.read()
    string_list = birthday.split()
    string_dict = dict()
    print(string_list)



    for word in string_list:
        if word in string_dict:
            string_dict[word] = string_dict[word] + 1
        else:
            string_dict[word] = 1

    print(string_dict)
    valuelist = []
    for key, values in string_dict.items():
        valuelist.append(values)
    sorteddict = {}
    for value in sorted(valuelist,reverse=True):
        for key in string_dict:
            if(value == string_dict[key]):
                sorteddict[key] = value
    print(sorteddict)

    count_list = string_dict.values()

    indentation = list(range(1,len(count_list) + 1))
    b1 = plt.barh(indentation,sorted(count_list),color = ("yellow"))

    plt.yticks(indentation,sorteddict)
    plt.title("Histogram")
    plt.xlabel("frequency")
    plt.ylabel("words")
    plt.show()
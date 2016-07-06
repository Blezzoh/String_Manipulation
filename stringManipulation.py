# a class to manipulate a string referred to as the StringToManipulate
# its methods are a complement to built_in methods for strings in python
# as a consequence they all receive a string as parameters


# method to capitalize a word

def capitalize_word(string):
    string = string
    temp = ''

    if type(string) != str:
        TypeError("parameter must be a string")
        return

    for i in range(len(string)):
        if i == 0:
            temp += string[i].upper()
        else:
            temp += string[i]

    return temp


# class to manipulate a string given as its input
# receives a string parameter or any object that can be cast to string
class StringToManipulate:
    def __init__(self, string_to_manipulate):
        if type(string_to_manipulate) == str:
            self.value = string_to_manipulate
        else:
            self.value = str(string_to_manipulate)

    # capitalizes the first word of a phrase or a word
    def capitalize(self):
        temp = capitalize_word(self)
        return temp

    # capitalizes every word in a phrase
    def capitalize_phrase(self):
        str_parts = list(self.value.split(" "))
        temp = ""
        for i in range(len(str_parts)):
            if i != (len(str_parts) - 1):
                temp += capitalize_word(str_parts[i] + " ")
            else:
                temp += capitalize_word(str_parts[i])
        return temp

    # returns the number of times a string(the target) occur in the StringToManipulate
    def find_occurrence(self, target):
        positions = list()
        string = self.value.lower()
        target = target.lower()
        while string.find(target) != -1:
            temp = string.find(target)
            positions.append(temp)
            if target != '_' * len(target):
                string = string[0:temp] + ('_' * len(target)) + string[(temp + len(target)):(len(string))]
            else:
                string = string[0:temp] + ('*' * len(target)) + string[(temp + len(target)):(len(string))]

        return len(positions)

    # removes a word in the StringToManipulate
    # can be used to clean lyrics
    def remove_word(self, target):
        positions = list()
        string = self.value.lower()
        target = target.lower()
        while string.find(target) != -1:
            temp = string.find(target)
            positions.append(temp)
            if target != '_' * len(target):
                string = string[0:temp] + ('_' * len(target)) + string[(temp + len(target)):(len(string))]
            else:
                string = string[0:temp] + ('*' * len(target)) + string[(temp + len(target)):(len(string))]

        return string

    # returns the position of the string(target) in the StringTiManipulate
    def find_all_positions(self, target):
        positions = list()
        string = self.value.lower()
        target = target.lower()
        while string.find(target) != -1:
            temp = string.find(target)
            positions.append(temp)
            print(temp)
            if target != '_' * len(target):
                string = string[0:temp] + ('_' * len(target)) + string[(temp + len(target)):(len(string))]
            else:
                string = string[0:temp] + ('*' * len(target)) + string[(temp + len(target)):(len(string))]

        print(string)
        return positions

    # returns the StringToManipulate in an acronym
    def to_acronym(self):
        temp = self.value.split(' ')
        new_str = ''
        for i in temp:
            new_str += i[0].upper() + '.'

        return new_str


def main():
    hook = StringToManipulate('''   \'Look at you
                                 Now look at us
                                 All my homies look richer than you
                                 All my homies look richer than you\' ''')
    print("the string to manipulate: ", hook.value, "\n")
    print("find_occurrence of homies : ", hook.find_occurrence("homies"), "\n")
    print("remove_word homies from the hook", hook.remove_word("homies"), "\n")

    word = StringToManipulate("you only live once")
    print("the next string to manipulate: ", word.value, "\n")
    print("capitalize_word: ", capitalize_word(hook), "\n same as capitalize ", word.capitalize(), "\n")
    print("capitalize_phrase: ", word.capitalize_phrase(), "\n")
    print("to_acronym: ", word.to_acronym(), "\n")
    print("isn't this cool: ", word.to_acronym(), "means", word.capitalize_phrase())

main()

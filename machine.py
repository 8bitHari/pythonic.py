emoticon = "v.v"


def main():
    global emoticon
    say("Is anyone there?")
    answer = input()
    if answer == "Y":
        emoticon = ":D"
        say("Oh ,hi!")
    elif answer == "N":
        emoticon
        say("where is everyone?")



def say(phrase):
    print(phrase + " " + emoticon)


main()


#emoticon = "v.v"

#def main():
#    say("Is anyone there?", emoticon)
#    answer = input()
#    if answer == "Y":
#        emoticon_new = ":D"
#        say("Oh hi!", emoticon_new)
#    elif answer == "N":
#        say("Where is everyone?", emoticon)
#
#def say(phrase, emoticon):
#    print(phrase + " " + emoticon)
#
#main()
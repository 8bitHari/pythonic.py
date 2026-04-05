list = {}
def main():
    while True:
        try:
            item = input()
        except EOFError:
            print("\n")
            break
        if item in list:  
            list[item] += 1
        else:
            list[item] = 1
    for item, count in sorted(list.items()): 
        print(count, item.upper())

main()
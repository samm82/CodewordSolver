# Main.py
# 3/25/2019

def main():

    masterList = [[chr(i) for i in range(ord("A"), ord("Z") + 1)] for j in range(27)]
    masterList[0] = []

    while True:
        word = input("Type 'exit' to exit or a word: ")
        if word == "exit":
            break
        else:
            letters = word.split(" ")
            print(letters)


    print("\n Quit")

main()
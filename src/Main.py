# Main.py
# 3/25/2019

def main():

    print("")

    masterList = [[chr(i) for i in range(ord("A"), ord("Z") + 1)] for j in range(27)]
    masterList[0] = []

    while True:
        word = input("Type 'exit' to exit or a codeword (separated by spaces): ")
        if word == "exit":
            break
        elif word == "":
            print("")
        else:
            letters = word.lower().split(" ")
            print(letters)

            file = open("words/words" + str(len(letters)).zfill(2) + ".txt", "r")
            lines = file.readlines()
            file.close()

            for i in range(len(letters)):
                try:
                    letters[i] = int(letters[i])
                except ValueError:
                    continue

            print(letters)

            print(lines[0])

    print("\n Quit")

main()
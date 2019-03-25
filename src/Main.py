# Main.py
# 3/25/2019

def main():

    masterList = [[chr(i) for i in range(ord("A"), ord("Z") + 1)] for j in range(27)]
    masterList[0] = []

    while True:
        word = input("Type 'exit' to exit or a codeword (separated by spaces): ")
        if word == "exit":
            break
        elif word == "":
            print("")
        else:
            letters = word.split(" ")
            print(letters)

            file = open("words/words" + str(len(letters)).zfill(2) + ".txt", "r")
            lines = file.readlines()
            file.close()

            print(lines[0])


    print("\n Quit")

main()
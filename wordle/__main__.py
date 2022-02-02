from wordle.query import query, CHARS


def main():
    max_num_rounds = 6
    characters = [CHARS, CHARS, CHARS, CHARS, CHARS]
    contains = set()
    t = 0

    while t < max_num_rounds:
        t += 1
        guess = query(characters)
        print(f"Try: '{guess[0][0]}' with rank {round(guess[0][1], 4)}")
        response = input(f"Round {t}: ")

        if len(response) == 5 + 4:
            print(f"🎉 🎉 🎉  Solved in {t} steps!")
            return

        for k, position in enumerate(response.split(",")):
            # Letter is not the word
            if "[" in position:
                for i in range(5):
                    characters[i] = characters[i].difference({position[1]})

            # Letter is in the word, but not this position
            elif "(" in position:
                characters[k] = characters[k].difference({position[1]})
                contains.add(position[1])

            # Letter is on correct place
            else:
                characters[k] = {position[0]}

    print(f"🐼 Not a lucky day! We couldn't solve it in {max_num_rounds} steps")


if __name__ == "__main__":
    main()

import json
import sys

try:
    data = open("story.json", "r", encoding="utf-8")
except:
    print("story.json was not found. Exiting.")
    sys.exit()

story = json.loads(data.read())

decision = "start"

ende = 0

while ende == 0:
    while True:
        try:

            decision_data = story[decision]
            print(decision_data["text"])

            if decision == "ende":
                ende = 1
                input()
                break

            answer = input()

            if answer == "text":
                raise None

            print("")
            decision = decision_data[answer]

            break

        except:
            print("\n\nBitte eine valide Antwort eingeben.\n\n")

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

while True:
    if ende == 1:
        break
    else:
        while True:
            try:

                decision_data = story[decision]
                print(decision_data["text"])

                if decision == "ende":
                    ende = 1
                    break

                answer = input()
                print("\n")
                decision = decision_data[answer]

                break

            except:
                print("Bitte eine valide Antwort eingeben. \n")

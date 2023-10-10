import time
from slimstampen.spacingmodel import SpacingModel, Fact, Response


def add_facts(model):
    #facts = [["hello", "bonjour"], ["dog", "chien"], ["cat", "chat"], ["computer", "ordinateur"]]
    facts = [["hai", "yes"], ["lie", "no"], ["sumimasen", "excuse me"], ["arigatoo gozaimas", "thank you"],
             ["tomodachi", "friend"], ["kazoku", "family"], ["kodomo", "children"], ["pan", "bread"],
             ["asa-gohan", "breakfast"], ["hiru-gohan", "lunch"], ["yoru-gohan", "dinner"]]
    for index in range(len(facts)):
        curr_fact = facts[index]
        fact = Fact(index + 1, curr_fact[0], curr_fact[1])
        model.add_fact(fact)


def learn_fact(model):
    cont = "y"
    while cont.lower() == "y":
        next_fact, new = model.get_next_fact(current_time=time.perf_counter())
        start_time = time.perf_counter()
        if new:
            print(next_fact.question + " => " + next_fact.answer)
            answer = input("Continue?")
            corr = True
        else:
            answer = input(next_fact.question + " => ").lower()
            corr = (next_fact.answer == answer)
        response_time = time.perf_counter() - start_time
        if not corr:
            print(f"Sorry, that response it wrong. \nThe correct answer is: '{next_fact.answer}'")
        elif not new:
            print("That answer is correct!")
        resp = Response(fact=next_fact, start_time=start_time, rt=response_time, correct=corr)
        model.register_response(resp)
        if not new:
            cont = input("Learn next fact? [y/n]\n")


if __name__ == '__main__':
    print("Welkom to SlimStampen (Now with competitions!)")
    model = SpacingModel()
    add_facts(model)
    next_fact, new = model.get_next_fact(current_time=34000)
    try:
        learn_fact(model)
    except:
        model.export_data("error.csv")

    model.export_data("data.csv")

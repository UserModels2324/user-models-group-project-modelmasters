import time
from slimstampen.spacingmodel import SpacingModel, Fact, Response


def add_facts(model):
    facts = [["hello", "bonjour"], ["dog", "chien"], ["cat", "chat"], ["computer", "ordinateur"]]
    for index in range(len(facts)):
        curr_fact = facts[index]
        fact = Fact(index + 1, curr_fact[0], curr_fact[1])
        model.add_fact(fact)


def learn_fact(model):
    cont = "y"
    start_time, end_time = 0, 0
    while cont.lower() == "y":
        next_fact, new = model.get_next_fact(current_time=time.perf_counter())
        start_time = time.perf_counter()
        if new:
            print(next_fact.question + " => " + next_fact.answer)
            answer = input("Continue?\n")
            corr = True
        else:
            answer = input(next_fact.question + "\n")
            corr = (next_fact.answer == answer)
        response_time = time.perf_counter() - start_time
        resp = Response(fact=next_fact, start_time=start_time, rt=response_time, correct=corr)
        model.register_response(resp)
        cont = input("Learn next fact? [y/n]\n")


if __name__ == '__main__':
    print(time.perf_counter())
    model = SpacingModel()
    add_facts(model)
    next_fact, new = model.get_next_fact(current_time=34000)
    try:
        learn_fact(model)
    except:
        model.export_data("error.csv")

    print(time.perf_counter())
    model.export_data("data.csv")

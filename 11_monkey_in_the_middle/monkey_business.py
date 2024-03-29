from Monkey import Monkey
from math import floor

def main(descriptions: list[list[str]]):
    
    monkeys = []
    monkeys: list[Monkey]
    for description in descriptions:
        monkeys.append(Monkey(description))
        print(description)
    for i in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                item_worry = floor(monkey.operation(item)/3.0)
                monkey.throws += 1
                if item_worry % monkey.test_num == 0:
                    monkeys[monkey.throw_if_true].items.append(item_worry)
                else: 
                    monkeys[monkey.throw_if_false].items.append(item_worry)
            monkey.items = []
    
    for monkey in monkeys:
        print(monkey)
    throws = sorted([monkey.throws for monkey in monkeys])
    print(throws[-1]*throws[-2])


if __name__=='__main__':
    demo = False
    if demo:
        input_file = 'demo.txt'
    else:
        input_file = 'input.txt'
    
    monkey_descriptions = []
    description = []

    with open(input_file, 'r') as monkey_machines:
        ctr = 0
        for line in monkey_machines:
            if line.strip() != '':
                description.append(line.strip())
                ctr += 1
            
            if ctr == 6:
                monkey_descriptions.append(description)
                description = []
                ctr = 0
    
    main(monkey_descriptions)

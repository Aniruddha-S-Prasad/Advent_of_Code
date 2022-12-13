def main(descriptions: list[list[str]]):
    for description in descriptions:
        print(description)

if __name__=='__main__':
    demo = True
    if demo:
        input_file = 'demo.txt'
    else:
        input_file = 'input.txt'
    
    monkey_descriptions = []
    description = []

    with open(input_file, 'r') as monkey_machines:
        for line in monkey_machines:
            if line != '\n':
                description.append(line.strip().split(':'))
                continue
            else:
                monkey_descriptions.append(description)
                description = []
    
    main(monkey_descriptions)

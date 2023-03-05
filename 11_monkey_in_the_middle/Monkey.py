class Monkey:
    def __init__(self, description: list[list[str]]) -> None:
        self.number = int(description[0][-2])
        self.items = [int(item) for item in description[1].split(':')[-1].split(',')]
        self.test_num = int(description[3].split(' ')[-1])
        self.throw_if_true = int(description[4].split(' ')[-1])
        self.throw_if_false = int(description[5].split(' ')[-1])
        self.operation = lambda old:  eval(description[2].split('=')[-1])
        
        self.throws = 0
    
    def __str__(self) -> str:
        return f'Monkey {self.number}\nItems: {self.items}\nDivisiblity check:{self.test_num}\nThrow if true:{self.throw_if_true}\nThrow if false: {self.throw_if_false}\nOperation on 1: {self.operation(1)}\nNumber of throws:{self.throws}\n'
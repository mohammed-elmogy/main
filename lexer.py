class Token:
    def __init__(self,type_,value):
        self.type=type_
        self.value=value
        
data={
    "num": {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    },
    "tens": {
        "ten": 10, "twenty": 20, "thirty": 30, "forty": 40,
        "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
        "ninety": 90
    },
    "multipliers": {
        "hundred": 100, "thousand": 1000, "million": 1000000,
        "billion": 1000000000, "trillion": 1000000000000,   
        "quadrillion": 1000000000000000, "quintillion": 1000000000000000000
        , "sextillion": 1000000000000000000000,
        "septillion": 1000000000000000000000000, "octillion": 1000000000000000000000000000,
        "nonillion": 1000000000000000000000000000000, "decillion": 100,
        "undecillion": 100,
        "duodecillion": 1000000000000, "tredecillion": 1000000000000000,
        "quattuordecillion": 1000000000000000000, "quindecillion": 1000000000000000000000,
        
    }
}

class Lexer:
    def __init__(self, text):
        self.text = text.split(" ")
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Advance the 'pointer' to the next character in the input string."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # End of input
        else:
            self.current_char = self.text[self.pos]
        
    def make_token(self):
        token=[]
        while self.current_char is not None :
            if self.current_char in data['num']:
                token.append(Token('NUM', data["num"][self.current_char]))
                self.advance()
            elif self.current_char in data["tens"]:
                token.append(Token('TENS', data["tens"][self.current_char]))
                self.advance()
            elif self.current_char in data["multipliers"]:
                token.append(Token('MULTIPLIER', data["multipliers"][self.current_char]))
                self.advance()
        return token
class NumNode:
    def __init__(self, value):
        self.value = value
class TensNode:
    def __init__(self, value):
        self.value = value
class MultiplierNode:
    def __init__(self, value):
        self.value = value
class NodeFactory:
    @staticmethod
    def create_node(token):
        if token.type == 'NUM':
            return NumNode(token.value)
        elif token.type == 'TENS':
            return TensNode(token.value)
        elif token.type == 'MULTIPLIER':
            return MultiplierNode(token.value)
        else:
            raise Exception('Unknown token type')
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if self.tokens else None

    def error(self):
        raise Exception('Invalid syntax')

    def advance(self):
        """Advance the 'pointer' to the next token in the input list."""
        self.pos += 1
        if self.pos > len(self.tokens) - 1:
            self.current_token = None  # End of input
        else:
            self.current_token = self.tokens[self.pos]
    def parse(self):
        """Parse the tokens and return a list of nodes."""
        nodes = []
        while self.current_token is not None:
            node = NodeFactory.create_node(self.current_token)
            nodes.append(node)
            self.advance()
        return nodes

class Interpreter:
    def __init__(self, nodes):
        self.nodes = nodes

    def interpret(self):
        total = 0
        current = 0
        for node in self.nodes:
            if isinstance(node, NumNode) or isinstance(node, TensNode):
                current += node.value
            elif isinstance(node, MultiplierNode):
                if node.value == 100:
                    current *= node.value
                else:
                    current *= node.value
                    total += current
                    current = 0
        total += current
        return total


def main(arg= "one hundred twenty three thousand four hundred fifty six"):#123456
    text=arg
    lexer = Lexer(text)
    tokens = lexer.make_token()
    
    parser = Parser(tokens)
    nodes = parser.parse()
    
    interpreter = Interpreter(nodes)
    result = interpreter.interpret()
    
    print(f"\n\tThe total value is: {result}") 
if __name__=="__main__":
    main()
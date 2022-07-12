from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
ASentence0 = And(AKnight, AKnave)
knowledge0 = And(
    Biconditional(AKnight, Not(AKnave)),    
    Biconditional(AKnight, ASentence0),     
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
ASentence1 = And(AKnave, BKnave)
knowledge1 = And(
    Biconditional(AKnight, Not(AKnave)),    
    Biconditional(BKnight, Not(BKnave)),    
    Biconditional(AKnight, ASentence1),     
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
ASentence2 = Or(And(AKnave, BKnave), And(AKnight, BKnight))
BSentence2 = Or(And(AKnave, BKnight), And(AKnight, BKnave))
knowledge2 = And(
    Biconditional(AKnight, Not(AKnave)),    
    Biconditional(BKnight, Not(BKnave)),   
    Biconditional(AKnight, ASentence2),     
    Biconditional(BKnight, BSentence2),     
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
BSentence3_1 = Biconditional(AKnight, AKnave)
BSentence3_2 = CKnave
CSentence3 = AKnight
knowledge3 = And(    
    Biconditional(AKnight, Not(AKnave)),    
    Biconditional(BKnight, Not(BKnave)),    
    Biconditional(CKnight, Not(CKnave)),    
    Biconditional(BKnight, BSentence3_1),   
    Biconditional(BKnight, BSentence3_2),   
    Biconditional(BKnight, CKnave),         
    Biconditional(CKnight, CSentence3),     
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()

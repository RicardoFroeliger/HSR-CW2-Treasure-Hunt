import random

rebuses_with_answers = {
    "O O O O O\nO O O O O\nO O X O O\nO O O O O\nO O O O O": "The middle", #TODO: Duidelijkheid over opdracht
    "1 2 3 4 5\n5 4 3 2 1\n1 2 3 4 5\n5 4 3 2 1": "symmetry", #TODO: Duidelijkheid over opdracht
    "2 - 4 - 8 - 16\n32 - 64 - 128 - 256\n512 - 1024 - 2048 - 4096\n8192 - 16384 - 32768 - 65536": "doubling", #TODO: Duidelijkheid over opdracht
    "🚗 📆": "car date",
    "🚗 R D S": "Carrots", #TODO: Andere
    "🎩 -d 🍰 t=g -r 🦌 -r +?": "Hoe gaat het?", #TODO: Engels
    "THE GOLD M": ["Mac", "Maccie", "Macdonalds"],
    "I C U 8 1 2": "I see you ate one too",
}
 
knowledge_questions_with_answers = {
    "Wat is de hoofdstad van Duitsland": "Berlijn",
    "Hoeveel dagen in een schrikkeljaar": "366",
    "Wat is de chemische formule voor water?": "H2O",
    "Wat zijn de eerste 2 decimalen van pi": "14",
    # TODO: Vraag over "Welke past niet in het rijtje"
    "Wat is de titel van de meest recente James Bond-film?": "No Time to Die",
    "Wat is de langste rivier ter wereld?": ["the Nile", "Nile"],
    "(7 * 3) + (10 / 2) - 4= ": "17",
    "8 * (5 - 3) = ": "16",
    "Wat is het aantal ringen verschil tussen het olympische logo en Audi?": "1",
    # TODO: Vraag over "Wat is het hoogste getal onder de 40 in de Fibonacci-reeks als je begint vanaf"
    "Welke sport wordt soms 'de koning der sporten' genoemd vanwege de veelzijdigheid en vaardigheden die het vereist zijn, zoals sprinten, springen en werpen?": "Atletiek ",
    # TODO: Vraag over "Wat is de grootste planeet in ons zonnestelsel?"
    "2x^2 - 5x - 3 = ": "0",
    "20/4*40/8+√9= ": "28",
    "mediaan bereken: 3, 7, 2, 8, 5 ": "5",
    # TODO: Vraag over "Wat is de hoofdstad van Australië?"
    # TODO: Vraag over "Welk element is het meest voorkomende element in het universum?"
    "(16 * 3) + (12 / 2) - (5^2) + (√25)= ": "34",
    "(10^2) - (8 * 4) + (√81) + (15 / 3) = ": "96",
}

def play_rebuses():
    rebuses = list(rebuses_with_answers.keys())
    random.shuffle(rebuses)
    
    for rebus in rebuses:
        answer = rebuses_with_answers[rebus]
        correct_answer = False
        
        while not correct_answer:
            print("Guess the rebus:")
            print(rebus)
            
            guess = input("Your answer: ").lower()
            
            if isinstance(answer, list):
                if guess in [a.lower() for a in answer]:
                    print("Congratulations! That is correct.")
                    option = input("Press Enter for the next rebus...").lower()
                    if option == '':
                        correct_answer = True
                else:
                    print("Unfortunately, that is not correct.")
                    option = input("Press A to try again or B for the next rebus: ").lower()
                    if option == 'b':
                        break
            else:
                answer_lower = answer.lower()
                if guess == answer_lower:
                    print("Congratulations! That is correct.")
                    option = input("Press Enter for the next rebus...").lower()
                    if option == '':
                        correct_answer = True
                else:
                    print("Unfortunately, that is not correct.")
                    option = input("Press A to try again or B for the next rebus: ").lower()
                    if option == 'b':
                        break
def sentence_maker(phrase):
    interogatives = ("how", "what", "why", "when", "did", "can")
    capital = phrase.capitalize()
    if phrase.startswith((interogatives)):
        return "{}?".format(capital)
    else: 
        return "{}.".format(capital)

#print(sentence_maker("how are you"))

results = []
while True:
    user_input = input("Say something:")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))



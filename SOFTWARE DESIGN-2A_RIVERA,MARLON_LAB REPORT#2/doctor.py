import random

hedges = ("Please tell me more.",
        "Many of my patients tell me the same thing.",
        "Please continue.")
qualifiers = ("Why do you say that ",
        "You seem to think that ",
        "Can you explain why ")
replacements = {"I":"you", "me":"you", "my":"your",
        "we":"you", "us":"you", "mine":"yours"}


class Doctor:

    def changePerson(self, sentence):
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(replacements.get(word, word))
        return " ".join(replyWords)     

    def reply(self, sentence):
        probability = random.randint(1, 4)
        if probability == 1:
            return random.choice(hedges)
        else:
            return random.choice(qualifiers) + self.changePerson(sentence)   

    def main(self):
        """Handles the interaction between patient and doctor."""
        print("Good morning, I hope you are well today.")
        print("What can I do for you?")
        while True:
            sentence = input("\n>> ")
            if sentence.upper() == "QUIT":
                print("Have a nice day!")
                break
            print(self.reply(sentence))


if __name__ == "__main__":
    main = Doctor()
    main.main()
!pip install chatterbot
!pip install chatterbot_corpus
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# naming the bot and giving it logic that it is supposed to be trained on. In this case, the logics are mathematical and text
my_bot = ChatBot(name="Richard", read_only=True, logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch"])

# training the bot with words it can use in conversations

small_gist = ["hi there",
              "hi", "How do you do?", "I am cool.", "Fine, you?", "always cool"
              "glad to hear that", "What can I do for you today?", "What is your name?"
              "My name is Richard,how can I help you?"]
math_talk = [
    "Algebra", "Pythogaros theorem"
]

trained_words = ListTrainer(my_bot)
for items in (small_gist, math_talk):
    trained_words.train(items)

print(my_bot.get_response("What is your name?"))

# ----------------------------------------------------------------------
# Name:      chat
# Purpose:   implement a simple chatbot
# Author(s): taylor
# ----------------------------------------------------------------------
"""
A simple chatbot

This bot will respond to simple one sentence expressions inputted by the
user via command line.
"""
import random
import string

TOPICS = {'family', 'friends', 'friend', 'mom', 'dad',
          'brother', 'sister', 'girlfriend', 'boyfriend',
          'children', 'son', 'daughter', 'child', 'wife',
          'husband', 'home', 'dog', 'cat', 'pet'}

def change_person(*words):
    """
    Takes variable number of words and swaps the pronouns to make a proper
    response.
    :param words: string
    :return: updated words concatenated into a string
    """
    # Use a dictionary to map each pronoun to it's replacement
    response = list(words)
    pronouns = {'i': 'you', 'am': 'are', 'my': 'your', 'your': 'my',
                'me': 'you', 'you': 'me'}
    for index in range(len(response)):
        for key in pronouns:
            if response[index].lower().strip(string.punctuation) == key.lower():
                # print(f'replacing {response[index]} with {pronouns[key]}')
                response[index] = pronouns[key]
                break  # so it doesn't replace an already replaced word
    return ' '.join(response)


def random_choice(*args):
    """
    returns a random string
    :param args: (string) words to select from
    :return: (string) randomly selected word
    """

    word = random.choice(args)
    return word


def check_because(statement):
    """
    checks if the statement contains the word 'because' and prints the
    proper response
    :param statement: list
    :return: boolean
    """
    if 'because' in statement:
        return True
    return False


def get_similar_topics(words):
    """
    compares list of words to TOPICS to find which words are in both
    :param: list
    :return (set) containing common words
    """
    set_of_words = set(words)
    comparison = set_of_words & TOPICS
    return comparison


def number_of_special_topics(statement):
    """
    finds the number of words the statement and TOPICS have in common
    :param statement: list
    :return: (int) number of common words
    """
    return len(get_similar_topics(statement))


def chat_with(name):
    """
    prompts the user to enter a phrase and then responds accordingly
    :param name: string
    :return: Boolean
    """
    # Enter your code below and take out the pass statement
    # Must use the match statement

    prompt = input('Talk to me please> ')
    words = prompt.lower().split()
    if check_because(words):
        print("Is that the real reason?")
        return False
    if number_of_special_topics(words) == 1:
        print(f"Tell me more about your "
              f"{' '.join(get_similar_topics(words))}.")
        return False
    if number_of_special_topics(words) > 1:
        print(f"Tell me more about your "
              f"{get_similar_topics(words).pop()},"
              f" {name}.")
        return False
    match words:
        case['bye' | 'bye.']:
            return True
        case['do' | 'can' | 'will' | 'would' as first, 'you', *rest]:
            result = random_choice("yes", "no")
            if result == 'yes':
                print(f"Yes I {first}.")
            else:
                no_answer = change_person(*tuple(rest))
                print(f"No {name}, I {first} not"
                      f" {no_answer.strip(string.punctuation)}.")
        case['why', *rest]:
            print("Why not?")
        case['how', *rest]:
            print(random_choice(f"{name}, why do you ask?",
                                f"{name}, how would an answer to "
                                f"that help you?"))
        case['what', *rest]:
            print(random_choice(f"What do you think {name}?",
                                f"Why is that important {name}?"))
        case['i', 'need' | 'think' | 'have' | 'want' as second, *rest]:
            print(f"Why do you {second} "
                  f"{change_person(*rest).strip(string.punctuation)}?")
        case['i', *middle, last]:
            last = last.strip(string.punctuation)
            if last != 'too':
                print(f"I {' '.join(middle)} {last} too.")
            else:
                print(random_choice("That's interesting", "Can you elaborate "
                                                          "on that?",
                                    "That's nice!"))
        case['tell'|'give' | 'say' as verb, *rest]:
            print(f"You {verb} {' '.join(rest).strip(string.punctuation)}.")
        case _:
            if words[-1][-1] == '?':
                print(random_choice("I have no clue.", "Maybe."))
            else:
                print(random_choice("That's interesting", "Can you elaborate "
                                    "on that?",
                                    "That's nice!"))


def main():
    # Enter your code following the outline below and take out the
    # pass statement.
    # 1.Prompt the user for their name
    # 2.Call chat_with repeatedly passing the name as argument
    # 3.When chat_with returns True, print the goodbye message.
    #

    name = input('Hello. What is your name please? ')
    done = False
    while not done:
        done = chat_with(name)
    if done:
        print(f"Bye {name}! Have a great day!")


if __name__ == '__main__':
    main()
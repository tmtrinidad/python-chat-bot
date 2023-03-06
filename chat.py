# ----------------------------------------------------------------------
# Name:      chat
# Purpose:   implement a chatbot
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


def get_response(res):
    """
    responds accordingly to a message
    :param name: string
    :param res: string 
    :return: string response
    """
    # Enter your code below and take out the pass statement
    # Must use the match statement

    words = res.lower().split()
    if check_because(words):
        return "Is that the real reason?"
    
    if number_of_special_topics(words) == 1:
        return (f"Tell me more about your "
              f"{' '.join(get_similar_topics(words))}.")
    
    if number_of_special_topics(words) > 1:
        return (f"Tell me more about your  {get_similar_topics(words).pop()}")

    match words:
        case['bye' | 'bye.']:
            return "Good bye!"
        case['hello' | 'hi']: 
            return "Hello! Talk to me!"
        case['do' | 'can' | 'will' | 'would' as first, 'you', *rest]:
            result = random_choice("yes", "no")
            if result == 'yes':
                return f"Yes I {first}."
            else:
                no_answer = change_person(*tuple(rest))
                return (f"No, I {first} not"
                      f" {no_answer.strip(string.punctuation)}.")
        case['why', *rest]:
            return "Why not?"
        case['how', *rest]:
            return(random_choice("Why do you ask?",
                                 "How would an answer to that help you?"))
        case['what', *rest]:
            return(random_choice("What do you think",
                                "Why is that important?"))
        case['i', 'need' | 'think' | 'have' | 'want' as second, *rest]:
            return(f"Why do you {second} "
                  f"{change_person(*rest).strip(string.punctuation)}?")
        case['i', *middle, last]:
            last = last.strip(string.punctuation)
            if last != 'too':
                return f"I {' '.join(middle)} {last} too."
            else:
                return (random_choice("That's interesting", "Can you elaborate "
                                                          "on that?",
                                    "That's nice!"))
        case['tell'|'give' | 'say' as verb, *rest]:
            return f"You {verb} {' '.join(rest).strip(string.punctuation)}."
        case _:
            if words[-1][-1] == '?':
                return random_choice("I have no clue.", "Maybe.")
            else:
                return (random_choice("That's interesting", "Can you elaborate "
                                    "on that?",
                                    "That's nice!"))
            
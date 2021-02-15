"""
Given a sentence, return a sentence with the words reversed
ex:
reverse("I am home") --> home am I
reverse("we are ready") --> ready are we
"""


def reverse(sent):
    word_list = sent.split()
    reversed_word_list = word_list[::-1]
    reversed_word_sent = " ".join(reversed_word_list)
    return reversed_word_sent

print(reverse("I am home"))
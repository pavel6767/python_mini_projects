shuffled_data = {
    'verbs': ['dance', 'swim', 'jump', 'run'],
    'adjectives': ['excited', 'angry', 'sad', 'happy'],
    'nouns': ['fish', 'bird', 'cat', 'dog'],
}
expected_sentences = [
    f"One {shuffled_data['nouns'][i]} {shuffled_data['verbs'][i]} quite {shuffled_data['adjectives'][i]}"
    for i in range(4)
]

print(expected_sentences)
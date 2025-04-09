def expected_dominant_offspring(filename):
    dominant_probs = [1, 1, 1, 0.75, 0.5, 0]

    with open(filename, 'r') as f:
        couple_counts = list(map(int, f.read().strip().split()))

    expected = 0
    for count, prob in zip(couple_counts, dominant_probs):
        expected += count * 2 * prob

    return expected

print(expected_dominant_offspring('sample_dataset.txt'))

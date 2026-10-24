# The data of the assignment and the functions to compute the metrics

N = 50   # gallery size

# mated searches: (name, rank of the correct identity, mate score)
mated = [
    ("M1", 1, 0.88),
    ("M2", 1, 0.81),
    ("M3", 2, 0.64),
    ("M4", 1, 0.59),
    ("M5", 3, 0.55),
    ("M6", 1, 0.72),
    ("M7", 5, 0.41),
    ("M8", 1, 0.66),
]

# non-mated searches: (name, highest score returned by the gallery)
non_mated = [
    ("N1", 0.62),
    ("N2", 0.48),
    ("N3", 0.71),
    ("N4", 0.39),
]


def rank_k_rate(k):
    # closed-set: how many mated searches have the correct identity within the first k
    count = 0
    for name, rank, score in mated:
        if rank <= k:
            count = count + 1
    return count / len(mated)


def open_set(tau, R=1):
    # mated searches: identified only if rank <= R AND score >= tau
    identified = 0
    for name, rank, score in mated:
        if rank <= R and score >= tau:
            identified = identified + 1

    # non-mated searches: false positive if the top score >= tau
    false_positives = 0
    for name, top_score in non_mated:
        if top_score >= tau:
            false_positives = false_positives + 1

    TPIR = identified / len(mated)
    FNIR = 1 - TPIR
    FPIR = false_positives / len(non_mated)
    return TPIR, FNIR, FPIR

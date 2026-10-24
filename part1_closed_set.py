import os
import matplotlib.pyplot as plt

from data import N, mated, non_mated, rank_k_rate


def run():
    os.makedirs("plots/part1", exist_ok=True)

    # ---------------- Question 1 ----------------
    print("=== Question 1: which searches are used? ===")
    print("Only the", len(mated), "MATED searches.")
    print("Closed-set assumes the correct identity is in the gallery,")
    print("so a rank exists only for mated searches.")
    print("The", len(non_mated), "non-mated searches have no correct identity, so no rank.")

    # ---------------- Questions 2, 3, 4, 5 ----------------
    print()
    print("=== Rank-k identification rates (N =", N, ") ===")
    ks = [1, 2, 3, 4, 5]
    cmc = []
    for k in ks:
        rate = rank_k_rate(k)
        cmc.append(rate)

        # count how many searches are found within the first k
        count = 0
        for name, rank, score in mated:
            if rank <= k:
                count = count + 1
        print("Rank-" + str(k), "=", count, "/", len(mated), "=", rate)

    # ---------------- CMC curve ----------------
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(ks, cmc, "b-o", markersize=8)
    for i in range(len(ks)):
        ax.text(ks[i], cmc[i] - 0.06, str(cmc[i]), ha="center")
    ax.set_xticks(ks)
    ax.set_ylim(0, 1.1)
    ax.set_xlabel("Rank k")
    ax.set_ylabel("Cumulative identification rate")
    ax.set_title("CMC curve (closed-set identification)")
    ax.grid(alpha=0.3)
    fig.savefig("plots/part1/part1_cmc.png", dpi=150)
    plt.close(fig)

    # ---------------- Question 6 ----------------
    print()
    print("=== Question 6: meaning ===")
    print("Rank-1: the correct person is the best candidate in the list.")
    print("Rank-3: the correct person is somewhere in the 3 best candidates.")
    print("Rank-5: the correct person is somewhere in the 5 best candidates.")
    print("Rank-k only measures WHERE the correct identity is in the ranked list.")
    print("It does not mean the system returns k identities as its final decision.")
    print()
    print("Plots saved in: plots/part1")

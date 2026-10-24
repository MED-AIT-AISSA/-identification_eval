import os
import matplotlib.pyplot as plt

from data import N, mated, non_mated, open_set


def evaluate(tau, R):
    print()
    print("========== tau =", tau, " R =", R, " N =", N, "==========")

    # mated searches
    print("Mated searches:")
    for name, rank, score in mated:
        if rank <= R and score >= tau:
            result = "correctly identified"
        else:
            # explain why it was missed
            if rank > R:
                result = "missed (rank " + str(rank) + " > R)"
            else:
                result = "missed (score " + str(score) + " < tau)"
        print("  ", name, "| rank =", rank, "| score =", score, "->", result)

    # non-mated searches
    print("Non-mated searches:")
    for name, top_score in non_mated:
        if top_score >= tau:
            result = "FALSE POSITIVE (returns an enrolled identity)"
        else:
            result = "correctly rejected as unknown"
        print("  ", name, "| top score =", top_score, "->", result)

    TPIR, FNIR, FPIR = open_set(tau, R)
    print("TPIR =", TPIR)
    print("FNIR =", FNIR, "(check: 1 - TPIR =", 1 - TPIR, ")")
    print("FPIR =", FPIR)
    return TPIR, FNIR, FPIR


def run():
    os.makedirs("plots/part2", exist_ok=True)
    R = 1

    # Questions 7 to 11 (tau = 0.60) and Question 12 (tau = 0.70)
    TPIR_60, FNIR_60, FPIR_60 = evaluate(0.60, R)
    TPIR_70, FNIR_70, FPIR_70 = evaluate(0.70, R)

    # Question 13
    print()
    print("=== Question 13: tau 0.60 -> 0.70 ===")
    print("TPIR:", TPIR_60, "->", TPIR_70, "(goes down)")
    print("FNIR:", FNIR_60, "->", FNIR_70, "(goes up)")
    print("FPIR:", FPIR_60, "->", FPIR_70, "(goes down)")

    # ---------------- Plot 1: operating points (Question 14) ----------------
    fig, ax = plt.subplots(figsize=(6.5, 6))
    ax.scatter(FPIR_60, FNIR_60, s=150, color="blue", label="tau = 0.60")
    ax.scatter(FPIR_70, FNIR_70, s=150, color="red", label="tau = 0.70")
    ax.plot([FPIR_60, FPIR_70], [FNIR_60, FNIR_70], "k--")
    ax.text(FPIR_60 + 0.01, FNIR_60 + 0.02,
            "(" + str(FPIR_60) + ", " + str(FNIR_60) + ")")
    ax.text(FPIR_70 + 0.01, FNIR_70 + 0.02,
            "(" + str(FPIR_70) + ", " + str(FNIR_70) + ")")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("FPIR")
    ax.set_ylabel("FNIR")
    ax.set_title("Open-set operating points (R = 1)")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.savefig("plots/part2/part2_operating_points.png", dpi=150)
    plt.close(fig)

    # ---------------- Plot 2: all the scores with the two thresholds ----------------
    fig, ax = plt.subplots(figsize=(9, 5.5))

    for name, rank, score in mated:
        if rank == 1:
            ax.scatter(score, 1, color="green", s=110, edgecolors="black")
        else:
            ax.scatter(score, 1, color="gray", s=110, edgecolors="black")
        ax.text(score, 1.08, name, ha="center", fontsize=8)

    for name, top_score in non_mated:
        ax.scatter(top_score, 0, color="red", s=110, edgecolors="black")
        ax.text(top_score, 0.08, name, ha="center", fontsize=8)

    ax.axvline(0.60, color="blue", linestyle="--", label="tau = 0.60")
    ax.axvline(0.70, color="red", linestyle="--", label="tau = 0.70")
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["Non-mated (top score)", "Mated (mate score)"])
    ax.set_ylim(-0.4, 1.5)
    ax.set_xlim(0.3, 1)
    ax.set_xlabel("similarity score")
    ax.set_title("Scores and thresholds (green = rank 1, gray = rank > 1)")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.savefig("plots/part2/part2_scores_thresholds.png", dpi=150)
    plt.close(fig)

    print()
    print("Plots saved in: plots/part2")

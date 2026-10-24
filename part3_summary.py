import os
import matplotlib.pyplot as plt

from data import N, mated, non_mated, rank_k_rate, open_set


def run():
    os.makedirs("plots/part3", exist_ok=True)

    rank1 = rank_k_rate(1)
    rank3 = rank_k_rate(3)
    rank5 = rank_k_rate(5)
    TPIR_60, FNIR_60, FPIR_60 = open_set(0.60, 1)
    TPIR_70, FNIR_70, FPIR_70 = open_set(0.70, 1)

    # ---------------- Question 15: threshold choice ----------------
    print("=== Question 15: threshold choice ===")
    print("A. Security watchlist     -> tau = 0.70 (FPIR", FPIR_70, "instead of", FPIR_60, ")")
    print("B. Staff identification   -> tau = 0.60 (TPIR", TPIR_60, "instead of", TPIR_70, ")")

    # ---------------- Questions 16 and 17: Rank-1 vs TPIR ----------------
    print()
    print("=== Questions 16-17: Rank-1 vs TPIR ===")
    print("Closed-set Rank-1 =", rank1)
    print("Open-set TPIR (tau = 0.60) =", TPIR_60)
    print("Difference: searches ranked first but with a score below tau:")
    for name, rank, score in mated:
        if rank == 1 and score < 0.60:
            print("  ", name, "| rank =", rank, "| score =", score, "< 0.60 -> rejected as unknown")

    # ---------------- Question 18: operating conditions ----------------
    print()
    print("=== Question 18: operating conditions to report ===")
    print("Gallery size N =", N)
    print("Rank cutoff R = 1")
    print("Threshold tau = 0.60 and 0.70")
    print("Number of mated searches =", len(mated))
    print("Number of non-mated searches =", len(non_mated))

    # ---------------- Question 19: summary table ----------------
    print()
    print("=== Question 19: FINAL SUMMARY TABLE ===")
    print("Closed-set    : Rank-1 =", rank1, "| Rank-3 =", rank3, "| Rank-5 =", rank5)
    print("Open-set 0.60 : TPIR =", TPIR_60, "| FNIR =", FNIR_60, "| FPIR =", FPIR_60)
    print("Open-set 0.70 : TPIR =", TPIR_70, "| FNIR =", FNIR_70, "| FPIR =", FPIR_70)

    # table as an image
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.axis("off")
    cell_text = [
        ["Closed-set", "-", rank1, rank3, rank5],
        ["Open-set", "0.60", TPIR_60, FNIR_60, FPIR_60],
        ["Open-set", "0.70", TPIR_70, FNIR_70, FPIR_70],
    ]
    columns = ["Evaluation", "tau", "Rank-1 / TPIR", "Rank-3 / FNIR", "Rank-5 / FPIR"]
    table = ax.table(cellText=cell_text, colLabels=columns, loc="center", cellLoc="center")
    table.scale(1, 2)
    ax.set_title("Final summary table (N = 50, R = 1, 8 mated, 4 non-mated)")
    fig.savefig("plots/part3/part3_summary_table.png", dpi=150, bbox_inches="tight")
    plt.close(fig)

    # bar chart: Rank-1 vs TPIR
    fig, ax = plt.subplots(figsize=(6, 5))
    names = ["Rank-1\n(closed-set)", "TPIR tau=0.60\n(open-set)", "TPIR tau=0.70\n(open-set)"]
    values = [rank1, TPIR_60, TPIR_70]
    ax.bar(names, values, color=["blue", "orange", "red"])
    for i in range(3):
        ax.text(i, values[i] + 0.02, str(values[i]), ha="center")
    ax.set_ylim(0, 1)
    ax.set_ylabel("rate")
    ax.set_title("Rank-1 is not the same as TPIR")
    ax.grid(alpha=0.3, axis="y")
    fig.savefig("plots/part3/part3_rank1_vs_tpir.png", dpi=150)
    plt.close(fig)

    print()
    print("Plots saved in: plots/part3")

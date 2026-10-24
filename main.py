import part1_closed_set
import part2_open_set
import part3_summary


def run_part(choice):
    if choice == "1":
        print("Running Part 1: closed-set identification (Questions 1-6)")
        part1_closed_set.run()

    elif choice == "2":
        print("Running Part 2: open-set identification (Questions 7-14)")
        part2_open_set.run()

    elif choice == "3":
        print("Running Part 3: choices, Rank-1 vs TPIR, summary (Questions 15-19)")
        part3_summary.run()

    elif choice == "all":
        part1_closed_set.run()
        part2_open_set.run()
        part3_summary.run()

    else:
        print("Unknown choice:", choice)


# Program starts here
while True:
    print()
    print("===== MENU =====")
    print("1) Part 1: closed-set identification, CMC (Questions 1-6)")
    print("2) Part 2: open-set identification, TPIR, FNIR, FPIR (Questions 7-14)")
    print("3) Part 3: threshold choice, Rank-1 vs TPIR, summary (Questions 15-19)")
    print("all) Run everything")
    print("q) Quit")

    choice = input("Your choice: ")
    choice = choice.strip().lower()

    if choice == "q":
        break

    run_part(choice)

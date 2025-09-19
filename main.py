import random


def ask_int(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        value = input(prompt).strip()
        if value.lower() in {"q", "quit", "exit"}:
            raise KeyboardInterrupt
        if value.isdigit():
            number = int(value)
            if min_value <= number <= max_value:
                return number
        print(f"Iltimos {min_value}–{max_value} oralig'ida butun son kiriting (yoki 'q' – chiqish).")


def play_game() -> None:
    print("Taxmin qilish o'yini – kompyuter 1 dan 100 gacha son o'yladi.")
    print("Maqsad: imkon qadar kam urinishda topish. Chiqish: q")
    secret = random.randint(1, 100)
    attempts = 0
    while True:
        attempts += 1
        try:
            guess = ask_int("Taxminingiz: ", 1, 100)
        except KeyboardInterrupt:
            print("\nChiqildi.")
            return
        if guess == secret:
            print(f"Tabriklayman! {attempts} urinishda topdingiz.")
            break
        if guess < secret:
            print("Yuqoriroq son o'ylangan.")
        else:
            print("Pastroq son o'ylangan.")

    again = input("Yana o'ynaysizmi? (ha/yo'q): ").strip().lower()
    if again in {"ha", "xa", "h", "yes", "y"}:
        print()
        play_game()


if __name__ == "__main__":
    play_game()



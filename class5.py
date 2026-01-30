def every_other(text, start=0, remove_spaces=False, reverse=False, case="normal"):
    if remove_spaces:
        text = text.replace(" ", "")

    result = text[start::2]

    if reverse:
        result = result[::-1]

    if case == "upper":
        result = result.upper()
    elif case == "lower":
        result = result.lower()

    return result


def menu():
    print("\n🔥 EVERY-OTHER-LETTER MACHINE 🔥")
    print("1) Start from FIRST character")
    print("2) Start from SECOND character")
    print("3) Reverse result")
    print("4) Remove spaces")
    print("5) Uppercase output")
    print("6) Lowercase output")
    print("7) Run")
    print("8) Exit")


def main():
    text = input("\nEnter your text: ")

    start = 0
    reverse = False
    remove_spaces = False
    case = "normal"

    while True:
        menu()
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            start = 0
            print("✅ Starting from FIRST character")
        elif choice == "2":
            start = 1
            print("✅ Starting from SECOND character")
        elif choice == "3":
            reverse = not reverse
            print(f"🔄 Reverse mode: {'ON' if reverse else 'OFF'}")
        elif choice == "4":
            remove_spaces = not remove_spaces
            print(f"🚫 Spaces removed: {'ON' if remove_spaces else 'OFF'}")
        elif choice == "5":
            case = "upper"
            print("🔠 Uppercase mode ON")
        elif choice == "6":
            case = "lower"
            print("🔡 Lowercase mode ON")
        elif choice == "7":
            result = every_other(
                text,
                start=start,
                remove_spaces=remove_spaces,
                reverse=reverse,
                case=case
            )

            print("\n✨ RESULT ✨")
            print(result)

            print("\n📊 STATS")
            print(f"Original length: {len(text)}")
            print(f"Result length: {len(result)}")
        elif choice == "8":
            print("\n👋 Later, legend.")
            break
        else:
            print("❌ Invalid option")


if __name__ == "__main__":
    main()

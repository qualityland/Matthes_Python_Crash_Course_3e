#!/usr/bin/env python3
import random

OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}

def generate_problem():
    op = random.choice(list(OPERATIONS.keys()))

    if op == "/":
        # Ensure whole-number division and no division by zero
        b = random.randint(1, 100)
        result = random.randint(0, 100)
        a = b * result
    elif op == "-":
        # Avoid negative results
        a = random.randint(0, 100)
        b = random.randint(0, a)
    else:
        a = random.randint(0, 100)
        b = random.randint(0, 100)

    return a, b, op

def main():
    print("🧮 Math Trainer (0–100)")
    print("Operations: +  -  *  /")
    print("Type 'q' to quit.\n")

    total = 0
    correct = 0

    while True:
        a, b, op = generate_problem()
        answer = OPERATIONS[op](a, b)

        user_input = input(f"{a} {op} {b} = ")

        if user_input.lower() in ("q", "quit", "exit"):
            break

        try:
            user_answer = int(user_input)
        except ValueError:
            print("❌ Please enter a whole number.\n")
            continue

        total += 1

        if user_answer == answer:
            correct += 1
            print("✅ Correct!\n")
        else:
            print(f"❌ Incorrect. Correct answer: {answer}\n")

    if total > 0:
        accuracy = (correct / total) * 100
        print(f"\nFinal Score: {correct}/{total} ({accuracy:.1f}%)")
    else:
        print("\nNo problems attempted.")

    print("Goodbye!")

if __name__ == "__main__":
    main()

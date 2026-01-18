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

    if op == "+":
        a = random.randint(0, 200)
        b = random.randint(0, 200 - a)

    elif op == "-":
        a = random.randint(0, 200)
        b = random.randint(0, a)

    elif op == "*":
        # Ensure product <= 200
        a = random.randint(0, 100)
        if a == 0:
            b = random.randint(0, 100)
        else:
            b = random.randint(0, 200 // a)

    elif op == "/":
        # Ensure whole-number result between 0 and 200
        result = random.randint(0, 200)
        b = random.randint(1, 100)
        a = result * b

    return a, b, op

def main():
    print("🧮 Math Trainer (Results 0–200)")
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

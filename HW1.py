#Q1-A

L1 = ["http", "https", "ftp", "dns"]
L2 = [80, 443, 21, 53]

D = {}
for i in range(len(L1)):
    D[L1[i]] = L2[i]

print(D)

#Q1-B

def factorial(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

num = int(input("Enter a number to calculate its factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print(f"The factorial of {num} is {factorial(num)}")

#Q1-C

L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']

for item in L:
    if item.startswith('B'):
        print(item)

#Q1-D

d = {i: i+1 for i in range(11)}
print(d)

#Q2

def binary_to_decimal(binary):
    try:
        decimal = int(binary, 2)
        return decimal
    except ValueError:
        return None

binary_number = input("Enter a binary number: ")

while not all(char.isdigit() for char in binary_number) or any(char not in ['0', '1'] for char in binary_number):
    print("Invalid input. Please enter a valid binary number")
    binary_number = input("Enter a binary number: ")

decimal_number = binary_to_decimal(binary_number)

if decimal_number is not None:
    print(f"The decimal equivalent of {binary_number} is {decimal_number}.")
else:
    print("Invalid binary number , u can try again")


#Q3

def load_questions(file_name):
    questions = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            question = lines[i].strip()
            answer = lines[i+1].strip()
            questions.append((question, answer))
    return questions

def save_results(user_name, score):
    with open('results.csv', 'a') as file:
        file.write(f"{user_name},{score}\n")

def take_quiz(questions):
    score = 0
    for question in questions:
        print(question[0])
        user_answer = input("Your answer: ")
        if user_answer.lower() == question[1].lower():
            score += 1
    return score

def main():
    questions = load_questions('quiz_noor.csv')
    
    user_name = input("Enter your name: ")
    user_score = take_quiz(questions)
    
    print(f"Your score: {user_score}/20")
    
    save_results(user_name, user_score)

if __name__ == '__main__':
    main()

#Q4

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

account = BankAccount(19110000, "NOOR")


account.deposit(1000)
print(f"Balance after deposit: {account.get_balance()}")

account.withdraw(500)
print(f"Balance after withdrawal: {account.get_balance()}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate/100
        self.balance = self.balance+ interest_amount

    def print(self):
        print("Current balance:" , self.balance , "Interest rate:",self.interest_rate )

savings_account = SavingsAccount(19110000, "NOOR", 5)
savings_account.deposit(1000)
savings_account.apply_interest()
savings_account.print()
   



# Color
""" ANSI color codes """
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"
RESET = "\033[0m"

print(YELLOW + "=" * 60 + RESET)
print(CYAN + "System".center(60) + RESET)
print(YELLOW + "=" * 60 + RESET)
while True:
    print(CYAN +"1  - Average caculator"+RESET)
    print(CYAN +"2  - Multiple caculator"+RESET)
    print(CYAN +"0  - Exit System"+RESET)
    chose = int(input("Chose Option:\t"))
    print("=" * 60)
    if chose == 1:
        # Find score
        studentName = str(input(CYAN + "Student Name: \t" + RESET))
        java = float(input(PURPLE + "Enter score for Java: " + RESET))
        python = float(input(PURPLE + "Enter score for Python: " + RESET))
        r = float(input(PURPLE + "Enter score for R: " + RESET))
        kotlin = float(input(PURPLE + "Enter score for Kotlin: " + RESET))
        php = float(input(PURPLE + "Enter score for PHP: " + RESET))

        # Calculate total and average
        total = java + python + r + kotlin + php
        average = total / 5

        # Display the results
        print("=" * 60)
        print("🎓 Enter Your Scores 🎓".center(60))
        print("=" * 60)
        print(f"📘 Java: {java}")
        print(f"🐍 Python: {python}")
        print(f"📊 R: {r}")
        print(f"📱 Kotlin: {kotlin}")
        print(f"🌐 PHP: {php}")
        print("=" * 60)

        # Determine and display the grade with colors
        if average >= 90:
            grade = "A"
            message = GREEN + "🌟 Outstanding! Keep up the excellent work!" + RESET
        elif average >= 80:
            grade = "B"
            message = BLUE + "💪 Great job! You're doing very well!" + RESET
        elif average >= 70:
            grade = "C"
            message = PURPLE + "👍 Good effort! Keep improving!" + RESET
        elif average >= 60:
            grade = "D"
            message = YELLOW + "⚠️ Fair work, but there’s room for improvement!" + RESET
        elif average >= 50:
            grade = "E"
            message = RED + "❗ Needs more focus and dedication!" + RESET
        else:
            grade = RED+"F"+RESET
            message = RED + "🚨 You have failed. Don't give up!" + RESET

        # Display final result with color
        print(f"Name Student:{studentName}")
        print(f"🏆 Your Grade: {grade}")
        print(YELLOW + "=" * 60 + RESET)
        print(message.center(60))
        print(YELLOW + "=" * 60 + RESET)

    elif chose == 2:
        multiple= int(input("Number for Multi : "))
        start=1
        end=11
        for number in range(start, end):
            print(multiple,"×",number,"=",BLUE,multiple*number,RESET)
            number+=1
        print("=" * 60)

    elif chose == 0:
        print(GREEN + "=" * 60 + RESET)
        print(YELLOW + "System Exit thank you for Testing...".center(60) + RESET)
        print(GREEN + "=" * 60 + RESET)
        break
    else:
        print(RED+"The number you chose is invalid. Please choose again."+GREEN+"(1,2,and 0)"+RESET)

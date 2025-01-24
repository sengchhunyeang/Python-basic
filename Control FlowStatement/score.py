# Find score
java = float(input("Enter score for Java: "))
python = float(input("Enter score for Python: "))
r = float(input("Enter score for R: "))
kotlin = float(input("Enter score for Kotlin: "))
php = float(input("Enter score for PHP: "))

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

print("📊 Score Report 📊".center(60))
print("=" * 60)
print(f"🎯 Total Score: {total:.2f}")
print(f"📈 Average Score: {average:.2f}")

# Determine and display the grade
if average >= 90:
    grade = "A"
    message = "🌟 Outstanding! Keep up the excellent work!"
elif average >= 80:
    grade = "B"
    message = "💪 Great job! You're doing very well!"
elif average >= 70:
    grade = "C"
    message = "👍 Good effort! Keep improving!"
elif average >= 60:
    grade = "D"
    message = "⚠️ Fair work, but there’s room for improvement!"
elif average >= 50:
    grade = "E"
    message = "❗ Needs more focus and dedication!"
else:
    grade = "F"
    message = "🚨 you have failed. Don't give up!"

print(f"🏆 Your Grade: {grade}")
print("=" * 60)
print(message.center(60))
print("=" * 60)

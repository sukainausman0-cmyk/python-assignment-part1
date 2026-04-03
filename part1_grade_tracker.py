# Students Grade Tracker
# Data Parsing and Profile cleaning
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]
# step 1: Cleaning each students data
cleaned_students = []
for student in raw_students:
    cleaned ={
        "name": student["name"].strip().title(), # Here i used strip() and title to remove extra spaces and coverts to standard format
        "roll": int(student["roll"]),            # converts roll number to integer
        "marks": [int(mark.strip()) for mark in student["marks_str"].split(",")]     # coverts marrks string to list of integers
    }
    cleaned_students.append(cleaned) # stores cleaned student data in new list

# step 2: Printing profile cards
for student in cleaned_students:
# step 3: Checking if name is valid
    is_valid = all(word.isalpha()for word in student["name"].split())  # checks if all words in the name are alphabetic (no numbers or special characters)
    if is_valid:
        print("✓ Valid name")
    else:
        print("✗ Invalid name")

    validity = "Valid" if is_valid else "Invalid"

    print ("=" * 30) # prints a separator line for better readability
    print(f"Student: {student['name']} ({validity})")
    print (f"Roll No : {student['roll']}")
    print(f"Marks: {student['marks']}")
    print("=" * 30) # prints another separator line after each student's profile card

#step 4: Print roll 103 in all caps and lowercase
for student in cleaned_students:
    if student["roll"] ==103:
        print(f"\nRoll 103 in uppercase: {student['name'].upper()}")
        print(f"Roll 103 in lowercase: {student['name'].lower()}")

#Task 2 - Mark Analysis
student_name = "Ayesha Sharma"
subjects = ["math", "physics","CS", "English", "Chemistry"]
marks = [88,72,95,60,78]

print("\n---Marks Analysis---")
for i in range(len(subjects)): # loops through each subject index
    m = marks[i]

    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subjects[i]} : {m} : {grade}")  # prints subject name, marks and grade in formatted string

print(f"\nTotal Marks: {sum(marks)}") 
print(f"Average Marks: {round(sum(marks)/len(marks), 2)}")
print(f"Highest subject: {subjects[marks.index(max(marks))]} {max(marks)} marks")
print(f"Lowest subject: {subjects[marks.index(min(marks))]} {min(marks)} marks")

# While Loop to add new subject
added = 0
while True:
    subject = input("\nEnter a new subject (or 'done' to stop): ").strip()
    if subject.lower() == 'done':
        break
    try:
        mark = int(input(f"Enter marks for {subject} (0-100): "))  # Get mark FIRST
        if 0 <= mark <= 100:  # THEN check range
            subjects.append(subject)
            marks.append(mark)
            added += 1
            print(f"Added {subject}: {mark}")
        else:
            print("Invalid! Marks must be 0-100.")
    except ValueError:
        print("Invalid! Please enter a number.")

print(f"\nAdded {added} subjects!")
print(f"Updated average: {round(sum(marks)/len(marks), 2)}")

# Task 3 — Class Performance Summary
print("\n===== CLASS PERFORMANCE SUMMARY =====\n")

# Given class data (name + list of marks)
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# Print table header
print("Name              | Average | Status")
print("----------------------------------------")

# Initialize counters and trackers
pass_count = 0          # to count students who passed
fail_count = 0          # to count students who failed
total_avg_sum = 0       # to calculate class average

topper_name = ""        # to store topper's name
topper_avg = 0          # to store highest average

# Loop through each student in class_data
for name, marks in class_data:
    
    # Calculate average marks for the student
    avg = round(sum(marks) / len(marks), 2)
    
    # Determine pass or fail based on average
    if avg >= 60:
        status = "Pass"
        pass_count += 1   # increment pass count
    else:
        status = "Fail"
        fail_count += 1   # increment fail count
    
    # Print formatted row for each student
    print(f"{name:<18} | {avg:>7} | {status}")
    
    # Check and update topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name
    
    # Add average to total for class average calculation
    total_avg_sum += avg

# After loop: print summary details
print("\nPassed:", pass_count)
print("Failed:", fail_count)

# Print topper details
print(f"Topper: {topper_name} ({topper_avg})")

# Calculate and print class average
class_avg = round(total_avg_sum / len(class_data), 2)
print(f"Class Average: {class_avg}")

#Task 4 — String Manipulation Utility
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning. "
# step 1: Remove extra spaces
clean_essay = essay.strip()
print ( "Clean Essay:", clean_essay )# removes leading and trailing spaces
 
# step 2: Convert to title case
print("Title Case:", clean_essay.title()) # converts first letter of each word to uppercase

# step 3: Count occurrences of "python"
count_python = clean_essay.lower().count("python") # counts how many times "python" appears in the essay (case-insensitive) 
print("Count of 'python':", count_python)

# step 4: Replace "python" with "Python 🐍"
replaced_essay = clean_essay.replace("python", "Python 🐍")
print("Replaced Essay:", replaced_essay)

# step 5: Split into sentences
sentences = clean_essay.split(". ") # splits the essay into sentences based on period followed by space
print("Sentences list:", sentences)

# step 6: Print numbered sentences
print("\nNumbered Sentences:")
for i, sentence in enumerate(sentences, 1):
    sentence = sentence.strip() # I added this to remove any extra spaces around sentences after splitting
    if sentence == "":
        continue
    if not sentence.endswith("."):
        sentence +="." # adds period at the end if missing
    print(f"{i}. {sentence}")

import pandas as pd
import numpy as np

# Student Performance Analytics System
SUBJECT_COLUMNS = ["Sem_1_Percentage", "Sem_2_Percentage"]
PASS_MARK = 40


def calculate_grade(average):
    """Return a simple grade based on the student's average percentage."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def calculate_pass_status(row):
    """A student passes when both semester percentages meet the pass mark."""
    for subject_column in SUBJECT_COLUMNS:
        if row[subject_column] < PASS_MARK:
            return "Fail"
    return "Pass"


def main():
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv("students.csv")

    # Display the data and basic information
    print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 42)
    print("\nDataset preview:")
    print(df.head())
    print("\nNumber of student records:", len(df))
    print("\nDataset information:")
    print(df.info())

    # Use NumPy to calculate total and average across the two semester percentages
    marks_array = df[SUBJECT_COLUMNS].to_numpy()
    df["Total_Percentage_Points"] = np.sum(marks_array, axis=1)
    df["Calculated_Average"] = np.mean(marks_array, axis=1)

    # Reusable function and loop to assign grades
    grades = []
    for average in df["Calculated_Average"]:
        grades.append(calculate_grade(average))
    df["Grade"] = grades

    # Apply the pass/fail rule to each student's semester results
    df["Pass_Status"] = df.apply(calculate_pass_status, axis=1)

    print("\nStudent results:")
    print(df[["Student_Name", "Sem_1_Percentage", "Sem_2_Percentage",
              "Calculated_Average", "Grade", "Pass_Status",
              "Attendance_Percentage"]].round(2).to_string(index=False))

    # Overall class analysis
    print("\nCLASS SUMMARY")
    print("-" * 42)
    print("Class average:", round(df["Calculated_Average"].mean(), 2))
    print("Highest student average:", round(df["Calculated_Average"].max(), 2))
    print("Lowest student average:", round(df["Calculated_Average"].min(), 2))
    print("Students passed:", int((df["Pass_Status"] == "Pass").sum()))
    print("Students failed:", int((df["Pass_Status"] == "Fail").sum()))
    print("Average attendance:", round(df["Attendance_Percentage"].mean(), 2), "%")

    # Compare average performance in each semester
    semester_averages = df[SUBJECT_COLUMNS].mean()
    print("\nSEMESTER-WISE AVERAGES")
    print(semester_averages.round(2).to_string())

    # Identify top five students
    print("\nTOP FIVE STUDENTS")
    top_students = df.sort_values("Calculated_Average", ascending=False).head(5)
    print(top_students[["Student_Name", "Calculated_Average", "Grade"]]
          .round(2).to_string(index=False))

    
# Identify top five students based on overall percentage
    print("\nTOP FIVE STUDENTS")
    top_students = df.sort_values(
    "Overall_Percentage", ascending=False
    ).head(5)

    print(
    top_students[
        ["Student_Name", "Overall_Percentage", "Grade"]
    ].round(2).to_string(index=False)
    )

    # Save the analysed results to a new CSV file
    df.to_csv("student_analysis_results.csv", index=False)
    print("\nAnalysis complete. Results saved to student_analysis_results.csv")


if __name__ == "__main__":
    main()

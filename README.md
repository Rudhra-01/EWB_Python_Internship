# Student Performance Analytics System

## 1. Project Overview

The **Student Performance Analytics System** is a Python-based mini project developed as part of the **Python with AI Internship at EWB Edutech Private Limited**.

It analyzes student academic data obtained from my college using Python, Pandas, and NumPy to calculate performance summaries, assign grades, identify pass/fail status, compare semester averages, and find the top five students based on overall percentage.

## 2. Objectives

- Analyze student academic performance.
- Calculate average percentages and grades.
- Identify pass/fail status.
- Find the highest, lowest, and average performance.
- Compare semester-wise results.
- Calculate average attendance.
- Identify the top five students.
- Export analysis results to a CSV file.

## 3. Technologies Used

- **Python** – Programming logic and functions
- **Pandas** – Data loading and analysis
- **NumPy** – Numerical calculations
- **CSV** – Dataset storage
- **Git and GitHub** – Version control and project hosting

## 4. Project Structure

```text
student-performance-analytics/
├── main.py
├── students.csv
├── README.md
└── student_analysis_results.csv
```

- `main.py` – Main analysis program
- `students.csv` – Student dataset
- `README.md` – Project documentation
- `student_analysis_results.csv` – Generated analysis results

## 5. Dataset

The project uses academic data obtained from my college and contains 24 student records.

The dataset includes student identifiers, names, Semester 1 and Semester 2 percentages, overall percentage, and attendance percentage.

**Note:** Attendance values and one student's adjusted Semester 1 percentage are sample values, not verified college records. Student names and register numbers should be anonymized before publishing the dataset publicly unless appropriate permission has been obtained.

## 6. Key Features

- Load student data using Pandas.
- Calculate total and average percentages using NumPy.
- Assign grades using predefined criteria.
- Determine pass/fail status.
- Calculate class performance summaries.
- Compare semester-wise averages.
- Display the top five students based on overall percentage.
- Save results to a CSV file.

## 7. Grade and Passing Criteria

**Grade criteria:**

| Percentage | Grade |
|---|---|
| 90 and above | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

A student is considered to have passed if they score at least 40% in both semesters. These are project-defined criteria and may differ from official college rules.

## 8. Installation and Execution

Install the required libraries:

```bash
pip install pandas numpy
```

Run the project from the folder containing `main.py` and `students.csv`:

```bash
python main.py
```

The program displays student performance, class summaries, semester averages, and the top five students. It also generates `student_analysis_results.csv`.

## 9. Learning Outcomes

- Practiced Python variables, conditions, loops, and functions.
- Learned data manipulation using Pandas.
- Performed numerical calculations using NumPy.
- Analyzed and sorted student performance.
- Exported results and managed project files using GitHub.

## 10. Future Enhancements

- Add verified subject-wise marks.
- Include performance charts and visualizations.
- Analyze attendance and academic performance.
- Develop an interactive dashboard.

## 11. Author

**Rudhra Roopini P**  
M.Sc. Data Science Student

## 12. Internship Details

**Internship:** Python with AI Internship  
**Organization:** EWB Edutech Private Limited

---

*Developed for educational purposes as part of my Python with AI learning journey.*

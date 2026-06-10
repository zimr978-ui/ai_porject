# Generate a Complete Streamlit Project

You are an award-winning Python developer, data analyst, and Streamlit expert.

Create a complete, production-ready Streamlit application for a school competition project.

## Project Title

Youth Obesity Prevention AI Health Coach

---

## Technical Requirements

* Must run successfully on Streamlit Cloud
* Use Python
* Use only:

  * streamlit
  * pandas
  * matplotlib
* Do NOT use any additional libraries
* Generate both:

  * app.py
  * requirements.txt
* The application must run immediately after deployment
* Include detailed comments
* Clean and professional code structure

---

## User Interface Requirements

* Modern and student-friendly design
* Attractive emoji usage
* Sidebar navigation menu
* Responsive layout
* Competition-quality UI
* Easy to understand for teenagers
* Friendly and encouraging language

---

## Required Sections

### Home

Display:

* Project introduction
* Why obesity prevention is important
* Health awareness message
* Daily motivational message

---

### Youth Obesity Statistics

#### Annual Obesity Trend

Create a line chart showing obesity rates:

| Year | Rate |
| ---- | ---- |
| 2018 | 9.8  |
| 2019 | 10.5 |
| 2020 | 11.7 |
| 2021 | 13.1 |
| 2022 | 14.2 |
| 2023 | 15.1 |

Requirements:

* Use matplotlib
* Display markers on data points
* Show trend clearly

---

#### Top 3 Obesity Types

Display a bar chart:

1. Lack of Exercise
2. Poor Eating Habits
3. Abdominal Obesity

Include percentages.

---

### BMI Calculator

Inputs:

* Height (cm)
* Weight (kg)

Calculate BMI automatically.

Display category:

* Underweight
* Normal
* Overweight
* Obese

Use different colors for each category.

---

### AI Health Coach

Based on BMI results, generate:

* Health assessment
* Weekly goals
* Improvement suggestions
* Motivational message

Example:

Current Status: Overweight

Weekly Goals:

✔ Walk 30 minutes daily

✔ Drink 8 glasses of water

✔ Reduce late-night snacks

Motivational Message:

Small healthy habits today create a healthier future.

---

### Personalized Health Solutions

#### Exercise Recommendations

Recommend at least 2 real exercises based on BMI category.

Examples:

* Walking
* Cycling
* Swimming
* Jogging
* Badminton
* Strength Training

---

#### Food Recommendations

Recommend at least 2 real foods based on BMI category.

Examples:

* Apple
* Banana
* Broccoli
* Egg
* Milk
* Salad

---

#### Obesity Management Tips

Include:

* Healthy eating habits
* Exercise habits
* Lifestyle improvement tips

At least 3 recommendations in each category.

---

### Recommended Books

Recommend at least 3 health-related books commonly available in major bookstores.

For each book include:

* Title
* Why it is recommended
* One-line review

---

### Recommended Health Documentaries and Movies

Recommend at least 3 titles.

Examples:

* Super Size Me
* The Game Changers
* Forks Over Knives

For each:

* Title
* Reason for recommendation
* One-line review

---

### Career Exploration

Recommend at least 5 careers related to health and wellness.

Examples:

* Exercise Physiologist
* Sports Trainer
* Dietitian
* Health Teacher
* Nurse

For each career include:

* Related major
* Job description
* Suitable personality traits

Display results in a professional table or cards.

---

### 7-Day Health Challenge

Create a weekly challenge:

Monday → Walk 30 minutes

Tuesday → Drink 8 glasses of water

Wednesday → Eat fruit

Thursday → Exercise 20 minutes

Friday → Eat vegetables

Saturday → Ride a bicycle

Sunday → Sleep well

Display visually.

---

### Health Score System

Start with 100 points.

Adjust score according to BMI.

Display:

* Current health score
* Personalized feedback

---

### Future Obesity Rate Prediction

Use a slider:

2024–2035

Predict future obesity rates using a simple linear trend.

Display:

* Predicted obesity rate
* Future trend graph

---

## Matplotlib Requirements

Prevent font issues:

```python
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.unicode_minus"] = False
```

All chart labels and titles must be displayed correctly.

---

## Code Quality Requirements

* Fully functional
* No syntax errors
* Streamlit Cloud compatible
* Professional project structure
* Well-commented code
* Competition-level quality
* Complete app.py source code
* Complete requirements.txt

Generate the full project.

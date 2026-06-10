Create a complete Streamlit application called:

"💪 Youth Obesity Solution AI"

Requirements:

1. Use only:
   - streamlit
   - pandas
   - matplotlib

2. Must run on Streamlit Cloud without additional libraries.

3. Use English for ALL text shown on screen:
   - Titles
   - Buttons
   - Labels
   - Tables
   - Graphs
   - Messages
   - Recommendations

4. Use:

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.unicode_minus"] = False

5. Configure page:

st.set_page_config(
    page_title="Youth Obesity Solution AI",
    page_icon="💪",
    layout="wide"
)

6. Create a BMI Calculator

Inputs:
- Height (cm)
- Weight (kg)

Calculate BMI automatically.

Categories:
- Underweight
- Normal
- Overweight
- Obese

Display BMI with st.metric().

Show colored status messages with emojis.

7. Add Annual Youth Obesity Rate Section

Display a line chart using:

Year:
2018, 2019, 2020, 2021, 2022, 2023

Rate:
9.8, 10.5, 11.7, 13.1, 14.2, 15.1

Chart title:
"Youth Obesity Trend"

X label:
"Year"

Y label:
"Rate (%)"

Add a short explanation below the chart.

8. Add Top 3 Youth Obesity Types Section

Display a bar chart.

Types:
- Lack of Exercise
- Poor Eating Habits
- Abdominal Obesity

Rates:
42
34
24

Chart title:
"Top 3 Obesity Types"

9. Create recommendation data for each BMI category.

Each category must contain:

- 2 exercises
- 2 foods
- 1 book
- 1 book review
- 1 movie
- 1 movie review

Example exercises:
- Walking
- Cycling
- Swimming
- Jogging
- Badminton
- Strength Training

Example foods:
- Apple
- Banana
- Broccoli
- Egg
- Milk
- Salad

10. Display Recommended Exercises section.

Use st.success() for each exercise.

11. Display Recommended Foods section.

Use st.success() for each food.

12. Display Recommended Book section.

Show:
- Book title
- One-line review

13. Display Recommended Movie section.

Show:
- Movie title
- One-line review

14. Add Health Career Recommendation Section.

Create a dataframe with:

Career:
- Exercise Physiologist
- Sports Trainer
- Dietitian
- Health Teacher
- Nurse

Columns:
- Career
- Recommended Major
- Suitable Personality

Display with st.dataframe().

15. Add Today's Health Mission Section.

Show:

- Walk for 30 Minutes
- Drink 6 Glasses of Water
- Eat One Fruit
- Reduce Smartphone Use Before Bed
- Sleep at Least 7 Hours

Display each mission separately.

Show st.balloons().

Add an encouraging message.

16. Add Future Youth Obesity Rate Prediction Section.

Create a slider:

2024 to 2035

Calculate prediction using a simple linear trend based on historical obesity data.

Display:

st.metric()

Example:
"Predicted Obesity Rate in 2030"

Create a prediction graph:

Historical Data
Prediction

Chart title:
"Youth Obesity Forecast"

Show a warning message:

"This prediction is based on a simple linear trend and should be used for reference only."

17. The application should be visually attractive.

18. Use emojis throughout the application.

19. Include clear comments in the code.

20. Generate the COMPLETE app.py file only.

Do not explain.
Return only executable Python code.

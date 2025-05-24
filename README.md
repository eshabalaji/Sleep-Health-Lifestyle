# 😴 Sleep Health & Lifestyle Analysis

## Overview

This project provides a comprehensive exploratory data analysis (EDA) of a "Sleep Health and Lifestyle" dataset. The goal is to uncover insights into sleep patterns, their relationship with various lifestyle factors, and potential correlations with sleep disorders. The analysis utilizes Python's powerful data manipulation and visualization libraries: Pandas, Matplotlib, and Seaborn.

## Dataset

The analysis is performed on the `Sleep_health_and_lifestyle_dataset.csv` dataset, which contains information related to:
* Gender
* Age
* Occupation
* Sleep Duration
* Quality of Sleep
* Physical Activity Level
* Stress Level
* BMI Category
* Daily Steps
* Heart Rate
* Blood Pressure
* Sleep Disorder

## Analysis & Key Findings

The analysis involves several steps, from data cleaning to visualization, leading to key conclusions about sleep health trends:

### Data Preprocessing & Cleaning

* The dataset contains 374 entries.
* Missing values in the 'Sleep Disorder' column are handled by filling them with 'None'.
* 'Normal Weight' in 'BMI Category' is standardized to 'Normal' for consistency.

### Exploratory Data Analysis (EDA)

Various distributions and relationships within the dataset are visualized:

* **Categorical Distributions:**
    * Gender Distribution: More males than females are present in the dataset.
    * Occupation Distribution: Nurses, Engineers, and Doctors represent the majority of occupations.
    * BMI Category Distribution: Many individuals fall into the 'Normal' BMI category.
    * Sleep Disorder Distribution: A significant portion of people do not suffer from any sleep disorder, while some experience Sleep Apnea and Insomnia.
* **Numerical Distributions:**
    * Age Distribution: Ages range from 27 to 59 years.
    * Sleep Duration Distribution: Most people sleep around 7 hours, with a range of 4 to 8.5 hours.
    * Quality of Sleep, Physical Activity Duration, Stress Levels, Daily Steps, Heart Rate, and Blood Pressure distributions are also explored.

### Insights & Relationships

* **Gender vs. Sleep Duration:** On average, women tend to sleep slightly more (around 7.22 hours) than men (around 7.03 hours).
* **Age vs. Heart Rate:** A scatter plot explores the relationship between age and heart rate.
* **Sleep Disorder Analysis:**
    * **Gender and BMI Category:** The distribution of sleep disorders across different genders and BMI categories is visualized.
    * **Sleep Disorder vs. Lifestyle Factors (Line Plots):** Line plots illustrate how Age, Sleep Duration, Quality of Sleep, Physical Activity Level, Stress Level, Heart Rate, and Daily Steps vary with different sleep disorders.
        * Individuals with Insomnia generally exhibit higher stress levels.
        * People suffering from Sleep Apnea tend to have a higher heart rate.
* **Physical Activity Level vs. Sleep Duration (Heatmap):** A heatmap shows the average sleep duration for different physical activity levels, indicating that people with more physical activities tend to have normal sleeping hours.
* **Occupation vs. Sleep Duration/Quality (Heatmaps):**
    * Heatmaps reveal the average sleep duration and quality of sleep across different occupations.
    * Engineers, according to this data, tend to have longer sleep durations and better sleep quality.
* **Daily Steps:** The average daily step count is around 7,000 steps, aligning with the minimum recommended by WHO.

## Conclusion

Based on this dataset, the key conclusions drawn are:
1.  The dataset contains more male participants than female participants.
2.  The majority of individuals in the dataset are Nurses, Engineers, and Doctors.
3.  Many individuals have no sleep disorder, while some experience Sleep Apnea and Insomnia.
4.  Individuals suffering from Insomnia tend to have higher stress levels compared to others.
5.  People diagnosed with Sleep Apnea generally exhibit a higher heart rate.
6.  The average daily step count is around 7,000 steps, which meets the minimum suggested by WHO.
7.  Individuals with higher physical activity levels tend to have normal sleeping hours.
8.  Engineers, as per this survey, report having more sleep duration and better sleep quality.

# NayePankh Foundation Data Analytics Dashboard

## Project Overview

This project was developed to analyze beneficiary and donation data for NayePankh Foundation using Python-based data analytics and visualization techniques.

The project generates a sample dataset of beneficiaries, performs exploratory data analysis (EDA), creates insightful visualizations, and develops an interactive dashboard to help understand program impact, donation trends, and beneficiary demographics.

## Objectives

* Generate and manage beneficiary data.
* Analyze beneficiary demographics and program participation.
* Visualize donation distribution across cities.
* Track beneficiary enrollment trends over time.
* Build an interactive dashboard for decision-making.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly

## Dataset Features

The dataset contains the following information:

* Beneficiary ID
* Name
* Age
* Gender
* City
* Program Type
* Year
* Month
* Income Group
* Donation Received
* Number of Volunteers
* Program Outcome

## Data Analysis Performed

### Dataset Overview

* Shape and structure analysis
* Data type inspection
* Missing value analysis
* Statistical summaries

### Category Analysis

* City-wise beneficiary distribution
* Program-wise participation
* Gender distribution
* Income group distribution
* Program outcome analysis

## Visualizations

The project generates the following visualizations:

### 1. Beneficiaries by City

Displays the number of beneficiaries across different cities.

### 2. Program Distribution

Shows the percentage distribution of foundation programs.

### 3. Gender Distribution

Analyzes beneficiary distribution by gender.

### 4. Donations by City

Visualizes total donations received across cities.

### 5. Yearly Enrollment Trend

Tracks beneficiary enrollment growth over multiple years.

## Interactive Dashboard

An interactive dashboard was developed using Plotly containing:

* Beneficiaries by City
* Program Distribution
* Gender Distribution
* Donations by City
* Yearly Enrollment Trends
* Income Group Distribution

The dashboard is exported as:

```text
nayepankh_dashboard.html
```

## Project Structure

```text
NayePankh_Data_Analytics/
│
├── nayepankh_analysis.py
├── nayepankh_data.csv
├── chart1_city.png
├── chart2_programs.png
├── chart3_gender.png
├── chart4_donations.png
├── chart5_trend.png
├── nayepankh_dashboard.html
└── README.md
```

## Installation

Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn plotly
```

## Running the Project

Execute the analysis script:

```bash
python nayepankh_analysis.py
```

The script will:

1. Generate the dataset
2. Perform exploratory data analysis
3. Create visualizations
4. Generate the interactive dashboard

## Key Insights

* Analyze beneficiary distribution across multiple cities.
* Understand program participation trends.
* Evaluate donation allocation patterns.
* Monitor yearly beneficiary enrollment growth.
* Assess demographic characteristics of beneficiaries.

## Future Enhancements

* Connect to real beneficiary data.
* Add predictive analytics using Machine Learning.
* Deploy dashboard using Streamlit or Power BI.
* Add real-time data updates.
* Create automated reporting functionality.

## Author

Nanci Rawat

BCA Student | Data Analytics Enthusiast | Aspiring Data Scientist

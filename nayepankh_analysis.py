import pandas as pd
import numpy as np

# using "random" to genrate dummy dataset 
np.random.seed(42)

# total number of records generated
n = 300

# Create the dataset
data = {
    'BeneficiaryID': range(1, n+1),
    'Name': ['Beneficiary_' + str(i) for i in range(1, n+1)],
    'Age': np.random.randint(5, 60, n),
    'Gender': np.random.choice(['Male', 'Female'], n),
    'City': np.random.choice(['Kanpur', 'Ghaziabad', 'Lucknow', 'Agra', 'Varanasi'], n),
    'Program': np.random.choice(['Education', 'Food Distribution', 'Health', 'Clothing'], n),
    'Year': np.random.choice([2021, 2022, 2023, 2024], n),
    'Month': np.random.choice(['Jan','Feb','Mar','Apr','May','Jun',
                               'Jul','Aug','Sep','Oct','Nov','Dec'], n),
    'Income_Group': np.random.choice(['Below Poverty Line', 'Low Income', 'Middle Income'], n),
    'Donation_Received': np.random.randint(500, 10000, n),
    'Volunteers': np.random.randint(1, 20, n),
    'Outcome': np.random.choice(['Successful', 'Ongoing', 'Needs Follow-up'], n)
}

df = pd.DataFrame(data)

# Saving dataset to CSV
df.to_csv('nayepankh_data.csv', index=False)

print("Dataset created successfully!")
print(df.shape)
df.head()


# Basic overview
print("="*50)
print("DATASET OVERVIEW")
print("="*50)
print("Shape of dataset:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nBasic statistics:\n", df.describe())

print("="*50)
print("CATEGORY COUNTS")
print("="*50)
print("\nCities:\n", df['City'].value_counts())
print("\nPrograms:\n", df['Program'].value_counts())
print("\nGender:\n", df['Gender'].value_counts())
print("\nIncome Groups:\n", df['Income_Group'].value_counts())
print("\nOutcomes:\n", df['Outcome'].value_counts())


import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# ---- CHART 1: Beneficiaries by City ----
plt.figure()
df['City'].value_counts().plot(kind='bar', color='steelblue')
plt.title('Beneficiaries by City')
plt.xlabel('City')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart1_city.png')
plt.show()
print("Chart 1 saved!")

# ---- CHART 2: Program Distribution ----
plt.figure()
df['Program'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Program Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig('chart2_programs.png')
plt.show()
print("Chart 2 saved!")

# ---- CHART 3: Gender Distribution ----
plt.figure()
df['Gender'].value_counts().plot(kind='bar', color=['coral', 'steelblue'])
plt.title('Gender Distribution of Beneficiaries')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('chart3_gender.png')
plt.show()
print("Chart 3 saved!")

# ---- CHART 4: Donations by City ----
plt.figure()
df.groupby('City')['Donation_Received'].sum().sort_values().plot(kind='barh', color='green')
plt.title('Total Donations Received by City')
plt.xlabel('Total Donation (₹)')
plt.tight_layout()
plt.savefig('chart4_donations.png')
plt.show()
print("Chart 4 saved!")

# ---- CHART 5: Yearly Trend ----
plt.figure()
df.groupby('Year')['BeneficiaryID'].count().plot(kind='line', marker='o', color='purple')
plt.title('Beneficiary Enrollment Trend by Year')
plt.xlabel('Year')
plt.ylabel('Number of Beneficiaries')
plt.tight_layout()
plt.savefig('chart5_trend.png')
plt.show()
print("Chart 5 saved!")


import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# ---- DASHBOARD ----
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        'Beneficiaries by City',
        'Program Distribution',
        'Gender Distribution',
        'Donations by City',
        'Yearly Enrollment Trend',
        'Income Group Distribution'
    ),
    specs=[
        [{"type": "xy"}, {"type": "domain"}],
        [{"type": "xy"}, {"type": "xy"}],
        [{"type": "xy"}, {"type": "xy"}]
    ]
)

# Chart 1 — City
city_counts = df['City'].value_counts()
fig.add_trace(go.Bar(
    x=city_counts.index,
    y=city_counts.values,
    marker_color='steelblue',
    name='City'
), row=1, col=1)

# Chart 2 — Program pie
program_counts = df['Program'].value_counts()
fig.add_trace(go.Pie(
    labels=program_counts.index,
    values=program_counts.values,
    name='Program'
), row=1, col=2)

# Chart 3 — Gender
gender_counts = df['Gender'].value_counts()
fig.add_trace(go.Bar(
    x=gender_counts.index,
    y=gender_counts.values,
    marker_color=['coral', 'steelblue'],
    name='Gender'
), row=2, col=1)

# Chart 4 — Donations by City
donations = df.groupby('City')['Donation_Received'].sum().sort_values()
fig.add_trace(go.Bar(
    x=donations.values,
    y=donations.index,
    orientation='h',
    marker_color='green',
    name='Donations'
), row=2, col=2)

# Chart 5 — Yearly trend
yearly = df.groupby('Year')['BeneficiaryID'].count()
fig.add_trace(go.Scatter(
    x=yearly.index,
    y=yearly.values,
    mode='lines+markers',
    marker_color='purple',
    name='Trend'
), row=3, col=1)

# Chart 6 — Income group
income_counts = df['Income_Group'].value_counts()
fig.add_trace(go.Bar(
    x=income_counts.index,
    y=income_counts.values,
    marker_color='orange',
    name='Income'
), row=3, col=2)

fig.update_layout(
    height=900,
    title_text='NayePankh Foundation — Data Analytics Dashboard',
    title_font_size=20,
    showlegend=False
)

fig.write_html('nayepankh_dashboard.html')
print("Dashboard saved as nayepankh_dashboard.html")

fig.show()

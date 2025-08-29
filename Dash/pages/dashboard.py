import streamlit as st
import seaborn as sns
import plotly.express as px

st.title("Explore Hidden Insights of Car Accidents")

df = sns.load_dataset("car_crashes")
st.dataframe(df)

#filters
state = st.sidebar.multiselect('State',
                                options = df['abbrev'].unique(),
                                default = df['abbrev'].unique())
                                

accidents = st.selectbox(
    "Select Accident Type:",
    ["total", "speeding", "alcohol"]
)

min_ins, max_ins = st.sidebar.slider('Insurance',
                                     min_value = int(df['ins_premium'].min()),
                                     max_value = int(df['ins_premium'].max()),
                                     value = (int(df['ins_premium'].min()), int(df['ins_premium'].max())))

fil_df = df[
    (df['abbrev'].isin(state)) &
    (df['ins_premium']>=min_ins) &
    (df['ins_premium']<=max_ins) 
]

# accidents by state (dynamic)
fig = px.bar(
    fil_df,
    x='abbrev',
    y=accidents,
    title=f"{accidents} accidents by state",
    labels={'abbrev': 'State', accidents: f'{accidents} Accidents'},
    color=accidents,
    template='plotly_dark'
)
st.plotly_chart(fig)



# top 10 states by insurance premium 
top10= fil_df.sort_values('ins_premium', ascending = False).head(10)
fig = px.bar(top10,x = 'abbrev',y='ins_premium',
             title = 'Top 10 states by insurance premium',
             labels ={'abbrev': 'State','ins_premium': 'insurance premium'},
             color = 'ins_premium',
             template = 'plotly_dark')
st.plotly_chart(fig)


# percentage of selected accident type
fig = px.pie(
    fil_df,
    values=accidents,
    names='abbrev',
    title=f'Percentage of {accidents} Accidents by state',
    labels={'abbrev': 'State', accidents: f'{accidents} Accidents'},
    template='plotly_dark',
    color=accidents
)
fig.update_traces(textinfo='percent+label', textposition='inside')
st.plotly_chart(fig)


# Manually map states to regions
region_map = {
    'CT': 'Northeast', 'ME': 'Northeast', 'MA': 'Northeast', 'NH': 'Northeast', 'RI': 'Northeast', 'VT': 'Northeast',
    'NJ': 'Northeast', 'NY': 'Northeast', 'PA': 'Northeast',
    'IL': 'Midwest', 'IN': 'Midwest', 'MI': 'Midwest', 'OH': 'Midwest', 'WI': 'Midwest',
    'IA': 'Midwest', 'KS': 'Midwest', 'MN': 'Midwest', 'MO': 'Midwest', 'NE': 'Midwest', 'ND': 'Midwest', 'SD': 'Midwest',
    'DE': 'South', 'FL': 'South', 'GA': 'South', 'MD': 'South', 'NC': 'South', 'SC': 'South', 'VA': 'South', 'DC': 'South',
    'WV': 'South', 'AL': 'South', 'KY': 'South', 'MS': 'South', 'TN': 'South', 'AR': 'South', 'LA': 'South', 'OK': 'South', 'TX': 'South',
    'AZ': 'West', 'CO': 'West', 'ID': 'West', 'MT': 'West', 'NV': 'West', 'NM': 'West', 'UT': 'West', 'WY': 'West',
    'AK': 'West', 'CA': 'West', 'HI': 'West', 'OR': 'West', 'WA': 'West'
}

# Add region column using abbrev
fil_df['region'] = fil_df['abbrev'].map(region_map)
fil_df

fig = px.sunburst(
    fil_df,
    path=['region', 'abbrev'],
    values=accidents,
    title=f'Region-wise, State-wise {accidents} Accidents',
    color=accidents,
    template='plotly_dark'
)
st.plotly_chart(fig)



# Alcohol vs Speeding
fig = px.scatter(fil_df, x = 'speeding',
                 y='alcohol',
                 color = 'abbrev',
                 size = 'total',
                 title = 'Speeding vs Alcoholic Accidents',
                 )
st.plotly_chart(fig)
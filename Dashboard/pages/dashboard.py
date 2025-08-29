import streamlit as st
import seaborn as sns
import plotly.express as px

st.title("Explore Hidden Insights of Titanic Incident")

df = sns.load_dataset("titanic")
st.dataframe(df)

#filters
gender = st.sidebar.multiselect('Gender',
                                options = df['sex'].unique(),
                                default = df['sex'].unique())
                                

pclass = st.sidebar.multiselect('Passenger Class',
                                options = df['class'].unique(),
                                default = df['class'].unique())

min_age, max_age = st.sidebar.slider('Age',
                                     min_value = int(df['age'].min()),
                                     max_value = int(df['age'].max()),
                                     value = (int(df['age'].min()), int(df['age'].max())))

fil_df = df[
    (df['sex'].isin(gender)) &
    (df['class'].isin(pclass)) &
    (df['age']>=min_age) &
    (df['age']<=max_age) 
]

# survival count
fig = px.bar(fil_df, x="survived", title="Survival Count")
st.plotly_chart(fig)

# Gender distribution
fig = px.pie(fil_df, names="sex", 
            title="Gender Distribution on Titanic",
            color = 'sex',)
st.plotly_chart(fig)

# age distribution across passengers class 
fig = px.box(fil_df, x="pclass", y="age", 
            title="Age Distribution Across Passenger Classes",
            color = "age")
st.plotly_chart(fig)

# age distribution of passengers
fig = px.histogram(fil_df, x="age", nbins=30, 
                   title="Age Distribution of Passengers",
                   color = "age")
st.plotly_chart(fig)

# age vs fare 
fig = px.scatter(fil_df, x="age", y="fare", color="survived",
                 title="Age vs Fare (Survival Colored)",
                 )
st.plotly_chart(fig)
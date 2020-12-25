import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
chart = px.scatter(df, x = "Date", y = "Cases", color = "Country", size = "Cases")
chart.show()
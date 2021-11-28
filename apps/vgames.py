import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

path = pathlib.Path(__file__).parent
data_path = path.joinpath("../datasets").resolve()

dfv = pd.read_csv(data_path.joinpath(("vgsales.csv")))
sales_list = []
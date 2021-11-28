import dash_html_components as html
from app import app

layout = html.Div([
    html.H1('About', style={"textAlign": "center"}),
    html.Br(),
    html.Div([
        html.H2('What is COVID-19?'),
        html.P("Coronavirus disease 2019 (COVID-19) is a contagious disease caused by severe acute respiratory "
               "syndrome coronavirus 2 (SARS-CoV-2). The first known case was identified in Wuhan, China, in December "
               "2019. The disease has since spread worldwide, leading to an ongoing pandemic. Symptoms of COVID-19 "
               "are variable, but often include fever, cough, headache, fatigue, breathing difficulties, and loss of "
               "smell and taste."),
    ])
])
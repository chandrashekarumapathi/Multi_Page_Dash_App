import dash

# meta-tags are for mobile device support, the app works well on laptops even without meta-tags
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])

server = app.server
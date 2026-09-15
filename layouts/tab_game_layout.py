import dash_mantine_components as dmc
from dash import dcc

game_layout = [
    dcc.Store(id='guest-cheese-count', data=0),
    dmc.Image(
        radius= "sm", 
        src="https://news.harvard.edu/wp-content/uploads/2024/11/cheese-wondering-min.png?w=1488", 
        w=150,
        ),
    dmc.Text("Click the button to get cheese!", id='txt-cheese-count'),
    dmc.Button("Add", id='btn-add', size="md"),
]

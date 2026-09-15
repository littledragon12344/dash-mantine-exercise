from dash import Dash
from dash_iconify import DashIconify
import dash_mantine_components as dmc

from layouts.main_layout import main_page_layout

import callbacks

app = Dash()
app.title = 'CODEVISION_TRAINING'

app.layout = [
    dmc.MantineProvider(
        children=[
            dmc.AppShell(
                children=[
                    dmc.AppShellHeader(children=[]),
                    dmc.AppShellNavbar(children=[]),
                    dmc.AppShell(dmc.AppShellMain(children = main_page_layout)),
                    dmc.AppShellFooter(children=[]),
                ]

            )

        ]

    )
]

if __name__ == "__main__" :
    
    #Load Tools to the Vector DB Tools
    #a_vector.load_tools_to_vectordb()

    app.run(debug=True,
            port=8060,
            host='localhost',
            )

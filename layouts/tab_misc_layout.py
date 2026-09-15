
from dash import dcc
from dash_iconify import DashIconify
import dash_mantine_components as dmc

misc_layout = [
    dmc.Flex(
        children= [
            dcc.Upload(
                children=dmc.Stack(
                    [
                        dmc.Box(
                            [
                                DashIconify(icon="line-md:file-upload"),
                                "Drag and Drop or Click to Upload Files",
                            ],
                        ),
                        dmc.Text(
                            "Supported formats: XLS, XLSX, DOC, DOCX",
                            size="sm",
                            c="dimmed",
                        ),
                    ],
                    gap=0,
                    align="center",
                ),
                id="files-upload",
                multiple=True,
            ),
            dmc.Box([], id='feedback-files-upload'),
        ],
        direction="column",
        justify="space-around",
        align="center",
        mx="15px"
    ),
]

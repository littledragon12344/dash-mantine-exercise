import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import dcc

settings_layout = [
    dmc.Group(
        children= [
            "Volumn",
            dmc.Slider(
                color= "red",
                size= "sm",
                radius= "md",
                showLabelOnHover= True,
                value= 50,
                w="80%",
                marks= [
                    {"value": 0, "label": "0%"},
                    {"value": 25, "label": "25%"},
                    {"value": 50, "label": "50%"},
                    {"value": 75, "label": "75%"},
                    {"value": 100, "label": "100%"},
                ],
                ml="auto",
            ),
        ],
        gap="sm",
        justify="space-around",
        align="center",
        mx="15px",
    ),
    dmc.Space(h="xl"),
    dmc.Group(
        children= [
            "Smelly Cheese",
            dmc.Switch(
                labelPosition= "right",
                size= "md",
                radius= "sm",
                color="teal",
                ml="auto",
            ),
        ],
        gap="sm",
        justify="space-around",
        align="center",
        mx="15px",
    ),
    dmc.Space(h="xl"),
    dmc.Flex(
        [
            dmc.Text("Avatar"),
            dmc.Box(
                children=dcc.Upload(
                    id='img-avatar-upload',
                    children= dmc.Stack(
                        [
                            dmc.Box(
                                [
                                    DashIconify(icon="line-md:file-upload"),
                                    "Drag and Drop or Click to Upload Image",
                                ],
                            ),
                            dmc.Text(
                                "Supported formats: PNG, JPG, JPEG, WEBP",
                                size="sm",
                                c="dimmed",
                            ),
                        ],
                        gap=0,
                        align="center",
                    ),
                    accept='.png, .jpg, .jpeg, .webp',
                ),
                ml="auto",
            )
        ],
        direction="row",
        justify="space-around",
        align="center",
        mx="15px",
    ),
    dmc.Box(children=[], id='feedback-avatar-upload'),
    
]

import dash_mantine_components as dmc

register_user_layout = dmc.Paper(
    children=[
        dmc.Modal(
            children=[
                dmc.Stack(
                    children=[
                        dmc.TextInput(
                            id='txt-input-regis-username',
                            placeholder="username",
                            label="Username",
                        ),
                        dmc.Group(
                            children=[
                                dmc.Button(
                                    "Cancel",
                                    id='btn-user-regis-cancel',
                                    color="red"
                                ),
                                dmc.Button(
                                    "Register",
                                    id='btn-user-regis',
                                    color="blue"
                                ),
                            ],
                            justify="space-evenly",
                            align="center",
                        ),
                    ]
                ),
            ],
            id='modal-regis'
            
        ),
        dmc.Flex(
            [], 
            id='feedback-regis',
            direction="column",
            justify="flex-end",
            align="center",
        ),
    ],
    ml="auto",
    variant="subtle",
)

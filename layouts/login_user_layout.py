import dash_mantine_components as dmc

login_user_layout = dmc.Paper(
    children=[
        dmc.Modal(
            children=[
                dmc.Stack(
                    children=[
                        dmc.TextInput(
                            id='txt-input-login-username',
                            placeholder="username",
                            label="Username",
                        ),
                        dmc.Group(
                            children=[
                                dmc.Text(
                                    "Don't have an account?",
                                    size="sm"
                                ),
                                dmc.Button(
                                    "Register here",
                                    id='btn-regis-txt',
                                    td="underline",
                                    variant="subtle",
                                    size="sm",
                                ),
                                
                            ],
                            justify="center",
                            align="center",
                        ),
                        dmc.Group(
                            children=[
                                dmc.Button(
                                    "Cancel",
                                    id='btn-user-login-cancel',
                                    color="red"
                                ),
                                dmc.Button(
                                    "Login",
                                    id='btn-user-login',
                                    color="blue"
                                ),
                            ],
                            justify="space-evenly",
                            align="center",
                        ),
                    ]
                ),
            ],
            id='modal-login'
            
        ),
        dmc.Flex(
            [], 
            id='feedback-login',
            direction="column",
            justify="flex-end",
            align="center",
        ),
    ],
    ml="auto",
    variant="subtle",
)

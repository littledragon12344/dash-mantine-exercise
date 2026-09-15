from db_tables_functions import db_crud
from dash import callback, Output, State, Input, ctx
import dash_mantine_components as dmc

# ============ toggle the login modal ============
@callback(
    Output('modal-login', 'opened'),
    State('modal-login', 'opened'),
    Input('btn-user-login', 'n_clicks'),
    Input('btn-user-login-cancel', 'n_clicks'),
    Input('btn-regis-txt', 'n_clicks'),
    Input('btn-avatar', 'n_clicks'),
    prevent_initial_call=True,
)
def toggle_login_modal(opened, *args):
    trigger = ctx.triggered_id
    
    if (trigger == 'btn-avatar'):
        return True
    else:
        return False

# ============ login action ============
@callback(
    Output('feedback-login', 'children'),
    Output('current-user', 'data'),
    Output('guest-cheese-count', 'data', allow_duplicate=True),
    State('txt-input-login-username', 'value'),
    State('guest-cheese-count', 'data'),
    Input('btn-user-login', 'n_clicks'),
    prevent_initial_call=True,
)
def login_user(username, guest_cheese_count, *args):
    user = db_crud.get_user(username=username)
    
    print(f"User record: {user}")
    
    if user is None:
        return (dmc.Text("User not found!", c="red"), None, guest_cheese_count)
    
    if guest_cheese_count > 0:
        db_crud.add_cheese_amount(
            user.username,
            "Cheddar",
            guest_cheese_count
        )

    return (
        dmc.Text(
            f"Welcome back {user.username}!",
            c="green"
        ),
        {
            "id" : user.id,
            "username" : user.username
        },
        0
    )

from db_tables_functions import db_crud
from dash import callback, Input,Output,State, no_update

# ============ add cheese using button ============
@callback(
    Output('guest-cheese-count', 'data'),
    Input('btn-add', 'n_clicks'),
    State('guest-cheese-count', 'data'),
    State('current-user', 'data'),
)
def btn_add_cheese_pressed(n_clicks, guest_cheese_count, current_user):
    if n_clicks is None:
        return no_update
    
    if current_user is not None:
        db_crud.increment_cheese_amount(current_user["username"], "Cheddar")
        cheese = db_crud.get_cheese_amount(current_user["username"], "Cheddar")
    else:
        guest_cheese_count += 1
    
    print(f"Clicked: {n_clicks}")
    return guest_cheese_count if current_user is None else cheese.amount

# ============ update cheese text display ============
@callback(
    Output("txt-cheese-count", "children"),
    Input("btn-add", "n_clicks"),
    Input("current-user", "data"),
    prevent_initial_call=True,
)
def update_cheese_count(n_clicks, current_user):
    if current_user is None:
        if n_clicks is None:
            return "Click the button to get cheese!"
        return f"You now have {n_clicks} cheese!"

    cheese = db_crud.get_cheese_amount(current_user["username"], "Cheddar")

    return f"You now have {cheese.amount} cheese!"

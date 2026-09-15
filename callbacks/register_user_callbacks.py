from db_tables_functions import db_crud
from dash import callback, Output, State, Input, ctx
import dash_mantine_components as dmc

# ============ toggle the regis modal ============
@callback(
    Output('modal-regis', 'opened'),
    State('modal-regis', 'opened'),
    Input('btn-user-regis', 'n_clicks'),
    Input('btn-user-regis-cancel', 'n_clicks'),
    Input('btn-regis-txt', 'n_clicks'),
    prevent_initial_call=True,
)
def toggle_regis_modal(opened, *args):
    trigger = ctx.triggered_id
    
    if (trigger == 'btn-regis-txt'):
        return True
    else:
        return False
    
# ============ register action ============
@callback(
    Output('feedback-regis', 'children'),
    State('txt-input-regis-username', 'value'),
    Input('btn-user-regis', 'n_clicks'),
    prevent_initial_call=True,
)
def register_user(username, n_clicks):
    feedback_msg = "Registered Successfully! Please Login now!"
    text_color = "green"
    
    try: 
        db_crud.register_user(username=username)
    except ValueError as e:
        feedback_msg = str(e)
        text_color = "red"
    except:
        feedback_msg = "Something went wrong while trying to register you!"
        text_color = "red"
    
    return dmc.Text(feedback_msg, c=text_color)

from db_tables_functions import db_crud
from dash import callback, Output, State, Input, no_update
import dash_mantine_components as dmc

# ============ upload avatar image ============
@callback(
    Output('avatar-player','src'),
    Output('feedback-avatar-upload','children'),
    Input('img-avatar-upload','contents'),
    State('img-avatar-upload','filename'),
    prevent_initial_call=True
)
def handle_avatar_upload(contents, filename):
    if contents is None:
        return no_update
    
    file_extension = str(filename).lower().split('.')[-1]
    
    print(file_extension)
    
    return (
        contents, 
        dmc.Alert(
            "Your Avatar is Uploaded and Updated!",
            title="SUCCESS!",
            color="green",
            withCloseButton=True
        )
    )

# ============ upload multiple files ============
@callback(
    Output('feedback-files-upload', 'children'),
    Input('files-upload', 'contents'),
    State('files-upload', 'filename'),
)
def handle_files_upload(contents,filename):
    if contents is None:
        return no_update
    
    # print(type(contents))
    # print(type(filename))
    
    result = []
    accepted_extensions = ['xls','xlsx', 'doc', 'docx']
    
    for data, name in zip(contents, filename):
        file_extension = str(name).lower().split('.')[-1]
        try:
            if file_extension in accepted_extensions:
                result.append(dmc.Alert(
                    f"{name} is uploaded successfully!",
                    title="SUCCESS!",
                    color="green",
                    withCloseButton=True
                ))
            else:
                raise Exception(f"{file_extension} file is not supported!")
        except Exception as e:
            result.append(dmc.Alert(
                str(e),
                title="ERROR!",
                color="red",
                withCloseButton=True
            ),)
        
        print("filename", name)
    
    return result


# ============ hide files upload alerts when switching tabs ============
@callback(
    Output('feedback-files-upload', 'children', allow_duplicate=True),
    Input('tabs-main', 'value'),
    prevent_initial_call=True
)
def clear_files_upload_alerts(active_tab):
    if active_tab != 'fourth':
        return []
    
    return no_update

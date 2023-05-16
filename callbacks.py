# Importing necessary modules
from dash import Input, Output
import plotly.express as px
from layout import df, dims

# Function to register all callbacks to a Dash app
def register_callbacks(app):
    # Callback 1: Updates table based on user's filters and range sliders.
    @app.callback(
        Output('players-table', 'data'),
        Input('activefilters', 'data'),
        Input('market-value-slider', 'value'),
        Input('contract-expiration-slider', 'value')
    )
    def update_table(activefilters, market_value_range, contract_expiration_range):
        dff = df.copy()

        for col, values in activefilters.items():
            if values:
                if len(values) == 1 and len(values[0]) == 2:
                    lower_bound, upper_bound = values[0]
                    dff = dff[(dff[col] >= lower_bound) & (dff[col] <= upper_bound)]
                else:
                    print(f"Unexpected values for {col}: {values}")

        dff = dff[(dff['Market Value'] >= market_value_range[0]) & (dff['Market Value'] <= market_value_range[1])]
        dff = dff[(dff['Contract Expiration Year'] >= contract_expiration_range[0]) & (
                dff['Contract Expiration Year'] <= contract_expiration_range[1])]

        return dff.to_dict('records')

    # Callback 2: Updates parallel coordinates plot based on range sliders.
    @app.callback(
        Output("parallel-coordinates-plot", "figure"),
        Input('market-value-slider', 'value'),
        Input('contract-expiration-slider', 'value'),
        Input('original-figure', 'data'),
    )
    def update_parallel_coordinates(market_value_range, contract_expiration_range, original_figure):
        dff = df.copy()
        dff = dff[(dff['Market Value'] >= market_value_range[0]) & (dff['Market Value'] <= market_value_range[1])]
        dff = dff[(dff['Contract Expiration Year'] >= contract_expiration_range[0]) & (
                dff['Contract Expiration Year'] <= contract_expiration_range[1])]

        updated_fig = px.parallel_coordinates(dff, dimensions=dims, color_continuous_scale=px.colors.diverging.Tealrose,
                                              color_continuous_midpoint=2)

        return updated_fig

    # Callback 3: Updates active filters based on plot selections.
    @app.callback(
        Output('activefilters', 'data'),
        Input("parallel-coordinates-plot", "restyleData")
    )
    def update_filters(data):
        activefilters = {}

        if data:
            updates = data[0]
            for key, value in updates.items():
                if 'dimensions[' in key:
                    dim_index = int(key.split('[')[1].split(']')[0])
                    dim_name = dims[dim_index]
                    activefilters[dim_name] = value

        return activefilters
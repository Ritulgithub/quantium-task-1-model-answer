import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.testing.application_runners import import_app
from dash.testing.wait import until
import pytest

# Import your Dash app
from task4 import app

# Create a test app runner
app_runner = import_app(app)


# Define the tests
def test_header_presence():
    # Start the app
    app_runner.run_server()

    # Wait until the header component is present
    until(lambda: any(isinstance(item, html.H1) and "Pink Morsels Sales Data" in item.children for item in
                      app_runner.app.layout.children), timeout=10)

    # Access the app's layout
    layout = app_runner.app.layout

    # Check if the header component is present
    assert any(isinstance(item, html.H1) and "Pink Morsels Sales Data" in item.children for item in
               layout.children), "Header is not present"


def test_visualization_presence():
    # Start the app
    app_runner.run_server()

    # Wait until the visualization component is present
    until(lambda: any(isinstance(item, dcc.Graph) for item in app_runner.app.layout.children), timeout=10)

    # Access the app's layout
    layout = app_runner.app.layout

    # Check if the visualization component is present
    assert any(isinstance(item, dcc.Graph) for item in layout.children), "Visualization is not present"


def test_region_picker_presence():
    # Start the app
    app_runner.run_server()

    # Wait until the region picker component is present
    until(lambda: any(
        isinstance(item, dcc.RadioItems) and item.id == "region-radio" for item in app_runner.app.layout.children),
          timeout=10)

    # Access the app's layout
    layout = app_runner.app.layout

    # Check if the region picker component is present
    assert any(isinstance(item, dcc.RadioItems) and item.id == "region-radio" for item in
               layout.children), "region picker is not present"


# Execute the test suite using Pytest
if __name__ == "__main__":
    pytest.main(["-vv", "test_dash_app.py"])

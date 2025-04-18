from visualisation import app

def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#header', timeout=10)

def test_visualisation(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#line_chart', timeout=10)

def test_region_picker(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#region_picker', timeout=10)

from app import app


def test_visual_output(dash_duo, expected_number_of_plots=None):
    dash_duo.start_server(app)
    dash_duo.find_element("#show-visualizations-btn").click()
    # Verify that the correct number of plots is generated
    plots = dash_duo.find_elements(".plot-container.plotly")
    assert len(plots) == expected_number_of_plots

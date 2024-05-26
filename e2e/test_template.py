from pathlib import Path

import pytest
from e2e_utils import StreamlitRunner
from playwright.sync_api import Page, expect

ROOT_DIRECTORY = Path(__file__).parent.parent.absolute()
BASIC_EXAMPLE_FILE = ROOT_DIRECTORY / "streamlit_pandera" / "Home.py"


@pytest.fixture(autouse=True, scope="module")
def streamlit_app():
    with StreamlitRunner(BASIC_EXAMPLE_FILE) as runner:
        yield runner


@pytest.fixture(autouse=True, scope="function")
def go_to_app(page: Page, streamlit_app: StreamlitRunner):
    page.goto(streamlit_app.server_url)
    # Wait for app to load
    page.get_by_role("img", name="Running...").is_hidden()


def test_selectbox_widget_rendering(page: Page):
    """Test that the selectbox widgets are correctly rendered via screenshot matching."""
    selectbox_widgets = page.get_by_test_id("stSelectbox")
    expect(selectbox_widgets).to_have_count(1)


def change_widget_values(app: Page):
    """Change the checkbox value."""
    # Get the first form:
    form_1 = app.get_by_test_id("stForm").nth(0)
    form_1.get_by_test_id("stCheckbox").nth(0).click()

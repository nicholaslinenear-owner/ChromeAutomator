"""
Tests for ChromeAutomator class
"""

import pytest

from chrome_automator import ChromeAutomator, AutomatorOptions


@pytest.fixture
def automator() -> ChromeAutomator:
    """Fixture to create automator instance"""
    return ChromeAutomator(
        options=AutomatorOptions(headless=True, timeout=30000)
    )


class TestChromeAutomator:
    """Tests for ChromeAutomator class"""

    def test_instantiate_with_default_options(self) -> None:
        """Test instantiation with default options"""
        automator = ChromeAutomator()
        assert automator is not None
        assert automator.browser is None
        assert automator.page is None

    def test_instantiate_with_custom_options(self) -> None:
        """Test instantiation with custom options"""
        options = AutomatorOptions(headless=False, timeout=60000)
        automator = ChromeAutomator(options=options)
        assert automator.options.headless is False
        assert automator.options.timeout == 60000

    @pytest.mark.asyncio
    async def test_launch_and_close(self, automator: ChromeAutomator) -> None:
        """Test launching and closing browser"""
        await automator.launch()
        assert automator.browser is not None
        assert automator.page is not None
        await automator.close()
        assert automator.browser is None

    @pytest.mark.asyncio
    async def test_launch_twice_raises_error(
        self, automator: ChromeAutomator
    ) -> None:
        """Test that launching twice raises error"""
        await automator.launch()
        try:
            with pytest.raises(RuntimeError, match="Browser is already launched"):
                await automator.launch()
        finally:
            await automator.close()

    @pytest.mark.asyncio
    async def test_navigate_without_launch_raises_error(
        self, automator: ChromeAutomator
    ) -> None:
        """Test that navigating without launch raises error"""
        with pytest.raises(RuntimeError, match="Browser not launched"):
            await automator.navigate("https://example.com")

    @pytest.mark.asyncio
    async def test_get_title_without_launch_raises_error(
        self, automator: ChromeAutomator
    ) -> None:
        """Test that getting title without launch raises error"""
        with pytest.raises(RuntimeError, match="Browser not launched"):
            await automator.get_title()

    @pytest.mark.asyncio
    async def test_screenshot_without_launch_raises_error(
        self, automator: ChromeAutomator
    ) -> None:
        """Test that screenshot without launch raises error"""
        with pytest.raises(RuntimeError, match="Browser not launched"):
            await automator.screenshot()

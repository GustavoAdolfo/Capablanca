from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Edit acessa a página inicial
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1366, 768)

        # Ela percebe que o inputbox está elegantemente centralizada
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            610,
            delta=10
        )

        # Ela inicia uma nova lista e vê que a entrada está elegantemente centralizada
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            610,
            delta=10
        )

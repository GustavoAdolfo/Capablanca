from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):
        # Edith ouviu falar de uma nova apliacação online interessate para
        # listas de tarefas. Ela decide verificar sua homepage.
        self.browser.get(self.live_server_url)

        # Ela percebe que o título da página e o cabeçalho mencionam listas de
        # tarefas(to-do)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # Ela é convidada a inserir uma lista de tarefas imediatamente
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item')
        # Ela digita "Bue peacock feathers" (comprar penas de pavão) em uma caixa
        # de texto (o hobby de Edith é fazer iscas para pesca com fly)
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Quando ela tecla enter, a página é atualizada, e agora a página lista
        # "1: Buy peacock feathers" como um item em uma lista de tarefas
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro
        # item. Ela insere "Use a peacock feathers to make a fly" (Usar penas de pavão
        # para fazer um fly - Edith é bem metódica)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use a peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # A página é atualizada novamente e agora mostra os dois itens em sua lista.
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use a peacock feathers to make a fly')

        # Edit se pergunta se o site lembrará de sua lista. Então ela nota
        # que o site gerou um URL único para ela - há um pequeno
        # texto explicativo para isso.
        self.fail('Finish the test!')

        # Ela acessa esse URL - sua lista de tarefas continua lá.

        # Satisfeita, ela volta a dormir

if __name__ == '__main__':
    unittest.main()



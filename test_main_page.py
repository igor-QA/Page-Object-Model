# Команда для запуска:
# pytest -v --tb=line --language=en test_main_page.py
# pytest -v --tb=line --language=en -m login_guest test_main_page.py
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage



@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес  
        page.open() #открываем страницу                     
        page.go_to_login_page() #выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


    def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    	link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = BasketPage(browser, link) #Гость открывает главную страницу 
        page.open()
        page.go_to_basket() #Переходит в корзину по кнопке в шапке сайта
        page.should_not_be_item_in_the_basket() #Ожидаем, что в корзине нет товаров
        page.should_message_basket_is_empty() #Ожидаем, что есть текст о том что корзина пуста 


 

'''
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали 
        self.product.delete()
        
'''
        

  
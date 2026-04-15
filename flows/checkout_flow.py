from app.pages.cart_page import CartPage
from app.pages.checkout_complete_page import CheckoutCompletePage
from app.pages.checkout_info_page import CheckoutInfoPage
from app.pages.checkout_overview_page import CheckoutOverviewPage


class CheckoutFlow:
    def __init__(
        self,
        cart_page: CartPage,
        info_page: CheckoutInfoPage,
        overview_page: CheckoutOverviewPage,
        complete_page: CheckoutCompletePage,
    ):
        self._cart_page = cart_page
        self._info_page = info_page
        self._overview_page = overview_page
        self._complete_page = complete_page

    def complete_full_checkout(
        self, first_name: str, last_name: str, zip_code: str
    ) -> CheckoutCompletePage:
        self._cart_page.click_checkout()
        self._info_page.fill_shipping_info(first_name, last_name, zip_code)
        self._info_page.click_continue()
        self._overview_page.click_finish()
        return self._complete_page

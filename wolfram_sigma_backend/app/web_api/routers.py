from wolfram_sigma_backend.app.web_api.main_page import main_page_router
from wolfram_sigma_backend.app.web_api.test_protected_route import test_router
from wolfram_sigma_backend.app.web_api.user_account import user_account_page

routers = [main_page_router, test_router, user_account_page]
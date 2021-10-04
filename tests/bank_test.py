import unittest
from src.models import BaseBank, Bank, UserPasswordBankLogin
from contextlib import AbstractAsyncContextManager, AbstractContextManager


class BankTest(unittest.TestCase):
    def test_bank_should_have_base_bank_urls(self):
        spy_bank = self._create_spy_bank()
        self.assertEqual(spy_bank.login_url, "login_url")
        self.assertEqual(spy_bank.accounts_url, "accounts_url")
        self.assertEqual(spy_bank.movements_url, "movements_url")
        self.assertEqual(spy_bank.logout_url, "logout_url")

    def test_should_implement_enter_exit_methods(self):
        spy_bank = self._create_spy_bank()
        self.assertTrue("__enter__" in dir(spy_bank), "Enter method not implemented")
        self.assertTrue("__exit__" in dir(spy_bank), "Exit method not implemented")

    def test_with_block_should_call_login_and_logout(self):
        with self._create_spy_bank() as spy_bank:
            pass

        self.assertEqual(spy_bank.called_login, 1)
        self.assertEqual(spy_bank.called_logout, 1)

    def _create_mock_bank(self):
        return MockedBaseBank(
            "login_url", "accounts_url", "movements_url", "logout_url"
        )

    def _create_spy_bank(self):
        mock_base_bank = self._create_mock_bank()
        bank = BankSpy(
            "Mocked",
            mock_base_bank,
            credentials=UserPasswordBankLogin("mocked_user", "mocked_password"),
        )
        return bank


class BankSpy(Bank):
    def __init__(self, name, baseBank, credentials):
        super().__init__(name, baseBank, credentials)
        self.called_login = 0
        self.called_fetch_accounts = 0
        self.called_logout = 0

    def login(self):
        self.called_login += 1

    def fetch_accounts(self):
        self.called_fetch_accounts += 1

    def logout(self):
        self.called_logout += 1


class MockedBaseBank(BaseBank):
    pass

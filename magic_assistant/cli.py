from loguru import logger
from rich.console import Console
from pydantic import BaseModel

from magic_assistant.tips import get_tip
from magic_assistant.models.llm.llm_factory import LlmFactory

class Cli():
    def __init__(self, language_code: str, llm_factory: LlmFactory):
        self.language_code: str = language_code
        self.llm_factory: LlmFactory = llm_factory
        self._console: Console = Console()

    def start_loop(self):
        welcome_tip = get_tip(self.language_code, "welcome")
        self._magic_assistant_output(welcome_tip)

        while True:
            user_input = self._user_input()
            self.llm_factory.predict(user_input)

    def _magic_assistant_output(self, output: str):
        role = "magic_assistant"
        self._console.print(f"[bold]{role}: {output}")
        logger.debug("_magic_assistant_output suc, input:%s" % output)

    def _user_input(self):
        role = "user"
        # user_input = self._console.input(f"[bold]{role}: ")
        user_input = self._console.input("user: ")

        logger.debug("_user_input suc, input:%s" % user_input)
        return user_input

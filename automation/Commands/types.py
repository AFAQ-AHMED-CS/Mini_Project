from abc import ABC, abstractmethod
from typing import Any, Dict

from selenium.webdriver import Firefox

from ..SocketInterface import clientsocket


class BaseCommand(ABC):
    def set_visit_browser_id(self, visit_id, browser_id):
        self.visit_id = visit_id
        self.browser_id = browser_id

    def set_start_time(self, start_time):
        self.start_time = start_time

    # FIXME: After transitioning all Commands to the new format this needs to be reenabled
    # @abstractmethod
    def execute(
        self,
        webdriver: Firefox,
        browser_settings: Dict[str, Any],
        browser_params: Dict[str, Any],
        manager_params: Dict[str, Any],
        extension_socket: clientsocket,
    ) -> None:
        raise NotImplementedError()


class DumpProfCommand(BaseCommand):
    def __init__(self, dump_folder, close_webdriver, compress):
        self.dump_folder = dump_folder
        self.close_webdriver = close_webdriver
        self.compress = compress

    def __repr__(self):
        return "DumpProfCommand({},{},{})".format(
            self.dump_folder, self.close_webdriver, self.compress
        )


class DumpPageSourceCommand(BaseCommand):
    def __init__(self, suffix):
        self.suffix = suffix

    def __repr__(self):
        return "DumpPageSourceCommand({})".format(self.suffix)


class RecursiveDumpPageSourceCommand(BaseCommand):
    def __init__(self, suffix):
        self.suffix = suffix

    def __repr__(self):
        return "RecursiveDumpPageSourceCommand({})".format(self.suffix)


class SaveScreenshotCommand(BaseCommand):
    def __init__(self, suffix):
        self.suffix = suffix

    def __repr__(self):
        return "SaveScreenshotCommand({})".format(self.suffix)


class ScreenshotFullPageCommand(BaseCommand):
    def __init__(self, suffix):
        self.suffix = suffix

    def __repr__(self):
        return "ScreenshotFullPageCommand({})".format(self.suffix)


class RunCustomFunctionCommand(BaseCommand):
    def __init__(self, function_handle, func_args):
        self.function_handle = function_handle
        self.func_args = func_args

    def __repr__(self):
        return "RunCustomFunctionCommand({},{})".format(
            self.function_handle, self.func_args
        )


class ShutdownCommand(BaseCommand):
    def __repr__(self):
        return "ShutdownCommand()"


class FinalizeCommand(BaseCommand):
    """This command is automatically appended to the end of a CommandSequence
    It's apperance means there won't be any more commands for this
    visit_id
    """

    def __init__(self, sleep):
        self.sleep = sleep

    def __repr__(self):
        return f"FinalizeCommand({self.sleep})"


class InitializeCommand(BaseCommand):
    """The command is automatically prepended to the beginning of a
    CommandSequence
    It initializes state both in the extensions as well in as the
    Aggregator
    """

    def __repr__(self):
        return "IntitializeCommand()"

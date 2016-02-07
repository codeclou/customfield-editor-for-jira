import sys
import colorama
import textwrap
import tabulate
class PrintHelper:

    def _success_prefix(self):
        if sys.stdout.encoding == 'UTF-8':
            return u'  ✓ '
        return '  SUCCESS '

    def _error_prefix(self):
        if sys.stdout.encoding == 'UTF-8':
            return u'  ✗ '
        return '  ERROR '

    def success(self, text):
        print(colorama.Fore.GREEN + self._success_prefix() + text)

    def error(self, text):
        print(colorama.Fore.RED + self._error_prefix() + text)

    def step(self, text):
        print(colorama.Fore.CYAN + '\n> ' + text)

    def headline(self, text):
        print(colorama.Fore.MAGENTA + '\n# ' + text)

    def action(self, text):
        print(colorama.Fore.MAGENTA + '\n# Action: ' + text)

    def table(self, json):
        print(textwrap.indent(tabulate.tabulate(json, headers="keys"), '  '))

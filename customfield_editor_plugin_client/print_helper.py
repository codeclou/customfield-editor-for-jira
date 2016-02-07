import sys
import colorama

class PrintHelper:

    def _success_prefix(self):
        """get success icon to print if system encoding is utf-8"""
        if sys.stdout.encoding == 'UTF-8':
            return u'✓ '
        return 'SUCCESS '

    def _error_prefix(self):
        """get success icon to print if system encoding is utf-8"""
        if sys.stdout.encoding == 'UTF-8':
            return u'❌ '
        return 'ERROR '

    def success(self, text):
        print(colorama.Fore.GREEN + self._success_prefix() + text)

    def error(self, text):
        print(colorama.Fore.RED + self._error_prefix() + text)

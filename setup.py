from setuptools import setup

setup(name='customfield_editor_plugin_client',
      version='1.2rc1',
      description='Python client for Customfield Editor Plugin for Atlassian JIRA®',
      url='https://github.com/codeclou/customfield-editor-plugin/tree/python-demo-client',
      author='codeclou.io',
      author_email='info@codeclou.io',
      license='MIT',
      packages=['customfield_editor_plugin_client'],
      install_requires=[
          'requests',
          'argparse',
          'validators',
          'colorama'
      ],
      zip_safe=False,
      entry_points = {
          'console_scripts': ['cep-client=customfield_editor_plugin_client.cli_client:main'],
      })

from setuptools import setup

setup(name='customfield_editor_plugin_client',
      version='0.1',
      description='Python client for Customfield Editor Plugin for Atlassian JIRA®',
      url='https://github.com/codeclou/customfield-editor-plugin/tree/python-demo-client',
      author='codeclou.io',
      author_email='info@codeclou.io',
      license='MIT',
      packages=['customfield_editor_plugin_client'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)

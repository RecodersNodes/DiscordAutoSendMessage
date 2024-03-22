from distutils.core import setup
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = 'DiscordAutoSendMessage',         # How you named your package folder (MyLib)
    packages = ['DiscordAutoSendMessage'],   # Chose the same as "name"
    version = '1.3',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'script to auto sending messages to discord channel/group',   # Give a short description about your library
    long_description=long_description,            # Give a long description about your library
    long_description_content_type='text/markdown',
    author = 'recodersnodes',                   # Type in your name
    author_email = 'hapizdnuryadin1412@gmail.com',      # Type in your E-Mail
    url = 'https://github.com/RecodersNodes/DiscordAutoSendMessage',   # Provide either the link to your github or to your website
    download_url = '',    # I explain this later on
    project_urls={
        'Documentation': 'https://github.com/RecodersNodes/DiscordAutoSendMessage',
        'Source': 'https://github.com/RecodersNodes/DiscordAutoSendMessage',
        'Tracker': 'https://github.com/RecodersNodes/DiscordAutoSendMessage/issues',
    }, 
    keywords = ['discord', 'auto', 'bot', 'message', 'chat'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests>=2.25.0',
          'PyYAML>=5.3',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ], 
)
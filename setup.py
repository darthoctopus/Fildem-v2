import setuptools
import os
import sys

import fildem

with open('README.md', 'r') as fh:
	long_description = fh.read()



def fildemStartup():
	return input("Would you like to run fildem on startup? [Y/N]: ")

def __Main__():
	if (sys.argv[1] == "install"):
		response = fildemStartup().lower()
		if (response == "y" or response == "yes"):
			os.system("mv ./fildemstartup/* ~/.config/autostart/")
		elif (response == "n" or response == "no"):
			print("")
		else:
			#Ask the question again
			__Main__()

__Main__()

setuptools.setup(
	name='fildem',
	version=fildem.__version__,
	author='Gonzalo',
	author_email='gonzaarcr@gmail.com',
	description='Fildem Global Menu for Gnome Desktop',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/gonzaarcr/Fildem',
	packages=setuptools.find_packages(),
	data_files=[
		('share/applications', ['fildem-hud.desktop'])
	],
	install_requires=[
		'PyGObject>=3.30.0', 'setproctitle'
	],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Operating System :: POSIX :: Linux'
	],
	project_urls={
		'Bug Reports': 'https://github.com/gonzaarcr/Fildem/issues',
		'Source': 'https://github.com/gonzaarcr/Fildem',
	},
	entry_points={
		'console_scripts': [
			'fildem = fildem.run:main',
			'fildem-hud = fildem.inithud:main'
		]
	}
)

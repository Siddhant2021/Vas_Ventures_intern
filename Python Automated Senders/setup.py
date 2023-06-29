from setuptools import setup

APP = ['v.py']

OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    # Include any additional packages your code depends on
    'packages': ['schedule'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

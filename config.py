# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'nashville',
    package_name = 'montclair-nashville',
    name = 'Go Nashville',
    description = 'Real Time Tracking of the Buses for Nashville, TN',
    url = 'https://nashville.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.6.1',
        revision = 1,
        title = 'Go Nashville',
        first_run_text = "Welcome to Nashville, TN's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.5',
        revision = 1,
        app_id = 'com.gotransitapp.nashville',
        app_store_id = '1495548837',
        app_store_url = 'https://apps.apple.com/us/app/go-nashville/id1495548837'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.2',
        revision = 1,
        app_id = 'com.gotransitapp.nashville',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.nashville'
    )
)

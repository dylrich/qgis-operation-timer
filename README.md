# Installation

Download the .zip file or clone this repository. Place the `operation-timer` folder inside of your QGIS plugins folder. By default it is located at one of the following directories:

##### Windows
`C:\Users\username\.qgis2\python\plugins`
##### MacOS
`/Users/username/.qgis2/python/plugins`
##### Linux
`/home/username/.qgis2/python/plugins`

# Warning

This plugin makes use of the pre and post process hooks in QGIS. If you have Python scripts already located there, this plugin will overwrite the path to those scripts. If you aren't familiar with these hooks, you won't notice any difference. Future improvements may include a more elegant solution to handling pre-existing scripts.

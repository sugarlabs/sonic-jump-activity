What is this?
=============

Sonic Jump is an arcade game for the Sugar desktop.

How to use?
===========

Sonic Jump is part of the Sugar desktop.  Please refer to;

* [How to Get Sugar on sugarlabs.org](https://sugarlabs.org/),
* [How to use Sugar](https://help.sugarlabs.org/),
* [Download Sonic Jump using Browse](https://activities.sugarlabs.org/), search for `Sonic Jump`, then download, and;
* Refer the 'How to play' section inside the activity

How to upgrade?
===============

On Sugar desktop systems;
* use [My Settings](https://help.sugarlabs.org/en/my_settings.html), [Software Update](https://help.sugarlabs.org/en/my_settings.html#software-update), or;
* use Browse to open [activities.sugarlabs.org](https://activities.sugarlabs.org/), search for `Sonic Jump`, then download.

How to run?
=================

Sonic Jump depends on Python, PyGTK and PyGame.

Sonic Jump is started by [Sugar](https://github.com/sugarlabs/sugar).

Sonic Jump is not packaged by Debian and Ubuntu distributions.  
On Ubuntu systems these required dependencies (`python-gtk2-dev` and
`python-pygame`) need to be manually installed.


**Running on Ubuntu**
- Install the dependencies - 
```
sudo apt install python-gtk2-dev python-pygame
```

- Clone the repo and run-
```
git clone https://github.com/sugarlabs/sonic-jump-activity.git
cd sonic-jump-activity
python main.py
```

**Running inside Sugar**

- Open Terminal activity and change to the Sonic Jump activity directory
```
cd activities\SonicJump.activity
```
- To run
```
sugar-activity .
```

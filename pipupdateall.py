"""
It checks for the outdated packages and updates them.
Run the command prompt as an administator to give the script priveleges to write to the C drive
then type  
python pipupdateall.py 
to execute the script and it will go on to update all the packages
"""
import subprocess

s = subprocess.check_output("pip list --outdated",shell=True)

s = s.decode("utf-8","ignore")

s = s.split()
s.insert(0,"[wheel]")

package_list = []
c = 0
for i in s:
	try:
		if(i == "[wheel]"):
			package_list.append(s[c + 1])
	except:
		continue
	c += 1

if(not package_list):
	print("All packages are up to date")
else:
	print("Outdated Packages are:")
	for i in package_list:
		print(i)
		
	for i in package_list:
		try:
			update_command = "pip install " + str(i) + " --upgrade"
			subprocess.run(update_command, shell=True)
		except:
			continue

		
	

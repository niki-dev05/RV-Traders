import time
import datetime
import os, errno, sys
import glob
import re
from bs4 import BeautifulSoup
import re
dir_path = os.path.dirname(os.path.realpath(__file__))

def processTemplate(_pagefile):
	tmplpagefile = open(_pagefile, "r").read()
	tokens = re.findall('{_[\w\.]+.html}', tmplpagefile)
	modules = []
	for token in tokens:
		token = token.replace("{", "").replace("}", "")
		modules.append(token)
		newWebPageFileName = pagefile.replace("templates", "").replace("pages", "").replace("_page_", "")
		with open(newWebPageFileName, 'w', encoding='utf-8') as outfile:
			newWebPageContent = tmplpagefile
			for moduleFileName in modules:
				with open(f"{dir_path}\\templates\\modules\\" + moduleFileName, encoding='utf-8') as moduleFile:
					newWebPageContent = newWebPageContent.replace("{" + moduleFileName + "}", moduleFile.read())
			newWebPageContent = newWebPageContent.replace("~CONTACT-FORM~", contact_form)
			newWebPageContent = re.sub(r"<!--(.|\s|\n)*?-->", "", newWebPageContent)
			soup = BeautifulSoup(newWebPageContent, 'html.parser')
			outfile.write(soup.prettify())

contact_form = open(f"{dir_path}\\templates\\modules\\_mod_contact_form.html", "r").read()

for pagefile in glob.glob(f'{dir_path}\\templates\\pages\\_page_*.html'):
    print(pagefile)
    processTemplate(pagefile)

print("All done...")

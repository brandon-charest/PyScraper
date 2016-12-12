'''
Created on Dec 11, 2016

@author: Brandon
'''
import urllib
import cookielib
import mechanize
from bs4 import BeautifulSoup
from cookielib import CookieJar
from Tix import Form


#Browser
br = mechanize.Browser()

#enable cookies for urllib
cookiejar = cookielib.LWPCookieJar()
br.set_cookiejar(cookiejar)

# Browser Options
br.set_handle_robots(False)
br.set_handle_redirect( True ) 

br.set_handle_referer( True ) 
br.set_handle_equiv( True ) 

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.open("http://testing-ground.scraping.pro/login")

for f in br.forms():
    print f

#User Credentials
#br.form.set_all_readonly(False)
br.form['usr'] = 'admin'
br.submit()

br.select_form(nr=0)
br.form['pwd'] = '12345'
br.submit()

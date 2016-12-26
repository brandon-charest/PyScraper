'''
Created on Dec 11, 2016

@author: Brandon
'''
import mechanize
import cookielib
from bs4 import BeautifulSoup

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
br.open('target-site')


# Select the second (index one) form (the first form is a search query box)
br.select_form(nr=0)

# User credentials
br.form['txtUser'] = 'username'
br.form['txtPass'] = 'password'

# Login
br.submit();

repsonse = br.open("target-site page after login");

soup = BeautifulSoup(repsonse, 'html.parser');
    
for span in soup.find_all('span', text=lambda x: x and x.startswith('string value')):
    for text in span.find_all('img'):
        reportName = text.contents[0];
        reportID = span.get('id');
        print reportID.strip('text'), ' - ', reportName;
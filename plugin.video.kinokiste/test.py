import urllib,urllib2,re

#KinoKiste - by Christof Torres 2011 - 2013.


user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
                        
url = 'http://www.kkiste.to/aktuelle-kinofilme/?page=1'

main_url = url
req = urllib2.Request(url)
req.add_header('User-Agent', user_agent)
response = urllib2.urlopen(req)
link = response.read()
response.close()
pages = re.compile('<li><a href="\?page=.+?">(.+?)</a></li>').findall(link)
match = re.compile('<a href="(.+?)" title="(.+?)" class="title">.+?</a>').findall(link)
for url,name in match:
                try:
                        url = 'http://www.kkiste.to'+url
                        req3 = urllib2.Request(url)
                        req3.add_header('User-Agent', user_agent)
                        response3 = urllib2.urlopen(req3)
                        link3 = response3.read()
                        response3.close()
                        name = name[6:len(name)]
                        name = name[0:name.find('Stream ansehen')-1]
                        thumbnail = re.compile('<img src="(.+?)" width="145" height="215" alt=".+?" />').findall(link3)[0]
                        director = re.compile('<p><span>von:</span> <a href=".+?">(.+?)</a>').findall(link3)[0]
                        rating = re.compile('IMDB Rating:</span> <a href=".+?" target="_blank" title=".+?">(.+?)</a>').findall(link3)[0]
                        year = re.compile('Jahr:</span> (.+?)</p>').findall(link3)[0] 
                        plot = re.compile('<p id="kk-plot">(.+?)<span class="kk-ds">').findall(link3)[0].replace("<br>","\n").replace("<br />","\n").replace("&nbsp;"," ")
                        actors = re.compile('<li><a href="/darsteller/.+?/" title=".+?">(.+?)</a></li>').findall(link3)
                        cast = ''
                        for actor in actors:
                                cast = cast+actor+'\n'
                        if (main_url[20:len(main_url)] == '/serien/'):
                                addDir(name,url,8,thumbnail)
                        else:
                                print name
                except:
                        print 'Unexpected error: '+url
last_page = pages[len(pages)-1]
current_page = main_url[46:len(main_url)]
print current_page
print last_page
                        

# -*- coding: utf-8 -*-
"""
Created on Fri May 19 13:49:21 2017

@author: C-Ashish.Singh
"""

import urllib.request, json 
from xml.dom import minidom
import urllib

with urllib.request.urlopen("https://api.crowdtangle.com/posts?token=h8sV43MKo76pemNbzXOEyV2LAzqQODjG4sxDH7JD&sortBy=overperforming&types=link&timeframe=2%20HOUR&listIds=256400") as url:
    data1 = json.loads(url.read().decode())
   


with urllib.request.urlopen("https://til-blogs.s3.amazonaws.com/feeds/crowdtangle/posts-2%20HOUR-overperforming-256400.xml") as url:
    
    data2 = minidom.parseString(url.read().decode())
    print(data2)
    


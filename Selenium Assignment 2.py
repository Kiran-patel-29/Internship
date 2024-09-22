#!/usr/bin/env python
# coding: utf-8

# # Q1: In this question you have to scrape data using the filters available on the webpage You have to use the location and salary filter.

# In[20]:


get_ipython().system('pip install selenium')


# In[21]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[22]:


driver = webdriver.Chrome()


# In[23]:


driver.get('https://www.naukri.com')


# In[24]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys("Data Scientist")


# In[25]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys("Delhi/NCR")


# In[26]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[27]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[28]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title "]')
for i in title_tags:
    title=i.text
    job_title.append(title)
    
    
location_tags=driver.find_elements(By.XPATH,'//span[@class="locWdth"]')
for i in location_tags:
    location=i.text
    job_location.append(location)
    
    
company_tags=driver.find_elements(By.XPATH,'//div[@class=" row2"]/span/a[1]')
for i in company_tags:
    company=i.text
    company_name.append(company)
    
    
experience_tags=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
for i in experience_tags:
    exp=i.text
    experience_required.append(exp)    
    


# In[30]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


##class="features-search_input"                   class="features-search_input features-search_input-submit"      
#class="subheader" heading


# 
# # Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data

# In[2]:


get_ipython().system('pip install selenium')


# In[3]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[4]:


driver = webdriver.Chrome()


# In[5]:


driver.get('https://www.shine.com')


# In[7]:


job_title=driver.find_element(By.CLASS_NAME,"form-control ")
job_title.send_keys("Data Analyst")


# In[8]:


location=driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys("Bangalore")


# In[9]:


search=driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search.click()


# In[10]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# title_tags=driver.find_elements(By.XPATH,'//a[@class="jobCard_pReplaceH2__xWmHg"]')
# for i in title_tags:
#     title=i.text
#     job_title.append(title)
#     
# location_tags=driver.find_elements(By.XPATH,'//span[@class="locWdth"]')
# for i in location_tags:
#     location=i.text
#     job_location.append(location)
#     
#     
# company_tags=driver.find_elements(By.XPATH,'//div[@class=" row2"]/span/a[1]')
# for i in company_tags:
#     company=i.text
#     company_name.append(company)
#     
#     
# experience_tags=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
# for i in experience_tags:
#     exp=i.text
#     experience_required.append(exp)    
#     
#     

# In[ ]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title "]')
for i in title_tags:
    title=i.text
    job_title.append(title)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Q3: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link

# In[11]:


get_ipython().system('pip install selenium')


# In[12]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[18]:


driver = webdriver.Chrome()


# In[19]:


driver.get('https://www.flipkart.com')


# In[20]:


product=driver.find_element(By.CLASS_NAME,"Pke_EE")
product.send_keys("apple-iphone-11-black-64-gb")


# In[21]:


search=driver.find_element(By.CLASS_NAME,"_2iLD__")
search.click()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Q4: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field.

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[3]:


driver = webdriver.Chrome()


# In[4]:


driver.get('https://www.flipkart.com')


# In[5]:


product=driver.find_element(By.CLASS_NAME,"Pke_EE")
product.send_keys("sneakers")


# In[6]:


search=driver.find_element(By.CLASS_NAME,"_2iLD__")
search.click()


# In[7]:


# price=   class="Nx9bqj"    brand =  class="syl9yP"   description = class="WKTcLC"


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Q5: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7” as shown in the below image:

# In[9]:


get_ipython().system('pip install selenium')


# In[10]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[11]:


driver = webdriver.Chrome()


# In[12]:


driver.get('https://www.amazon.in')


# In[18]:


product=driver.find_element(By.CLASS_NAME,"nav-fill")
product.send_keys("Laptop")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Q6: Write a python program to scrape data for Top 1000 Quotes of All Time.Q6: Write a python program to scrape data for Top 1000 Quotes of All Time.

# In[19]:


get_ipython().system('pip install selenium')


# In[20]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[21]:


driver = webdriver.Chrome()


# In[22]:


driver.get('https://www.azquotes.com')


# In[23]:


quaut=driver.find_element(By.CLASS_NAME,"front")
quaut.send_keys("Quote")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Q7: Write a python program to display list of respected former Prime Ministers of India

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[3]:


driver = webdriver.Chrome()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Q8: Write a python program to display list of 50 Most expensive cars in the world

# In[12]:


get_ipython().system('pip install selenium')


# In[14]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[15]:


driver = webdriver.Chrome()


# In[16]:


driver.get('https://www.motor1.com')


# In[19]:


page=driver.find_element(By.CLASS_NAME,"adgrid-ad-container")
page.send_keys("50 most expensive cars")


# In[ ]:





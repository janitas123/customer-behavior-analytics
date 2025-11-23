#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
df=pd.read_csv(r"C:\Users\fahaam\Downloads\customer_shopping_behavior.csv")


# In[7]:


df.head()


# In[8]:


df.info()


# In[9]:


df.describe(include='all')


# In[10]:


df.isnull().sum()


# In[11]:


df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))


# In[12]:


df.isnull().sum()


# In[13]:


df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[14]:


df.columns


# In[15]:


labels=['young adult','adult','middle-aged','teenager']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)


# In[16]:


df[['age','age_group']].head(10)


# In[17]:


frequency_mapping={
    
'Fortnightly':14,
'Weekly':7,
'Annually':365,
'Quarterly':90,
'Bi-Weekly':14,
'Every 3 Months':90,
'Monthly':30
}
    
df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)
    


# In[18]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[19]:


(df['discount_applied']==df['promo_code_used']).all()


# In[20]:


df=df.drop('promo_code_used',axis=1)


# In[21]:


df.columns


# In[22]:


get_ipython().system('pip install pyodbc sqlalchemy')


# In[50]:





# In[49]:


import pyodbc
print(pyodbc.drivers())


# In[56]:





# In[ ]:


import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# SQL Server parameters
server = "LAPTOP-6M62LVG0"  # your machine name
database = "customer_shopping_behavior"
driver = "ODBC Driver 17 for SQL Server"

# URL encode the driver
params = quote_plus(f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes")

# Create engine
engine = create_engine("mssql+pyodbc://@your_server_name/customer_shopping_behavior?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes")

# Load CSV
df = pd.read_csv(r"C:\Users\fahaam\Downloads\customer_shopping_behavior.csv")

# Push to SQL Server
df.to_sql('customer_shopping_behavior', con=engine, if_exists='replace', index=False)

print("CSV successfully loaded into SQL Server!")


# In[4]:


import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# SQL Server parameters
server = "LAPTOP-6M62LVG0"  # your machine name
database = "customer_shopping_behavior"
driver = "ODBC Driver 17 for SQL Server"

# URL encode the driver
params = quote_plus(f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes")

# Create engine
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# Load CSV
df = pd.read_csv(r"C:\Users\fahaam\Downloads\customer_shopping_behavior.csv")

# Push to SQL Server
df.to_sql('customer_shopping_behavior', con=engine, if_exists='replace', index=False)

print("CSV successfully loaded into SQL Server!")


# In[5]:





# In[23]:


from sqlalchemy import create_engine
from urllib.parse import quote_plus

# -----------------------------
# SQL Server connection setup
# -----------------------------
server = "LAPTOP-6M62LVG0"  # your machine name
database = "customer_shopping_behavior"
driver = "ODBC Driver 17 for SQL Server"

# URL encode driver
params = quote_plus(f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes")

# Create SQLAlchemy engine
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# -----------------------------
# PUSH CLEANED DATA TO SQL
# -----------------------------
df.to_sql(
    'customer_shopping_behavior',  # Table name in SQL
    con=engine,
    if_exists='replace',           # Replace old table if exists
    index=False
)

print("Cleaned DataFrame successfully loaded into SQL Server!")


# In[ ]:





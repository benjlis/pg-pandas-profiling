"""
"""
from sqlalchemy import create_engine
from os import getenv
import pandas as pd
from pandas_profiling import ProfileReport

# read query file
# qry = 'select * from etc.doc_cnts order by corpora_cnt desc, total_docs desc'
qry = """
select id, setname, title, creator, description, rights, uri, sid, has_doc,
       jpg_url, pdf_url, size, pg_cnt, word_cnt, char_cnt
from foiarchive.un_archives_docs
"""
print(qry)

# db configuration and connection
user = getenv('DBUSER')
pswd = getenv('DBPSWD')
host = getenv('DBHOST')
db = getenv('DBDB')
connect_str = 'postgresql+psycopg2://' + user + ':' + pswd + '@' + host + '/' \
              + db
# print(connect_str)
engine = create_engine(connect_str)
df = pd.read_sql_query(qry, engine)
print('rows:' + str(len(df.index)))
print(df.head())
profile = ProfileReport(df, title="UN Archive Docs Report", explorative=True)
profile.to_file("un_docs_explorative.html")
# profile = ProfileReport(df, title="UN Archive Docs Report", minimal=True)
# profile.to_file("un_docs.html")
# df.to_excel('ciameta.xlsx', engine='xlsxwriter')

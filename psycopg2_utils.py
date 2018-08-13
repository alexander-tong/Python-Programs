'''
Developed and Tested with Python 2.7.14 

@author: Alexander Tong
'''

def db_connect(host,dbname,user,password):
    '''
    Description: Query and Return
    
    Args:
        host (str): e.g., localhost
        dbname (str): e.g., testdb
        user (str): e.g., postgres
        password (str): e.g., password
            
    Returns: 
        db connection
    '''     
    import psycopg2
    
    try:
        credentials = "host=" + host + ' ' \
                      + "dbname=" + dbname + ' '\
                      + "user=" + user + ' '\
                      + "password=" + password
        
        connection = psycopg2.connect(credentials)
        
        # if 0 connection successful; if >0 not successful  
        if connection.closed == 0:
            
            print ' ' + '\n' + \
                  '... connection successful' 
                  
            return connection
    
    except psycopg2.OperationalError as OE:
        
        print OE
        print '... connection unsuccessful'
        
    
def db_close(connection):
    '''
    Description: close/sever db connection
    
    Args:
        connection (function): 
  
    Returns: 
        closed db connection 
    '''
    print '... connection severed'
    return connection.close()


def query(connection, statement, fetch):
    '''
    Description: Query and Return
    
    Args:
        connection (function): use def db_connect() as input e.g., connection = db_connect(*args)
        statement (str): SQL statement 
        fetch (str or int): input: 'one' ...retrieve first row
                            input: 'all' ...retrieve all rows
                            input: int   ...retrieve int rows
    Returns: 
        SQL Query    
    ''' 
    import psycopg2
    
    try:
        if connection.closed == 0:
            cursor = connection.cursor()
            cursor.execute(statement)   
             
            if fetch == 'one':  
                return cursor.fetchone()
            
            elif type(fetch) == int:
                return  cursor.fetchmany(fetch)
            
            elif fetch == 'all':
                return cursor.fetchall()
            
        else:
            
            return 'closed: {0} {1}'.format(str(connection.closed), '...db is not connected')
        
    except psycopg2.Error as E:
         
        return E
    
#    finally:
#        
#        db_close(connection)
        
    
def create_table(connection, statement):
    '''
    Description: create a table
    
    Args:
        connection (function):
        statement (str):
            
    Returns: 
        if table does not exist, return True
        else table exists, return error 
    '''
    import psycopg2
    try:
        
        cursor = connection.cursor()  
        cursor.execute(statement)
        
#        #below does not work 
#        table = statement.split('CREATE TABLE')[1]
#      
#        #cannot do a check on this using psycopg2 ... 
#        cursor.execute("CREATE TABLE IF NOT EXISTS" + table)
        
        return True 
    
    except psycopg2.Error as E:
         
        return E   


def commit_table(connection, create_table, statement):
    '''
    Description: commit a table
    
    $ table doesn't exist, create
    $ if doesn't exist and has NO rows, use 'CREATE TABLE IF NOT EXISTS' 
    $ check if table exists by asking for first row... 
    '''
    import psycopg2
    try:
        if create_table == True:

            connection.commit()
            
            return 'table created'
        
        else:
            print 'CREATE TABLE STATMENT does not exist; table may already exist, or error in statement' 
            
    except psycopg2.Error as E:
         
        return E  
    
    finally:
        
        db_close(connection)
       
        
def table_exists(connection, table):
    '''
    Description: This function only works if the table is not empty. 
    
    Args:
        connection (function):
        table (str): input schema.tablename 
    
    Returns:
        Return boolean True if table is not empty 
    '''
    import psycopg2
        
    try:
        if table:
            cursor = connection.cursor() 
            cursor.execute("SELECT EXISTS (SELECT 1 FROM " + table +");")
            
            return cursor.fetchone() is not None
        
        elif table:
            cursor = connection.cursor() 
            cursor.execute("SELECT COUNT(*) FROM " + table + " LIMIT 1" + ");")
            
            return cursor.fetchone() is None
        
    except psycopg2.Error as E:
         
        return E    
    
#    finally:
#        
#        db_close(connection)
        
   
def commit_drop(connection, table):
    '''
    '''
    import psycopg2
    
    try:
        cursor = connection.cursor() 
        cursor.execute('DROP TABLE ' + '"' + table + '"' + ';')   
        connection.commit()
        
    except psycopg2.Error as E:
         
        return E  

def commit_insert(connection, statement):
    '''
    Description: drop specified table
    '''
    import psycopg2
    
    try:
        cursor = connection.cursor() 
        cursor.execute(statement)
        connection.commit() 
        
    except psycopg2.Error as E:
         
        return E  


def commit_delete(connection, statement):
    '''
    Description: delete specified row(s) from table
    '''
    import psycopg2
    
    try:
        cursor = connection.cursor() 
        cursor.execute(statement)
        connection.commit() 
        
    except psycopg2.Error as E:
         
        return E 
    


def copy_to_db(connection, filename):
    '''
    $ to be implemented:
        .txt
        binary 
        
    $ need to create one that accepts sas files 
    '''
    #use the copy_from instead
    if 'csv': 
        with open(filename, 'r') as f:
            # Notice that we don't need the `csv` module.
            next(f)  # Skip the header row.
            cursor = connection.cursor() 
            cursor.copy_from(f, 'users', sep=',')
            
        connection.commit()
        
    elif 'text':
        pass 
    
    elif 'binary':
        pass

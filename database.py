try:        
    import sys
    sys.path.insert(1, '/Applications/MAMP/htdocs/Time-Boxing-AI/Database/')           
except:
    print("Issue Getting Database File")
else:    
    from db import Db
    print("Imported File Successfully")
    
conn = Db().connect()
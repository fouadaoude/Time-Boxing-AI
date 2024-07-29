try:        
    import sys
    sys.path.insert(1, '/Applications/XAMPP/xamppfiles/htdocs/Database/Time-Boxing-AI')           
    from db import Db
except:
    print("Issue Getting Database File")
else:        
    print("Imported Database File Successfully")
    conn = Db()
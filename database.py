try:
    import sys
    sys.path.append(1, '/Applications/MAMP/htdocs/Time-Boxing-AI/Database')       
     
except:
    print("Issue Getting Database File")
else:
    from database import Database
    print("Imported File Successfully")
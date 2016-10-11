import pg
from sys import exit

#Accesses existing phonebook dtabase and creates table 'phonebook'
def phoneApp(db_name):
    try:
        db = pg.DB(dbname=db_name)
        # db.debug = True
        # print '\nDatabase opened...'

    except:
        print 'No phonebook database exists!'
        exit(0)

    if 'public.phonebook' in db.get_tables():
        # print 'Phonebook accessed!'
        phonebook(db)
    else:
        try:
            db.query("""
                CREATE TABLE phonebook (
                id serial PRIMARY KEY,
                name varchar NOT NULL UNIQUE,
                phone varchar,
                email varchar UNIQUE
                )"""
            )
            print 'Phonebook created!'
            phonebook(db)
        except:
            print 'Phonebook table could not be created!'
            phonebook(db)

#Prompts user with option list and calls function based on choice
def phonebook(db):
    print '\nElectronic Phone Book'
    print '====================='
    print '1. Look up an entry'
    print '2. Set an entry'
    print '3. Delete an entry'
    print '4. List all entries'
    print '5. Clear ALL entries'
    print '6. Quit'

    choice = choose()

    if choice == 1:
        lookUpEntry(db)
    elif choice == 2:
        setEntry(db)
    elif choice == 3:
        deleteEntry(db)
    elif choice == 4:
        listEntries(db)
    elif choice == 5:
        clearEntries(db)
    else:
        quitPhonebook()

#Enforces valid choices for app options 1-5
def choose():
    choice = int(raw_input('Please choose an option (1-6): \n'))
    if choice not in range(1,7):
        print "Only enter 1-6!"
        choose()
    else:
        return choice

#Ask to go back to 1-5 option menu if current option returns error
def goBack():
    back = raw_input('Go back? (y/n) ')
    if back == 'y' or back == 'n':
        if back == 'n':
            return False
        else:
            return True
    else:
        print "Only enter 'y' or 'n'!"
        goBack()

#Functions for phonebook methods
def lookUpEntry(db):
    n = raw_input('Name: ')
    query = db.query("select * from phonebook where name='" + n + "'")
    if len(query.namedresult()) >= 1:
        print ''
        print query
    else:
        print 'That person is not in the phonebook!'
    phonebook(db)

def setEntry(db):
    n = raw_input('Name: ')
    print 'Enter contact information: '
    print '(if none, press enter)'
    p = raw_input('phone: ')
    e = raw_input('email: ')
    try:
        db.insert('phonebook',name=n,phone=p,email=e)
        print 'Entry stored for {0}: phone: {1}  email: {2}'.format(n,p,e)
    except:
        print 'Invalid entry - try again'
    phonebook(db)

def deleteEntry(db):
    name = raw_input('Name: ')
    try:
        result = db.query("""delete from phonebook where name='"""+name+"'")
        print 'Deleted entry for {0}\n'.format(name)
        phonebook(db)
    except:
        print 'That person is not in the phonebook!'
        phonebook(db)

def listEntries(db):
    query = db.query('select * from phonebook')
    if len(query.namedresult()) >= 1:
        print ''
        print query
        phonebook(db)
    else:
        print 'No entries yet!\n'
        phonebook(db)

def clearEntries(db):
    db.query("""drop table phonebook""")
    print 'Entries cleared!'
    phoneApp('phonebook2')

def quitPhonebook():
    print 'Entries Saved! - GOODBYE\n'
    exit(0)


phoneApp('phonebook2')

import sqlite3
import os

class Database:
    def __init__(self, db_path = 'mydata.db'):
        self.conn = sqlite3.connect(db_path) #connect to db
        self.cursor = self.conn.cursor() #cursor object to exeute SQL commands
        #self.db_file = 'mydatabase.db'
        self.initialize_database()
        
    def initialize_database(self):
        """Initialize the database with required tables"""
        '''try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()'''
                
                # Create users table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            mobile TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
                
                # Create skintypes table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS skintypes (
            skintype_id INTEGER PRIMARY KEY AUTOINCREMENT,
            skintype TEXT NOT NULL,
            ingredient TEXT NOT NULL
        )
        ''')
                
                # Create concerns table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS concerns (
            concern_id INTEGER PRIMARY KEY AUTOINCREMENT,
            concern TEXT NOT NULL,
            ingredient TEXT NOT NULL
        )
        ''')

        self.conn.commit()
                
        '''except sqlite3.Error as e:
            print(f"Database initialization error: {e}") '''
            
    '''def add_item(self, ingredient, concern) :
        self.cursor.execute("INSERT INTO concerns (ingredient, concern) VALUES(?, ?)", (ingredient, concern))
        self.conn.commit()'''
            
            
    def add_user(self, username, email, password, mobile):
        """Add a new user to the database"""
        try:
            #with sqlite3.connect(self.db_file) as conn:
            #cursor = self.conn.cursor()
            self.cursor.execute('''
                INSERT INTO users (username, email, password, mobile)
                VALUES (?, ?, ?, ?)
                ''', (username, email, password, mobile))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # Username or email already exists
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")
            return False
        
    def authenticate_user(self, username, password):
        """Authenticate a user's login credentials"""
        try:
            #with sqlite3.connect(self.db_file) as conn:
            #cursor = self.conn.cursor()
            self.cursor.execute('''
                SELECT user_id FROM users 
                WHERE username = ? AND password = ?
                ''', (username, password))
            result = self.cursor.fetchone()
            return result is not None
        except sqlite3.Error as e:
            print(f"Authentication error: {e}")
            return False
        
    def update_password(self, email, new_password):
        """Update a user's password"""
        try:
            #with sqlite3.connect(self.db_file) as conn:
                #cursor = conn.cursor()'''
            self.cursor.execute('''
                UPDATE users 
                SET password = ?
                WHERE email = ?
                ''', (new_password, email))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Password update error: {e}")
            return False
        
    def check_email_exists(self, email):
        """Check if email exists in database"""
        try:
            #with sqlite3.connect(self.db_file) as conn:
                #cursor = conn.cursor()'''
            self.cursor.execute('SELECT email FROM users WHERE email = ?', (email,))
            return self.cursor.fetchone() is not None
        except sqlite3.Error as e:
            print(f"Error checking email: {e}")
            return False
        
        '''def add_skintype_ingredient(self, skintype, ingredient):
        """Add a skintype-ingredient relationship"""
        try:
            #with sqlite3.connect(self.db_file) as conn:
                #cursor = conn.cursor()'''
            #self.cursor.execute('''
                #INSERT INTO skintypes (skintype, ingredient)
                #VALUES (?, ?)
                #''', (skintype, ingredient))
            #self.conn.commit()
            #return True
        #except sqlite3.Error as e:
            #print(f"Error adding skintype ingredient: {e}")
            #return False
        
    #def add_concern_ingredient(self, concern, ingredient):
        #"""Add a concern-ingredient relationship"""
        #'''try:
           # with sqlite3.connect(self.db_file) as conn:
                #cursor = conn.cursor()'''
        #self.cursor.execute('''
            #INSERT INTO concerns (concern, ingredient)
            #VALUES (?, ?)
            #''', (concern, ingredient))
        #self.conn.commit()
        #return True
        #'''except sqlite3.Error as e:
            #print(f"Error adding concern ingredient: {e}")
            #return False'''
        
    def get_ingredients_by_type_and_concern(self, skintype, concern):
        """Get ingredients that match both skin type and concern"""
        '''try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()'''
        self.cursor.execute('''
            SELECT concerns.ingredient 
            FROM concerns 
            JOIN skintypes ON concerns.ingredient = skintypes.ingredient 
            WHERE concern = ? AND skintype = ?
            ''', (concern, skintype))
        return [row[0] for row in self.cursor.fetchall()]
        '''except sqlite3.Error as e:
            print(f"Error getting ingredients: {e}")
            return []'''
        
# Create global database instance
db = Database()
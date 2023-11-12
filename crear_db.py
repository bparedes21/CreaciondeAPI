

def crear_db_sqlite():
    import sqlite3
    name_db="Racing_BB.db"
    conn=sqlite3.connect(name_db)
    cursor = conn.cursor()

    # Comando SQL para crear una tabla llamada 'races' 
    cursor.execute('''DROP TABLE IF EXISTS races;''')

    create_table_query = '''
    CREATE TABLE races (
        raceId INTEGER NOT NULL,
        year INTEGER,
        round INTEGER,
        circuitId INTEGER  NOT NULL,
        name TEXT,
        date TEXT,
        time TEXT,
        url TEXT
    );
    '''
    # Ejecutar el comando SQL para crear la tabla
    cursor.execute(create_table_query)
    conn.commit()


    # Comando SQL para crear una tabla llamada 'results' 
    cursor.execute('''DROP TABLE IF EXISTS results;''')
    create_table_query = '''
    CREATE TABLE results (
        resultId INTEGER NOT NULL,
        raceId INTEGER NOT NULL,
        driverId INTEGER NOT NULL,
        constructorId INTEGER NOT NULL,
        number INTEGER,
        grid REAL,
        position INTEGER,
        positionText REAL,
        positionOrder	INTEGER,
        points	REAL,
        laps INTEGER,
        time TEXT,
        milliseconds TEXT,
        fastestLap INTEGER,
        rank INTEGER,
        fastestLapTime TEXT,
        fastestLapSpeed REAL,
        statusId INTEGER
        
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()

    # Comando SQL para crear una tabla llamada 'drivers' 
    cursor.execute('''DROP TABLE IF EXISTS drivers;''')

    create_table_query = '''
    CREATE TABLE drivers (
        driverId INTEGER NOT NULL,
        driverRef TEXT,
        number REAL,
        code TEXT,
        dob TEXT,
        nationality TEXT,
        url TEXT,
        forename TEXT,	
        surname TEXT
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()

    # Comando SQL para crear una tabla llamada 'circuits' 
    cursor.execute('''DROP TABLE IF EXISTS circuits;''')

    create_table_query = '''
    CREATE TABLE circuits (
        circuitId INTEGER NOT NULL,
        circuitRef TEXT,
        name REAL,
        location TEXT,
        country TEXT,
        lat TEXT,
        lng TEXT,
        alt INTEGER,	
        url TEXT
    );
    '''

    cursor.execute(create_table_query)

    conn.commit()

    # Comando SQL para crear una tabla llamada 'constructors' 
    cursor.execute('''DROP TABLE IF EXISTS constructors;''')

    create_table_query = '''
    CREATE TABLE constructors (
        constructorId INTEGER NOT NULL,
        constructorRef TEXT,
        name REAL,
        location TEXT,
        country TEXT,
        lat TEXT,
        lng TEXT,
        alt INTEGER,	
        url TEXT
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()

    return conn


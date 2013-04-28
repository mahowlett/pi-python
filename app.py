from bottle import default_app,route,template
import MySQLdb as mdb
import config

con = None

@route('/hello')
def hello():
	return "Hello World!"

@route('/hello/<name>')
def greet(name):
	return template('Hello {{name}} how you doin?',name=name)

@route('/')
def index():
	return "Smee!!!"

@route('/mysqlver')
def mysqlver():
        try:

            con=mdb.connect('localhost', 'root',config.dbPassword, 'test');

            cur=con.cursor();
            cur.execute("SELECT VERSION()");
            data = cur.fetchone();

            output = "Database version is %s " % data;
        except mdb.Error, e:
            output =  "Error %d %s" % (e.args[0],e.args[1]);

        finally:
            if con:
                con.close()
        return output;

@route('/mysqlselect')
def mysqlselecttable():
        try:
                output = "Results: </br>"
                con=mdb.connect('localhost','root',config.dbPassword,'test')
                cur=con.cursor()
                cur.execute("Select * from Writers")
                rows=cur.fetchall()
                for row in rows:
                        output = output + row[1] + "</br>"
        except mdb.Error, e:
                output = "Error %d %s" % (e,args[0],e.args[1]);
        finally:
                if con:
                        con.close()
        return output;

@route('/mysqlcreate') 
def mysqlcreatetable():
        try:
                con=mdb.connect('localhost', 'root', config.dbPassword, 'test')
                cur=con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS \
                        Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(35))")
                cur.execute("INSERT INTO Writers(Name) VALUES('William Shakespeare')")
                cur.execute("INSERT INTO Writers(Name) VALUES('John Keats')")
                cur.execute("INSERT INTO Writers(Name) VALUES('W.B.Yates')")
                cur.execute("INSERT INTO Writers(Name) VALUES('James Herbert')")
                cur.execute("INSERT INTO Writers(Name) VALUES('Stephen King')")
                con.commit()
                output = "Table created and data inserted";
        except mdb.Error, e:
                output =  "Error %d %s" % (e.args[0],e.args[1]);

        finally:
                if con:
                        con.close()
        return output;

application = default_app()


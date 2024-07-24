from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '42170007'
app.config['MYSQL_DB'] = 'Enseignants_ESP'
mysql = MySQL(app)


#login
@app.route('/login', methods = ['POST'])
def login():

    if request.method == 'POST':
        # Get the username and password from the form
        mail = request.form ['mail']
        password = request.form['password']

        

        # If the user exists, log them in
        if mail =='G5@esp.mr' and password == '0000':
            return  redirect (url_for('accueil'))
        # Otherwise, display an error message
        else:
            return  render_template('login.html')
        #  error = "Invalid username or password"   
        #return render_template('registre.html',error=error)

@app.route('/') 
def login_te():
    return render_template('login.html')

#menu
@app.route('/accueil')
def accueil():
    return render_template('menu.html')


    
@app.route('/listeem')
def Indexem():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM em")
    dataem = cur.fetchall()
    cur.close()
    return render_template('liste_emp_em.html', empsem=dataem )

@app.route('/homeem')
def homeem():
    return render_template('em.html' )

@app.route('/insertem', methods = ['POST'])
def insertem():
    if request.method == 'POST':
        code = request.form['code_EM']
        nom = request.form['nom_EM']
        coeff = request.form['coefficient']
        credit= request.form['credit']
        cm = request.form['CM']
        td = request.form['TD']
        tp = request.form['TP']
        pr = request.form['PR']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO em (code_EM,nom_EM, coefficient,credit,CM,TD,TP,PR) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)", (code,nom, coeff, credit,cm,td,tp,pr) )
        mysql.connection.commit()
        return redirect(url_for('Indexem'))

@app.route('/delete/<code_EM>', methods = ['GET'])
def deleteem(code_EM):

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM em WHERE Code_EM=%s",(code_EM,))
    mysql.connection.commit()
    return redirect(url_for('Indexem'))

@app.route('/update_rec/<code_EM>', methods=['GET'])
def update_recem(code_EM):
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM em WHERE code_EM=%s",(code_EM,))
    data = cur.fetchone()
    cur.close()
    return render_template ('modifier_em.html', emp=data)
@app.route('/updateem/', methods=['POST'])
def updateem():
    if request.method == 'POST':
        code = request.form['code_EM']
        nom = request.form['nom_EM']
        coeff = request.form['coefficient']
        credit = request.form['credit']
        cm = request.form['CM']
        td = request.form['TD']
        tp = request.form['TP']
        pr = request.form['PR']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE em
            SET code_EM = %s,
                nom_EM = %s,
                coeff_EM = %s,
                credit_EM = %s,
                V_CM = %s
                V_TD = %s
                V_TP = %s
                V_PR = %s
            WHERE code_EM = %s
        """, (code, nom, coeff,credit,cm,td,tp,pr))
        mysql.connection.commit()
        return redirect(url_for('Indexem'))


@app.route('/homeens')
def homeens():
    return render_template('enseignant.html' )



@app.route('/listens')
def Indexens():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM enseignant")
    data = cur.fetchall()
    cur.close()
    return render_template('liste_emp_enseignant.html', emps=data )



@app.route('/insertens', methods = ['POST'])
def insertens():
    if request.method == "POST":

        nom = request.form['nom_E']
        prenom = request.form['prenom_E']
        email = request.form['e_mail_E']
        statut= request.form['statut_E']
        departement = request.form['departement']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO enseignant (nom_E, prenom_E, e_mail_E,statut_E,Departement) VALUES (%s, %s, %s,%s,%s)", (nom, prenom, email,statut,departement) )
        mysql.connection.commit()
        return redirect(url_for('Indexens'))

@app.route('/delete_ens/<num_E>', methods = ['GET'])
def deleteens(num_E):

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM enseignant WHERE num_E=%s",(num_E,))
    mysql.connection.commit()
    return redirect(url_for('Indexens'))

@app.route('/update_ens/<num_E>', methods=['GET'])
def update_ens(num_E):
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM enseignant WHERE num_E=%s", (num_E,) )
    data = cur.fetchone()
    cur.close()
    return render_template ('update_ens.html', emp=data)

@app.route('/updateens/', methods=['GET','POST'])
def updateens():
    if request.method == 'POST':
        num_E = request.form['num_E']
        nom = request.form['nom_E']
        prenom = request.form['prenom_E']
        email = request.form['e_mail_E']
        statut = request.form['statut_E']
        departement = request.form['departement_E']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE enseignant 
            SET num_E = %s, 
            nom_E = %s,
            prenom_E = %s, 
            e_mail_E = %s, 
            statut_E = %s,
            Departement = %s 
            WHERE num_E = %s """, (num_E, nom, prenom, email, statut, departement, num_E))       
        mysql.connection.commit()
        return redirect(url_for('Indexens'))


@app.route('/listes')
def Indexes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM semestre ")
    data = cur.fetchall()
    cur.close()
    return render_template('liste_emp_semestre.html', emps=data)


@app.route('/homes')
def homes():
    return render_template('semestre.html')


@app.route('/insertes', methods=['POST'])
def insertes():
    if request.method == "POST":
        nom = request.form['nom_sem']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO semestre (nom_sem) VALUES (%s)", (nom,))
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<nom_sem>', methods=['GET'])
def deletees(nom_sem):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM semestre WHERE nom_sem=%s", (nom_sem,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/update_rec/<nom_sem>', methods=['GET'])
def update_reces(nom_sem):
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM semestre WHERE nom_sem=%s", (nom_sem,))
    data = cur.fetchone()
    cur.close()
    return render_template('modifier_semestre.html', emp=data)


@app.route('/update/', methods=['POST'])
def updatees():
    if request.method == 'POST':
        nom = request.form['nom_sem']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE semestre
            SET nom_sem = %s,

            WHERE nom_sem = %s
        """, nom)
        mysql.connection.commit()
        return redirect(url_for('Indexes'))
    

#brouillon

#page enseignant
# @app.route('/listens.html')
# def A():
#     return render_template('liste_emp_enseignant.html')

#page element de module
# @app.route('/listeem.html')
# def C():
#     return render_template('liste_emp_em.html')


# #page semester
# @app.route('/listes.html')
# def D():
#     return render_template('liste_emp_semestre.html')

# #page enseignement
# @app.route('/liste.html')
# def E():
#     return render_template('liste_emp.html')

# @app.route('/c')
# def B():
#     return render_template('menu.html')


# @app.route('/home', methods=["GET","POST"])
# def Index():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT  * FROM enseignement")
#     cur2 = mysql.connection.cursor()
#     cur1 = mysql.connection.cursor()
#     cur3 = mysql.connection.cursor()
#     cur4 = mysql.connection.cursor()
#     cur5 = mysql.connection.cursor()
#     cur2.execute("select * from enseignant order by num_E")
#     cur1.execute("SELECT * FROM em ")
#     cur3.execute("SELECT * FROM type ")
#     cur4.execute("SELECT * FROM plage")
#     cur5.execute("SELECT * FROM semestre")
#     semestre= cur5.fetchall()
#     type = cur3.fetchall()
#     plage = cur4.fetchall()
#     em = cur1.fetchall()
#     enseignant= cur2.fetchall()
#     data = cur.fetchall()
#     cur.close()
#     print(type)
#     return render_template('enseignement.html', emps=data, em=em, enseignant=enseignant,type=type,plage=plage ,semestre=semestre)


@app.route('/liste')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM enseignement")
    data = cur.fetchall()
    return render_template('liste_emp.html' ,loq=data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        nom_E = request.form['nom_E']
        # nom_EM = request.form['nom_EM']
        type = request.form['type']
        plage = request.form['plage']
        semestre = request.form['semestre']
        duree = request.form['duree']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO enseignement (id, nom_EM, nom_E,type, plage, semestre, duree) VALUES (%s,%s,%s,%s,%s,%s,%s)", (id,nom_E, nom_E,type,plage,semestre,duree))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<id>', methods = ['GET'])
def delete(id):

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM enseignant WHERE id=%s",(id,))
    mysql.connection.commit()
    return redirect(url_for('index'))

@app.route('/update_rec/<id>', methods=['GET'])
def update_rec(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM enseignement WHERE id=%s", (id,) )
    data = cur.fetchone()
    cur.close()
    return render_template ('modifier.html', emp=data)
@app.route('/update/', methods=['POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        nom_EM = request.form['nom_EM']
        nom_E = request.form['nom_E']
        prenom_E = request.form['prenom_E']
        type = request.form['type']
        plage = request.form['plage']
        semestre = request.form['semestre']
        duree = request.form['duree']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE enseignement
            SET id = %s,
                nom_EM = %s,
                nom_E = %s,
                prenom_E = %s,
                type=%s,
                plage=%s,
                semestre=%s,
                duree=%s,

            WHERE id= %s
        """, (id, nom_EM,prenom_E, nom_E,type,duree,semestre,plage,id))
        mysql.connection.commit()
        return redirect(url_for('Index'))



@app.route('/enseignement')
def Index5():
    cur = mysql.connection.cursor()
    cur1 = mysql.connection.cursor()
    cur.execute("select * from enseignant order by num_E")
    cur1.execute("SELECT * FROM em ")
    em = cur1.fetchall()
    enseignant= cur.fetchall()
    cur.close()
    return render_template('index.html')

#  #login
# @app.route('/register', methods =['GET','POST']) 
# def register():
#    if request.method =="POST":
#        # the usemane, password, and email from the form 
#     username =request.form["username"]
#     password = request.form["password"] 
#     email=request.form["email"]
#       # Connect to the database
#     cursor=mysql.connection.cursor()
#       # Check if the username is already taken
#     cursor.execute ("SELECT * FROM users WHERE username = %s", (username,)) 
#     user = cursor.fetchone ()
# # If the username is not taken, register the user
#     if not user : 
#        cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
#        mysql.connection.commit()
#     return (url_for('accueil'))
# # Otherwise, display an error message
#    else:
#         error = "Username already taken" 
#         redirect (url_for('login'))
#         return render_template('login.html')
 
# @app.route('/register template')
# def register_template():
#    return render_template('login.html')











@app.route('/statype')
def sexe2():
    cur = mysql.connection.cursor()

    cursor1 = mysql.connection.cursor()
    cursor2 = mysql.connection.cursor()
    cursor3 = mysql.connection.cursor()

    cursor2.execute(
        "SELECT type  FROM enseignement  group by type")
    rows2 = cursor2.fetchall()
    labels1 = list()
    i = 0
    for row in rows2:
        labels1.append(row[i])

    cursor3.execute(
        "SELECT COUNT( * )  FROM  enseignement  group by type")
    rows3 = cursor3.fetchall()
    values1 = list()
    i = 0
    for row in rows3:
        values1.append(row[i])

    line_labels = labels1
    line_values = values1
    print(line_values)
    print(line_labels)
    return render_template('graph.html', title="Type ", max=60, labels1=line_labels, values1=line_values)





@app.route('/mar')
def se():
    curs = mysql.connection.cursor()

    cursor11 = mysql.connection.cursor()
    cursor21 = mysql.connection.cursor()
    cursor31 = mysql.connection.cursor()

    cursor21.execute(
        "SELECT semestre  FROM enseignement  group by semestre")
    rows21 = cursor21.fetchall()
    labels11 = list()
    i = 0
    for row in rows21:
        labels11.append(row[i])

    cursor31.execute(
        "SELECT COUNT( * )  FROM  enseignement  group by semestre")
    rows31 = cursor31.fetchall()
    values11 = list()
    i = 0
    for row in rows31:
        values11.append(row[i])

    line_labels1 = labels11
    line_values1 = values11
    print(line_values1)
    print(line_labels1)
    return render_template('bar_chart.html', title="nombre de cours fait durant chaque semestre  ", max=20, labels=line_labels1, values=line_values1)



@app.route('/td')
def TD():
    curs = mysql.connection.cursor()

    cursor11 = mysql.connection.cursor()
    cursor21 = mysql.connection.cursor()
    cursor31 = mysql.connection.cursor()

    cursor21.execute(
        "SELECT `nom_E` FROM `enseignement` group by `nom_E`")
    rows21 = cursor21.fetchall()
    labels11 = list()
    i = 0
    for row in rows21:
        labels11.append(row[i])

    cursor31.execute(
        "SELECT count(nom_E) FROM `enseignement` where type='TD' group by `nom_E`")
    rows31 = cursor31.fetchall()
    values11 = list()
    i = 0
    for row in rows31:
        values11.append(row[i])

    line_labels1 = labels11
    line_values1 = values11
    print(line_values1)
    print(line_labels1)
    return render_template('line_chart2.html', title="Nombre de TD fait par chaque Enseignant   ", max=10, labels=line_labels1, values=line_values1)



@app.route('/cm')
def CM():
    curs = mysql.connection.cursor()

    cursor11 = mysql.connection.cursor()
    cursor21 = mysql.connection.cursor()
    cursor31 = mysql.connection.cursor()

    cursor21.execute(
        "SELECT `nom_E` FROM `enseignement` group by `nom_E`")
    rows21 = cursor21.fetchall()
    labels11 = list()
    i = 0
    for row in rows21:
        labels11.append(row[i])

    cursor31.execute(
        "SELECT count(nom_E) FROM `enseignement` where type='CM' group by `nom_E`")
    rows31 = cursor31.fetchall()
    values11 = list()
    i = 0
    for row in rows31:
        values11.append(row[i])

    line_labels1 = labels11
    line_values1 = values11
    print(line_values1)
    print(line_labels1)
    return render_template('line_chart2.html', title="Nombre de CM fait par chaque Enseignant    ", max=10, labels=line_labels1, values=line_values1)






if __name__ == "__main__":
    app.run(debug=True)

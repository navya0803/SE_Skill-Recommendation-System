import docx2txt
from pyresparser import ResumeParser
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from flask import Flask,render_template,request,redirect,url_for,flash,session
import mysql.connector
import pandas as pd
import nltk
nltk.download('stopwords')
db=mysql.connector.connect(user="root",password="",port='3306',database='resume')
cur=db.cursor()
# from flask_mail import *
app=Flask(__name__)
app.secret_key="CBJcb786874wrf78chdchsdcv"
import requests
import os
import random

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/signup")
def signup():
    return render_template('registration.html')


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        useremail=request.form['useremail']
        session['useremail']=useremail
        userpassword=request.form['userpassword']
        sql="select * from user where useremail='%s' and userpassword='%s'"%(useremail,userpassword)
        cur.execute(sql)
        data=cur.fetchall()
        db.commit()
        if data ==[]:
            msg="user Credentials Are not valid"
            return render_template("login.html",name=msg)
        else:
            return render_template("Upload.html",myname=data[0][1])
    return render_template('login.html')

@app.route('/register',methods=["POST","GET"])
def registration():
    if request.method=='POST':
        username=request.form['username']
        useremail = request.form['useremail']
        userpassword = request.form['userpassword']
        conpassword = request.form['conpassword']
        Age = request.form['Age']
        address = request.form['address']
        contact = request.form['contact']
        if userpassword == conpassword:
            sql="select * from user where useremail='%s' and userpassword='%s'"%(useremail,userpassword)
            cur.execute(sql)
            data=cur.fetchall()
            db.commit()
            print(data)
            if data==[]:
                sql = "insert into user(Username,Useremail,Userpassword,Age,Address,Contact)values(%s,%s,%s,%s,%s,%s)"
                val=(username,useremail,userpassword,Age,address,contact)
                cur.execute(sql,val)
                db.commit()
                flash("Registered successfully","success")
                return render_template("login.html")
            else:
                flash("Details are invalid","warning")
                return render_template("registration.html")
        else:
            flash("Password doesn't match", "warning")
            return render_template("registration.html")
    return render_template('registration.html')

@app.route('/upload',methods=["POST","GET"])
def upload():
    return render_template('upload.html')

@app.route('/load',methods=["POST","GET"])
def load():
    if request.method=="POST":
        
        files1 = request.files['resume']
        files2 = request.files['job_description']

        files1.save(os.path.join('upload', files1.filename))
        resume = docx2txt.process(files1)
        print(resume)

        # Store the job description into a variable
        files2.save(os.path.join('upload', files2.filename))
        jd = docx2txt.process(files2)
        print(jd)

        # Print the job description
        print(jd)

        text = [resume, jd]

        
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(text)

        #Print the similarity scores
        print("\nSimilarity Scores:")
        print(cosine_similarity(count_matrix))

        #get the match percentage
        matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
        matchPercentage1 = round(matchPercentage, 2) # round to two decimal
        # msg = print("Your resume matches about "+ str(matchPercentage)+ "% of the job description.")

        if matchPercentage1>=70:                      
             m1="Your resume matches about "+ str(matchPercentage)+ "% of the job description. You have a nice resume"
        else:
            m1="Your resume matches about "+ str(matchPercentage)+ "% of the job description.You need to work on your resume to improve."
        from pyresparser import ResumeParser
        data = ResumeParser(os.path.join('upload', files1.filename)).get_extracted_data()
        list = data['skills']
        print(list)
        data1 = ResumeParser(os.path.join('upload', files2.filename)).get_extracted_data()
        list1 = data1['skills']

        matches=[]
        for item_a in list1:
            for item_b in list:
                if item_a == item_b:
                     matches.append(item_a)
        print( matches)
        # extract email and name
        email = data['email']
        name = data['name']

        msg2="The matching skills are as "+ " ,".join(matches)
        # get the unmatched skills from the list and list1 
        unmatched_skills = [item for item in list1 if item not in list]
        msg3 = "The unmatched skills are as "+ ",".join(unmatched_skills)

        dir_path = os.getcwd()  # get current working directory
        all_files = os.listdir(os.path.join(dir_path,'static','resumes'))  # get all files in directory

        # select 5 random files
        random_files = random.sample(all_files,5)

        file_names = [os.path.basename(f) for f in random_files]

        return render_template('load.html',m1=m1,msg2=msg2, msg3 = msg3,msg4=name,msg5= email , file_names = random_files)

    return render_template('load.html')
   

















if __name__=="__main__":
    app.run(debug=True,port=8000)
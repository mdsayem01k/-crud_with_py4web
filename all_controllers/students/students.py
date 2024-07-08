from py4web import action, request, abort, redirect, URL,Flash

from py4web.utils.form import Form, FormStyleBulma
from py4web.core import Field
from ..common import db

# List all students
@action('students', method=['GET'])
@action.uses('students/students.html', db)
def students():
    records_list_sql = "SELECT * FROM student;"
    records_list = db.executesql(records_list_sql,as_dict=True)
    return dict(records_list=records_list)
    
    

# Create a new student

@action('students/create_student', method=['GET', 'POST'])
@action.uses('students/student_form.html', db)
def create_student():
    if request.method == "GET":
        id = request.GET.get('id')
        if id==None or id=='':
             edit_data={}
             return dict(edit_data=edit_data)
        query=f"SELECT * FROM student where id={id} limit 1;"
        insert=db.executesql(query,as_dict=True)
        return dict(edit_data=insert)
    
    if request.method == "POST":
        name = request.POST.get('name')
        cls=request.POST.get('class')
        roll=request.POST.get('roll')
        contact=request.POST.get('contact')
        
        query=f"""insert into student (name,class,roll,contact) values ('{name}','{cls}','{roll}','{contact}');"""
        insert=db.executesql(query)
        
        redirect('../students')
    
    return dict()


@action('students/update_student', method=['GET', 'POST'])
@action.uses('students/student_form.html', db)
def create_student():
    if request.method == "GET":
        id = request.GET.get('id')
        query=f"SELECT * FROM student where id={id} limit 1;"
        insert=db.executesql(query,as_dict=True)
        
        return dict(edit_data=insert)
    if request.method == "POST":
        id = request.GET.get('id')
        name = request.POST.get('name')
        cls=request.POST.get('class')
        roll=request.POST.get('roll')
        contact=request.POST.get('contact')
        
        query=f"""update   student set Name='{name}',Class='{cls}',Roll={roll},Contact='{contact}' where id={id};"""
        insert=db.executesql(query)
        
        redirect('../students')
    
    return dict()

@action('students/delete')
def delete():
    student_id = request.params.get('id')
    query=f"""delete from student where id='{student_id}' limit 1;"""
    insert=db.executesql(query)
    redirect(URL('students'))
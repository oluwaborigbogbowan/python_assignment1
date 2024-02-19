from fastapi import FastAPI
from uuid import UUID


app = FastAPI()


students={}

student_data = {'id':int, 'name': str, 'age': int, 'sex': str, 'height':float}

@app.get("/")
def home():
    return {"message": "Hello from my student api"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{id}")
def get_students_by_id(id:int):
    student = students.get(id)
    if not student:
        return {"error": "student not found"}
    return student

@app.post("/students")
def create_student(
    name,age,sex,height
):
    new_student = student_data.copy()
    new_student['id']= int(UUID(int=len(students) + 1))
    new_student['name']= name
    new_student['age']= age
    new_student['sex']= sex
    new_student['height']= height

    students[new_student['id']] = new_student
    return {"message":"book added successfully","data": new_student}

@app.put("/students/{id}")
def update_student(
  id:int,
  name:str,
  age:int,
  sex:str,
  height:float
):
    student = students.get(id)
    if not student:
        return {"error": "student not found"}
    student['name']= name
    student['age']= age
    student['sex']= sex
    student['height']= height

    return {"message":"student updated successfully","data": student}

@app.delete("/students/{id}")
def delete_student(id:int):
    student = students.get(id)
    if not student:
        return {"error": "student not found"}
    del students[id]
    return {"message":"student deleted successfully"}
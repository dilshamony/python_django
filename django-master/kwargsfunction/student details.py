#students details using *args and **kwargs

def student_details(**kwargs):
    print(kwargs)
student_details(id=100,name="vijay",course="python")

def student_details(*args):
    print(args)
student_details(100,"vijay","python")
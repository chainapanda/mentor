#Придумай ситуацию\задачу в которой лучше использовать именно кортежи, а не списки.
# Опиши задачу словами и напиши для нее код.
login = (input())
password = (input())
login_password = tuple(map(int, (login,password).split(',')))
print(login_password)
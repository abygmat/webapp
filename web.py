import  streamlit as st
import functions

def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My todo-app")
st.subheader("This is my todo app")
st.write("<h2>This app is used to increase the <b>productivity</b></h2",unsafe_allow_html=True)

todos=functions.get_todos()

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="enter a todo",placeholder="Add new todo",on_change=add_todo,key="new_todo")


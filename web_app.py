import streamlit as st
import functions as fun

todos = fun.get_todos()


def add_todo():
    new = st.session_state['new_todo'] + '\n'
    todos.append(new)
    fun.update_todos(todos)


st.title("Welcome to the TODO Application")
st.subheader("This is a minimal todo application")
st.write("Let's explore the TODO app")

for index,todo in enumerate(todos):
    check = st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        fun.update_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='', placeholder='Write new TODO to add...', on_change=add_todo, key='new_todo')


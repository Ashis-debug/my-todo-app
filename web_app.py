import streamlit as st
import functions as fun

todos = fun.get_todos()


def add_todo():
    new = st.session_state['new_todo'] + '\n'
    todos.append(new)
    fun.update_todos(todos)


st.title("My Todo App")
st.subheader("This is a minimal todo application")
st.write("This app will increase your productivity.")

for index,todo in enumerate(todos):
    check = st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        fun.update_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='', placeholder='Write new TODO to add...', on_change=add_todo, key='new_todo')


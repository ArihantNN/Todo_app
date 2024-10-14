import streamlit as st
import functions

st.title('My Todo App')
st.subheader('Todos List')

todos = functions.get_todos()

def add_todo():
   todo = st.session_state["new_todo"] + '\n'
   todos.append(todo)
   functions.write_todos(todos)
   print(todo)



for todo in todos:
    st.checkbox(todo)

st.text_input(label ="Enter a new todo", placeholder = 'Add a new todo..',
              on_change=add_todo, key='new_todo',
              label_visibility='hidden')

st.session_state
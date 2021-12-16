import streamlit as st

from plotter import master

st.title('Compare Sorting Algorithms')
st.text('by Marius Nielsen')

algos = st.multiselect(
    label = 'Choose some Algorithms',
    options = ['Bubblesort','Mergesort','Quicksort','Quick3','Mariusort', 'Selectionsort'],
    key = 'algo'
)

listType = st.selectbox(
    label = 'Choose some Algorithms',
    options = ['Sorted','Nearly Sorted','Random','Few Uniques','Reverse Order'],
    key = 'listType'
)

interval = st.selectbox(
    label = 'Choose the maximum size of n',
    options = [100,1000,5000,10000,100000,1000000]

)

a = False

a = st.button(
    label = 'Run Algorithms',
    key = 'run',
)


if a:
    st.pyplot(
    fig = master(interval,listType,algos)
    )


print(algos)
print(listType)
print(a)
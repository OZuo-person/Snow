# Import python packages.
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col



# Write directly to the app.
st.title(f"Customize Your Smoothies! :cup_with_straw: ")
st.write(
  """Choose the fruit you want ub your custome smoothie
  """
)

name_on_order = st.text_input("Name on SMoothie")
#st.write("The name on your moothie", name_on_order)
cnx =st.connection("snowflkae")
session = cnx.session() 
#session = get_active_session()
my_dataframe = session.table("SMOOTHIES.PUBLIC.FRUIT_OPTIONS").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)


ingradients_list = st.multiselect('Choose up to 5 ingredients:', my_dataframe, max_selections = 5)

if ingradients_list:
    #st.write(ingradients_list)
    #st.text(ingradients_list)
    
    ingradients_string = ''
    #name_on_order = ''
    for fruit_chosen in ingradients_list:
        ingradients_string += fruit_chosen + ' '

    #st.write(ingradients_string)  
    #st.write(name_on_order)
  
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
                    values ('""" + ingradients_string + """','""" + name_on_order+ """')"""

   # st.write(my_insert_stmt)
    #st.stop()
    
    #st.write(my_insert_stmt)
    time_to_insert = st.button('Submit Order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()

        st.success('Your Smoothie is ordered!', icon="✅")
    


    

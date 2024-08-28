import streamlit as st

st.set_page_config(page_title='Food')
#assets
a=('1.webp')
b=('2.webp')
c=('3.webp')
d=('4.webp')
e1=('5.webp')
f1=("6.webp")
g1=("7.webp")
h1=("8.webp")
i1=("9.webp")
j1=("10.webp")
a2=("11.webp")
a3=('12.webp')
a5=('13.webp')
a6=('14.webp')
a7=("15.webp")
a8=('16.webp')
a9=("17.webp")
b2=('18.webp')
b3=('19.webp')
b4=('20.webp')
b5=('21.webp')
b6=('im.webp')
b7=("23.webp")
b8=("24.webp")
b9=("25.webp")
bala=("bell.mp4")
with st.container():
    st.header("Food..")
    j10,j2,j3,j4,j5,j6,j7,j8,j9=st.columns(9)
    
    with j2:
        st.button("RECIPES")
    with j3:
        st.button("POPULAR")
    with j4:
        st.button("SEAFOOD")
    with j5:
        st.button("HEALTHY & DIET")
    with j6:
        st.button("HOLIDAYS")
    with j7:
        st.button("CUISINE")
    with j8:
        st.button("SEASONAL")
 


with st.container():
    
    st.image(a)
with st.container():
    st.header("WHAT WE'RE CRAVING")
    o,s,e= st.columns([3,3,3])
    with o:
        st.image(b,"FRESH TOMATO RECIPES FOR SUMMER")
        
    with s:
        st.image(c,"VEGETARIAN RECIPES FOR SUMMER")
    with e:
        st.image(d,"BEST SUMMER RECIPES FOR TWO")
with st.container():
    st.header("EXPLORE MORE") 
    a,b,c,d,e,f= st.columns([2,2,2,2,2,2])
    with a:
        st.image(e1,'COMFORT FOOD CLASSICS')
    with b:
        st.image(f1,'INTERNATIONAL EATS')
   
    with c:
        st.image(g1,'BREAKFAST & BRUNCH')
  
    with d:
        st.image(h1,'COMMUNITY PICKS')
       
    with e:
        st.image(i1,'QUICK & EASY')
    with f:
        st.image(j1,'COPYCAT RECIPES')  
    
 
with st.container():
    st.header("TRENDING NOW") 
    k,l,m,n=st.columns([3,3,3,3])
    with k:
        st.image(a2,"PEACH AND ROASTED RED PEPPER BRUSCHETTA")
       
    with l:
        st.image(a3,"COURGETTE ZUCCHINI PASTA WITH CHILI,GARLIC &AMP; PARMESAN")
    with m:
        st.image(a5,"MISO-GLAZED EGGPLANT")
    with n:
        st.image(a6,"MISO-GLAZED EGGPLANT")
        
        
with st.container():
    st.header("DON'T MISS") 
    o,p,q=st.columns([3,3,3])
    with o:
        st.image(a7,"GREEK VILLAGE SALAD")
        
    with p:
        st.image(a8,"TAMALE PEPPERS")
    with q:
        st.image(a9,"Heirloom Tomato Tart")
        
with st.container():
    st.header("MORE IDEAS") 
    r,s,t,u=st.columns([3,3,3,3])
    with r:
        st.image(b2,"CHICKEN TIKKA MASALA")
    with s:
        st.image(b3,"VEGAN BACON")
    with t:
        st.image(b4,"COPYCAT MCDONALD'S BIG MAC SAUCE")
    with u:
        st.image(b5,"CROCK-POT BEEF ROAST")
     
with st.container():
    st.write("____")
    v,w=st.columns([5,4])
    with v:
        st.image(b6)
    with w:
        st.text('RECIPE')
        st.subheader('HOW TO GRILL OYSTERS')
       
        st.text("   SUPER simple!!! Serve with a squeeze of lemon, BBQ sauce, \ncocktail sauce, horseradish, salsa. .you name it! No shucking \nrequired. NOTE: make sure you buy LARGE oysters, as they are quite \nsmall when cooked and also make sure your heat is on HIGH or else \nthe shells won't pop open. 2 dozen oysters will serve 4 as \nan appetizer 2 as a main course. Recipe from Steven Raichlen's \nHow to Grill.")
        st.subheader("Ingredients:")
        st.text("* Fresh oysters in the shell")
        st.text("* Butter (unsalted)")
        st.text("* Garlic (minced)")
        st.text("* Lemon juice")
        st.text("* Parsley (chopped)")
        st.text("* Hot sauce (optional)")
        st.text("* Salt and pepper to taste")
                
with st.container():
    st.subheader("Food making video")
    st.video(bala)

with st.container():
    
    ba=st.columns(5)
    import streamlit as st
    css = """
<style>
.stApp {
    background-color: F0FFF0;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

with st.container():
    st.header("About..")
    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
        st.text('All Categories')
        st.markdown("[🥰 insta](https://www.instagram.com)")
        st.markdown("[🫥 facebook](https://www.facebook.com)")
    with col4:
        st.markdown("[Advertise](https://wbd.com)")
        st.markdown("[AdChoices](https://www.wbdprivacy.com)")
        st.markdown("[Privacy Policy](https://www.wbdprivacy.com)")
      
        
        
        button_css = """
                    <style>
                    .stButton > button {
                        background-color:F0FFF0; 
                    }

                    </style>
                    """
        st.markdown(button_css, unsafe_allow_html=True)
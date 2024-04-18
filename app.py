import streamlit as st
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Stunt:
    urls: List[str]  
    name: str
    level: int
    tags: Optional[List[str]]
    start_time: Optional[List[str]] = field(default_factory=lambda: ["0s"])
    end_time:Optional[List[str]] = field(default_factory=lambda: ["10s"])

    def __str__(self):
        urls_formatted = ', '.join(self.urls)  
        return f"{self.name} (Level: {self.level}) - Tags: {self.tags} - URLs: {urls_formatted}"



icing = Stunt(urls=["https://www.youtube.com/watch?v=VmEumb06YMQ", "https://www.youtube.com/watch?v=gjwQ3NdCZbI", "https://www.youtube.com/watch?v=YcHsWLuTlW0"], name="Icing On The Cake", level=2, tags=["L-Base", "Waschmaschine"])
pickpocket = Stunt(urls=["https://www.youtube.com/watch?v=pKWozRamuh4"], name="Clumsy Pickpocket", level=2, tags=["Waschmaschine", "L-Base"])
high_bird = Stunt(urls=["https://www.youtube.com/watch?v=jZWKYBlTljc", "https://www.youtube.com/watch?v=jZWKYBlTljc&t=5m12s"], name="Schwalbe", level=3, tags=["S-Base"], start_time=["2s", "5m12s"], end_time=["13s", "10h"])
whip_series = Stunt(urls=["https://www.youtube.com/watch?v=JmImpFX8srE"], name="50 Whips & Pops", level=3, tags="Whip/Pop", start_time=["14s"], end_time=["7m17s"])
stunts = [icing, pickpocket, high_bird, whip_series]


        

st.title("Akrobatik Sammlung")
level =  st.selectbox("Schwierigkeit",("Alle", "Level 1", "Level 2", "Level 3")  ,help="1 = Einfach, 5 = Sehr schwer")

def displayStunt(stunt, level):
    if str(stunt.level) in level or level == "Alle": 
        with st.expander(stunt.name):
            tab1, tab2 = st.tabs(["Demonstration", "Erklärung"])
            with tab1:
                st.subheader("Demonstration")
                st.video(stunt.urls[0], start_time=stunt.start_time[0], end_time=stunt.end_time[0])
            with tab2:
                if len(stunt.urls)>1:
                    st.subheader("Erklärung")
                    for url in stunt.urls[1:]:       
                        st.video(url, start_time=stunt.start_time[-1], end_time=stunt.end_time[-1])
                else: st.write("Leider keine Erklärung verfügbar 🥲")

tag_filter = st.multiselect(
    'Nach welcher Art von Figur suchst du?',
    ['Waschmaschine', 'L-Base', 'S-Base', 'Whip/Pop', 'Icarian'], placeholder="Alle Figuren")


at_least_one_shown = False
for stunt in stunts:
    if not tag_filter or set(tag_filter) <= set(stunt.tags):
        displayStunt(stunt, level)
        at_least_one_shown = True
if not at_least_one_shown: st.info("Zu deinen Filteroptionen gibt es noch kein Video")


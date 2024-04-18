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
    end_time: Optional[List[str]] = field(default_factory=lambda: ["10s"])

    def __str__(self):
        urls_formatted = ", ".join(self.urls)
        return f"{self.name} (Level: {self.level}) - Tags: {self.tags} - URLs: {urls_formatted}"


icing = Stunt(
    urls=[
        "https://www.youtube.com/watch?v=VmEumb06YMQ",
        "https://www.youtube.com/watch?v=gjwQ3NdCZbI",
        "https://www.youtube.com/watch?v=YcHsWLuTlW0",
    ],
    name="Icing On The Cake",
    level=2,
    tags=["L-Base", "Waschmaschine"],
)
pickpocket = Stunt(
    urls=["https://www.youtube.com/watch?v=pKWozRamuh4"],
    name="Clumsy Pickpocket",
    level=2,
    tags=["Waschmaschine", "L-Base"],
)
high_bird = Stunt(
    urls=[
        "https://www.youtube.com/watch?v=jZWKYBlTljc",
        "https://www.youtube.com/watch?v=jZWKYBlTljc&t=5m12s",
    ],
    name="Schwalbe (High Bird)",
    level=3,
    tags=["S-Base"],
    start_time=["2s", "5m12s"],
    end_time=["13s", "10h"],
)
whip_series = Stunt(
    urls=["https://www.youtube.com/watch?v=JmImpFX8srE"],
    name="50 Whips & Pops",
    level=3,
    tags="Whip/Pop",
    start_time=["14s"],
    end_time=["7m17s"],
)
star = Stunt(
    urls=[
        "https://www.youtube.com/watch?v=6HngmitsKuQ",
        "https://www.youtube.com/watch?v=6HngmitsKuQ",
    ],
    name="Schulterstand auf den Füßen (Star)",
    level=1,
    tags=["L-Base"],
    start_time=["2m26s", "1m52s"],
    end_time=["2m47s", "3m58s"],
)
twisted_tornado = Stunt(
    urls=["https://www.youtube.com/watch?v=HvG_V2oyUbg"],
    name="Twisted Tornado",
    level=3,
    tags=["L-Base", "Waschmaschine"],
)
peaceful_warrior_series = Stunt(
    urls=["https://www.youtube.com/watch?v=5Aw5_U-YC3E"],
    name="Peaceful Warrior Flow",
    level=4,
    tags=["Flow/Choreo", "L-Base"],
    start_time=["15s"],
    end_time=["2m46s"]
)
monkey_frog = Stunt(
    urls=["https://www.youtube.com/watch?v=JPd4YzU_T9o", "https://www.youtube.com/watch?v=JPd4YzU_T9o"],
    name="Monkey Frog",
    level=3,
    tags=["L-Base", "Waschmaschine"],
    start_time=["2s", "1m12s"],
    end_time=["32s", "9m44s"]
)
h2h = Stunt(
    urls=["https://www.youtube.com/watch?v=IL3scQYAo7w", "https://www.youtube.com/watch?v=IL3scQYAo7w"],
    name="Hand to Hand",
    level=3,
    tags=["L-Base"],
    start_time=["2s", "1m33s"],
    end_time=["25s", "10h"]
)
stunts = [icing, pickpocket, high_bird, whip_series, star, twisted_tornado, peaceful_warrior_series, monkey_frog, h2h]


st.title("Akrobatik Sammlung")
with st.popover("QR Code zur Website"):
    st.image("qr.png", width=320)
level = st.selectbox(
    "Schwierigkeit",
    ("Alle", "Level 1", "Level 2", "Level 3"),
    help="1 = Einfach, 5 = Sehr schwer",
)


def displayStunt(stunt, level):
    if str(stunt.level) in level or level == "Alle":
        with st.expander(stunt.name):
            tab1, tab2 = st.tabs(["Demonstration", "Erklärung"])
            with tab1:
                st.subheader("Demonstration")
                st.video(
                    stunt.urls[0],
                    start_time=stunt.start_time[0],
                    end_time=stunt.end_time[0],
                )
            with tab2:
                if len(stunt.urls) > 1:
                    st.subheader("Erklärung")
                    for url in stunt.urls[1:]:
                        st.video(
                            url,
                            start_time=stunt.start_time[-1],
                            end_time=stunt.end_time[-1],
                        )
                else:
                    st.write("Leider keine Erklärung verfügbar 🥲")


tag_filter = st.multiselect(
    "Nach welcher Art von Figur suchst du?",
    ["Waschmaschine", "L-Base", "S-Base", "Whip/Pop", "Flow/Choreo" "Icarian"],
    placeholder="Alle Figuren",
)


at_least_one_shown = False
for stunt in stunts:
    if not tag_filter or set(tag_filter) <= set(stunt.tags):
        displayStunt(stunt, level)
        at_least_one_shown = True
if not at_least_one_shown:
    st.info("Zu deinen Filteroptionen gibt es noch kein Video")

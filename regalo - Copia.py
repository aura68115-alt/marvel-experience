#codice app

import json
import os
import random
import urllib.parse
import webbrowser
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog


# ============================================================
# MARVEL EXPERIENCE — CONFIGURAZIONE
# ============================================================

NOME_FILE_DATI = "dati_utenti_multipli.json"

LINK_VIDEO_DRIVE = "https://drive.google.com/your-video-link-here"

COLOR_BG = "#080910"
COLOR_BG_2 = "#0d0e15"
COLOR_CARD = "#161823"
COLOR_CARD_ALT = "#1f2232"

COLOR_ACCENT = "#e50914"
COLOR_ACCENT_HOVER = "#ff1e27"
COLOR_PURPLE = "#8a2be2"
COLOR_PURPLE_HOVER = "#9d4edd"
COLOR_GREEN = "#2ed573"

COLOR_TEXT_MAIN = "#ffffff"
COLOR_TEXT_MUTED = "#a0a5b5"

FONT_TITOLO = ("Helvetica", 20, "bold")
FONT_TESTO = ("Segoe UI", 10)
FONT_BTN = ("Helvetica", 11, "bold")


# ============================================================
# CATALOGO FILM
# ============================================================

dati_film = {

    "Iron Man (2008)": {
        "fase": "MCU Fase 1",
        "anno": 2008,
        "durata": "126 min",
        "regia": "Jon Favreau",
        "cast": "Robert Downey Jr., Gwyneth Paltrow, Jeff Bridges",
        "trama": "Tony Stark, geniale miliardario e inventore, costruisce una potente armatura dopo essere stato rapito. Nasce così Iron Man."
    },

    "L'incredibile Hulk (2008)": {
        "fase": "MCU Fase 1",
        "anno": 2008,
        "durata": "112 min",
        "regia": "Louis Leterrier",
        "cast": "Edward Norton, Liv Tyler, Tim Roth",
        "trama": "Bruce Banner cerca una cura per la sua trasformazione nell'incredibile Hulk, mentre viene inseguito dalle forze militari."
    },

    "Iron Man 2 (2010)": {
        "fase": "MCU Fase 1",
        "anno": 2010,
        "durata": "124 min",
        "regia": "Jon Favreau",
        "cast": "Robert Downey Jr., Mickey Rourke, Scarlett Johansson",
        "trama": "Tony Stark deve affrontare nuovi nemici e le conseguenze della sua identità pubblica di Iron Man."
    },

    "Thor (2011)": {
        "fase": "MCU Fase 1",
        "anno": 2011,
        "durata": "115 min",
        "regia": "Kenneth Branagh",
        "cast": "Chris Hemsworth, Natalie Portman, Tom Hiddleston",
        "trama": "Thor viene esiliato sulla Terra e deve imparare cosa significa essere veramente degno del potere che possiede."
    },

    "Captain America - Il primo Vendicatore (2011)": {
        "fase": "MCU Fase 1",
        "anno": 2011,
        "durata": "124 min",
        "regia": "Joe Johnston",
        "cast": "Chris Evans, Hugo Weaving, Hayley Atwell",
        "trama": "Steve Rogers diventa Captain America e combatte contro Hydra durante la Seconda Guerra Mondiale."
    },

    "The Avengers (2012)": {
        "fase": "MCU Fase 1",
        "anno": 2012,
        "durata": "143 min",
        "regia": "Joss Whedon",
        "cast": "Robert Downey Jr., Chris Evans, Scarlett Johansson, Chris Hemsworth",
        "trama": "I più grandi eroi della Terra devono unirsi per fermare Loki e un'invasione aliena."
    },

    "Iron Man 3 (2013)": {
        "fase": "MCU Fase 2",
        "anno": 2013,
        "durata": "130 min",
        "regia": "Shane Black",
        "cast": "Robert Downey Jr., Guy Pearce, Gwyneth Paltrow",
        "trama": "Tony Stark affronta un nemico misterioso mentre cerca di superare le conseguenze della battaglia di New York."
    },

    "Thor: The Dark World (2013)": {
        "fase": "MCU Fase 2",
        "anno": 2013,
        "durata": "112 min",
        "regia": "Alan Taylor",
        "cast": "Chris Hemsworth, Natalie Portman, Tom Hiddleston",
        "trama": "Thor deve fermare un'antica minaccia legata agli Elfi Oscuri e all'Etere."
    },

    "Captain America: The Winter Soldier (2014)": {
        "fase": "MCU Fase 2",
        "anno": 2014,
        "durata": "136 min",
        "regia": "Anthony e Joe Russo",
        "cast": "Chris Evans, Sebastian Stan, Scarlett Johansson",
        "trama": "Captain America scopre una cospirazione all'interno dello S.H.I.E.L.D. e affronta Winter Soldier."
    },

    "Guardiani della Galassia (2014)": {
        "fase": "MCU Fase 2",
        "anno": 2014,
        "durata": "121 min",
        "regia": "James Gunn",
        "cast": "Chris Pratt, Zoe Saldana, Dave Bautista",
        "trama": "Un gruppo improbabile di criminali spaziali deve unirsi per proteggere una potente sfera e salvare la galassia."
    },

    "Avengers: Age of Ultron (2015)": {
        "fase": "MCU Fase 2",
        "anno": 2015,
        "durata": "141 min",
        "regia": "Joss Whedon",
        "cast": "Robert Downey Jr., Chris Evans, Mark Ruffalo",
        "trama": "Gli Avengers creano accidentalmente Ultron, un'intelligenza artificiale che decide che l'umanità rappresenta una minaccia."
    },

    "Ant-Man (2015)": {
        "fase": "MCU Fase 2",
        "anno": 2015,
        "durata": "117 min",
        "regia": "Peyton Reed",
        "cast": "Paul Rudd, Michael Douglas, Evangeline Lilly",
        "trama": "Scott Lang diventa Ant-Man e deve utilizzare le sue capacità per compiere una rapina impossibile."
    },

    "Captain America: Civil War (2016)": {
        "fase": "MCU Fase 3",
        "anno": 2016,
        "durata": "147 min",
        "regia": "Anthony e Joe Russo",
        "cast": "Chris Evans, Robert Downey Jr., Sebastian Stan",
        "trama": "Gli Avengers si dividono sulla questione della supervisione governativa."
    },

    "Doctor Strange (2016)": {
        "fase": "MCU Fase 3",
        "anno": 2016,
        "durata": "115 min",
        "regia": "Scott Derrickson",
        "cast": "Benedict Cumberbatch, Rachel McAdams, Tilda Swinton",
        "trama": "Stephen Strange scopre le arti mistiche e diventa uno dei più potenti maghi della Terra."
    },

    "Guardiani della Galassia Vol. 2 (2017)": {
        "fase": "MCU Fase 3",
        "anno": 2017,
        "durata": "136 min",
        "regia": "James Gunn",
        "cast": "Chris Pratt, Zoe Saldana, Kurt Russell",
        "trama": "I Guardiani affrontano nuove minacce mentre Peter Quill scopre la verità sulle proprie origini."
    },

    "Spider-Man: Homecoming (2017)": {
        "fase": "MCU Fase 3",
        "anno": 2017,
        "durata": "133 min",
        "regia": "Jon Watts",
        "cast": "Tom Holland, Michael Keaton, Robert Downey Jr.",
        "trama": "Peter Parker cerca di bilanciare la vita da adolescente con quella da supereroe mentre affronta l'Avvoltoio."
    },

    "Thor: Ragnarok (2017)": {
        "fase": "MCU Fase 3",
        "anno": 2017,
        "durata": "130 min",
        "regia": "Taika Waititi",
        "cast": "Chris Hemsworth, Tom Hiddleston, Cate Blanchett",
        "trama": "Thor deve affrontare Hela prima che Asgard venga distrutta."
    },

    "Black Panther (2018)": {
        "fase": "MCU Fase 3",
        "anno": 2018,
        "durata": "134 min",
        "regia": "Ryan Coogler",
        "cast": "Chadwick Boseman, Michael B. Jordan, Lupita Nyong'o",
        "trama": "T'Challa torna in Wakanda e deve difendere il suo popolo da una minaccia legata al passato."
    },

    "Avengers: Infinity War (2018)": {
        "fase": "MCU Fase 3",
        "anno": 2018,
        "durata": "149 min",
        "regia": "Anthony e Joe Russo",
        "cast": "Robert Downey Jr., Chris Hemsworth, Josh Brolin",
        "trama": "Thanos cerca di riunire le Gemme dell'Infinito."
    },

    "Ant-Man and the Wasp (2018)": {
        "fase": "MCU Fase 3",
        "anno": 2018,
        "durata": "118 min",
        "regia": "Peyton Reed",
        "cast": "Paul Rudd, Evangeline Lilly, Michael Douglas",
        "trama": "Scott Lang collabora con Hope Van Dyne per una missione legata al Regno Quantico."
    },

    "Captain Marvel (2019)": {
        "fase": "MCU Fase 3",
        "anno": 2019,
        "durata": "124 min",
        "regia": "Anna Boden, Ryan Fleck",
        "cast": "Brie Larson, Samuel L. Jackson, Ben Mendelsohn",
        "trama": "Carol Danvers diventa una delle eroine più potenti dell'universo."
    },

    "Avengers: Endgame (2019)": {
        "fase": "MCU Fase 3",
        "anno": 2019,
        "durata": "181 min",
        "regia": "Anthony e Joe Russo",
        "cast": "Robert Downey Jr., Chris Evans, Mark Ruffalo",
        "trama": "Gli Avengers rimasti devono trovare un modo per annullare le conseguenze dello schiocco di Thanos."
    },

    "Spider-Man: Far from Home (2019)": {
        "fase": "MCU Fase 3",
        "anno": 2019,
        "durata": "129 min",
        "regia": "Jon Watts",
        "cast": "Tom Holland, Jake Gyllenhaal, Zendaya",
        "trama": "Peter Parker parte per un viaggio in Europa, ma una nuova minaccia lo costringe a tornare in azione."
    },

    "Black Widow (2021)": {
        "fase": "MCU Fase 4",
        "anno": 2021,
        "durata": "134 min",
        "regia": "Cate Shortland",
        "cast": "Scarlett Johansson, Florence Pugh, David Harbour",
        "trama": "Natasha Romanoff affronta il proprio passato e torna a confrontarsi con la Red Room."
    },

    "Shang-Chi e la leggenda dei Dieci Anelli (2021)": {
        "fase": "MCU Fase 4",
        "anno": 2021,
        "durata": "132 min",
        "regia": "Destin Daniel Cretton",
        "cast": "Simu Liu, Awkwafina, Tony Leung",
        "trama": "Shang-Chi viene costretto ad affrontare il passato della propria famiglia."
    },

    "Eternals (2021)": {
        "fase": "MCU Fase 4",
        "anno": 2021,
        "durata": "156 min",
        "regia": "Chloé Zhao",
        "cast": "Gemma Chan, Richard Madden, Angelina Jolie",
        "trama": "Un gruppo di esseri immortali protegge segretamente la Terra da migliaia di anni."
    },

    "Spider-Man: No Way Home (2021)": {
        "fase": "MCU Fase 4",
        "anno": 2021,
        "durata": "148 min",
        "regia": "Jon Watts",
        "cast": "Tom Holland, Zendaya, Benedict Cumberbatch, Tobey Maguire, Andrew Garfield",
        "trama": "Peter Parker chiede aiuto a Doctor Strange per far dimenticare al mondo la sua identità."
    },

    "Doctor Strange nel Multiverso della Follia (2022)": {
        "fase": "MCU Fase 4",
        "anno": 2022,
        "durata": "126 min",
        "regia": "Sam Raimi",
        "cast": "Benedict Cumberbatch, Elizabeth Olsen, Xochitl Gomez",
        "trama": "Doctor Strange attraversa diverse realtà del multiverso."
    },

    "Thor: Love and Thunder (2022)": {
        "fase": "MCU Fase 4",
        "anno": 2022,
        "durata": "119 min",
        "regia": "Taika Waititi",
        "cast": "Chris Hemsworth, Christian Bale, Natalie Portman",
        "trama": "Thor deve affrontare Gorr, un nemico deciso a eliminare gli dei."
    },

    "Black Panther: Wakanda Forever (2022)": {
        "fase": "MCU Fase 4",
        "anno": 2022,
        "durata": "161 min",
        "regia": "Ryan Coogler",
        "cast": "Letitia Wright, Lupita Nyong'o, Tenoch Huerta",
        "trama": "Wakanda deve affrontare una nuova minaccia."
    },

    "Ant-Man and the Wasp: Quantumania (2023)": {
        "fase": "MCU Fase 5",
        "anno": 2023,
        "durata": "125 min",
        "regia": "Peyton Reed",
        "cast": "Paul Rudd, Evangeline Lilly, Jonathan Majors",
        "trama": "La famiglia Ant-Man viene trascinata nel Regno Quantico."
    },

    "Guardiani della Galassia Vol. 3 (2023)": {
        "fase": "MCU Fase 5",
        "anno": 2023,
        "durata": "150 min",
        "regia": "James Gunn",
        "cast": "Chris Pratt, Chukwudi Iwuji, Bradley Cooper",
        "trama": "I Guardiani affrontano una missione disperata per salvare Rocket."
    },

    "The Marvels (2023)": {
        "fase": "MCU Fase 5",
        "anno": 2023,
        "durata": "105 min",
        "regia": "Nia DaCosta",
        "cast": "Brie Larson, Teyonah Parris, Iman Vellani",
        "trama": "Captain Marvel, Monica Rambeau e Kamala Khan si ritrovano coinvolte in una misteriosa connessione cosmica."
    },

    "Deadpool & Wolverine (2024)": {
        "fase": "MCU Fase 5",
        "anno": 2024,
        "durata": "128 min",
        "regia": "Shawn Levy",
        "cast": "Ryan Reynolds, Hugh Jackman, Emma Corrin",
        "trama": "Deadpool viene coinvolto in una missione attraverso il multiverso e chiede aiuto a Wolverine."
    },

    "Spider-Man (2002)": {
        "fase": "Trilogia Raimi",
        "anno": 2002,
        "durata": "121 min",
        "regia": "Sam Raimi",
        "cast": "Tobey Maguire, Willem Dafoe, Kirsten Dunst",
        "trama": "Peter Parker viene morso da un ragno geneticamente modificato."
    },

    "Spider-Man 2 (2004)": {
        "fase": "Trilogia Raimi",
        "anno": 2004,
        "durata": "127 min",
        "regia": "Sam Raimi",
        "cast": "Tobey Maguire, Alfred Molina, Kirsten Dunst",
        "trama": "Peter deve affrontare Doctor Octopus."
    },

    "Spider-Man 3 (2007)": {
        "fase": "Trilogia Raimi",
        "anno": 2007,
        "durata": "139 min",
        "regia": "Sam Raimi",
        "cast": "Tobey Maguire, Topher Grace, Thomas Haden Church",
        "trama": "Peter affronta nuovi nemici e una misteriosa sostanza aliena."
    },

    "The Amazing Spider-Man (2012)": {
        "fase": "The Amazing Spider-Man",
        "anno": 2012,
        "durata": "136 min",
        "regia": "Marc Webb",
        "cast": "Andrew Garfield, Emma Stone, Rhys Ifans",
        "trama": "Peter Parker scopre nuovi segreti sul proprio passato e affronta Lizard."
    },

    "The Amazing Spider-Man 2 (2014)": {
        "fase": "The Amazing Spider-Man",
        "anno": 2014,
        "durata": "142 min",
        "regia": "Marc Webb",
        "cast": "Andrew Garfield, Emma Stone, Jamie Foxx",
        "trama": "Spider-Man affronta Electro e altri nemici."
    },

    "Venom (2018)": {
        "fase": "Sony's Spider-Man Universe",
        "anno": 2018,
        "durata": "112 min",
        "regia": "Ruben Fleischer",
        "cast": "Tom Hardy, Michelle Williams, Riz Ahmed",
        "trama": "Eddie Brock entra in contatto con un simbionte alieno e diventa Venom."
    },

    "Venom: La furia di Carnage (2021)": {
        "fase": "Sony's Spider-Man Universe",
        "anno": 2021,
        "durata": "97 min",
        "regia": "Andy Serkis",
        "cast": "Tom Hardy, Woody Harrelson, Michelle Williams",
        "trama": "Venom affronta Carnage."
    },

    "Venom: The Last Dance (2024)": {
        "fase": "Sony's Spider-Man Universe",
        "anno": 2024,
        "durata": "109 min",
        "regia": "Kelly Marcel",
        "cast": "Tom Hardy, Chiwetel Ejiofor, Juno Temple",
        "trama": "Eddie e Venom sono costretti a fuggire mentre una nuova minaccia mette in pericolo il loro futuro."
    },
}


TITOLO_ESCLUSIVO = "⭐ FILM ESCLUSIVO - Sorpresa di Compleanno! 🎁"

dati_film[TITOLO_ESCLUSIVO] = {
    "fase": "Edizione Speciale 🎁",
    "anno": 2026,
    "durata": "Edizione Speciale",
    "regia": "Alessandro",
    "cast": "Giuliana",
    "trama": (
        "🎁 La grande conclusione "
        "per questa Marvel Experience.\n\n"
        "Buon compleanno "
        "Il contenuto completo è disponibile tramite il pulsante dedicato."
    )
}


# ============================================================
# DATABASE
# ============================================================

database_utenti_default = {
    "Alessandro": {
        "password": None,
        "preferiti": [],
        "visti": [],
        "valutazioni": {},
        "record_gioco": 0,
        "achievement_sbloccati": []
    },
    "Giuliana": {
        "password": None,
        "preferiti": [],
        "visti": [],
        "valutazioni": {},
        "record_gioco": 0,
        "achievement_sbloccati": []
    }
}

database_utenti = {}
utente_corrente = None
film_selezionato_corrente = None
titoli_filtrati = []


def crea_database_pulito():
    return {
        nome: {
            "password": dati["password"],
            "preferiti": list(dati["preferiti"]),
            "visti": list(dati["visti"]),
            "valutazioni": dict(dati["valutazioni"]),
            "record_gioco": dati["record_gioco"],
            "achievement_sbloccati": list(
                dati.get("achievement_sbloccati", [])
            )
        }
        for nome, dati in database_utenti_default.items()
    }


def normalizza_database():
    global database_utenti

    for nome in database_utenti_default:
        if nome not in database_utenti:
            database_utenti[nome] = crea_database_pulito()[nome]

        dati = database_utenti[nome]

        if not isinstance(dati.get("preferiti"), list):
            dati["preferiti"] = []

        if not isinstance(dati.get("visti"), list):
            dati["visti"] = []

        if not isinstance(dati.get("valutazioni"), dict):
            dati["valutazioni"] = {}

        if not isinstance(dati.get("record_gioco"), int):
            dati["record_gioco"] = 0

        if not isinstance(dati.get("achievement_sbloccati"), list):
            dati["achievement_sbloccati"] = []


def carica_dati():
    global database_utenti

    database_utenti = crea_database_pulito()

    if not os.path.exists(NOME_FILE_DATI):
        return

    try:
        with open(NOME_FILE_DATI, "r", encoding="utf-8") as file:
            dati_salvati = json.load(file)

        if isinstance(dati_salvati, dict):
            for nome in database_utenti:
                if nome in dati_salvati and isinstance(
                    dati_salvati[nome],
                    dict
                ):
                    database_utenti[nome].update(
                        dati_salvati[nome]
                    )

        normalizza_database()

    except (json.JSONDecodeError, OSError, TypeError):
        database_utenti = crea_database_pulito()


def salva_dati():
    try:
        with open(
            NOME_FILE_DATI,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                database_utenti,
                file,
                ensure_ascii=False,
                indent=4
            )

    except OSError:
        messagebox.showerror(
            "Errore salvataggio",
            "Non riesco a salvare i dati degli utenti."
        )


# ============================================================
# ACHIEVEMENT
# ============================================================

def spider_man_completo(d):
    spider_film = [
        "Spider-Man (2002)",
        "Spider-Man 2 (2004)",
        "Spider-Man 3 (2007)",
        "The Amazing Spider-Man (2012)",
        "The Amazing Spider-Man 2 (2014)",
        "Spider-Man: Homecoming (2017)",
        "Spider-Man: Far from Home (2019)",
        "Spider-Man: No Way Home (2021)"
    ]

    return all(
        film in d["visti"]
        for film in spider_film
    )


def fasi_1_3_complete(d):
    film_fasi = [
        titolo
        for titolo, info in dati_film.items()
        if info["fase"] in [
            "MCU Fase 1",
            "MCU Fase 2",
            "MCU Fase 3"
        ]
    ]

    return all(
        film in d["visti"]
        for film in film_fasi
    )


ACHIEVEMENTS = {
    "primo_passo": {
        "nome": "Primo passo",
        "descrizione": "Guarda il primo film",
        "icona": "🥉",
        "controllo": lambda d: len(d["visti"]) >= 1
    },

    "maratoneta": {
        "nome": "Maratoneta",
        "descrizione": "Guarda 10 film",
        "icona": "🥈",
        "controllo": lambda d: len(d["visti"]) >= 10
    },

    "archivista": {
        "nome": "Archivista Marvel",
        "descrizione": "Guarda 25 film",
        "icona": "🥇",
        "controllo": lambda d: len(d["visti"]) >= 25
    },

    "fan_assoluto": {
        "nome": "Fan assoluto",
        "descrizione": "Aggiungi 15 preferiti",
        "icona": "❤️",
        "controllo": lambda d: len(d["preferiti"]) >= 15
    },

    "critico": {
        "nome": "Critico cinematografico",
        "descrizione": "Vota 20 film",
        "icona": "⭐",
        "controllo": lambda d: len(d["valutazioni"]) >= 20
    },

    "spider_verse": {
        "nome": "Spider-Verse",
        "descrizione": "Guarda tutti gli Spider-Man",
        "icona": "🕷️",
        "controllo": spider_man_completo
    },

    "avenger": {
        "nome": "Avenger",
        "descrizione": "Completa tutte le Fasi 1–3",
        "icona": "⚡",
        "controllo": fasi_1_3_complete
    },

    "sopravvissuto": {
        "nome": "Sopravvissuto al Multiverso",
        "descrizione": "Raggiungi 500 punti nel gioco",
        "icona": "💀",
        "controllo": lambda d: d.get(
            "record_gioco",
            0
        ) >= 500
    },

    "collezionista": {
        "nome": "Collezionista",
        "descrizione": "Aggiungi 5 preferiti",
        "icona": "💎",
        "controllo": lambda d: len(d["preferiti"]) >= 5
    },

    "cinefilo": {
        "nome": "Cinefilo",
        "descrizione": "Guarda 50 film",
        "icona": "🎬",
        "controllo": lambda d: len(d["visti"]) >= 50
    },

    "cinque_stelle": {
        "nome": "Cinque stelle",
        "descrizione": "Dai almeno una valutazione da 5 stelle",
        "icona": "🌟",
        "controllo": lambda d: 5 in d["valutazioni"].values()
    },

    "multiverso": {
        "nome": "Esploratore del Multiverso",
        "descrizione": "Guarda film di 5 universi differenti",
        "icona": "🌌",
        "controllo": lambda d: len(set(
            dati_film[f]["fase"]
            for f in d["visti"]
            if f in dati_film
        )) >= 5
    },

    "campione": {
        "nome": "Campione dell'arena",
        "descrizione": "Raggiungi 1000 punti",
        "icona": "🏆",
        "controllo": lambda d: d.get(
            "record_gioco",
            0
        ) >= 1000
    },

    "legendario": {
        "nome": "Leggendario",
        "descrizione": "Guarda 75 film",
        "icona": "👑",
        "controllo": lambda d: len(d["visti"]) >= 75
    },

    "completista": {
        "nome": "Completista",
        "descrizione": "Guarda tutto il catalogo",
        "icona": "🔥",
        "controllo": lambda d: len(d["visti"]) >= len(dati_film)
    }
}


def achievement_sbloccati(dati):
    return [
        key
        for key, achievement in ACHIEVEMENTS.items()
        if achievement["controllo"](dati)
    ]


def controlla_achievement(mostra_popup=True):
    if not utente_corrente:
        return

    dati = database_utenti[utente_corrente]

    vecchi = set(
        dati.get(
            "achievement_sbloccati",
            []
        )
    )

    nuovi_sbloccati = set(
        achievement_sbloccati(dati)
    )

    nuovi = nuovi_sbloccati - vecchi

    dati["achievement_sbloccati"] = list(
        nuovi_sbloccati
    )

    if nuovi:
        salva_dati()

        if mostra_popup:
            for key in nuovi:
                achievement = ACHIEVEMENTS[key]

                messagebox.showinfo(
                    "🏆 ACHIEVEMENT SBLOCCATO!",
                    f"{achievement['icona']} "
                    f"{achievement['nome']}\n\n"
                    f"{achievement['descrizione']}"
                )


# ============================================================
# STATISTICHE PROFILO
# ============================================================

def ore_marvel(dati):
    minuti_totali = 0

    for titolo in dati["visti"]:
        if titolo not in dati_film:
            continue

        durata = dati_film[titolo]["durata"]

        try:
            minuti = int(
                durata.split()[0]
            )

            minuti_totali += minuti

        except (ValueError, IndexError):
            pass

    return (
        minuti_totali // 60,
        minuti_totali % 60
    )


def media_voti(dati):
    voti = list(
        dati["valutazioni"].values()
    )

    if not voti:
        return 0

    return sum(voti) / len(voti)


def fase_preferita(dati):
    conteggio = {}

    for titolo in dati["visti"]:
        if titolo not in dati_film:
            continue

        fase = dati_film[titolo]["fase"]

        conteggio[fase] = (
            conteggio.get(fase, 0) + 1
        )

    if not conteggio:
        return "Nessuna"

    return max(
        conteggio,
        key=conteggio.get
    )


def personaggio_preferito(dati):
    personaggi = {
        "Iron Man": [
            "Iron Man (2008)",
            "Iron Man 2 (2010)",
            "Iron Man 3 (2013)",
            "Avengers: Endgame (2019)"
        ],

        "Spider-Man": [
            "Spider-Man (2002)",
            "Spider-Man 2 (2004)",
            "Spider-Man 3 (2007)",
            "The Amazing Spider-Man (2012)",
            "The Amazing Spider-Man 2 (2014)",
            "Spider-Man: Homecoming (2017)",
            "Spider-Man: Far from Home (2019)",
            "Spider-Man: No Way Home (2021)"
        ],

        "Thor": [
            "Thor (2011)",
            "Thor: The Dark World (2013)",
            "Thor: Ragnarok (2017)",
            "Thor: Love and Thunder (2022)"
        ],

        "Captain America": [
            "Captain America - Il primo Vendicatore (2011)",
            "Captain America: The Winter Soldier (2014)",
            "Captain America: Civil War (2016)"
        ],

        "Guardiani della Galassia": [
            "Guardiani della Galassia (2014)",
            "Guardiani della Galassia Vol. 2 (2017)",
            "Guardiani della Galassia Vol. 3 (2023)"
        ]
    }

    conteggio = {}

    for personaggio, film in personaggi.items():
        conteggio[personaggio] = sum(
            1
            for film_titolo in film
            if film_titolo in dati["visti"]
        )

    if not conteggio:
        return "Non ancora"

    migliore = max(
        conteggio,
        key=conteggio.get
    )

    if conteggio[migliore] == 0:
        return "Non ancora"

    return migliore


# ============================================================
# FINESTRA
# ============================================================

root = tk.Tk()
root.title("Marvel Experience")
root.geometry("1200x800")
root.minsize(950, 650)
root.configure(bg=COLOR_BG)


# ============================================================
# UTILITÀ
# ============================================================

def aggiungi_hover(widget, normale, hover):
    widget.bind(
        "<Enter>",
        lambda e: widget.config(bg=hover)
    )

    widget.bind(
        "<Leave>",
        lambda e: widget.config(bg=normale)
    )


def apri_video_drive():
    webbrowser.open(
        LINK_VIDEO_DRIVE
    )


def apri_trailer_youtube():
    if not film_selezionato_corrente:
        return

    query = urllib.parse.quote(
        film_selezionato_corrente
        + " trailer ita"
    )

    webbrowser.open(
        "https://www.youtube.com/results?search_query="
        + query
    )


# ============================================================
# LOADING
# ============================================================

frame_loading = tk.Frame(
    root,
    bg=COLOR_BG
)

loading_canvas = tk.Canvas(
    frame_loading,
    bg=COLOR_BG,
    highlightthickness=0
)

loading_canvas.pack(
    fill="both",
    expand=True
)

loading_particles = []
loading_running = False
loading_x = -300


def crea_particelle():
    global loading_particles

    loading_particles.clear()

    w = max(
        1200,
        loading_canvas.winfo_width()
    )

    h = max(
        800,
        loading_canvas.winfo_height()
    )

    for _ in range(90):
        x = random.randint(0, w)
        y = random.randint(0, h)
        size = random.choice([1, 1, 2, 2, 3])

        color = random.choice([
            "#ffffff",
            "#e50914",
            "#ff3340",
            "#8a2be2",
            "#555a70"
        ])

        item = loading_canvas.create_oval(
            x,
            y,
            x + size,
            y + size,
            fill=color,
            outline=""
        )

        loading_particles.append([
            item,
            x,
            y,
            random.uniform(0.4, 2),
            size
        ])


def anima_loading():
    global loading_x

    if not loading_running:
        return

    w = loading_canvas.winfo_width()
    h = loading_canvas.winfo_height()

    for p in loading_particles:
        p[2] -= p[3]

        if p[2] < -5:
            p[2] = h + 5
            p[1] = random.randint(
                0,
                max(1, w)
            )

        loading_canvas.coords(
            p[0],
            p[1],
            p[2],
            p[1] + p[4],
            p[2] + p[4]
        )

    loading_x += 10

    if loading_x > w + 300:
        loading_x = -300

    root.after(
        25,
        anima_loading
    )


def termina_loading():
    global loading_running

    loading_running = False
    mostra_login()


def avvia_loading():
    global loading_running

    loading_running = True

    frame_loading.pack(
        fill="both",
        expand=True
    )

    loading_canvas.delete("all")

    crea_particelle()

    loading_canvas.create_text(
        600,
        280,
        text="MARVEL",
        font=("Helvetica", 68, "bold"),
        fill=COLOR_ACCENT
    )

    loading_canvas.create_text(
        600,
        355,
        text="EXPERIENCE",
        font=("Helvetica", 24, "bold"),
        fill=COLOR_TEXT_MAIN
    )

    loading_canvas.create_line(
        450,
        390,
        750,
        390,
        fill=COLOR_ACCENT,
        width=3
    )

    loading_status = loading_canvas.create_text(
        600,
        440,
        text="Preparazione del Multiverso...",
        font=("Segoe UI", 11, "bold"),
        fill=COLOR_TEXT_MUTED
    )

    loading_percent = loading_canvas.create_text(
        600,
        500,
        text="0%",
        font=("Helvetica", 16, "bold"),
        fill=COLOR_TEXT_MAIN
    )

    loading_canvas.create_rectangle(
        350,
        535,
        850,
        543,
        fill="#191b29",
        outline=""
    )

    progress = {"value": 0}

    def aggiorna():
        if not loading_running:
            return

        progress["value"] += 1

        valore = progress["value"]

        loading_canvas.itemconfig(
            loading_percent,
            text=f"{valore}%"
        )

        messaggi = [
            "Preparazione del Multiverso...",
            "Caricamento universi...",
            "Sincronizzazione profili...",
            "Caricamento catalogo...",
            "Calibrazione del cinema...",
            "Preparazione dell'arena...",
            "Quasi pronto..."
        ]

        indice = min(
            len(messaggi) - 1,
            int(
                valore / 100
                * len(messaggi)
            )
        )

        loading_canvas.itemconfig(
            loading_status,
            text=messaggi[indice]
        )

        loading_canvas.delete(
            "progress"
        )

        loading_canvas.create_rectangle(
            350,
            535,
            350 + valore * 5,
            543,
            fill=COLOR_ACCENT,
            outline="",
            tags="progress"
        )

        if valore >= 100:
            root.after(
                700,
                termina_loading
            )

        else:
            root.after(
                random.randint(15, 35),
                aggiorna
            )

    anima_loading()

    root.after(
        500,
        aggiorna
    )


# ============================================================
# LOGIN
# ============================================================

frame_login = tk.Frame(
    root,
    bg=COLOR_BG
)

lbl_titolo_login = tk.Label(
    frame_login,
    text="SCEGLI IL TUO PROFILO",
    font=("Helvetica", 26, "bold"),
    fg=COLOR_TEXT_MAIN,
    bg=COLOR_BG
)

lbl_titolo_login.pack(
    pady=(45, 5)
)

tk.Label(
    frame_login,
    text="Entra nel tuo universo personale",
    font=("Segoe UI", 11),
    fg=COLOR_TEXT_MUTED,
    bg=COLOR_BG
).pack(
    pady=(0, 35)
)

frame_profili = tk.Frame(
    frame_login,
    bg=COLOR_BG
)

frame_profili.pack(
    expand=True
)


def seleziona_profilo(nome):
    global utente_corrente

    utente_corrente = nome

    frame_profili.pack_forget()
    frame_password.pack(
        pady=20
    )

    aggiorna_login()

    entry_pass.delete(
        0,
        tk.END
    )

    entry_pass.focus_set()


def crea_profilo(parent, nome, iniziale, colore):
    card = tk.Frame(
        parent,
        bg=COLOR_CARD,
        width=330,
        height=380,
        highlightbackground="#292c3a",
        highlightthickness=2
    )

    card.pack_propagate(False)

    canvas = tk.Canvas(
        card,
        width=130,
        height=130,
        bg=COLOR_CARD,
        highlightthickness=0
    )

    canvas.pack(
        pady=(35, 15)
    )

    canvas.create_oval(
        8,
        8,
        122,
        122,
        fill=COLOR_CARD_ALT,
        outline=colore,
        width=4
    )

    canvas.create_text(
        65,
        65,
        text=iniziale,
        font=("Helvetica", 50, "bold"),
        fill=COLOR_TEXT_MAIN
    )

    tk.Label(
        card,
        text=nome.upper(),
        font=("Helvetica", 22, "bold"),
        fg=COLOR_TEXT_MAIN,
        bg=COLOR_CARD
    ).pack()

    tk.Label(
        card,
        text="MARVEL CINEMA EXPERIENCE",
        font=("Segoe UI", 9, "bold"),
        fg=COLOR_TEXT_MUTED,
        bg=COLOR_CARD
    ).pack(pady=8)

    btn = tk.Button(
        card,
        text="SELEZIONA",
        font=FONT_BTN,
        bg=colore,
        fg="white",
        activebackground=COLOR_ACCENT_HOVER,
        bd=0,
        padx=40,
        pady=10,
        cursor="hand2",
        command=lambda: seleziona_profilo(nome)
    )

    btn.pack(pady=12)

    aggiungi_hover(
        btn,
        colore,
        COLOR_ACCENT_HOVER
    )

    for widget in (
        card,
        canvas
    ):
        widget.bind(
            "<Button-1>",
            lambda e, n=nome:
            seleziona_profilo(n)
        )

    return card


crea_profilo(
    frame_profili,
    "Giuliana",
    "G",
    COLOR_PURPLE
).pack(
    side="left",
    padx=25
)

crea_profilo(
    frame_profili,
    "Alessandro",
    "A",
    COLOR_ACCENT
).pack(
    side="left",
    padx=25
)


frame_password = tk.Frame(
    frame_login,
    bg=COLOR_CARD,
    padx=45,
    pady=30,
    highlightbackground=COLOR_ACCENT,
    highlightthickness=2
)

tk.Label(
    frame_password,
    text="🔐",
    font=("Helvetica", 42),
    bg=COLOR_CARD,
    fg="white"
).pack()

lbl_login = tk.Label(
    frame_password,
    text="",
    font=FONT_TITOLO,
    fg=COLOR_TEXT_MAIN,
    bg=COLOR_CARD
)

lbl_login.pack(pady=5)

lbl_sub_login = tk.Label(
    frame_password,
    text="",
    font=FONT_TESTO,
    fg=COLOR_TEXT_MUTED,
    bg=COLOR_CARD
)

lbl_sub_login.pack()

entry_pass = tk.Entry(
    frame_password,
    show="*",
    font=FONT_TESTO,
    bg=COLOR_CARD_ALT,
    fg="white",
    insertbackground="white",
    justify="center",
    bd=0
)

entry_pass.pack(
    fill="x",
    ipady=10,
    pady=15
)


def aggiorna_login():
    dati = database_utenti[
        utente_corrente
    ]

    if not dati.get("password"):
        lbl_login.config(
            text=f"BENVENUTO/A {utente_corrente.upper()}!"
        )

        lbl_sub_login.config(
            text="Crea una password personale:"
        )

        btn_login.config(
            text="CREA PASSWORD ED ENTRA 🔑"
        )

        btn_cambia_pass.pack_forget()

    else:
        lbl_login.config(
            text=f"ACCESSO {utente_corrente.upper()}"
        )

        lbl_sub_login.config(
            text="Inserisci la tua password:"
        )

        btn_login.config(
            text="ENTRA NELLA MARVEL EXPERIENCE 🚀"
        )

        btn_cambia_pass.pack(
            pady=(10, 0)
        )


def verifica_accesso(event=None):
    if not utente_corrente:
        return

    password = entry_pass.get()

    if not password:
        messagebox.showwarning(
            "Password",
            "Inserisci una password."
        )
        return

    dati = database_utenti[
        utente_corrente
    ]

    if not dati.get("password"):

        if len(password) < 3:
            messagebox.showwarning(
                "Password troppo corta",
                "La password deve contenere almeno 3 caratteri."
            )
            return

        dati["password"] = password

        salva_dati()

        mostra_home()

    elif password == dati["password"]:
        mostra_home()

    else:
        messagebox.showerror(
            "Accesso negato",
            "La password non è corretta."
        )

        entry_pass.delete(
            0,
            tk.END
        )


entry_pass.bind(
    "<Return>",
    verifica_accesso
)


btn_login = tk.Button(
    frame_password,
    text="",
    font=FONT_BTN,
    bg=COLOR_ACCENT,
    fg="white",
    activebackground=COLOR_ACCENT_HOVER,
    bd=0,
    cursor="hand2",
    command=verifica_accesso
)

btn_login.pack(
    fill="x",
    ipady=10
)

aggiungi_hover(
    btn_login,
    COLOR_ACCENT,
    COLOR_ACCENT_HOVER
)


def cambia_password():
    dati = database_utenti[
        utente_corrente
    ]

    vecchia = simpledialog.askstring(
        "Cambio Password",
        "Vecchia password:",
        show="*"
    )

    if vecchia != dati.get("password"):
        messagebox.showerror(
            "Errore",
            "Password errata."
        )
        return

    nuova = simpledialog.askstring(
        "Cambio Password",
        "Nuova password:",
        show="*"
    )

    if nuova and len(nuova.strip()) >= 3:
        dati["password"] = nuova.strip()

        salva_dati()

        messagebox.showinfo(
            "Successo",
            "Password cambiata."
        )


btn_cambia_pass = tk.Button(
    frame_password,
    text="⚙️ Cambia Password",
    font=("Segoe UI", 9),
    bg=COLOR_CARD_ALT,
    fg=COLOR_TEXT_MUTED,
    bd=0,
    command=cambia_password
)


def torna_profili():
    frame_password.pack_forget()
    frame_profili.pack(
        expand=True
    )

    entry_pass.delete(
        0,
        tk.END
    )


tk.Button(
    frame_password,
    text="← Cambia profilo",
    font=("Segoe UI", 9),
    bg=COLOR_CARD,
    fg=COLOR_TEXT_MUTED,
    bd=0,
    command=torna_profili
).pack(
    pady=(15, 0)
)


def mostra_login():
    frame_loading.pack_forget()
    frame_home.pack_forget()
    frame_cinema.pack_forget()
    frame_game.pack_forget()
    frame_profilo.pack_forget()
    frame_achievement.pack_forget()

    frame_login.pack(
        fill="both",
        expand=True
    )

    frame_password.pack_forget()
    frame_profili.pack(
        expand=True
    )


# ============================================================
# HOME
# ============================================================

frame_home = tk.Frame(
    root,
    bg=COLOR_BG
)

home_canvas = tk.Canvas(
    frame_home,
    bg=COLOR_BG,
    highlightthickness=0
)

home_canvas.place(
    relx=0,
    rely=0,
    relwidth=1,
    relheight=1
)

home_particles = []


def crea_home_particles():
    global home_particles

    for item in home_particles:
        home_canvas.delete(
            item[0]
        )

    home_particles = []

    w = max(
        1000,
        home_canvas.winfo_width()
    )

    h = max(
        700,
        home_canvas.winfo_height()
    )

    for _ in range(70):
        x = random.randint(0, w)
        y = random.randint(0, h)

        item = home_canvas.create_oval(
            x,
            y,
            x + 2,
            y + 2,
            fill=random.choice([
                "#e50914",
                "#8a2be2",
                "#ffffff",
                "#34374c"
            ]),
            outline=""
        )

        home_particles.append([
            item,
            x,
            y,
            random.uniform(.2, 1.2)
        ])


def anima_home():
    if not frame_home.winfo_ismapped():
        return

    h = home_canvas.winfo_height()

    for p in home_particles:
        p[2] -= p[3]

        if p[2] < 0:
            p[2] = h

        home_canvas.coords(
            p[0],
            p[1],
            p[2],
            p[1] + 2,
            p[2] + 2
        )

    root.after(
        40,
        anima_home
    )


home_content = tk.Frame(
    frame_home,
    bg=COLOR_BG
)

home_content.place(
    relx=.5,
    rely=.5,
    anchor="center"
)

tk.Label(
    home_content,
    text="MARVEL",
    font=("Helvetica", 55, "bold"),
    fg=COLOR_ACCENT,
    bg=COLOR_BG
).pack()

tk.Label(
    home_content,
    text="EXPERIENCE",
    font=("Helvetica", 22, "bold"),
    fg=COLOR_TEXT_MAIN,
    bg=COLOR_BG
).pack()

lbl_home_welcome = tk.Label(
    home_content,
    text="",
    font=("Segoe UI", 11),
    fg=COLOR_TEXT_MUTED,
    bg=COLOR_BG
)

lbl_home_welcome.pack(
    pady=(12, 20)
)

frame_home_cards = tk.Frame(
    home_content,
    bg=COLOR_BG
)

frame_home_cards.pack()


def crea_home_card(
    parent,
    emoji,
    titolo,
    descrizione,
    colore,
    command
):
    card = tk.Frame(
        parent,
        bg=COLOR_CARD,
        width=300,
        height=210,
        highlightbackground="#292c3a",
        highlightthickness=2,
        cursor="hand2"
    )

    card.pack_propagate(False)

    tk.Label(
        card,
        text=emoji,
        font=("Segoe UI Emoji", 38),
        bg=COLOR_CARD,
        fg="white"
    ).pack(
        pady=(20, 5)
    )

    tk.Label(
        card,
        text=titolo,
        font=("Helvetica", 18, "bold"),
        bg=COLOR_CARD,
        fg="white"
    ).pack()

    tk.Label(
        card,
        text=descrizione,
        font=("Segoe UI", 9),
        bg=COLOR_CARD,
        fg=COLOR_TEXT_MUTED,
        justify="center"
    ).pack(
        pady=6
    )

    btn = tk.Button(
        card,
        text="ENTRA",
        font=("Helvetica", 10, "bold"),
        bg=colore,
        fg="white",
        bd=0,
        padx=40,
        pady=7,
        cursor="hand2",
        command=command
    )

    btn.pack()

    aggiungi_hover(
        btn,
        colore,
        COLOR_ACCENT_HOVER
    )

    card.bind(
        "<Enter>",
        lambda e:
        card.config(
            highlightbackground=colore
        )
    )

    card.bind(
        "<Leave>",
        lambda e:
        card.config(
            highlightbackground="#292c3a"
        )
    )

    return card


crea_home_card(
    frame_home_cards,
    "🎬",
    "CINEMA",
    "Esplora Marvel, Spider-Man,\npreferiti, trailer e molto altro.",
    COLOR_ACCENT,
    lambda: apri_cinema()
).pack(
    side="left",
    padx=10
)

crea_home_card(
    frame_home_cards,
    "🎮",
    "GIOCHI",
    "Entra nell'arena e prova a\nbattere il tuo record.",
    COLOR_PURPLE,
    lambda: apri_gioco()
).pack(
    side="left",
    padx=10
)


# ============================================================
# PROFILO
# ============================================================

frame_profilo = tk.Frame(
    root,
    bg=COLOR_BG
)

profilo_header = tk.Frame(
    frame_profilo,
    bg=COLOR_CARD,
    padx=20,
    pady=12
)

profilo_header.pack(
    fill="x"
)

tk.Button(
    profilo_header,
    text="← HOME",
    font=("Segoe UI", 9, "bold"),
    bg=COLOR_CARD_ALT,
    fg=COLOR_TEXT_MUTED,
    bd=0,
    command=lambda: mostra_home()
).pack(
    side="left"
)

tk.Label(
    profilo_header,
    text="📊 IL MIO PROFILO",
    font=FONT_TITOLO,
    fg=COLOR_ACCENT,
    bg=COLOR_CARD
).pack(
    side="left",
    padx=20
)

profilo_canvas = tk.Canvas(
    frame_profilo,
    bg=COLOR_BG,
    highlightthickness=0
)

profilo_scrollbar = tk.Scrollbar(
    frame_profilo,
    command=profilo_canvas.yview
)

profilo_scrollbar.pack(
    side="right",
    fill="y"
)

profilo_canvas.pack(
    side="left",
    fill="both",
    expand=True
)

profilo_canvas.configure(
    yscrollcommand=profilo_scrollbar.set
)

profilo_content = tk.Frame(
    profilo_canvas,
    bg=COLOR_BG
)

profilo_window = profilo_canvas.create_window(
    (0, 0),
    window=profilo_content,
    anchor="nw"
)


def aggiorna_scroll_profilo(event=None):
    profilo_canvas.configure(
        scrollregion=profilo_canvas.bbox("all")
    )

    profilo_canvas.itemconfig(
        profilo_window,
        width=profilo_canvas.winfo_width()
    )


profilo_content.bind(
    "<Configure>",
    aggiorna_scroll_profilo
)


def mostra_profilo():
    frame_home.pack_forget()
    frame_cinema.pack_forget()
    frame_game.pack_forget()
    frame_achievement.pack_forget()

    frame_profilo.pack(
        fill="both",
        expand=True
    )

    controlla_achievement(
        mostra_popup=False
    )

    for widget in profilo_content.winfo_children():
        widget.destroy()

    dati = database_utenti[
        utente_corrente
    ]

    visti = len(
        dati["visti"]
    )

    totale = len(
        dati_film
    )

    preferiti = len(
        dati["preferiti"]
    )

    media = media_voti(
        dati
    )

    record = dati.get(
        "record_gioco",
        0
    )

    sbloccati = len(
        achievement_sbloccati(
            dati
        )
    )

    totale_achievement = len(
        ACHIEVEMENTS
    )

    ore, minuti = ore_marvel(
        dati
    )

    personaggio = personaggio_preferito(
        dati
    )

    fase = fase_preferita(
        dati
    )

    percentuale = int(
        visti / totale * 100
    ) if totale else 0

    tk.Label(
        profilo_content,
        text=f"PROFILO DI {utente_corrente.upper()}",
        font=("Helvetica", 28, "bold"),
        fg="white",
        bg=COLOR_BG
    ).pack(
        pady=(25, 5)
    )

    tk.Label(
        profilo_content,
        text="Il tuo universo Marvel personale",
        font=("Segoe UI", 11),
        fg=COLOR_TEXT_MUTED,
        bg=COLOR_BG
    ).pack(
        pady=(0, 20)
    )

    # Barra progresso
    progress_card = tk.Frame(
        profilo_content,
        bg=COLOR_CARD,
        padx=25,
        pady=20,
        highlightbackground=COLOR_ACCENT,
        highlightthickness=1
    )

    progress_card.pack(
        fill="x",
        padx=25,
        pady=(0, 15)
    )

    tk.Label(
        progress_card,
        text=f"🎬 PROGRESSO MARVEL — {percentuale}%",
        font=("Helvetica", 14, "bold"),
        fg="white",
        bg=COLOR_CARD
    ).pack(
        anchor="w"
    )

    tk.Label(
        progress_card,
        text=f"{visti} / {totale} film completati",
        font=("Segoe UI", 9),
        fg=COLOR_TEXT_MUTED,
        bg=COLOR_CARD
    ).pack(
        anchor="w",
        pady=(3, 10)
    )

    progress = ttk.Progressbar(
        progress_card,
        orient="horizontal",
        mode="determinate",
        maximum=100,
        value=percentuale
    )

    progress.pack(
        fill="x"
    )

    # Statistiche
    stats = tk.Frame(
        profilo_content,
        bg=COLOR_BG
    )

    stats.pack(
        fill="x",
        padx=20
    )

    def stat_card(
        parent,
        emoji,
        titolo,
        valore,
        colore
    ):
        card = tk.Frame(
            parent,
            bg=COLOR_CARD,
            height=130,
            highlightbackground="#292c3a",
            highlightthickness=1
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text=emoji,
            font=("Segoe UI Emoji", 24),
            fg="white",
            bg=COLOR_CARD
        ).pack(
            pady=(10, 0)
        )

        tk.Label(
            card,
            text=valore,
            font=("Helvetica", 17, "bold"),
            fg=colore,
            bg=COLOR_CARD
        ).pack()

        tk.Label(
            card,
            text=titolo,
            font=("Segoe UI", 8, "bold"),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CARD
        ).pack()

    stat_card(
        stats,
        "🎬",
        "FILM VISTI",
        f"{visti}/{totale}",
        COLOR_ACCENT
    )

    stat_card(
        stats,
        "❤️",
        "PREFERITI",
        str(preferiti),
        "#ff4757"
    )

    stat_card(
        stats,
        "⭐",
        "MEDIA VOTI",
        f"{media:.1f}/5"
        if media else "—",
        "#ffa500"
    )

    stat_card(
        stats,
        "🎮",
        "RECORD",
        str(record),
        COLOR_PURPLE
    )

    # Seconda riga
    stats2 = tk.Frame(
        profilo_content,
        bg=COLOR_BG
    )

    stats2.pack(
        fill="x",
        padx=20,
        pady=10
    )

    stat_card(
        stats2,
        "🏆",
        "ACHIEVEMENT",
        f"{sbloccati}/{totale_achievement}",
        "#ffd700"
    )

    stat_card(
        stats2,
        "⏱️",
        "ORE MARVEL",
        f"{ore}h {minuti}m",
        COLOR_GREEN
    )

    stat_card(
        stats2,
        "🦸",
        "PERSONAGGIO",
        personaggio,
        COLOR_ACCENT
    )

    stat_card(
        stats2,
        "🎞️",
        "FASE PREFERITA",
        fase,
        COLOR_PURPLE
    )

    # Pulsanti
    buttons = tk.Frame(
        profilo_content,
        bg=COLOR_BG
    )

    buttons.pack(
        pady=20
    )

    tk.Button(
        buttons,
        text="🏆 I MIEI ACHIEVEMENT",
        font=FONT_BTN,
        bg="#3b2d00",
        fg="#ffd700",
        bd=0,
        padx=25,
        pady=10,
        cursor="hand2",
        command=mostra_achievement
    ).pack(
        side="left",
        padx=5
    )

    tk.Button(
        buttons,
        text="🎬 VAI AL CINEMA",
        font=FONT_BTN,
        bg=COLOR_ACCENT,
        fg="white",
        bd=0,
        padx=25,
        pady=10,
        cursor="hand2",
        command=apri_cinema
    ).pack(
        side="left",
        padx=5
    )

    profilo_canvas.update_idletasks()

    profilo_canvas.configure(
        scrollregion=profilo_canvas.bbox("all")
    )


# ============================================================
# ACHIEVEMENT PAGE
# ============================================================

frame_achievement = tk.Frame(
    root,
    bg=COLOR_BG
)

achievement_header = tk.Frame(
    frame_achievement,
    bg=COLOR_CARD,
    padx=20,
    pady=12
)

achievement_header.pack(
    fill="x"
)

tk.Button(
    achievement_header,
    text="← PROFILO",
    font=("Segoe UI", 9, "bold"),
    bg=COLOR_CARD_ALT,
    fg=COLOR_TEXT_MUTED,
    bd=0,
    command=mostra_profilo
).pack(
    side="left"
)

tk.Label(
    achievement_header,
    text="🏆 I MIEI ACHIEVEMENT",
    font=FONT_TITOLO,
    fg="#ffd700",
    bg=COLOR_CARD
).pack(
    side="left",
    padx=20
)

achievement_canvas = tk.Canvas(
    frame_achievement,
    bg=COLOR_BG,
    highlightthickness=0
)

achievement_scrollbar = tk.Scrollbar(
    frame_achievement,
    command=achievement_canvas.yview
)

achievement_scrollbar.pack(
    side="right",
    fill="y"
)

achievement_canvas.pack(
    side="left",
    fill="both",
    expand=True
)

achievement_canvas.configure(
    yscrollcommand=achievement_scrollbar.set
)

achievement_content = tk.Frame(
    achievement_canvas,
    bg=COLOR_BG
)

achievement_window = achievement_canvas.create_window(
    (0, 0),
    window=achievement_content,
    anchor="nw"
)


def aggiorna_scroll_achievement(event=None):
    achievement_canvas.configure(
        scrollregion=achievement_canvas.bbox("all")
    )

    achievement_canvas.itemconfig(
        achievement_window,
        width=achievement_canvas.winfo_width()
    )


achievement_content.bind(
    "<Configure>",
    aggiorna_scroll_achievement
)


def mostra_achievement():
    frame_home.pack_forget()
    frame_cinema.pack_forget()
    frame_game.pack_forget()
    frame_profilo.pack_forget()

    frame_achievement.pack(
        fill="both",
        expand=True
    )

    controlla_achievement(
        mostra_popup=False
    )

    for widget in achievement_content.winfo_children():
        widget.destroy()

    dati = database_utenti[
        utente_corrente
    ]

    sbloccati = achievement_sbloccati(
        dati
    )

    totale = len(
        ACHIEVEMENTS
    )

    percentuale = int(
        len(sbloccati) / totale * 100
    ) if totale else 0

    tk.Label(
        achievement_content,
        text=f"{len(sbloccati)} / {totale}",
        font=("Helvetica", 38, "bold"),
        fg="#ffd700",
        bg=COLOR_BG
    ).pack(
        pady=(25, 0)
    )

    tk.Label(
        achievement_content,
        text="ACHIEVEMENT SBLOCCATI",
        font=("Helvetica", 14, "bold"),
        fg="white",
        bg=COLOR_BG
    ).pack()

    tk.Label(
        achievement_content,
        text=f"Progresso: {percentuale}%",
        font=("Segoe UI", 10),
        fg=COLOR_TEXT_MUTED,
        bg=COLOR_BG
    ).pack(
        pady=(5, 20)
    )

    grid = tk.Frame(
        achievement_content,
        bg=COLOR_BG
    )

    grid.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=10
    )

    for indice, (
        key,
        achievement
    ) in enumerate(
        ACHIEVEMENTS.items()
    ):

        sbloccato = (
            key in sbloccati
        )

        riga = indice // 3
        colonna = indice % 3

        if sbloccato:
            bg_card = "#302800"
            bordo = "#ffd700"
            colore_titolo = "#ffd700"
            colore_descrizione = "#eeeeee"
            icona = achievement["icona"]
        else:
            bg_card = COLOR_CARD
            bordo = "#292c3a"
            colore_titolo = "#666b7c"
            colore_descrizione = "#555a70"
            icona = "🔒"

        card = tk.Frame(
            grid,
            bg=bg_card,
            width=330,
            height=160,
            highlightbackground=bordo,
            highlightthickness=2
        )

        card.grid(
            row=riga,
            column=colonna,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        card.grid_propagate(False)

        grid.grid_columnconfigure(
            colonna,
            weight=1
        )

        tk.Label(
            card,
            text=icona,
            font=("Segoe UI Emoji", 30),
            bg=bg_card,
            fg="white"
        ).pack(
            pady=(10, 0)
        )

        tk.Label(
            card,
            text=(
                achievement["nome"]
                if sbloccato
                else "Achievement bloccato"
            ),
            font=("Helvetica", 12, "bold"),
            bg=bg_card,
            fg=colore_titolo
        ).pack()

        tk.Label(
            card,
            text=achievement["descrizione"],
            font=("Segoe UI", 8),
            bg=bg_card,
            fg=colore_descrizione,
            wraplength=280,
            justify="center"
        ).pack(
            pady=5
        )

    achievement_canvas.update_idletasks()

    achievement_canvas.configure(
        scrollregion=achievement_canvas.bbox("all")
    )


# ============================================================
# HOME — FUNZIONE
# ============================================================

def mostra_home():
    frame_login.pack_forget()
    frame_cinema.pack_forget()
    frame_game.pack_forget()
    frame_profilo.pack_forget()
    frame_achievement.pack_forget()

    frame_home.pack(
        fill="both",
        expand=True
    )

    dati = database_utenti[
        utente_corrente
    ]

    controlla_achievement(
        mostra_popup=False
    )

    sbloccati = len(
        achievement_sbloccati(
            dati
        )
    )

    lbl_home_welcome.config(
        text=(
            f"✨ BENVENUTO/A "
            f"{utente_corrente.upper()} ✨\n"
            f"🍿 {len(dati['visti'])}/"
            f"{len(dati_film)} film visti   "
            f"❤️ {len(dati['preferiti'])} preferiti   "
            f"🏆 {sbloccati}/{len(ACHIEVEMENTS)} achievement   "
            f"🎮 Record: "
            f"{dati.get('record_gioco', 0)}"
        )
    )

    root.after(
        100,
        crea_home_particles
    )

    root.after(
        100,
        anima_home
    )


tk.Label(
    home_content,
    text="⚡ IL TUO UNIVERSO. LE TUE REGOLE. ⚡",
    font=("Segoe UI", 9, "bold"),
    fg="#555a70",
    bg=COLOR_BG
).pack(
    pady=(20, 10)
)

frame_home_extra = tk.Frame(
    home_content,
    bg=COLOR_BG
)

frame_home_extra.pack(
    pady=(0, 10)
)

tk.Button(
    frame_home_extra,
    text="📊 IL MIO PROFILO",
    font=("Helvetica", 10, "bold"),
    bg=COLOR_CARD_ALT,
    fg="white",
    bd=0,
    padx=25,
    pady=9,
    cursor="hand2",
    command=mostra_profilo
).pack(
    side="left",
    padx=5
)

tk.Button(
    frame_home_extra,
    text="🏆 ACHIEVEMENT",
    font=("Helvetica", 10, "bold"),
    bg="#3b2d00",
    fg="#ffd700",
    bd=0,
    padx=25,
    pady=9,
    cursor="hand2",
    command=mostra_achievement
).pack(
    side="left",
    padx=5
)

tk.Button(
    home_content,
    text="🚪 Cambia utente",
    font=("Segoe UI", 9, "bold"),
    bg=COLOR_CARD_ALT,
    fg=COLOR_TEXT_MUTED,
    bd=0,
    padx=15,
    pady=7,
    command=mostra_login
).pack()


# ============================================================
# CINEMA
# ============================================================

frame_cinema = tk.Frame(
    root,
    bg=COLOR_BG
)


def torna_home():
    frame_cinema.pack_forget()
    frame_game.pack_forget()
    frame_profilo.pack_forget()
    frame_achievement.pack_forget()

    mostra_home()


header = tk.Frame(
    frame_cinema,
    bg=COLOR_CARD,
    pady=12,
    padx=20
)

header.pack(
    fill="x"
)

tk.Button(
    header,
    text="← HOME",
    font=("Segoe UI", 9, "bold"),
    bg=COLOR_CARD_ALT,
    fg=COLOR_TEXT_MUTED,
    bd=0,
    cursor="hand2",
    command=torna_home
).pack(
    side="left"
)

lbl_benvenuta = tk.Label(
    header,
    text="MARVEL EXPERIENCE",
    font=FONT_TITOLO,
    fg=COLOR_ACCENT,
    bg=COLOR_CARD
)

lbl_benvenuta.pack(
    side="left",
    padx=20
)

lbl_maratona = tk.Label(
    header,
    text="",
    font=("Segoe UI", 10, "bold"),
    fg=COLOR_TEXT_MUTED,
    bg=COLOR_CARD
)

lbl_maratona.pack(
    side="right"
)

frame_contenuto = tk.Frame(
    frame_cinema,
    bg=COLOR_BG
)

frame_contenuto.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=15
)

frame_sinistra = tk.Frame(
    frame_contenuto,
    bg=COLOR_BG
)

frame_sinistra.pack(
    side="left",
    fill="both",
    expand=True
)

frame_ricerca = tk.Frame(
    frame_sinistra,
    bg=COLOR_CARD_ALT,
    padx=8,
    pady=7
)

frame_ricerca.pack(
    fill="x",
    pady=(0, 8)
)

tk.Label(
    frame_ricerca,
    text="🔍",
    bg=COLOR_CARD_ALT,
    fg=COLOR_TEXT_MUTED
).pack(
    side="left"
)

var_ricerca = tk.StringVar()

entry_ricerca = tk.Entry(
    frame_ricerca,
    textvariable=var_ricerca,
    font=FONT_TESTO,
    bg=COLOR_CARD_ALT,
    fg="white",
    insertbackground="white",
    bd=0
)

entry_ricerca.pack(
    side="left",
    fill="x",
    expand=True,
    padx=5
)

frame_controlli = tk.Frame(
    frame_sinistra,
    bg=COLOR_BG
)

frame_controlli.pack(
    fill="x",
    pady=(0, 8)
)

combo_fase = ttk.Combobox(
    frame_controlli,
    state="readonly",
    values=[
        "Tutte le Fasi",
        "❤️ Preferiti",
        "MCU Fase 1",
        "MCU Fase 2",
        "MCU Fase 3",
        "MCU Fase 4",
        "MCU Fase 5",
        "Trilogia Raimi",
        "The Amazing Spider-Man",
        "Sony's Spider-Man Universe",
        "Edizione Speciale 🎁"
    ]
)

combo_fase.set(
    "Tutte le Fasi"
)

combo_fase.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 5)
)

combo_ordine = ttk.Combobox(
    frame_controlli,
    state="readonly",
    values=[
        "Anno (Crescente)",
        "Anno (Decrescente)",
        "Titolo (A-Z)"
    ]
)

combo_ordine.set(
    "Anno (Crescente)"
)

combo_ordine.pack(
    side="right",
    fill="x",
    expand=True
)

lbl_risultati = tk.Label(
    frame_sinistra,
    text="",
    font=("Segoe UI", 9),
    fg=COLOR_TEXT_MUTED,
    bg=COLOR_BG,
    anchor="w"
)

lbl_risultati.pack(
    fill="x",
    pady=(0, 5)
)

frame_lista = tk.Frame(
    frame_sinistra,
    bg=COLOR_BG
)

frame_lista.pack(
    fill="both",
    expand=True
)

scrollbar = tk.Scrollbar(
    frame_lista
)

scrollbar.pack(
    side="right",
    fill="y"
)

listbox_film = tk.Listbox(
    frame_lista,
    font=("Segoe UI", 10, "bold"),
    bg=COLOR_CARD,
    fg="#e0e0e0",
    selectbackground=COLOR_ACCENT,
    selectforeground="white",
    bd=0,
    highlightthickness=0,
    yscrollcommand=scrollbar.set
)

listbox_film.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.config(
    command=listbox_film.yview
)

frame_dettaglio = tk.Frame(
    frame_contenuto,
    bg=COLOR_CARD,
    padx=20,
    pady=15
)

frame_dettaglio.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(15, 0)
)

lbl_titolo_film = tk.Label(
    frame_dettaglio,
    text="Scegli un film dalla lista...",
    font=("Helvetica", 14, "bold"),
    fg="white",
    bg=COLOR_CARD,
    wraplength=420,
    justify="left"
)

lbl_titolo_film.pack(
    fill="x",
    pady=(0, 8)
)

frame_badges = tk.Frame(
    frame_dettaglio,
    bg=COLOR_CARD
)

frame_badges.pack(
    fill="x",
    pady=(0, 8)
)

lbl_badge_fase = tk.Label(
    frame_badges,
    text="",
    font=("Segoe UI", 8, "bold"),
    bg=COLOR_PURPLE,
    fg="white"
)

lbl_badge_fase.pack(
    side="left",
    padx=(0, 5)
)

lbl_badge_anno = tk.Label(
    frame_badges,
    text="",
    font=("Segoe UI", 8, "bold"),
    bg=COLOR_CARD_ALT,
    fg=COLOR_TEXT_MUTED
)

lbl_badge_anno.pack(
    side="left",
    padx=(0, 5)
)

lbl_badge_durata = tk.Label(
    frame_badges,
    text="",
    font=("Segoe UI", 8, "bold"),
    bg=COLOR_CARD_ALT,
    fg=COLOR_TEXT_MUTED
)

lbl_badge_durata.pack(
    side="left"
)

frame_interattivo = tk.Frame(
    frame_dettaglio,
    bg=COLOR_CARD
)

frame_interattivo.pack(
    fill="x",
    pady=(0, 10)
)


def toggle_preferito():
    if not film_selezionato_corrente:
        return

    dati = database_utenti[
        utente_corrente
    ]

    if film_selezionato_corrente in dati["preferiti"]:
        dati["preferiti"].remove(
            film_selezionato_corrente
        )

    else:
        dati["preferiti"].append(
            film_selezionato_corrente
        )

    salva_dati()

    controlla_achievement()

    mostra_dettagli()
    filtra_film()


btn_pref = tk.Button(
    frame_interattivo,
    text="🤍 Preferito",
    font=("Segoe UI", 9, "bold"),
    bg=COLOR_CARD_ALT,
    fg=COLOR_TEXT_MUTED,
    bd=0,
    command=toggle_preferito
)

btn_pref.pack(
    side="left",
    padx=(0, 8)
)


def toggle_visto():
    if not film_selezionato_corrente:
        return

    dati = database_utenti[
        utente_corrente
    ]

    if film_selezionato_corrente in dati["visti"]:
        dati["visti"].remove(
            film_selezionato_corrente
        )

    else:
        dati["visti"].append(
            film_selezionato_corrente
        )

    salva_dati()

    controlla_achievement()

    aggiorna_contatore()
    mostra_dettagli()
    filtra_film()


btn_visto = tk.Button(
    frame_interattivo,
    text="☐ Già Visto",
    font=("Segoe UI", 9, "bold"),
    bg=COLOR_CARD_ALT,
    fg=COLOR_TEXT_MUTED,
    bd=0,
    command=toggle_visto
)

btn_visto.pack(
    side="left",
    padx=(0, 15)
)

btn_stelle = []


def imposta_voto(voto):
    if not film_selezionato_corrente:
        return

    database_utenti[
        utente_corrente
    ]["valutazioni"][
        film_selezionato_corrente
    ] = voto

    salva_dati()

    controlla_achievement()

    aggiorna_stelle(voto)


def aggiorna_stelle(voto):
    for i, btn in enumerate(
        btn_stelle,
        1
    ):
        btn.config(
            text=(
                "★"
                if i <= voto
                else "☆"
            ),
            fg=(
                "#ffa500"
                if i <= voto
                else COLOR_TEXT_MUTED
            )
        )


for i in range(5):
    btn = tk.Button(
        frame_interattivo,
        text="☆",
        font=("Helvetica", 12),
        bg=COLOR_CARD,
        fg=COLOR_TEXT_MUTED,
        bd=0,
        command=lambda voto=i + 1:
        imposta_voto(voto)
    )

    btn.pack(
        side="left"
    )

    btn_stelle.append(
        btn
    )


lbl_info_meta = tk.Label(
    frame_dettaglio,
    text="",
    font=("Segoe UI", 9, "italic"),
    fg=COLOR_TEXT_MUTED,
    bg=COLOR_CARD,
    justify="left",
    anchor="w"
)

lbl_info_meta.pack(
    fill="x",
    pady=(0, 8)
)

tk.Frame(
    frame_dettaglio,
    bg=COLOR_ACCENT,
    height=2
).pack(
    fill="x",
    pady=(0, 10)
)

frame_trama = tk.Frame(
    frame_dettaglio,
    bg=COLOR_CARD
)

frame_trama.pack(
    fill="both",
    expand=True
)

text_trama = tk.Text(
    frame_trama,
    wrap="word",
    font=FONT_TESTO,
    bg=COLOR_CARD,
    fg="#cccccc",
    bd=0,
    highlightthickness=0
)

text_trama.pack(
    fill="both",
    expand=True
)

text_trama.insert(
    tk.END,
    "Seleziona un film a sinistra."
)

text_trama.config(
    state="disabled"
)

btn_trailer = tk.Button(
    frame_dettaglio,
    text="🎬 GUARDA TRAILER SU YOUTUBE",
    font=FONT_BTN,
    bg=COLOR_ACCENT,
    fg="white",
    activebackground=COLOR_ACCENT_HOVER,
    bd=0,
    command=apri_trailer_youtube
)

aggiungi_hover(
    btn_trailer,
    COLOR_ACCENT,
    COLOR_ACCENT_HOVER
)

btn_guarda_ora = tk.Button(
    frame_dettaglio,
    text="🎁 GUARDA IL VIDEO SPECIALE",
    font=FONT_BTN,
    bg=COLOR_PURPLE,
    fg="white",
    activebackground=COLOR_PURPLE_HOVER,
    bd=0,
    command=apri_video_drive
)

aggiungi_hover(
    btn_guarda_ora,
    COLOR_PURPLE,
    COLOR_PURPLE_HOVER
)


def aggiorna_contatore():
    dati = database_utenti[
        utente_corrente
    ]

    totale = len(
        dati_film
    )

    visti = len(
        dati["visti"]
    )

    percentuale = int(
        visti / totale * 100
    ) if totale else 0

    lbl_maratona.config(
        text=(
            f"🍿 {visti}/{totale} "
            f"film ({percentuale}%)"
        )
    )


def filtra_film(*args):
    global titoli_filtrati

    if not utente_corrente:
        return

    query = (
        var_ricerca
        .get()
        .lower()
        .strip()
    )

    fase = combo_fase.get()
    ordine = combo_ordine.get()

    dati = database_utenti[
        utente_corrente
    ]

    titoli = list(
        dati_film.keys()
    )

    if ordine == "Anno (Crescente)":
        titoli.sort(
            key=lambda x:
            dati_film[x]["anno"]
        )

    elif ordine == "Anno (Decrescente)":
        titoli.sort(
            key=lambda x:
            dati_film[x]["anno"],
            reverse=True
        )

    else:
        titoli.sort(
            key=lambda x:
            x.lower()
        )

    listbox_film.delete(
        0,
        tk.END
    )

    titoli_filtrati = []

    for titolo in titoli:

        info = dati_film[
            titolo
        ]

        if fase == "❤️ Preferiti":

            if titolo not in dati["preferiti"]:
                continue

        elif fase != "Tutte le Fasi":

            if info["fase"] != fase:
                continue

        testo = (
            titolo
            + " "
            + str(info["anno"])
            + " "
            + info["fase"]
            + " "
            + info["regia"]
            + " "
            + info["cast"]
            + " "
            + info["trama"]
        ).lower()

        if query not in testo:
            continue

        titoli_filtrati.append(
            titolo
        )

        pref = (
            "❤️ "
            if titolo in dati["preferiti"]
            else ""
        )

        visto = (
            "☑️ "
            if titolo in dati["visti"]
            else ""
        )

        listbox_film.insert(
            tk.END,
            visto
            + pref
            + titolo
        )

    lbl_risultati.config(
        text=(
            f"{len(titoli_filtrati)} "
            f"film trovati"
        )
    )


def mostra_dettagli(event=None):
    global film_selezionato_corrente

    selezione = (
        listbox_film.curselection()
    )

    if not selezione:
        return

    indice = selezione[0]

    if indice >= len(
        titoli_filtrati
    ):
        return

    film_selezionato_corrente = (
        titoli_filtrati[indice]
    )

    info = dati_film[
        film_selezionato_corrente
    ]

    dati = database_utenti[
        utente_corrente
    ]

    lbl_titolo_film.config(
        text=film_selezionato_corrente
    )

    lbl_badge_fase.config(
        text=f" {info['fase']} "
    )

    lbl_badge_anno.config(
        text=f" 🗓️ {info['anno']} "
    )

    lbl_badge_durata.config(
        text=f" ⏱️ {info['durata']} "
    )

    lbl_info_meta.config(
        text=(
            f"🎬 Regia: {info['regia']}\n"
            f"👥 Cast: {info['cast']}"
        )
    )

    text_trama.config(
        state="normal"
    )

    text_trama.delete(
        "1.0",
        tk.END
    )

    text_trama.insert(
        tk.END,
        info["trama"]
    )

    text_trama.config(
        state="disabled"
    )

    if film_selezionato_corrente in dati["preferiti"]:
        btn_pref.config(
            text="❤️ Preferito",
            fg="#ff4757"
        )

    else:
        btn_pref.config(
            text="🤍 Preferito",
            fg=COLOR_TEXT_MUTED
        )

    if film_selezionato_corrente in dati["visti"]:
        btn_visto.config(
            text="☑️ Già Visto",
            fg=COLOR_GREEN
        )

    else:
        btn_visto.config(
            text="☐ Già Visto",
            fg=COLOR_TEXT_MUTED
        )

    voto = dati[
        "valutazioni"
    ].get(
        film_selezionato_corrente,
        0
    )

    aggiorna_stelle(
        voto
    )

    btn_trailer.pack_forget()
    btn_guarda_ora.pack_forget()

    if film_selezionato_corrente == TITOLO_ESCLUSIVO:

        btn_guarda_ora.pack(
            fill="x",
            pady=(10, 0)
        )

    else:

        btn_trailer.pack(
            fill="x",
            pady=(10, 0)
        )


listbox_film.bind(
    "<<ListboxSelect>>",
    mostra_dettagli
)

var_ricerca.trace_add(
    "write",
    filtra_film
)

combo_fase.bind(
    "<<ComboboxSelected>>",
    filtra_film
)

combo_ordine.bind(
    "<<ComboboxSelected>>",
    filtra_film
)


def apri_cinema():
    frame_home.pack_forget()
    frame_game.pack_forget()
    frame_profilo.pack_forget()
    frame_achievement.pack_forget()

    frame_cinema.pack(
        fill="both",
        expand=True
    )

    lbl_benvenuta.config(
        text=(
            f"🎬 CINEMA — "
            f"{utente_corrente.upper()}"
        )
    )

    aggiorna_contatore()
    filtra_film()


# ============================================================
# VIDEOGIOCO
# ============================================================

frame_game = tk.Frame(
    root,
    bg="#05060a"
)

game_header = tk.Frame(
    frame_game,
    bg=COLOR_CARD,
    padx=20,
    pady=10
)

game_header.pack(
    fill="x"
)

tk.Button(
    game_header,
    text="← HOME",
    font=("Segoe UI", 9, "bold"),
    bg=COLOR_CARD_ALT,
    fg=COLOR_TEXT_MUTED,
    bd=0,
    command=torna_home
).pack(
    side="left"
)

tk.Label(
    game_header,
    text="🕷️ MULTIVERSE RUN",
    font=("Helvetica", 19, "bold"),
    fg=COLOR_ACCENT,
    bg=COLOR_CARD
).pack(
    side="left",
    padx=20
)

game_score_label = tk.Label(
    game_header,
    text="PUNTEGGIO: 0",
    font=("Segoe UI", 10, "bold"),
    fg="white",
    bg=COLOR_CARD
)

game_score_label.pack(
    side="right",
    padx=20
)

game_record_label = tk.Label(
    game_header,
    text="RECORD: 0",
    font=("Segoe UI", 10, "bold"),
    fg="#ffa500",
    bg=COLOR_CARD
)

game_record_label.pack(
    side="right"
)

game_canvas = tk.Canvas(
    frame_game,
    bg="#05060a",
    highlightthickness=0
)

game_canvas.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=15
)

game_running = False
game_score = 0
game_lives = 3
game_player_x = 500
game_player_y = 550
game_enemies = []
game_coins = []
game_keys = set()


def aggiorna_game_header():
    game_score_label.config(
        text=f"PUNTEGGIO: {game_score}"
    )

    record = database_utenti[
        utente_corrente
    ].get(
        "record_gioco",
        0
    )

    game_record_label.config(
        text=f"RECORD: {record}"
    )


def disegna_game():
    game_canvas.delete(
        "all"
    )

    w = max(
        game_canvas.winfo_width(),
        1000
    )

    h = max(
        game_canvas.winfo_height(),
        600
    )

    for y in range(
        0,
        h,
        50
    ):
        game_canvas.create_line(
            0,
            y,
            w,
            y,
            fill="#101322"
        )

    random.seed(4)

    for _ in range(80):
        x = random.randint(
            0,
            w
        )

        y = random.randint(
            0,
            h
        )

        game_canvas.create_oval(
            x,
            y,
            x + 2,
            y + 2,
            fill="#30354c",
            outline=""
        )

    game_canvas.create_text(
        w / 2,
        35,
        text="MULTIVERSE RUN",
        font=("Helvetica", 25, "bold"),
        fill=COLOR_ACCENT
    )

    game_canvas.create_text(
        w / 2,
        70,
        text=(
            "Muovi Spider-Man e "
            "raccogli i simboli del multiverso!"
        ),
        font=("Segoe UI", 10),
        fill=COLOR_TEXT_MUTED
    )


def crea_player():
    global game_player_x
    global game_player_y

    w = game_canvas.winfo_width()
    h = game_canvas.winfo_height()

    if w < 500:
        w = 1000

    if h < 400:
        h = 600

    game_player_x = w / 2
    game_player_y = h - 90

    game_canvas.create_oval(
        game_player_x - 28,
        game_player_y - 28,
        game_player_x + 28,
        game_player_y + 28,
        fill="#b00020",
        outline="#ff3340",
        width=3,
        tags="player"
    )

    game_canvas.create_text(
        game_player_x,
        game_player_y,
        text="🕷️",
        font=("Segoe UI Emoji", 24),
        tags="player"
    )


def crea_enemy():
    if not game_running:
        return

    w = game_canvas.winfo_width()

    x = random.randint(
        30,
        max(
            31,
            w - 30
        )
    )

    y = -30

    item = game_canvas.create_oval(
        x - 20,
        y - 20,
        x + 20,
        y + 20,
        fill=COLOR_PURPLE,
        outline="#c77dff",
        width=2
    )

    game_enemies.append([
        item,
        x,
        y,
        random.uniform(3, 6)
    ])

    root.after(
        random.randint(700, 1300),
        crea_enemy
    )


def crea_coin():
    if not game_running:
        return

    w = game_canvas.winfo_width()

    x = random.randint(
        30,
        max(
            31,
            w - 30
        )
    )

    y = -20

    item = game_canvas.create_oval(
        x - 13,
        y - 13,
        x + 13,
        y + 13,
        fill="#ffd700",
        outline="#fff2a8",
        width=2
    )

    game_coins.append([
        item,
        x,
        y,
        random.uniform(3, 5)
    ])

    root.after(
        random.randint(500, 1000),
        crea_coin
    )


def collisione(
    x1,
    y1,
    r1,
    x2,
    y2,
    r2
):
    return (
        (x1 - x2) ** 2
        + (y1 - y2) ** 2
    ) <= (
        r1 + r2
    ) ** 2


def game_loop():
    global game_player_x
    global game_player_y
    global game_score
    global game_lives

    if not game_running:
        return

    w = game_canvas.winfo_width()
    h = game_canvas.winfo_height()

    velocita = 8

    if (
        "Left" in game_keys
        or "a" in game_keys
    ):
        game_player_x -= velocita

    if (
        "Right" in game_keys
        or "d" in game_keys
    ):
        game_player_x += velocita

    if (
        "Up" in game_keys
        or "w" in game_keys
    ):
        game_player_y -= velocita

    if (
        "Down" in game_keys
        or "s" in game_keys
    ):
        game_player_y += velocita

    game_player_x = max(
        30,
        min(
            w - 30,
            game_player_x
        )
    )

    game_player_y = max(
        110,
        min(
            h - 30,
            game_player_y
        )
    )

    game_canvas.coords(
        "player",
        game_player_x - 28,
        game_player_y - 28,
        game_player_x + 28,
        game_player_y + 28
    )

    for enemy in game_enemies[:]:

        item, x, y, speed = enemy

        y += speed

        enemy[2] = y

        game_canvas.move(
            item,
            0,
            speed
        )

        if collisione(
            game_player_x,
            game_player_y,
            28,
            x,
            y,
            20
        ):

            game_canvas.delete(
                item
            )

            game_enemies.remove(
                enemy
            )

            game_lives -= 1

            if game_lives <= 0:
                game_over()
                return

        elif y > h + 50:

            game_canvas.delete(
                item
            )

            game_enemies.remove(
                enemy
            )

    for coin in game_coins[:]:

        item, x, y, speed = coin

        y += speed

        coin[2] = y

        game_canvas.move(
            item,
            0,
            speed
        )

        if collisione(
            game_player_x,
            game_player_y,
            28,
            x,
            y,
            13
        ):

            game_canvas.delete(
                item
            )

            game_coins.remove(
                coin
            )

            game_score += 10

            record = database_utenti[
                utente_corrente
            ].get(
                "record_gioco",
                0
            )

            if game_score > record:

                database_utenti[
                    utente_corrente
                ]["record_gioco"] = (
                    game_score
                )

                salva_dati()

                controlla_achievement()

            aggiorna_game_header()

        elif y > h + 40:

            game_canvas.delete(
                item
            )

            game_coins.remove(
                coin
            )

    game_canvas.delete(
        "lives"
    )

    game_canvas.create_text(
        80,
        105,
        text=f"❤️ VITE: {game_lives}",
        font=("Segoe UI", 12, "bold"),
        fill="#ff4757",
        tags="lives"
    )

    root.after(
        30,
        game_loop
    )


def game_key_down(event):
    game_keys.add(
        event.keysym
    )


def game_key_up(event):
    game_keys.discard(
        event.keysym
    )


root.bind(
    "<KeyPress>",
    game_key_down
)

root.bind(
    "<KeyRelease>",
    game_key_up
)


def game_over():
    global game_running

    game_running = False

    record = database_utenti[
        utente_corrente
    ].get(
        "record_gioco",
        0
    )

    game_canvas.create_rectangle(
        0,
        0,
        game_canvas.winfo_width(),
        game_canvas.winfo_height(),
        fill="#000000",
        stipple="gray50",
        outline=""
    )

    game_canvas.create_text(
        game_canvas.winfo_width() / 2,
        game_canvas.winfo_height() / 2 - 80,
        text="GAME OVER",
        font=("Helvetica", 45, "bold"),
        fill=COLOR_ACCENT
    )

    game_canvas.create_text(
        game_canvas.winfo_width() / 2,
        game_canvas.winfo_height() / 2 - 20,
        text=f"Punteggio: {game_score}",
        font=("Helvetica", 20, "bold"),
        fill="white"
    )

    game_canvas.create_text(
        game_canvas.winfo_width() / 2,
        game_canvas.winfo_height() / 2 + 20,
        text=f"🏆 Record: {record}",
        font=("Helvetica", 16, "bold"),
        fill="#ffd700"
    )

    btn_restart.place(
        relx=.5,
        rely=.65,
        anchor="center"
    )


btn_restart = tk.Button(
    frame_game,
    text="🔄 RIGIOCA",
    font=FONT_BTN,
    bg=COLOR_ACCENT,
    fg="white",
    bd=0,
    padx=35,
    pady=10,
    command=lambda: avvia_gioco()
)


def avvia_gioco():
    global game_running
    global game_score
    global game_lives
    global game_enemies
    global game_coins

    btn_restart.place_forget()

    game_running = False

    for enemy in game_enemies:
        game_canvas.delete(
            enemy[0]
        )

    for coin in game_coins:
        game_canvas.delete(
            coin[0]
        )

    game_enemies.clear()
    game_coins.clear()

    game_score = 0
    game_lives = 3

    game_canvas.delete(
        "all"
    )

    disegna_game()
    crea_player()

    game_running = True

    aggiorna_game_header()

    root.after(
        500,
        crea_enemy
    )

    root.after(
        700,
        crea_coin
    )

    root.after(
        100,
        game_loop
    )


def apri_gioco():
    frame_home.pack_forget()
    frame_cinema.pack_forget()
    frame_profilo.pack_forget()
    frame_achievement.pack_forget()

    frame_game.pack(
        fill="both",
        expand=True
    )

    aggiorna_game_header()
    avvia_gioco()


# ============================================================
# AVVIO
# ============================================================

carica_dati()

frame_login.pack_forget()
frame_home.pack_forget()
frame_cinema.pack_forget()
frame_game.pack_forget()
frame_profilo.pack_forget()
frame_achievement.pack_forget()

avvia_loading()

root.mainloop()

















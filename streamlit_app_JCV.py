### PROYECTO VISUALIZACION DE DATOS
### Jaime Camacho Vazquez

##################################################

# Carga de librerías
import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
import plotly.express as px

# Título de la página
st.set_page_config(page_title="Guía NBA temporada 22-23",
                   page_icon=":basketball:",
                   layout="wide",
                   menu_items={
                       'Report a bug': "https://www.instagram.com/jaimecamacho_/",
                       'Get help': "https://www.linkedin.com/in/jaime-camacho-v%C3%A1zquez-353571236/",
                       'About':
                           '''
                            Muchas gracias por usar la aplicación.
                            
                            Espero que te haya gustado mucho. Por favor, si
                            encuentras algún error, no dudes en decírmelo.
                            Tienes mis contactos en "Report a bug" y en "Get help"
                            '''
                   }
                   )

### CARGA DE DATOS

jugadores = pd.read_csv(
    r"C:\Users\jaime\OneDrive\Escritorio\Loyola\Visualizacióndedatos\Entrega 2\STREAMLIT-20221129\STREAMLIT\Jugadores.csv",
    encoding='latin1', sep=";")
# st.write(jugadores)
jugadores = jugadores.drop(["Rk", "GS", "FG", "FGA", "eFG%", "FT", "FTA", "ORB", "DRB","PF"], axis=1)
jugadores.rename(columns={"Player":"Player Name","Pos": "Posición", "Age": "Edad",
                          "Tm": "Equipo", "G": "Partidos",
                          "MP": "Minutos", "3PA": "3P.I",
                          "2PA": "2P.I", "FT%": "TL%", "TRB": "RB", "STL": "Robos",
                          "BLK": "Tapones", "TOV": "Pérdidas"},
                 inplace=True)
jugadores = jugadores.replace({"TOR": "Toronto Raptors", "MEM": "Memphis Grizzlies","GSW":"Golden State Warriors","CHO":"Charlot Hornets","SAS":"San Antonio Spurs",
"MIA": "Miami Heat", "UTA": "Utah Jazz","NYK":"New York Nicks","WAS":"Washington Wizards","PHO":"Phoenix Suns","DET":"Detroit Pistons",
"MIL": "Milwaukee Bucks","CLE":"Cleveland Cavaliers","NOP":"New Orleans Pelicans","MIN":"Minnesota Timberwolves","ORL":"Orlando Magic",
"SAC":"Sacramento Kings","LAC":"Los Angeles Clippers","OKC":"Oklahoma City Thunder","DAL":"Dallas Maveriks","LAL":"Los Angeles Lakers",
"IND":"Indiana Pacers","ATL":"Atlanta Hawks","CHI":"Chicago Bulls","DEN":"Denver Nuggets","BOS":"Boston Celtics","POR":"Portland Trail Blazers","HOU":"Houston Rockets",
"BRK":"Brooklyn Nets","PHI":"Philadelphia 76ers",
"C":"Pívot","PF":"Ala-Pívot","SG":"Escolta","SF":"Alero","PG":"Base"
})
def redondeo(x):
    return int(x)
def porcentaje(y):
    return y*100
jugadores["Minutos"] = jugadores["Minutos"].apply(redondeo)
jugadores["FG%"] = jugadores["FG%"].apply(porcentaje)
jugadores["FG%"] = jugadores["FG%"].apply(redondeo)
jugadores["3P"] = jugadores["3P"].apply(redondeo)
jugadores["3P.I"] = jugadores["3P.I"].apply(redondeo)
jugadores["3P%"] = jugadores["3P%"].apply(porcentaje)
jugadores["3P%"] = jugadores["3P%"].apply(redondeo)
jugadores["2P"] = jugadores["2P"].apply(redondeo)
jugadores["2P.I"] = jugadores["2P.I"].apply(redondeo)
jugadores["2P%"] = jugadores["2P%"].apply(porcentaje)
jugadores["2P%"] = jugadores["2P%"].apply(redondeo)
jugadores["TL%"] = jugadores["TL%"].apply(porcentaje)
jugadores["TL%"] = jugadores["TL%"].apply(redondeo)
jugadores["RB"] = jugadores["RB"].apply(redondeo)
jugadores["AST"] = jugadores["AST"].apply(redondeo)
jugadores["Robos"] = jugadores["Robos"].apply(redondeo)
jugadores["Tapones"] = jugadores["Tapones"].apply(redondeo)
jugadores["Pérdidas"] = jugadores["Pérdidas"].apply(redondeo)
jugadores["PTS"] = jugadores["PTS"].apply(redondeo)

equipos = pd.read_csv(
    r"C:\Users\jaime\OneDrive\Escritorio\Loyola\Visualizacióndedatos\Entrega 2\STREAMLIT-20221129\STREAMLIT\Equipos.csv",
    encoding='latin1', sep=",")
# Eliminamos columnas
equipos = equipos.drop(["LEAGUE_ID", "TEAM_ID"], axis=1)
# Añadimos estado de cada equipo
estados = ["Georgia", "Massachusetts", "Louisiana", "Illinois", "Texas", "Colorado", "Texas", "California",
           "California", "Florida", "Wisconsin", "Minnesota", "New York", "New York", "Florida", "Indiana",
           "Pennsylvania", "Arizona", "Oregon", "California", "Texas", "Oklahoma", "New York", "Utah", "Tennessee",
           "Washington", "Michigan", "North Carolina", "Ohio", "California"]
equipos["State Name"] = estados
# st.write(equipos)

data_estados = pd.read_csv(
    r"C:\Users\jaime\OneDrive\Escritorio\Loyola\Visualizacióndedatos\Entrega 2\STREAMLIT-20221129\STREAMLIT\Estados_frecuencia.csv",
    encoding='latin1', sep=";")


# st.write(data_estados)


# Definición de la función para meter gifts
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


nba_logo = load_lottiefile("nbalogo.json")
jugador_baloncesto = load_lottiefile("basketball1.json")
morty_dancer = load_lottiefile("morty-dancer.json")

# Configuración menú de la izquierda
with st.sidebar:
    selected = option_menu(
        menu_title="Menú principal",
        options=["Introducción", "Historia de la NBA", "Franquicias", "Jugadores",
                 "Desarrollo de la página"],
        icons=["bookmarks", "inboxes-fill", "globe2", "people-fill", "gear-fill"],
        menu_icon="cast",
        default_index=0
    )

#### INTRODUCCIÓN
# Configuracion de la pagina para titulo y subtitulo
if selected == "Introducción":
    APP_TITLE = "Guía NBA Temporada 2022-2023"
    APP_SUBTITLE = "Todo lo que debes saber sobre la mejor liga de baloncesto del mundo"

    st.title(APP_TITLE)
    st.subheader(APP_SUBTITLE)
    st_lottie(
        nba_logo,
        speed=1,
        reverse=False,
        loop=True,
    )
    st.audio("XGS Lets get ready to Rumble  Jock Jams.mp3")
    st.header("Introducción")
    st.write(
        "La National Basketball Association, más conocida simplemente por sus siglas NBA, es una liga privada de baloncesto profesional que se disputa en Estados Unidos desde 1949, cuando se fusionaron las ligas profesionales National Basketball League (NBL, creada en 1937) y la Basketball Association of America (BAA, fundada en 1946).")

    st.image("Imagen_inicio.jpg", caption="Madison Square Garden en un partido", width=800)

    st.subheader("Sistema de competición")

    st.write(
        """
        En la temporada regular cada equipo disputa 82 partidos, divididos en partes iguales entre encuentros de local y visitante. El calendario no es el mismo para todos. Los equipos se enfrentan con los oponentes de su propia división en cuatro ocasiones; ante los de las otras dos divisiones de su conferencia, entre tres o cuatro veces; 
        y contra los de la otra conferencia, dos veces al año.
        """
    )

    st.write(
        """
        En febrero, la NBA se interrumpe para celebrar el anual All-Star Game.
        Los entrenadores que mejor balance victorias-derrotas llevan con su equipo hasta febrero son los encargados de dirigir al equipo de su conferencia, y no pueden dirigir en años consecutivos. 
        El Oeste y el Este se enfrentan, y el jugador que mejor actuación haya realizado durante el encuentro será galardonado con el premio MVP del All-Star. Otra de las atracciones del fin de semana 
        de las estrellas es el partido entre los rookies (novatos) y los sophomores (jugadores de segundo año), y los concursos de triples, de mates y de habilidades.
        
        """
    )

    st.image("concurso-mates.jpg",
             caption="Derrick Jones Jr con el mate que le proclama ganador en el All Star de 2020", width=800)

    st.write(
        """
        Los Playoffs de la NBA consiste en cuatro rondas de competición entre dieciséis equipos repartidos en la Conferencia Oeste y la Conferencia Este, ocho equipos por cada Conferencia. Los ganadores de la Primera Ronda (o cuartos de final de conferencia)
         avanzan a las Semifinales de Conferencia, posteriormente a las Finales de Conferencia y los vencedores a las Finales de la NBA, disputadas entre los campeones de cada conferencia.
        
        Las series de playoffs siguen un formato de competición. Cada eliminatoria es al mejor de siete partidos, avanzando de serie el primero que gane cuatro partidos, mientras que el perdedor es eliminado de los playoffs.
        """
    )

    st.image("campeon-nba.jpg", caption="Klay Thompson y Stephen Curry en la celebración de campeones de 2022",
             width=800)

### HISTORIA DE LA NBA
if selected == "Historia de la NBA":
    st.header("Historia de la NBA")
    st.subheader("Primeros inicios")

    st.write(
        """
    La Basketball Association of America (BAA) fue fundada en 1946 por propietarios de los principales pabellones
    deportivos del noreste y medio-oeste, como el Madison Square Garden de Nueva York. Los 11 equipos que abrieron el telón en la temporada 
    inaugural 1946-47 fueron Boston Celtics, Philadelphia Warriors, New York Knicks, Washington Capitols, Providence Steamrollers, Toronto Huskies, 
    Chicago Stags, St. Louis Bombers, Cleveland Rebels, Detroit Falcons y Pittsburgh Ironmen.
    """
    )
    st.write(
        """Únicamente tres de esos equipos han perdurado hasta nuestros días: 
    Boston Celtics, New York Knicks y Golden State Warriors siendo por tanto los únicos que han disputado todas las temporadas de la liga desde su fundación. De ellos, tan solo Boston Celtics y New York Knicks no se han 
    movido de ciudad siendo considerados por estos motivos como dos de los equipos más representativos e históricos de la liga. En cambio, los Warriors nacieron en Filadelfia, para mudarse en 1962 a San Francisco y en 1971 a Oakland,
    lugar que han ocupado hasta 2019, año 
    en el que se volvieron a trasladar a San Francisco.
    """
    )

    st.image("primer-partido-nba.png",
             caption="Primer partido de la historia de la NBA el 1 de noviembre de 1946, entre los Toronto Huskies y los New York Knickerbockers",
             width=800)

    st.subheader("Años dorados de la NBA")
    st.write(
        """
    En la temporada 1979-80, la NBA agregó de la ABA la innovadora línea de tres puntos.16​ Esa temporada, entrarían en la liga los rookies 
    Magic Johnson y Larry Bird, para jugar en los Lakers y Celtics respectivamente,
    y se dio comienzo a un periodo en el que el interés por la liga y el número de aficionados creció tanto en el país como en el mundo entero. 
    La preciosa rivalidad que mantenían estos dos jugadores fue, como muchos dicen, uno de los salvadores de la liga, que parecía que empezaba a vagar sin rumbo antes de sus llegadas.
    """
    )
    st.write(
        "En 1984, Michael Jordan empezó a jugar en la NBA, provocando un mayor interés en la liga. En 1989, el número de equipos se elevaba ya a 27, siguiendo el proceso de expansión.")

    st.image("años-dorados.jpg", caption="Larry Bird, Michael Jordan y Magic Jhonson, integrantes del Dream Team",
             width=800)

    st.write(
        """
        En los Juegos Olímpicos de Barcelona de 1992 se vio al que está considerado mejor equipo de la historia del baloncesto de selecciones, el popular 'Dream Team' de Estados Unidos, que contaba por primera vez con jugadores NBA,
        con estrellas como Michael Jordan, Larry Bird, Magic Johnson, Scottie Pippen, Charles Barkley o John Stockton. En esta década, un elevado número de jugadores comenzó a llegar de otros países. Al principio, esos jugadores, 
        como Hakeem Olajuwon (Jugador más valioso en 1994) de Nigeria, primero jugaban en la NCAA para perfeccionar sus habilidades.
        
        """
    )
    st.write(
        """
        Ahora, un número creciente de jugadores llega a la NBA directamente desde Europa o cualquier otra parte del mundo, 
        casos como Yao Ming (número 1 del draft de 2002) de China, o los 'All-Star' Dirk Nowitzki (Alemania, además de ser el MVP de la temporada en 2007), Tony Parker (Francia), Manu Ginobili (Argentina) y Pau Gasol (Rookie del año en 2002) de España. 
        A día de hoy, los jóvenes jugadores de habla inglesa suelen enrolarse en universidades estadounidenses antes de empezar a jugar en la NBA, como por ejemplo, el australiano Andrew Bogut (número 1 del draft de 2005) y el canadiense Steve Nash (MVP de la temporada en 2005 y 2006),
        mientras que otros jugadores internacionales llegan procedentes de equipos profesionales de sus respectivos países.
        """
    )

    st.subheader("Actualidad")

    st.write(
        """
        El 1 de julio de 2011, a las 12:01 del mediodía, la NBA anunció un cierre patronal. Después de que las primeras semanas de la temporada fueran canceladas, los jugadores y los dueños ratificaron un nuevo convenio colectivo el 8 de diciembre de 2011 estableciendo una temporada acortada de 66 partidos, por los 82 que se juegan regularmente.

        Después del recorte y la temporada regular, los Miami Heat regresaron a las finales con el trío formado por Dwyane Wade, LeBron James y Chris Bosh quienes se enfrentaron al formado por Kevin Durant, Russell Westbrook y James Harden de los Oklahoma City Thunder. El equipo de Florida consiguió vencer en cinco partidos, conquistando su segundo título 
        de la NBA en seis años. Su éxito continuó en la siguiente temporada, venciendo sobre los San Antonio Spurs en 2013, reeditando la final un año después que esta vez se decantó del lado de los texanos tras cinco partidos. 
   
        """
    )

    st.image("finales-2012.jpg", caption="Lebron James y Kevin Durant disputando las finales de 2012", width=800)

    st.write(

        """ 
    Después de esa serie, LeBron James anunció que volvería a sus originarios Cleveland Cavaliers. James lideró al equipo de su estado natal a 
    la segunda aparición de su historia en las finales, donde cayeron frente a los Golden State Warriors de Stephen Curry en seis partidos. Con Curry a la cabeza los Warriors volverían a la final en la temporada 2016, pero esta vez vencerían los Cavaliers ganando su primer campeonato de la NBA, tras necesitar jugarse un séptimo partido y siendo la primera vez 
    que un equipo da vuelta un 3-1 adverso en las finales. Cabe destacar en esa temporada, el récord de 73-9 que lograron los californianos, dejando atrás a los míticos Bulls de Jordan y su récord de 72-10, en ambos casos con participación de Steve Kerr, primero en cancha con los Bulls y luego como entrenador de los Warriors. Así mismo, para la temporada 2017 
    también se repitió la final, demostrando la hegemonía alcanzada por Golden State y Cleveland en las últimas tres temporadas, en donde los de Oakland, liderados por un gran Curry y un decisivo Kevin Durant, ganarían la final en el quinto partido, tras doblegar sin mayores complicaciones a los de Ohio. En 2018 Golden State Warriors volvió a superar a Cleveland Cavaliers, 
    esta vez con un rotundo 4-0. Sin embargo, en 2019, Toronto Raptors se convirtió en el primer equipo no estadounidense en ganar un título de la NBA a superar a Golden State Warriors.
    """
    )

    st.image("actualidad.jpg", caption="Icónico tapón de Lebron James a Iguoadala en las Finales de 2016", width=800)

    st.write(
        """
        La temporada 2019-2020 estuvo afectada por la pandemia mundial del COVID-19, y fue cancelada en marzo después de que varios jugadores dieron positivo por el virus. La NBA buscó maneras de volver a la competición el 30 de julio,
        con un torneo para finalizar la temporada en Orlando, Florida.28​ Finalmente, los Lakers de LeBron James ganaron el anillo frente a Miami Heat.
    """)

### FRANQUICIAS
if selected == "Franquicias":

    st.header("Franquicias de la NBA")
    st.write(
        """
        Desde 2004, la NBA está conformada por 30 franquicias y sigue desarrollándose como una de las principales ligas deportivas del mundo.
        De ellos, un total de 29 se encuentran localizados en Estados Unidos y solamente uno se encuentra en Canadá. 
        Desde su nacimiento se han producido un total de once expansiones para albergar a dieciocho nuevos equipos.
        """
    )

    st.write(
        """
        La organización actual de la liga divide a los equipos en dos conferencias —la Oeste y la Este— de tres divisiones cada una, las cuales constan a su vez de cinco equipos. La división territorial actual fue introducida en la temporada 2004-05.
        Reflejando la distribución de la población de los Estados Unidos y de Canadá en conjunto, la mayoría de los equipos están en la mitad del este del país: trece equipos están en la zona horaria del este, nueve en la zona central, tres en la zona horaria montañosa, y cinco en la Pacífico.

        El comisionado se encarga de que haya el mismo número de franquicias en cada conferencia para mantener una división equivalente. En los casos en los que se produce una reubicación de franquicia, el mapa divisional se reestructura para que cada división cuente con los cinco equipos del cupo.
        """
    )

    map = folium.Map(location=[38, -95.0], zoom_start=4, scrollWheelZoom=False, tiles="CartoDB positron")

    choropleth = folium.Choropleth(
        geo_data=r"C:\Users\jaime\OneDrive\Escritorio\Loyola\Visualizacióndedatos\Entrega 2\STREAMLIT-20221129\STREAMLIT\us-state-boundaries.geojson",
        data=data_estados,
        columns=("State Name", "Frecuencia"),
        key_on="feature.properties.name",
        line_opacity=0.8,
        highlight=True
    )
    choropleth.geojson.add_to(map)

    data_estados = data_estados.set_index("State Name")

    for feature in choropleth.geojson.data["features"]:
        state_name2 = feature["properties"]["name"]
        feature["properties"]["population"] = "Equipos: " + str((data_estados.loc[state_name2, "Equipos"]))

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(["name", "population"], labels=False)
    )

    st_map = st_folium(map, width=900, height=600)

    st.markdown("---")

    st.header("Equipos por conferencias")
    c1, c2 = st.columns([5,5])
    c1.markdown("#### Conferencia Oeste: ")
    c1.markdown("""
    Los Angeles Lakers
    
    Los Angeles Clippers
    
    Golden State Warriors
    
    Memphis Grizzlies
    
    Dallas Mavericks
    
    Portland Trail Blazers
    
    Phoenix Suns
    
    Denver Nuggets
    
    Utah Jazz
    
    Sacramento Kings
    
    New Orleans Pelicans
    
    Houston Rockets
    
    Minnesota Timberwolves
    
    Oklahoma City Thunder
    
    Sacramento Kings
"""
                )
    c2.markdown("#### Conferencia Este: ")
    c2.markdown("""
    Bolton Celtics
    
    Milwaukee Bucks
    
    Cleveland Cavaliers
    
    Brooklyn Nets
    
    New York Knicks
    
    Philadelphia 76ers
    
    Chicago Bulls
    
    Miami Heat
    
    Toronto Raptors
    
    Atlanta Hawks
    
    Indiana Pacers
    
    Detroit Pistons
    
    Washington Wizards
    
    Charlotte Hornets
    
    Orlango Magic
    
"""
                )

    st.markdown("---")
    st.header("Estadísticas por equipo")

    st.write("""
       Las estadísticas en la NBA toman un papel importantísimo, ya que el rendimiento de cada jugador puede verse reflejado en los datos.

       Aquí abajo, podrás elegir la estadística que quieres mostrar de cada jugador de cualquier equipo.      
                """)


    def interactive_plot(dataframe):
        x_axis = st.selectbox("Selecciona el equipo", options=dataframe["Equipo"].unique())
        gk = jugadores.groupby("Equipo")
        y_axis = st.selectbox("Estadística que quieres mostrar",
                              options=["Edad", "Partidos", "Minutos", "FG%", "3P", "3P%", "3P.I", "2P", "2P%", "2P.I",
                                       "TL%", "RB", "AST", "Tapones", "Pérdidas", "PTS"])

        plot = px.bar(dataframe, x=gk.get_group(x_axis)["Player Name"], y=gk.get_group(x_axis)[y_axis],
                      color_discrete_sequence=["#00CC96"] * len(dataframe))
        st.plotly_chart(plot)


    interactive_plot(jugadores)

#### JUGADORES
if selected == "Jugadores":
    st.title("Jugadores")
    st.header("Estadísticas individuales")
    st.write("""
    Si la NBA es tan conocida a nivel mundial es por sus jugadores, los cuales son auténticas estrellas. Acumulan millones de seguidores en redes sociales y son ídolos
    para muchas personas. 
    
    Pero aún siendo tan mediáticos, deben competir durante toda la temporada en el máximo nivel. Están en la lupa de todo el mundo y trabajan para sobresalir en la pista.
    
    Aquí podemos ver las estadísticas de tu jugador favorito.
    """
             )
    jugador = st.text_input("Escribe abajo el nombre del jugador:")
    st.write(jugadores[jugadores["Player Name"] == jugador])

    st.markdown("---")

    # DASHBOARD
    st.sidebar.header("Filtra aquí:")
    equipo_dashboard = st.sidebar.multiselect(
        "Selecciona el equipo",
        options=jugadores["Equipo"].unique(),
        default=[]
    )
    posiciones_dashboard = st.sidebar.multiselect(
        "Selecciona la posición",
        options=jugadores["Posición"].unique(),
        default=[]
    )
    jugadores_selection = jugadores.query(
        "Equipo == @equipo_dashboard & Posición == @posiciones_dashboard"
    )

    st.header("Estadísticas grupales")
    st.write("""
    También es importante el nivel que tiene cada equipo por posición en el campo. Por tanto, es necesario, observar las estadísticas conjuntas de cada grupo de
    jugadores que se encuentran en la misma posición por franquicia.
    """)
    st.dataframe(jugadores_selection, width=1500)


    ### Cabecera de abajo
    st.title(":bar_chart: Porcentajes")
    st.markdown("##")

    media_edad = round(jugadores_selection["Edad"].mean(),1)
    media_puntos = round(jugadores_selection["PTS"].mean(),1)
    media_porcentaje = round(jugadores_selection["FG%"].mean(),1)
    left_column, middle_column, right_column = st.columns([2,3,5])
    with left_column:
        st.subheader("Edad media:")
        st.subheader(media_edad)
    with middle_column:
        st.subheader("Media de puntos:")
        st.subheader(media_puntos)
    with right_column:
        st.subheader("Porcentaje medio de anotación:")
        st.subheader(str(media_porcentaje) + "%")
    c3, c4 = st.columns([7,3])
    figura1 = px.bar(
        jugadores_selection,
        x="PTS",
        y=jugadores_selection["Player Name"],
        orientation="h",
        title="<b>Puntos de cada jugador</b>",
        color_discrete_sequence=["#00CC96"] * len(jugadores_selection),
        template="plotly_white"
    )

    with c3:
        st.plotly_chart(figura1)

    with c4:
        st_lottie(
            jugador_baloncesto,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",
            height=400
        )
    st.markdown("---")
    st.audio("tomp3.cc - Shakira Ozuna  Monotonía LetraLyrics.mp3", start_time=7)
    st_lottie(
        morty_dancer,
        speed=1,
        reverse=False,
        loop=True,
        height=350
    )


#### DESARROLLO DE LA PÁGINA
if selected == "Desarrollo de la página":
    st.title("Desarrollo de la página")
    st.header("Explicación de las variables")
    c6,c7 = st.columns([5,5])
    with c6:
        st.write("""
        - Player Name: Nombre del jugador.
        - Posición: Posición del jugador en cuestión.
        - Edad: Edad del jugador.
        - Equipo: Equipo del jugador.
        - Partidos: Partidos jugados en lo que va de temporada.
        - Minutos: Minutos por partido.
        - FG%: Porcentaje de tiros anotados.
        - 3P: Triples anotados por partido.
        - 3P.I: Triples intentados por partido. 
        - 3P%: Porcentaje de triples anotados.
        """)
    with c7:
        st.write("""
        - 2P: Tiros de dos puntos anotados por partido.
        - 2P.I: Tiros de dos puntos intentados por partido. 
        - 2P%: Porcentaje de tiros de dos puntos anotados. 
        - TL%: Porcentaje de tiros libres anotados.
        - RB: Rebotes por partido.
        - AST: Asistencias por partido.
        - Robos: Robos por partido.
        - Tapones: Tapones por partido.
        - Pérdidas: Pérdidas por partido.
        - PTS: Puntos por partido. 
""")
    st.markdown("---")
    st.header(":books: Creador de la página")
    st.write("Soy Jaime Camacho Vázquez, estudiante de 22 años del máster de 'Data Analytics' en la Universidad Loyola, en Sevilla. Graduado en Matemáticas, y con una gran afición por los deportes, en especial, el fútbol, el boxeo y por supuesto el baloncesto. Mis redes sociales y contactos varios están proporcionados un poco más abajo.")
    st.write("""
                Esta página es el resultado de un proyecto en la asignatura 'Visualización de datos', del máster que estoy cursando. Aquí, se nos invitaba a realizar una página web sobre un tema en el que tuviéramos un especial interés. 
             
                Querría agradecer en primer lugar al profesor Manuel Podadera, principal culpable de que se pudiéramos realizar este trabajo. Y, por último, pero no menos importante a mis compañeros, en especial a Javier Vázquez, que ha sido de gran ayuda en la aportación de ideas.
              
                ¡Muchas gracias!
    
    """)
             
    st.image("jaime.jfif",width=300)

    st.header(":link: Redes sociales")
    st.write("Instagram: https://www.instagram.com/jaimecamacho_/")
    st.write("Linkedin: https://www.linkedin.com/in/jaime-camacho-v%C3%A1zquez-353571236/")
    st.markdown("---")

    st.header(":mailbox: ¡Ponte en contacto conmigo!")
    st.write("""
       Esta página está en constante evolución y abierta a todo tipo de cambios y sugerencias. Si usted tiene una propuesta de valor y quiere contribuir con el trabajo, no dude en comentarlo justo abajo.

       Sería de gran ayuda.
    """
             )
    # Cuerpo para mandar el correo
    contact_form = """
    <form action="https://formsubmit.co/jcamachovazquez@al.uloyola.es" method="POST">
        <input type="hidden" name "_captcha" value="false">
        <input type="text" name="name" placeholder="Tu nombre" required>
        <input type="email" name="email" placeholder="Tu email" required>
        <textarea name="message" placeholder="Deja aquí tu mensaje"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)


    # Usamos el local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")

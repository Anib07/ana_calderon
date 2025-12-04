# populate_sqlite.py
import sqlite3
from datetime import datetime

DB_FILE = "ani_trivia.db"

# Conexión a SQLite
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# --- Crear tablas ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    score INTEGER,
    category TEXT,
    difficulty TEXT,
    date_played TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    difficulty TEXT,
    question TEXT,
    option1 TEXT,
    option2 TEXT,
    option3 TEXT,
    option4 TEXT,
    correct_option INTEGER
)
""")

# --- Lista de preguntas ---
questions = [
    # Historia - Fácil
    ("Historia","Fácil","¿En qué año llegó Cristóbal Colón a América?","1492","1500","1485","1510",1),
    ("Historia","Fácil","¿Quién fue el primer presidente de los Estados Unidos?","George Washington","Abraham Lincoln","Thomas Jefferson","John Adams",1),
    ("Historia","Fácil","¿Qué civilización construyó las pirámides de Egipto?","Griega","Romana","Egipcia","Maya",3),
    ("Historia","Fácil","¿En qué país nació Napoleón Bonaparte?","Francia","Italia","España","Córcega",4),
    ("Historia","Fácil","¿Cómo se llamaba el barco en el que viajó Colón en su primer viaje?","La Pinta","La Niña","La Santa María","El Mayflower",3),
    ("Historia","Fácil","¿Qué guerra terminó en 1945?","Primera Guerra Mundial","Guerra Civil Española","Segunda Guerra Mundial","Guerra Fría",3),
    ("Historia","Fácil","¿Quién pintó la Última Cena durante el Renacimiento?","Miguel Ángel","Leonardo da Vinci","Rafael","Donatello",2),
    ("Historia","Fácil","¿Cuál era la capital del Imperio Romano?","Roma","Atenas","París","Constantinopla",1),
    ("Historia","Fácil","¿Qué pueblo indígena habitaba el actual territorio de Paraguay antes de la llegada de los españoles?","Mapuches","Guaraníes","Incas","Mayas",2),

    # Historia - Medio
    ("Historia","Medio","¿En qué año comenzó la Primera Guerra Mundial?","1910","1914","1918","1920",2),
    ("Historia","Medio","¿Quién fue el emperador romano durante la crucifixión de Jesús?","Augusto","Nerón","Tiberio","César",3),
    ("Historia","Medio","¿Qué tratado puso fin a la Primera Guerra Mundial?","Tratado de Roma","Tratado de París","Tratado de Versalles","Tratado de Viena",3),
    ("Historia","Medio","¿Qué país fue el primero en abolir la esclavitud?","Francia","Inglaterra","Haití","España",3),
    ("Historia","Medio","¿En qué año se declaró la independencia de Paraguay?","1810","1811","1821","1825",2),
    ("Historia","Medio","¿Qué emperador ordenó construir la Gran Muralla China?","Confucio","Qin Shi Huang","Mao Zedong","Sun Tzu",2),
    ("Historia","Medio","¿Qué líder sudafricano luchó contra el apartheid y se convirtió en presidente?","Desmond Tutu","Nelson Mandela","Jacob Zuma","Steve Biko",2),
    ("Historia","Medio","¿Qué evento dio inicio a la Segunda Guerra Mundial?","Invasión a Polonia","Ataque a Pearl Harbor","Firma del Pacto de Varsovia","Guerra Civil Española",1),
    ("Historia","Medio","¿Qué invento revolucionó la impresión en el siglo XV?","La brújula","La imprenta","El telescopio","El reloj",2),
    ("Historia","Medio","¿Qué país descubrió Vasco da Gama al llegar a Asia por mar?","India","China","Japón","Filipinas",1),
    ("Historia","Medio","¿Qué dinastía gobernó China durante el siglo XV?","Ming","Han","Tang","Qing",1),
    ("Historia","Medio","¿Quién fue el último zar de Rusia?","Nicolás I","Nicolás II","Alejandro III","Iván IV",2),
    ("Historia","Medio","¿Cuál fue la capital del Imperio Bizantino?","Roma","Constantinopla","Atenas","Alejandría",2),
    ("Historia","Medio","¿Qué civilización desarrolló el calendario solar más preciso de la antigüedad?","Egipcia","Azteca","Maya","Inca",3),

    # Historia - Difícil
    ("Historia","Difícil","¿En qué año cayó el Imperio Romano de Occidente?","395","410","476","500",3),
    ("Historia","Difícil","¿Qué emperador dividió el Imperio Romano en dos?","Nerón","Constantino","Diocleciano","Augusto",3),
    ("Historia","Difícil","¿Qué papa excomulgó a Martín Lutero?","León X","Urbano II","Gregorio VII","Inocencio III",1),
    ("Historia","Difícil","¿Quién fue el general cartaginés que cruzó los Alpes para atacar Roma?","Julio César","Aníbal","Escipión","Pompeyo",2),
    ("Historia","Difícil","¿Qué rey inglés tuvo seis esposas?","Enrique VIII","Ricardo Corazón de León","Carlos I","Jorge III",1),

    # Ciencia - Fácil
    ("Ciencia", "Fácil", "¿Qué planeta está más cerca del Sol?", "Venus", "Mercurio", "Tierra", "Marte", 2),
    ("Ciencia", "Fácil", "¿Qué órgano se encarga de bombear la sangre?", "Pulmones", "Cerebro", "Corazón", "Estómago", 3),
    ("Ciencia", "Fácil", "¿Cuál es el planeta conocido como el planeta rojo?", "Saturno", "Venus", "Marte", "Júpiter", 3),
    ("Ciencia", "Fácil", "¿Qué gas necesitan las plantas para hacer la fotosíntesis?", "Oxígeno", "Nitrógeno", "Dióxido de carbono", "Helio", 3),
    ("Ciencia", "Fácil", "¿Cuántos planetas hay en el sistema solar?", "7", "8", "9", "10", 2),
    ("Ciencia", "Fácil", "¿Qué astro ilumina la Tierra durante el día?", "La Luna", "El Sol", "Las Estrellas", "El Cometa", 2),
    ("Ciencia", "Fácil", "¿Qué sentido usamos para oír?", "Vista", "Tacto", "Oído", "Olfato", 3),
    ("Ciencia", "Fácil", "¿De qué está hecho principalmente el cuerpo humano?", "Metal", "Agua", "Huesos", "Grasa", 2),
    ("Ciencia", "Fácil", "¿Qué instrumento se usa para medir la temperatura?", "Reloj", "Microscopio", "Termómetro", "Telescopio", 3),

    # Ciencia - Medio
    ("Ciencia", "Medio", "¿Cuál es el planeta más grande del sistema solar?", "Tierra", "Saturno", "Júpiter", "Neptuno", 3),
    ("Ciencia", "Medio", "¿Qué gas respiramos los seres humanos?", "Oxígeno", "Dióxido de carbono", "Nitrógeno", "Helio", 1),
    ("Ciencia", "Medio", "¿Qué parte del cuerpo controla las funciones principales del organismo?", "Cerebro", "Corazón", "Pulmones", "Hígado", 1),
    ("Ciencia", "Medio", "¿Cómo se llama el proceso por el cual las plantas producen su alimento?", "Digestión", "Fotosíntesis", "Respiración", "Transpiración", 2),
    ("Ciencia", "Medio", "¿Qué planeta tiene un gran sistema de anillos?", "Urano", "Neptuno", "Saturno", "Júpiter", 3),
    ("Ciencia", "Medio", "¿Cuál es el metal más liviano?", "Hierro", "Litio", "Plomo", "Cobre", 2),
    ("Ciencia", "Medio", "¿Qué tipo de sangre es considerado el donante universal?", "O negativo", "A positivo", "B positivo", "AB negativo", 1),
    ("Ciencia", "Medio", "¿Qué fenómeno natural mide la escala de Richter?", "Huracanes", "Erupciones volcánicas", "Terremotos", "Tormentas eléctricas", 3),
    ("Ciencia", "Medio", "¿Cuál es el órgano más grande del cuerpo humano?", "Piel", "Hígado", "Cerebro", "Pulmones", 1),
    ("Ciencia", "Medio", "¿Qué científico descubrió la ley de la gravedad?", "Newton", "Galileo", "Einstein", "Copérnico", 1),
    ("Ciencia", "Medio", "¿Qué aparato sirve para observar objetos muy pequeños?", "Telescopio", "Microscopio", "Binoculares", "Periscopio", 2),
    ("Ciencia", "Medio", "¿Cuál es la capa más externa de la Tierra?", "Manto", "Núcleo", "Corteza", "Atmósfera", 3),
    ("Ciencia", "Medio", "¿Qué órgano es responsable de filtrar la sangre?", "Corazón", "Riñones", "Pulmones", "Hígado", 2),
    ("Ciencia", "Medio", "¿Qué fuerza mantiene a los planetas en órbita alrededor del Sol?", "Gravedad", "Magnetismo", "Inercia", "Energía solar", 1),

    # Ciencia - Difícil
    ("Ciencia", "Difícil", "¿Cuál es el elemento más abundante en el universo?", "Hidrógeno", "Helio", "Oxígeno", "Carbono", 1),
    ("Ciencia", "Difícil", "¿Qué científico descubrió la penicilina?", "Alexander Fleming", "Louis Pasteur", "Isaac Newton", "Gregor Mendel", 1),
    ("Ciencia", "Difícil", "¿Qué órgano produce la insulina?", "Hígado", "Páncreas", "Riñón", "Estómago", 2),
    ("Ciencia", "Difícil", "¿Qué parte del ojo humano controla la cantidad de luz que entra?", "Pupila", "Iris", "Retina", "Córnea", 2),
    ("Ciencia", "Difícil", "¿Qué científico propuso la teoría de la relatividad?", "Einstein", "Galileo", "Bohr", "Tesla", 1),
    ("Ciencia", "Difícil", "¿Cuál es la fórmula química del ozono?", "O2", "O3", "CO2", "N2", 2),
    ("Ciencia", "Difícil", "¿Qué unidad mide la intensidad de corriente eléctrica?", "Voltio", "Ohmio", "Amperio", "Julio", 3),
    ("Ciencia", "Difícil", "¿Qué científico formuló las leyes del movimiento?", "Newton", "Einstein", "Galileo", "Faraday", 1),
    ("Ciencia", "Difícil", "¿Qué planeta tiene el día más corto?", "Júpiter", "Mercurio", "Marte", "Venus", 1),
    ("Ciencia", "Difícil", "¿Qué vitamina se obtiene principalmente del sol?", "Vitamina A", "Vitamina C", "Vitamina D", "Vitamina E", 3),
    ("Ciencia", "Difícil", "¿Cuál es el componente principal del aire?", "Nitrógeno", "Oxígeno", "Dióxido de carbono", "Argón", 1),
    ("Ciencia", "Difícil", "¿Qué tipo de célula no tiene núcleo?", "Animal", "Vegetal", "Procariota", "Eucariota", 3),
    ("Ciencia", "Difícil", "¿Qué científico desarrolló el modelo atómico con órbitas?", "Bohr", "Thomson", "Rutherford", "Dalton", 1),
    ("Ciencia", "Difícil", "¿Qué aparato mide la presión atmosférica?", "Barómetro", "Termómetro", "Higrómetro", "Anemómetro", 1),
    ("Ciencia", "Difícil", "¿Qué sustancia en la sangre transporta el oxígeno?", "Plasma", "Glóbulos blancos", "Hemoglobina", "Plaquetas", 3),
    ("Ciencia", "Difícil", "¿Qué partícula tiene carga negativa?", "Protón", "Neutrón", "Electrón", "Positrón", 3),
    ("Ciencia", "Difícil", "¿Qué científico descubrió la radiactividad?", "Marie Curie", "Henri Becquerel", "Niels Bohr", "Rutherford", 2),
    ("Ciencia", "Difícil", "¿Cuál es la capa más externa del sol?", "Corona", "Fotosfera", "Cromosfera", "Núcleo", 1),
    ("Ciencia", "Difícil", "¿Qué ley explica la relación entre presión y volumen de un gas?", "Ley de Boyle", "Ley de Ohm", "Ley de Newton", "Ley de Pascal", 1),
    ("Informática", "Fácil", "¿Qué significa la sigla CPU?", "Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Control Process Utility", 2),
    ("Informática", "Fácil", "¿Cuál de los siguientes es un sistema operativo?", "Python", "Linux", "HTML", "Excel", 2),
    ("Informática", "Fácil", "¿Qué componente se usa para almacenar datos de forma permanente?", "RAM", "Disco duro", "Procesador", "Tarjeta gráfica", 2),
    ("Informática", "Fácil", "¿Qué es un bit?", "Una unidad de medida de velocidad", "Una unidad de información", "Un tipo de archivo", "Un componente físico", 2),
    ("Informática", "Fácil", "¿Qué dispositivo se usa para ingresar texto a la computadora?", "Monitor", "Teclado", "Altavoz", "Proyector", 2),
    ("Informática", "Fácil", "¿Qué programa se usa para navegar en Internet?", "Word", "Excel", "Chrome", "Paint", 3),
    ("Informática", "Fácil", "¿Qué significa WWW?", "World Wide Web", "Wide World Web", "Web World Wide", "Wide Web World", 1),
    ("Informática", "Fácil", "¿Cuál de los siguientes es un periférico de salida?", "Teclado", "Mouse", "Impresora", "Micrófono", 3),
    ("Informática", "Fácil", "¿Qué es un archivo PDF?", "Un formato de imagen", "Un tipo de virus", "Un formato de documento", "Un programa de video", 3),

    # Informática - Medio
    ("Informática", "Medio", "¿Qué lenguaje se utiliza principalmente para crear páginas web?", "Python", "C++", "HTML", "SQL", 3),
    ("Informática", "Medio", "¿Qué componente es considerado el cerebro del computador?", "Disco duro", "Procesador", "Memoria RAM", "Fuente de poder", 2),
    ("Informática", "Medio", "¿Qué extensión tienen los archivos ejecutables en Windows?", ".txt", ".exe", ".jpg", ".mp3", 2),
    ("Informática", "Medio", "¿Cuál es el navegador desarrollado por Google?", "Firefox", "Safari", "Edge", "Chrome", 4),
    ("Informática", "Medio", "¿Qué dispositivo convierte señales digitales en analógicas?", "Router", "Modem", "Switch", "Servidor", 2),
    ("Informática", "Medio", "¿Qué hace el comando 'Ctrl + C' en la mayoría de los programas?", "Copia el texto", "Pega el texto", "Corta el texto", "Guarda el archivo", 1),
    ("Informática", "Medio", "¿Qué tipo de software es Microsoft Word?", "Sistema operativo", "Procesador de texto", "Antivirus", "Navegador", 2),
    ("Informática", "Medio", "¿Qué es la nube en informática?", "Un programa local", "Un tipo de hardware", "Un servicio de almacenamiento en Internet", "Un tipo de virus", 3),
    ("Informática", "Medio", "¿Qué empresa desarrolló el sistema operativo Windows?", "Apple", "IBM", "Microsoft", "Google", 3),
    ("Informática", "Medio", "¿Qué parte de la computadora realiza cálculos y operaciones lógicas?", "Procesador", "RAM", "Fuente", "Disco duro", 1),
    ("Informática", "Medio", "¿Qué lenguaje se usa para dar estilo a las páginas web?", "CSS", "Java", "PHP", "Python", 1),
    ("Informática", "Medio", "¿Qué unidad se usa para medir la capacidad de almacenamiento?", "Hertz", "Píxeles", "Bytes", "Vatios", 3),
    ("Informática", "Medio", "¿Qué es un archivo comprimido?", "Un archivo con virus", "Un archivo reducido de tamaño", "Un archivo de texto", "Un archivo encriptado", 2),
    ("Informática", "Medio", "¿Qué significa el acrónimo USB?", "Universal Serial Bus", "United System Base", "User Software Block", "Universal System Bus", 1),

    # Informática - Difícil
    ("Informática", "Difícil", "¿Quién es considerado el padre de la computación?", "Alan Turing", "Bill Gates", "Steve Jobs", "Charles Babbage", 4),
    ("Informática", "Difícil", "¿En qué año se lanzó el primer sistema operativo Windows?", "1985", "1990", "1978", "1995", 1),
    ("Informática", "Difícil", "¿Qué protocolo se utiliza para transferir archivos en Internet?", "HTTP", "FTP", "SMTP", "TCP", 2),
    ("Informática", "Difícil", "¿Cuál de los siguientes es un lenguaje de programación orientado a objetos?", "C", "Assembly", "Python", "HTML", 3),
    ("Informática", "Difícil", "¿Qué significa IP en redes informáticas?", "Internet Provider", "Internet Protocol", "Internal Process", "Input Program", 2),
    ("Informática", "Difícil", "¿Qué componente almacena temporalmente los datos mientras se procesan?", "RAM", "Disco duro", "ROM", "Cache", 1),
    ("Informática", "Difícil", "¿Qué es un firewall?", "Un tipo de hardware de sonido", "Un sistema de protección de red", "Un lenguaje de programación", "Un virus", 2),
    ("Informática", "Difícil", "¿Qué hace un servidor DNS?", "Traduce nombres de dominio en direcciones IP", "Controla la velocidad de conexión", "Almacena contraseñas", "Protege contra virus", 1),
    ("Informática", "Difícil", "¿Qué tipo de base de datos utiliza SQL?", "Orientada a objetos", "Relacional", "Jerárquica", "Distribuida", 2),
    ("Informática", "Difícil", "¿Qué significa BIOS?", "Basic Input Output System", "Binary Integrated Operating Software", "Base Internal Operating System", "Bus Information Operating System", 1),
    ("Informática", "Difícil", "¿Qué algoritmo se utiliza en la encriptación RSA?", "Clave pública", "Hash simple", "Compresión", "Firma digital", 1),
    ("Informática", "Difícil", "¿Qué significa LAN?", "Local Area Network", "Logical Access Node", "Limited Application Network", "Linked Area Node", 1),
    ("Informática", "Difícil", "¿Cuál es la función de un compilador?", "Ejecutar el código directamente", "Convertir código fuente en código máquina", "Editar texto", "Proteger archivos", 2),
    ("Informática", "Difícil", "¿Qué es un sistema operativo de código abierto?", "Un software gratuito sin código", "Un sistema cuyo código fuente es público", "Un sistema ilegal", "Un programa privado", 2),
    ("Informática", "Difícil", "¿Qué lenguaje se usa para consultas en bases de datos?", "HTML", "Python", "SQL", "CSS", 3),
    ("Informática", "Difícil", "¿Qué modelo de red describe las capas de comunicación?", "Modelo OSI", "Modelo TCP/IP", "Modelo HTTP", "Modelo LAN", 1),
    ("Informática", "Difícil", "¿Qué es una dirección MAC?", "Una dirección física única de red", "Un tipo de protocolo web", "Un programa de Apple", "Una contraseña de red", 1),
    ("Informática", "Difícil", "¿Qué tipo de software es Linux?", "Software de aplicación", "Software propietario", "Software libre", "Software comercial", 3),
    ("Informática", "Difícil", "¿Qué tipo de memoria conserva los datos aunque se apague el equipo?", "RAM", "ROM", "Cache", "Virtual", 2),


# --- Deportes - Fácil

    ("Deportes", "Fácil", "¿Cuántos jugadores hay en un equipo de fútbol?", "9", "10", "11", "12", 3),
    ("Deportes", "Fácil", "¿En qué deporte se usa una raqueta y un volante?", "Tenis", "Bádminton", "Ping Pong", "Squash", 2),
    ("Deportes", "Fácil", "¿Cuál es el país de origen del fútbol?", "España", "Inglaterra", "Brasil", "Italia", 2),
    ("Deportes", "Fácil", "¿Qué instrumento se utiliza para golpear la bola en el golf?", "Palo", "Raqueta", "Bate", "Cetro", 1),
    ("Deportes", "Fácil", "¿Cuánto dura un partido de baloncesto profesional?", "40 minutos", "48 minutos", "60 minutos", "90 minutos", 2),
    ("Deportes", "Fácil", "¿Qué deporte se juega en Wimbledon?", "Tenis", "Fútbol", "Cricket", "Golf", 1),
    ("Deportes", "Fácil", "¿Cuántos puntos vale un touchdown en fútbol americano?", "5", "6", "7", "3", 2),
    ("Deportes", "Fácil", "¿Qué deporte utiliza guantes y ring?", "Boxeo", "Judo", "Fútbol", "Baloncesto", 1),
    ("Deportes", "Fácil", "¿Cuál es el deporte más popular en Brasil?", "Voleibol", "Fútbol", "Baloncesto", "Rugby", 2),

    # Deportes - Medio
    ("Deportes", "Medio", "¿Cuántos sets se juegan en un partido de tenis masculino del Grand Slam?", "3", "5", "4", "2", 2),
    ("Deportes", "Medio", "¿Quién tiene más goles en la historia de la Copa del Mundo?", "Pelé", "Cristiano Ronaldo", "Miroslav Klose", "Lionel Messi", 3),
    ("Deportes", "Medio", "¿En qué año se celebraron los primeros Juegos Olímpicos modernos?", "1896", "1900", "1924", "1912", 1),
    ("Deportes", "Medio", "¿Qué país ganó la Eurocopa 2020?", "Italia", "España", "Francia", "Inglaterra", 1),
    ("Deportes", "Medio", "¿Cuál es la distancia oficial de un maratón?", "40 km", "42,195 km", "50 km", "45 km", 2),
    ("Deportes", "Medio", "¿Cuántos jugadores hay en un equipo de voleibol?", "5", "6", "7", "8", 2),
    ("Deportes", "Medio", "¿Qué significa MMA en deportes de combate?", "Mixed Martial Arts", "Major Martial Arts", "Modern Martial Arena", "Multiple Martial Arts", 1),
    ("Deportes", "Medio", "¿Qué deporte se juega en el Estadio Maracaná?", "Rugby", "Fútbol", "Cricket", "Béisbol", 2),
    ("Deportes", "Medio", "¿Cuánto dura un tiempo en fútbol profesional?", "40 min", "45 min", "50 min", "60 min", 2),
    ("Deportes", "Medio", "¿Quién es conocido como 'La Pulga' en fútbol?", "Cristiano Ronaldo", "Lionel Messi", "Neymar", "Zlatan Ibrahimovic", 2),
    ("Deportes", "Medio", "¿En qué deporte se hace un 'hole in one'?", "Golf", "Béisbol", "Cricket", "Tenis", 1),
    ("Deportes", "Medio", "¿Qué país ganó más medallas en los Juegos Olímpicos de Tokio 2020?", "China", "Estados Unidos", "Japón", "Rusia", 2),
    ("Deportes", "Medio", "¿Qué significa NBA?", "National Basketball Association", "National Baseball Association", "New Basketball Alliance", "National Boxing Association", 1),
    ("Deportes", "Medio", "¿Cuál es el país con más títulos mundiales de fútbol?", "Alemania", "Italia", "Brasil", "Argentina", 3),
    ("Deportes", "Difícil", "¿Qué atleta tiene el récord mundial de los 100 metros planos?", "Usain Bolt", "Carl Lewis", "Justin Gatlin", "Yohan Blake", 1),
    ("Deportes", "Difícil", "¿Cuál es la cancha más grande del mundo en tenis?", "Roland Garros", "Wimbledon", "Arthur Ashe", "Melbourne Park", 3),
    ("Deportes", "Difícil", "¿En qué deporte se utiliza el 'spike'?", "Voleibol", "Baloncesto", "Tenis", "Fútbol", 1),
    ("Deportes", "Difícil", "¿Qué país organizó los Juegos Olímpicos de 2008?", "China", "Grecia", "Reino Unido", "Brasil", 1),
    ("Deportes", "Difícil", "¿Qué ciclista ganó más veces el Tour de Francia?", "Lance Armstrong", "Miguel Indurain", "Eddy Merckx", "Bernard Hinault", 3),
    ("Deportes", "Difícil", "¿Qué significa 'KO' en boxeo?", "Knockout", "Kick Out", "Kick Off", "Knock Over", 1),
    ("Deportes", "Difícil", "¿Cuántos jugadores participan en un partido de rugby por equipo?", "13", "14", "15", "16", 3),
    ("Deportes", "Difícil", "¿Qué deporte inventó James Naismith?", "Baloncesto", "Fútbol", "Voleibol", "Béisbol", 1),
    ("Deportes", "Difícil", "¿En qué año se celebraron los primeros Juegos Olímpicos modernos?", "1896", "1900", "1924", "1912", 1),
    ("Deportes", "Difícil", "¿Qué país ganó la Copa Mundial de Rugby 2019?", "Inglaterra", "Sudáfrica", "Nueva Zelanda", "Australia", 2),
    ("Deportes", "Difícil", "¿Cuántos puntos vale un aro en baloncesto?", "2 o 3", "1", "4", "5", 1),
    ("Deportes", "Difícil", "¿Qué país ganó más medallas en la historia de los Juegos Olímpicos?", "Estados Unidos", "China", "Rusia", "Alemania", 1),
    ("Deportes", "Difícil", "¿Qué jugador de tenis tiene más títulos de Grand Slam masculino?", "Roger Federer", "Rafael Nadal", "Novak Djokovic", "Pete Sampras", 3),
    ("Deportes", "Difícil", "¿Qué es el 'offside' en fútbol?", "Falta", "Posición adelantada", "Tiro libre", "Penal", 2),
    ("Deportes", "Difícil", "¿Qué país es sede del maratón de Boston?", "Canadá", "Estados Unidos", "Reino Unido", "Australia", 2),
    ("Deportes", "Difícil", "¿Qué significa TKO en boxeo?", "Technical Knockout", "Total Knockout", "Time Knockout", "Team Knockout", 1),
    ("Deportes", "Difícil", "¿Cuántos sets se juegan en un partido de Grand Slam femenino?", "3", "5", "4", "2", 1),
    ("Deportes", "Difícil", "¿Cuál es la distancia de un campo de fútbol reglamentario?", "90-120 m", "80-100 m", "100-130 m", "70-90 m", 1),
    ("Deportes", "Difícil", "¿Qué país ganó la Copa América 2021?", "Brasil", "Argentina", "Colombia", "Chile", 2)

]


# --- Insertar preguntas ---
for q in questions:
    cursor.execute("""
        INSERT INTO questions (category, difficulty, question, option1, option2, option3, option4, correct_option)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, q)

conn.commit()
conn.close()
print("Base de datos SQLite creada y preguntas insertadas ✅")

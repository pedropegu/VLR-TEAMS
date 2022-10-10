
# VLR TEAMS

## <u>**¿Qué es valorant?**</u>

Valorant es un hero shooter en primera persona multijugador gratuito desarrollado y publicado por [Riot Games](https://es.wikipedia.org/wiki/Riot_Games). 

Los jugadores asumen el control de agentes, personajes que provienen de una gran cantidad de países y culturas de todo el mundo. En el modo de juego principal, los jugadores se unen al equipo atacante o defensor con cada equipo que tiene cinco jugadores. Los agentes tienen habilidades únicas y usan un sistema económico para comprar sus habilidades y armas.

El equipo atacante tiene una bomba, llamada Spike, que necesitan plantar en un sitio. Si el equipo atacante protege con éxito la Spike durante 40 segundos y detona, obtendrán un punto. Si el equipo defensor desactiva con éxito la Spike, o el temporizador de la ronda de 100 segundos expira, el equipo defensor obtiene un punto. Si se eliminan todos los miembros de un equipo, el equipo contrario gana un punto. Después de doce rondas, el equipo atacante cambia al equipo defensor y viceversa. El primer equipo en ganar 13 rondas gana la partida. Exceptuando el tiempo extra, donde deberás conseguir 2 victorias/rondas seguidas.

En total, hay seis modos de juego: No Competitivo, Competitivo, Combate a Muerte, Fiebre De La Spike, Réplica y Carrera Armamentística.
También cuenta con un modo llamado personalizado en el cual se puede crear una partida con los ajustes que el jugador desee.

Los roles de los que dispone el juego son los siguientes:

- Controlador
- Duelista
- Iniciador
- Centinela

Normalmente los jugadores se especializan en varios roles pero siempre existe tu rol principal que es el que más has jugado y que se te da mejor.


Centrándonos en el modo Competitivo, disponemos de un sistema de rango en el cual podrás ir escalando a medida que ganes partidas y consigas los puntos necesarios para subir de rango (NOTA: Si pierdes partidas pierdes puntos, por tanto también puedes bajar de rango).

![img](https://lh6.googleusercontent.com/powOHkw7SpnhvCmuFMBXu-OukFl4OgbNpKk0phnT9ovsSQYLbnHVYkWKI8eBODmt2ANwRdjo2KLdtZu8XdJGtTwg5RtGlAnyY2QN6UwWvhhNi9YwApuNCRvMJhZfSRzQiZQOyG6M3zdqoe-kyhhXJvTMjw9GfM6TAHDzcIqeKjGPTKMOa4cQqi0_Yg)

Este modo nos interesa ya que a partir de este modo sacaremos las estadísticas de los jugadores la cual les interesa a los equipos para la búsqueda de integrantes de este.

El interés de crear equipos surge para jugar torneos e ir creciendo en el mundo profesional de los eSports de tal forma que tu equipo pueda llegar a ser conocido e importante en este mundo. 

Más información sobre el modo competitivo:  https://support-valorant.riotgames.com/hc/es-419/articles/360047937633-VALORANT-preguntas-frecuentes-sobre-el-modo-competitivo

Enlace Valorant Esports: https://playvalorant.com/es-mx/news/esports/

API para los datos: https://docs.henrikdev.xyz/valorant.html



## <u>Base de datos</u>

### 	Especificación.

La aplicación que voy a desarrollar trata de lo siguiente:
Una aplicación web para la búsqueda de jugadores, equipos, Managers, Coach en valorant.Vamos a tener un registro común para todos los clientes de la página, el cual tendrá el nombre del usuario, correo, contraseña, edad y una breve descripción.
Luego podrá elegir entre distintas opciones: **Staff, Cuerpo técnico, Jugador.**

Cada una de estas opciones te otorgará “permisos” diferentes.

Explicando cada uno de estos tenemos que:

- **Jugador:** Deberá vincular seleccionar su cuenta de Riot, especificar su rol principal en el juego, la experiencia que tiene jugando en equipos, su disponibilidad de horarios (Tardes / Mañanas), además deberá incluir una descripción breve y rellenar un campo para ver si ya se encuentra en un equipo o no. 

  "Este podrá sumarse al Marketplace"

  

- **Directivo:**

  Se trata de aquellos usuarios que podrán crear un equipo / gestionarlo, estos constaran de lo siguiente: Cargo ( CEO / MANAGER ), experiencia , descripción breve.

  
  
- **Equipo**: Nombre, fecha de fundación y si se asignará sueldo a jugadores o no (Bool)

- **Entrenador:** Se trata del entrenador del equipo, este deberá seleccionar su cuenta de riot, la experiencia que tiene ejerciendo como Coach, información a añadir y si se encuentra actualmente en un equipo o no (Bool).

- **Anuncios.**

  Los directivos podrán colgar anuncios los cuales estarán compuestos de: Titular, mensaje.


- **Marketplace.**

Este apartado será el lugar donde se podrán buscar jugadores, estos no aparecerán en este apartado de forma inmediata sino que mediante un “tick” en la página el usuario podrá añadirse al Marketplace donde los equipos podrán buscarle y contactarle a través de correo como en los anuncios.



### 	Entity Relationship.


![oficial](https://user-images.githubusercontent.com/95850823/194899660-d70f152d-0e96-4e48-adca-b526fad3e129.jpeg)








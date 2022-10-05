[![Build and deploy Python app to Azure Web App - testimoniesreport](https://github.com/dzarkV/testimonial-victims-API-REST/actions/workflows/az-deploy_testimoniesreport.yml/badge.svg)](https://github.com/dzarkV/testimonial-victims-API-REST/actions/workflows/az-deploy_testimoniesreport.yml)

# Testimonial victims API-REST

REST API with NER atributes of victim's testimonies from Cuando los pájaros no cantaban. 
This is the Truth Comission's report with some testimonies of colombian armed conflict's victims.

## Technologies

* Mongo Atlas for DB
* Python language
* FastAPI framework
* Azure Cognitive Search for NER atributes (people, locations, organizations and key words)
* Meilisearch for free text search
* Azure Web Service and Git Actions for continuous deployment (CD)  

## Flow

The components developed until now are as follow:

<img src="https://github.com/dzarkV/testimonial-victims-API-REST/blob/main/pic/victims-testimonies-flow.png" width=50% height=50%>

## Use

You can see it deployed in Azure Web [here](http://testimoniesreport.azurewebsites.net/). 

Select a GET method, click on <kbd>Try it out</kbd> and <kbd>Execute</kbd>! 

You can consume it with Postman too, or with Power BI for analytics like [this](https://youtu.be/FuGZoRkRmyI?t=64).

### With CLI

Make sure you have `curl` and `jq` packages installed.

```shell
# Retrieve six of all testimonies
curl -X 'GET' \
  'http://testimoniesreport.azurewebsites.net/testimonios?limit=6' \
  -H 'accept: application/json' | jq 

# Retrieve eight of all testimonies with all NER each
curl -X 'GET' \
  'http://testimoniesreport.azurewebsites.net/testimonios?limit=8&allNER=true' \
  -H 'accept: application/json' | jq 

# Retrieve testimony with id 40 with NER atributes
curl -X 'GET' \
  'http://testimoniesreport.azurewebsites.net/testimonios/40' \
  -H 'accept: application/json' | jq 

# Free text search in testimonies
curl -X 'GET' \
  'http://testimoniesreport.azurewebsites.net/search?q=paz' \
  -H 'accept: application/json' | jq 
```

Example response:

```json
{
"id": 27,
  "titulo": "El crucifijo ",
  "texto": "Juan Daniel fue más independiente que los otros hermanos. Cuando decidí estudiar, él se quedaba solo. Yo le daba plata, y así él le cogió amor a la plata. No quiso estudiar. Mi hijo fue un muchacho muy despierto. Él aprendió a defenderse solito. Conseguía sus amistades, pero mire que eran siempre mayores. De hecho, Juan Dantel tuvo una niña, y la mamá de ella es mayor que él, no mucho, pero sí es mayor. Glorta, la última pareja que tuvo, también era mayorcísima. \nUn día Juan Dantel llegó con un señor que le iba a vender una moto. Esa persona trabajaba así. Compraba la moto, se la daba a los muchachos y ellos se la iban pagando a diario. Como Juan Daniel era menor de edad, el señor vino y me preguntó si yo estaba de acuerdo con que él consiguiera esa moto. Yo le dije «pues sí porque él ya no quiere estudiar; lo que quiere es trabajar». Lo apoyamos con eso y fue uno de los primeros muchachos que tuvo moto en esa calle. \nJuan Dantel hizo un curso de repostería. Después trabajó de taxista y nosotros le ayudamos a que tuviera el pase. Él trabajaba en eso cuando no estaba en algún restaurante trabajando lo de pastelería. Así se pasó su corta vida. \nÉl tenía moto. Juan Daniel le daba tan duro a la moto, que se mantenía de ese negocio. Cuando llegaban los domingos, se me desaparecía, y yo me preguntaba: «:Juan Daniel dónde está? ¿Juan Daniel cómo se me desaparece? ¿Dónde estará este muchacho? ¿Este muchacho por qué se me desaparece?». Una de mis hijas me decía «no, mamá, él se va es para el Dagua a hacer esas carreras que hacen». Él también se iba para el Instituto Técnico Industrial, a lo mismo. Por ahí tengo una foto donde Juan Dantel puso, después de una carrera, una palabra que dice «vive la vida intensamente, minuto a minuto, tenemos mucho tiempo para estar muertos». Ahora que ya le pasó lo que le pasó, conocidos empezaron a mandar todas esas fotos de las carreras. Él vivía de esa manera porque iba a estar mucho tiempo muerto. Mis esperanzas de que Daniel esté vivo son muy remotas. Yo no me voy a estar engañando, pensando en que él está vivo. Él no está vivo. La verdad, no sabemos realmente que fue lo que pasó, pero él estaba de taxista cuando lo desaparecieron. En su momento, yo lo veía con amistades policías, y en mi ingenuidad pensaba que estaba rodeado de buenas amistades, pero ahora me doy cuenta de que no. \nEn esa misma semana, él había llevado a Sofía, la hija, a pasear. La llevó a dar vuelta en el taxi. Juan Dantel llegó y me dijo: «Mamá, me metí en un problema, llevaba a Sofía pa la 14 y miró una casa de muñecas. Quiere que se la compre. Vale 500.000 pesos». «Ah, pues póngase a ahorrar pa que le compré la casa de muñecas a su hija». \nÉl estaba ya reuniendo la plata. Ese mismo día volvió a llegar, fue el último día que lo vi. Me dijo: «Mamá, voy a llevar a Sofía a dormir conmigo». «No, no te la llevés porque mañana yo voy a madrugar. Voy a viajar a Tuluá». Él quería, como presintiendo, dormir con su hija y no pudo. \nEse día él me llamó a las sets y cinco de la mañana. Yo me extrañé. No puedo explicar lo que sentí, no lo puedo explicar. Yo sentí algo con esa llamada. ¿Por qué tan temprano? Me contestó que era pa mandarme la copia de la cita que me había sacado para visitar al papá de él, que estaba preso. Ese día Dantel cogió su tax y salió a trabajar, como a eso de las nueve y media, yo lo llamé y le pregunté: «:Dónde está?». «Estoy acá en el Bolívar. Para que me hagás un favor». «Sí, pero me demoro». «Igual estás arriba, cuando bajés me hacés el favor». «Sh», me dijo. No hablé más con él, no hablé más con él. \nEsos días Juan Daniel había estado haciendo las cositas que uno le pedía. Yo le decía a mi hermana: «Juan Daniel está cogiendo juicio, está comprando costtas pa la casa». Glorta, la señora de él, también estaba contenta, porque Juan Daniel era muy amiguero, y por andar siempre con amigos era muy suelto: podía tener 10.000 pesos y si el amigo se los pedía, se los daba. \nEse día Gloria, la mujer con la que tuvo una hija, me empezó a llamar como a las tres de la tarde. Ella empezó a sospechar desde el mediodía o antes. Glorta entraba a trabajar al mediodía, es dormilona... por eso ellos habían hablado de que él la llamaba a las ocho de la mañana, para despertarla. Él siempre salía madrugado de la casa por lo que era taxista. Si a las ocho Gloria no se había despertado, lo hacía a las diez; así cocinaba, se arreglaba y se iba. Juan Daniel la llamaba a las ocho, a las diez, a las doce, y así. Pero ese día llegaron las diez y no la llamó. Llegaron las doce y no la llamó. Glorra me dijo «pero Juan Dantel, tan raro, no me llamó a las diez, no me llamó a las doce». \nAun así, Glorta cocmó. Ella se iba a sentar a comer cuando un crucifijo se viene allá de la mesa. Uno siempre tiene su televisor y el televisor tiene adorno. El crucifijo estaba en la mesa donde estaba el televisor. Ese crucifijo se vino de allá y se partió la cabecita. \nCuando el crucifijo se vino, ella dijo «¡Dantel!>. Glorta dice que de una vez se le vino a la mente Juan Daniel, sobre todo porque ella estaba prevenida. Él no la había llamado. Ella empezó a marcarle, empezó a llamar a otras personas. No me acuerdo si me llamó a esa hora, la verdad. Y nada, ella aun así se va a trabajar con esa preocupación. \nDieron las tres de la tarde y nada que Dantel la llamaba. Ella me llamó: «¡Isabel!, ¿sabés algo de tu hijo? ¡Mirá!, son las tres y tu hijo no me ha llamado». «No, yo no lo he visto. Hoy no lo he visto. Hablé con él en la mañana». «Voy air a la casa, y si la comida está, fue que algo le pasó. Si yo llego a la casa y la comida está ahí, algo le pasó», me dijo. \nSobre todo st estaba el jugo, porque él tomaba muchísimo líquido. Daniel siempre iba a almorzar de dos a tres de la tarde. Glorta llegó a la casa. Vio la comida ahí. Fue a abrir la nevera y estaba el jugo. Oscureció y el dueño del taxi me llamó y me dijo que le habían entregado su carro a eso del mediodía, que la Policía lo había llamado para que fuera a recoger su carro. Yo inmediatamente empecé a llorar y le dije a Cristian, mi otro hijo: «Algo le pasó a Daniel, él no iba a dejar el carro tirado». ¿Quién va a dejar su vehículo con la llave pegada? \nEl día que Daniel salió de la casa, sonó una canción de reguetón. No sé cómo es el título, pero la letra comienza como «dicen que soy un delincuente, pero no me importa que comenten porque a nadie le debo nada. Que hablen, que comenten porque a nadie le debo nada». Y dice como «le doy gracias a Dios por dejarme llegar donde estoy, por dejarme llegar a donde estoy». Que los amigos lo traicionaron, que son unos judas, que lo juzgan a él pero no juzgan a los grandes. Que allá arriba hay un Dios que todo lo ve. Me cuenta Gloria que él escuchó esa canción cinco veces antes de salir de la casa, y yo la tuve que escuchar seis veces seguidas para dejar de llorar cada vez que sonaba. \n\n",
  "personas": [
    "Juan Daniel",
    "Juan Dantel",
    "Glorta",
    "Daniel",
    "Sofía",
    "Dantel",
    "Gloria",
    "Glorra",
    "Isabel",
    "Cristian",
    "Dios"
  ],
  "organizaciones": [
    "Instituto Técnico Industrial",
    "Policía"
  ],
  "lugares": [
    "calle",
    "restaurante",
    "pastelería",
    "Dagua",
    "casa",
    "Tuluá",
    "Bolívar"
  ]
}
```

## License

This distribution is covered by the **GNU GENERAL PUBLIC LICENSE**, Version 3, 29 June 2007.

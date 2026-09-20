#!/usr/bin/env python3
"""Generador de páginas de productos Alfapro."""

import os

BASE = "/Users/luisarmijos/Desktop/alfapro-ecommerce"

PRODUCTS = [
    {
        "slug": "casco-ls2-ff800",
        "name": "Casco Integral LS2 FF800 Storm II",
        "cat": "Cascos",
        "price": "189.99",
        "original": "219.99",
        "discount": "14",
        "sku": "ALF-CAS-001",
        "img": "1571819507488-0e1dfe7cc22d",
        "img2": "1611004061856-ccc3cbe944b2",
        "img3": "1492144534655-ae79c964c9d7",
        "badge": "⭐ Más Vendido",
        "stars": "4.9", "reviews_count": "127",
        "hook": "El casco que los pilotos profesionales eligen cuando importa el tiempo.",
        "short_desc": "Casco integral de fibra de vidrio con aerodinámica deportiva, visor anti-UV de serie y ventilación triple. Disponible en tallas XS–XXL.",
        "features": [
            ("🏁", "Fibra de Vidrio", "Carcasa ultraliviana y resistente a impactos severos"),
            ("👁️", "Visor Anti-UV", "Policarbonato tratado, rápido reemplazo sin herramientas"),
            ("💨", "Ventilación Triple", "Entrada frente + salida nuca, nunca más sudar"),
            ("🔒", "Cierre Micro-lock", "Sin errores. Sin fallos. Siempre ajustado."),
        ],
        "specs": [
            ("Material carcasa", "Fibra de vidrio"),
            ("Peso aprox.", "1,350 g"),
            ("Tallas", "XS / S / M / L / XL / XXL"),
            ("Homologación", "DOT / ECE 22.06"),
            ("Visor", "Anti-UV, transparente de serie"),
            ("Forro", "Desmontable y lavable"),
            ("Ventilación", "Triple (frente, lateral, nuca)"),
            ("Colores", "Negro Mate / Blanco Perla / Rojo Racing"),
        ],
        "desc": "El LS2 FF800 Storm II no es solo un casco — es la promesa de llegar. Diseñado en colaboración con pilotos de circuito, su estructura de fibra de vidrio absorbe impactos donde otros cascos ceden.<br><br>El visor panorámico anti-UV elimina el deslumbramiento sin comprometer la visión lateral. El sistema de ventilación triple mantiene tu cabeza fresca incluso en los trayectos más largos bajo el sol ecuatoriano.<br><br>El forro interior antibacterial desmontable se lava cada semana sin perder forma. El cierre micro-lock que nunca falla. Y ese silencio aerodinámico que distingue un casco profesional de uno cualquiera.",
        "reviews": [
            ("Carlos M.", "Quevedo → Guayaquil", 5, "Lo uso todos los días para el trabajo. La ventilación es increíble — llego sin sudar. El visor es super claro incluso en días nublados. Vale cada centavo."),
            ("Diego P.", "Santo Domingo", 5, "Me caí dos veces y no tiene ni un rasguño interior. El forro huele bien aunque lo usé intenso dos semanas. Muy buena compra desde Alfapro."),
            ("Andrés V.", "Quito", 4, "Excelente casco, llegó rápido y bien empacado. Le quito una estrella porque el visor oscuro no viene incluido pero se compra por separado."),
        ],
        "related": [1, 2, 8],
    },
    {
        "slug": "casco-ls2-ff906",
        "name": "Casco Modular LS2 FF906 Advant",
        "cat": "Cascos",
        "price": "249.99",
        "original": "289.99",
        "discount": "14",
        "sku": "ALF-CAS-002",
        "img": "1611004061856-ccc3cbe944b2",
        "img2": "1571819507488-0e1dfe7cc22d",
        "img3": "1492144534655-ae79c964c9d7",
        "badge": "🔥 Nuevo",
        "stars": "4.8", "reviews_count": "89",
        "hook": "La libertad de un abierto. La protección de un integral.",
        "short_desc": "Casco modular con apertura one-touch, sistema 2-en-1, preparado para comunicadores Bluetooth y homologado en posición cerrada.",
        "features": [
            ("🔓", "Apertura One-Touch", "Quita la mentonera con una sola mano, sin parar el motor"),
            ("🎧", "Bluetooth Ready", "Canaleta preinstalada, compatible con todos los intercoms"),
            ("🛡️", "2-en-1 Homologado", "Homologado P/J en posición cerrada con certificación ECE"),
            ("💨", "AeroFlow Dual", "Doble canal de ventilación activa en mentonera y cúpula"),
        ],
        "specs": [
            ("Tipo", "Modular / Abatible"),
            ("Material", "ABS tricapa reforzado"),
            ("Peso aprox.", "1,500 g"),
            ("Tallas", "XS / S / M / L / XL / XXL"),
            ("Homologación", "ECE 22.06 P/J"),
            ("Visor", "Doble: exterior transparente + sol interior retráctil"),
            ("Bluetooth", "Canaleta preinstalada Cardo/Sena compatible"),
            ("Colores", "Negro Brillante / Gris Titanio / Blanco"),
        ],
        "desc": "El motorista moderno no elige entre seguridad y comodidad. El LS2 FF906 Advant elimina ese dilema con una arquitectura modular que abre con un solo toque — para saludar, pagar, hablar — y cierra con la rigidez de un casco integral completo.<br><br>Su doble visor integrado (exterior transparente + sol interior retráctil) elimina la necesidad de llevar gafas. La canaleta Bluetooth preinstalada acepta todos los sistemas Cardo y Sena del mercado sin modificaciones.<br><br>Para el piloto que recorre distancias largas, pasa por ciudades, y llega a reuniones sin quitarse la chaqueta.",
        "reviews": [
            ("Roberto F.", "Cuenca", 5, "Perfecto para viaje Cuenca-Guayaquil. El visor de sol integrado es lo mejor. Ya no llevo gafas. La apertura es super suave y rápida."),
            ("Paola S.", "Quito", 5, "Mi primer casco modular y ya no volvería a uno normal. El Bluetooth Cardo cabe perfecto sin modificar nada. Sonido impresionante."),
            ("Mauricio H.", "Manta", 4, "Muy buen casco. Al principio el ajuste se siente apretado pero a la semana ya adaptó perfecto a mi cabeza. Pesa un poco más de lo esperado."),
        ],
        "related": [0, 2, 8],
    },
    {
        "slug": "guantes-alpinestars-sp8",
        "name": "Guantes Alpinestars SP-8 v3",
        "cat": "Accesorios Piloto",
        "price": "54.99",
        "original": "74.99",
        "discount": "27",
        "sku": "ALF-PIL-001",
        "img": "1545284662-c3dda8bd045d",
        "img2": "1492144534655-ae79c964c9d7",
        "img3": "1611004061856-ccc3cbe944b2",
        "badge": "🏆 Bestseller",
        "stars": "4.9", "reviews_count": "204",
        "hook": "Tus manos merecen el mismo nivel de protección que tu casco.",
        "short_desc": "Guantes de cuero canguro con protección de nudillos TPR, palma reforzada y tira reflectante. El estándar de los pilotos de circuito, para tu calle.",
        "features": [
            ("🤜", "Cuero Canguro", "Palma en cuero de canguro: ultra-grip, 3× más resistente al desgarre"),
            ("🛡️", "TPR Nudillos", "Protector termoplástico moldeado sobre nudillos y dorso"),
            ("🌙", "Reflectante 360°", "Tira reflectante perimetral — visible en la noche desde 150m"),
            ("✋", "Ajuste Micro", "Velcro de ajuste en muñeca + apertura posterior stretch"),
        ],
        "specs": [
            ("Material exterior", "Cuero bovino + parches cuero canguro"),
            ("Protección", "Nudillos TPR + palma reforzada"),
            ("Tallas", "S / M / L / XL / 2XL"),
            ("Certificación", "CE Nivel 1 EN 13594"),
            ("Interior", "Microfibra absorbente transpirable"),
            ("Cierre", "Velcro ancho de liberación rápida"),
            ("Visibilidad", "Tira reflectante 360°"),
            ("Temporada", "3 estaciones (frío moderado - calor)"),
        ],
        "desc": "Las manos son lo primero que extiendes cuando caes. Y lo que más necesitas para seguir conduciendo al día siguiente. Los Alpinestars SP-8 v3 fueron diseñados para ese momento — el que esperas que nunca llegue, pero si llega, te encuentre listo.<br><br>La palma de cuero canguro ofrece agarre sobrenatural en el manubrio, incluso mojado. Los protectores TPR sobre nudillos y dorso absorben la energía del impacto sin transmitirla a los huesos. El forro interior de microfibra hace que los quieras puestos todo el tiempo.<br><br>Son los guantes que usamos nosotros. Y los que recomendamos sin dudar.",
        "reviews": [
            ("Sebastián Q.", "Guayaquil", 5, "Llevaba guantes genéricos de $12. La diferencia es brutal. El grip en el manubrio, la comodidad después de 2 horas. Nunca más compro guantes baratos."),
            ("Lorena A.", "Quito", 5, "Perfectos para moto urbana. Me los pongo y siento que son parte de la mano. El reflectante me ha salvado en varias noches de tráfico."),
            ("Marco T.", "Latacunga", 5, "Talla M perfecta para mis manos. Pedí el miércoles y llegaron el viernes a Latacunga. Impresionante el servicio de Alfapro."),
        ],
        "related": [3, 0, 9],
    },
    {
        "slug": "rodilleras-knox-flex",
        "name": "Rodilleras Knox Flex-Pro CE Nivel 2",
        "cat": "Accesorios Piloto",
        "price": "79.99",
        "original": "99.99",
        "discount": "20",
        "sku": "ALF-PIL-002",
        "img": "1504215680853-026ed2a45def",
        "img2": "1492144534655-ae79c964c9d7",
        "img3": "1545284662-c3dda8bd045d",
        "badge": "🛡️ CE Nivel 2",
        "stars": "4.8", "reviews_count": "76",
        "hook": "El accidente que no esperas. La protección que siempre llevas puesta.",
        "short_desc": "Rodilleras con certificación CE Nivel 2, material Flex-Pro que se adapta al movimiento, correas ajustables y uso compatible on/off road.",
        "features": [
            ("🦵", "CE Nivel 2", "La máxima certificación para protecciones independientes"),
            ("🤸", "Flex-Pro D3O", "Material que se endurece en impacto, flexible en movimiento"),
            ("⚡", "Universal Fit", "Correas 360° ajustables, compatible con pantalón o directo en piel"),
            ("💧", "Resistente Agua", "Exterior ventilado + interior absorbente no retiene humedad"),
        ],
        "specs": [
            ("Certificación", "CE EN 1621-1 Nivel 2"),
            ("Material", "Flex-Pro (D3O compatible)"),
            ("Cobertura", "Rótula, tendón rotuliano y menisco lateral"),
            ("Ajuste", "3 correas de velcro independientes"),
            ("Tallas", "S-M / L-XL (ajustables)"),
            ("Peso por unidad", "280 g"),
            ("Uso", "Road / Offroad / Urban"),
            ("Lavado", "A mano, 30°C"),
        ],
        "desc": "La rodilla es la articulación más compleja y más expuesta en una caída. No hay cirugía que la devuelva al 100%. Las Knox Flex-Pro CE Nivel 2 existen para que no necesites descubrir eso por ti mismo.<br><br>El material Flex-Pro se comporta como gel flexible cuando caminas y montas. En el microsegundo de un impacto, se endurece y distribuye la energía en superficie, protegiendo rótula, tendones y menisco lateral — simultáneamente.<br><br>Van sobre el pantalón o directo en la piel. Las correas se ajustan en 15 segundos. No se notan debajo de un jean. No hay excusa para no usarlas.",
        "reviews": [
            ("Germán E.", "Ambato", 5, "Las uso dentro del jean y nadie nota que las llevo. Después de 8 horas en moto no me molestan nada. Ya no salgo sin ellas."),
            ("Valeria O.", "Riobamba", 5, "Las compré tras caerme sin protecciones. Llegué bien pero fue susto. Ahora estas van puestas siempre. La calidad es impresionante."),
            ("Felipe N.", "Manta", 4, "Muy buenas rodilleras. Las tiras son un poco más complicadas de ajustar al principio pero después se vuelve automático."),
        ],
        "related": [2, 0, 4],
    },
    {
        "slug": "espejos-cnc-racing",
        "name": "Espejos Retrovisores CNC Racing Universal",
        "cat": "Accesorios Moto",
        "price": "34.99",
        "original": "49.99",
        "discount": "30",
        "sku": "ALF-MOT-001",
        "img": "1558618666-fcd25c85cd64",
        "img2": "1492144534655-ae79c964c9d7",
        "img3": "1504215680853-026ed2a45def",
        "badge": "🔧 Universal",
        "stars": "4.7", "reviews_count": "143",
        "hook": "Diseñados para correr. Construidos para durar.",
        "short_desc": "Par de espejos retrovisores en aluminio CNC fresado, cristal convexo 180°, antivibración y rosca universal 10mm/8mm derecha e izquierda.",
        "features": [
            ("⚙️", "CNC Fresado", "Aluminio 6061-T6 mecanizado en fábrica, sin uniones ni soldaduras"),
            ("👁️", "Cristal Convexo 180°", "Campo visual ampliado, elimina el punto ciego lateral"),
            ("🎯", "Anti-vibración", "Junta amortiguadora en base elimina el titileo a alta velocidad"),
            ("🔩", "Universal 10/8mm", "Adaptadores incluidos para casi cualquier moto del mercado"),
        ],
        "specs": [
            ("Material", "Aluminio CNC 6061-T6 anodizado negro"),
            ("Cristal", "Convexo, vidrio templado antirayones"),
            ("Ángulo", "Ajustable 360° en rótula esférica"),
            ("Rosca", "10mm derecha + 8mm izquierda (adaptadores incluidos)"),
            ("Altura espejo", "195 mm"),
            ("Peso por unidad", "120 g"),
            ("Antivibración", "Sí, junta caucho en base"),
            ("Colores", "Negro mate / Plata / Dorado"),
        ],
        "desc": "Los espejos retrovisores originales de fábrica tienen un problema conocido: vibran, distorsionan y reducen el ángulo de visión justo cuando más lo necesitas. Los CNC Racing resuelven los tres problemas de raíz.<br><br>El aluminio CNC fresado elimina las vibraciones que deforman la imagen a más de 80 km/h. El cristal convexo amplía el campo visual lateral en un 40% sobre los espejos planos. Y el sistema de rótula esférica permite ajustar el ángulo exacto para tu posición de conducción, no para una posición genérica de fábrica.<br><br>Instalación en menos de 10 minutos. Compatible con Honda, Yamaha, Suzuki, Kawasaki, Bajaj, TVS y la mayoría de marcas del mercado.",
        "reviews": [
            ("Javier R.", "Guayaquil", 5, "Mis espejos originales vibraban horrible a 100km/h. Con estos, imagen perfecta a cualquier velocidad. La instalación fue facilísima."),
            ("Miguel A.", "Quito", 4, "Muy buenos espejos. El dorado queda increíble en mi Yamaha MT-07. Solo sugiero poner un poco de Loctite en la rosca para que no aflojen."),
            ("Andrea L.", "Cuenca", 5, "Los puse en mi Honda CB190. Quedaron perfectos. La visibilidad mejoró notablemente. Relación precio-calidad excelente."),
        ],
        "related": [5, 6, 2],
    },
    {
        "slug": "kit-cadena-did-428",
        "name": "Kit Cadena DID 428VX + Piñón + Corona",
        "cat": "Partes y Piezas",
        "price": "44.99",
        "original": "64.99",
        "discount": "31",
        "sku": "ALF-PAR-001",
        "img": "1558980394-4c7c9299fe96",
        "img2": "1504215680853-026ed2a45def",
        "img3": "1492144534655-ae79c964c9d7",
        "badge": "✅ Kit Completo",
        "stars": "4.8", "reviews_count": "98",
        "hook": "Una cadena rota te deja a pie. Una cadena DID te lleva lejos.",
        "short_desc": "Kit completo: cadena DID 428VX O-ring de 120 eslabones + piñón y corona en acero forjado CNC. Para motos 125-250cc.",
        "features": [
            ("🔗", "O-Ring Sellado", "Retención de lubricante interna, vida útil 3× superior"),
            ("⚙️", "Acero Forjado", "Piñón y corona CNC en acero 420 HV tratado térmicamente"),
            ("🔢", "120 Eslabones", "Eslabones y remaches con cierre de seguridad incluido"),
            ("🔧", "Kit Completo", "Cadena + piñón + corona + pasador de cierre en una caja"),
        ],
        "specs": [
            ("Cadena", "DID 428VX O-ring"),
            ("Eslabones", "120 (cortable)"),
            ("Piñón", "Acero forjado, 14T ó 15T (seleccionar)"),
            ("Corona", "Acero CNC 420HV, 45T ó 48T (seleccionar)"),
            ("Paso", "428"),
            ("Carga rotura", "2,600 kgf"),
            ("Lubricación", "O-ring sellado, sin mantenimiento semanal"),
            ("Compatible", "Honda, Yamaha, Suzuki 125-250cc"),
        ],
        "desc": "La cadena es el eslabón literal entre el motor y la rueda trasera. Una cadena barata no falla de un día para otro — se va estirando, saltando, perdiendo eficiencia hasta que un día, en la autopista, te deja parado.<br><br>La DID 428VX con sistema O-ring mantiene la lubricación interna sellada entre los rodillos, lo que significa hasta 3 veces más vida útil que una cadena estándar sin anillos. El piñón y la corona en acero forjado CNC mantienen el desgaste uniforme y preservan el paso de la cadena durante más tiempo.<br><br>Un kit nuevo reemplaza los tres componentes de transmisión al mismo tiempo — que es exactamente lo correcto. Los mecánicos que reemplazan solo la cadena o solo la corona te están costando más a largo plazo.",
        "reviews": [
            ("Ramiro C.", "Latacunga", 5, "Llevaba 2 años con la cadena original y ya sonaba. Puse este kit y la diferencia es enorme. La moto agarra diferente, más suave. Excelente."),
            ("Patricia V.", "Quevedo", 5, "Kit completo a buen precio. Mi mecánico me dijo que la calidad es muy buena comparada con otros kits genéricos. Llegó en 3 días."),
            ("Esteban M.", "Ambato", 4, "Muy buen producto. La única observación es que el manual de instalación viene en inglés. El kit en sí es de primera."),
        ],
        "related": [6, 4, 7],
    },
    {
        "slug": "pastillas-ebc-fa",
        "name": "Pastillas de Freno EBC FA Series",
        "cat": "Partes y Piezas",
        "price": "19.99",
        "original": "28.99",
        "discount": "31",
        "sku": "ALF-PAR-002",
        "img": "1585747860715-2ba37e788b70",
        "img2": "1558980394-4c7c9299fe96",
        "img3": "1504215680853-026ed2a45def",
        "badge": "🔴 Seguridad",
        "stars": "4.9", "reviews_count": "186",
        "hook": "Cuando frenas, no hay segunda oportunidad.",
        "short_desc": "Pastillas de freno EBC FA Series en compuesto orgánico de alta fricción, sin período de rodaje, fade resistente y compatibles con la mayoría de motos del mercado.",
        "features": [
            ("🛑", "Sin Break-in", "Máxima fricción desde la primera frenada, sin período de rodaje"),
            ("🌡️", "Fade Resistente", "Mantienen coeficiente a 350°C — sin fade en bajadas largas"),
            ("📏", "Precisión OEM", "Geometría idéntica a la pieza original, sin rectificado"),
            ("♻️", "Sin Metales Pesados", "Compuesto libre de asbesto y cobre — frenas limpio"),
        ],
        "specs": [
            ("Compuesto", "Orgánico FA Series"),
            ("Temperatura máx.", "350°C sostenidos"),
            ("Coeficiente fricción", "0.45 µ (estable caliente/frío)"),
            ("Break-in", "No requerido"),
            ("Compatibilidad", "Ver tabla de aplicación por modelo"),
            ("Placa soporte", "Acero estampado anti-corrosión"),
            ("Asbesto", "No"),
            ("Garantía", "18 meses o 15,000 km"),
        ],
        "desc": "Las pastillas de freno son el componente de seguridad con mayor relación importancia/precio de toda la moto. Y son las que más se descuidan.<br><br>Las EBC FA Series usan un compuesto orgánico que alcanza su coeficiente de fricción máximo desde la primera frenada — sin el período de rodaje de 200 km que requieren otras pastillas. En frenadas de emergencia, eso es la diferencia entre parar a tiempo o no.<br><br>El compuesto mantiene 0.45 µ desde temperatura ambiente hasta 350°C sostenidos. Ni en bajadas de volcán pierden el mordiente. No hay excusa para no tener pastillas buenas — cuestan menos que un tanque de gasolina.",
        "reviews": [
            ("Nelson T.", "Quito", 5, "Las monté y la diferencia es inmediata. El freno muerde desde el primer jalón. Las originales se sentían esponjosas comparadas con estas."),
            ("Carmen R.", "Guayaquil", 5, "Las recomendó mi mecánico de confianza. Llevo 4,000 km y siguen perfectas. Para moto urbana de Guayaquil, ideales."),
            ("Luis A.", "Loja", 5, "Precio increíble para la calidad. Las EBC son marca reconocida en todo el mundo. Perfecto que Alfapro las tenga disponibles en Ecuador."),
        ],
        "related": [5, 4, 7],
    },
    {
        "slug": "aceite-motul-7100",
        "name": "Aceite Motul 7100 4T 10W-40 1L",
        "cat": "Motor",
        "price": "15.99",
        "original": "21.99",
        "discount": "27",
        "sku": "ALF-MOT-001",
        "img": "1746014995485-e8a698f39804",
        "img2": "1776264762509-60b8091cfb20",
        "img3": "1504215680853-026ed2a45def",
        "badge": "💚 100% Sintético",
        "stars": "4.9", "reviews_count": "312",
        "hook": "El lubricante que el motor de competición necesita. Para tu moto de calle.",
        "short_desc": "Aceite 100% sintético con tecnología Éster para motores 4T. Protección extrema en arranque frío y alta temperatura. JASO MA2 certificado.",
        "features": [
            ("⚗️", "Tecnología Éster", "Lubricación molecular que recubre las superficies metálicas 24/7"),
            ("🌡️", "Rango Extremo", "Viscosidad estable de -20°C hasta 150°C de temperatura de aceite"),
            ("✅", "JASO MA2", "Certificación obligatoria para motos con embrague en baño de aceite"),
            ("⏱️", "Intervalo Extendido", "Hasta 5,000 km entre cambios con motor en perfecto estado"),
        ],
        "specs": [
            ("Tipo", "100% Sintético"),
            ("Viscosidad", "SAE 10W-40"),
            ("Norma API", "SN"),
            ("Certificación", "JASO MA2"),
            ("Volumen", "1 litro"),
            ("Intervalo cambio", "5,000 km (uso normal)"),
            ("Temperatura mín.", "-20°C"),
            ("Temperatura máx.", "+150°C aceite"),
        ],
        "desc": "El motor de tu moto tiene tolerancias de décimas de milímetro entre pistón y cilindro. La película de aceite que separa esas superficies tiene un grosor medido en micras. Si esa película falla — en el arranque frío, en la subida de la sierra, en el tráfico de Guayaquil — el daño es irreversible y costoso.<br><br>El Motul 7100 con tecnología Éster forma una capa de lubricación molecular que se adhiere a las superficies metálicas incluso cuando el motor está parado. Eso significa que desde el primer giro del arranque, hay protección — no 30 segundos después cuando el aceite convencional finalmente circula.<br><br>Para motos con embrague húmedo (la mayoría de motos 125-400cc del mercado ecuatoriano), la certificación JASO MA2 es obligatoria. El Motul 7100 la tiene.",
        "reviews": [
            ("Hernán G.", "Quito", 5, "Uso Motul 7100 desde hace 3 años en mi Yamaha FZ. El motor suena diferente, más silencioso y fluido. No cambio de marca."),
            ("Sandra M.", "Guayaquil", 5, "Mi mecánico me dijo que el 7100 es lo mejor que le puedo poner a mi Honda. Compré 6 litros para tener en casa. Precio muy bueno en Alfapro."),
            ("Ricardo P.", "Cuenca", 5, "Excelente aceite para la sierra. Con otros aceites el motor sonaba más a las mañanas frías. Con el Motul, arranca suave desde el primer segundo."),
        ],
        "related": [6, 5, 8],
    },
    {
        "slug": "kit-led-h4",
        "name": "Kit LED H4 Canbus 6000K Plug & Play",
        "cat": "Eléctrico",
        "price": "39.99",
        "original": "59.99",
        "discount": "33",
        "sku": "ALF-ELE-001",
        "img": "1711150943978-8d045550dd33",
        "img2": "1492144534655-ae79c964c9d7",
        "img3": "1504215680853-026ed2a45def",
        "badge": "⚡ Plug & Play",
        "stars": "4.7", "reviews_count": "221",
        "hook": "Ve y sé visto. La diferencia entre un percance y llegar a casa.",
        "short_desc": "Kit de conversión LED H4 con tecnología Canbus anti-error, luz blanca 6000K, 200% más brillo que halógena original. Instalación en 5 minutos.",
        "features": [
            ("💡", "200% Más Brillo", "2,800 lumens vs. 1,100 lumens de la halógena estándar H4"),
            ("🔌", "Canbus Anti-error", "Resistencia interna que previene códigos de error en el tablero"),
            ("❄️", "6000K Luz Día", "Temperatura de color 6000K — máxima visibilidad en lluvia y noche"),
            ("💧", "IP68 Sellado", "Resistente a lluvia, polvo, lavados a presión"),
        ],
        "specs": [
            ("Base", "H4 (bi-foco: cruce y carretera)"),
            ("Voltaje", "9-32V (moto, carro, camión)"),
            ("Potencia", "35W por bombillo"),
            ("Flujo", "2,800 lm por bombillo"),
            ("Temperatura color", "6000K (blanco día)"),
            ("Canbus", "Sí, anti-error integrado"),
            ("IP", "IP68 (sumergible)"),
            ("Vida útil", "50,000 horas"),
        ],
        "desc": "La halógena de fábrica en tu moto fue diseñada para un presupuesto de manufactura, no para tu seguridad nocturna. Con 1,100 lúmenes proyecta luz apenas 40 metros hacia adelante. No es suficiente para reaccionar a tiempo a un bache, un perro, o un carro sin luces a 70 km/h.<br><br>El Kit LED H4 6000K entrega 2,800 lúmenes — 200% más brillo, 90 metros de visión adelante. La temperatura de color 6000K simula la luz del día, que el ojo humano procesa más rápido que la amarilla de una halógena.<br><br>El sistema Canbus integrado evita que el tablero de tu moto muestre error de bombillo — el problema más común en conversiones LED baratas. Plug & Play significa que conectas igual que la original: sin cortar cables, sin relay externo, sin conocimiento técnico.",
        "reviews": [
            ("David C.", "Santo Domingo", 5, "Instalé en 5 minutos en mi Yamaha YBR. La diferencia nocturna es brutal. Ya me han preguntado 4 personas qué bombillo tengo. 100% recomendado."),
            ("Marcelo V.", "Ibarra", 5, "Sin error en el tablero. Sin modificaciones. Solo enchufar y listo. El brillo es impresionante. Por este precio es una ganga total."),
            ("Natalia F.", "Loja", 4, "Excelente luz. En lluvia marca una diferencia enorme. Le quito una estrella porque el calor del disipador es bastante — normal en LED pero igual vale mencionar."),
        ],
        "related": [6, 5, 4],
    },
    {
        "slug": "llanta-michelin-pilot",
        "name": "Llanta Michelin Pilot Street 2 140/70-17",
        "cat": "Llantas",
        "price": "89.99",
        "original": "119.99",
        "discount": "25",
        "sku": "ALF-LLA-001",
        "img": "1763142185959-be6f3dbdd31a",
        "img2": "1492144534655-ae79c964c9d7",
        "img3": "1504215680853-026ed2a45def",
        "badge": "🇫🇷 Michelin",
        "stars": "4.9", "reviews_count": "167",
        "hook": "La única llanta que tu moto necesita. Para todo clima, todo asfalto.",
        "short_desc": "Llanta trasera Michelin Pilot Street 2 en compuesto 2CT para clima tropical. Freno en mojado mejorado 20%, duración +30% sobre genéricas. Para motos 125cc+.",
        "features": [
            ("🌧️", "Freno Mojado +20%", "Compuesto 2CT, el mismo de las Pilot Power de MotoGP adaptado a calle"),
            ("📐", "Durabilidad +30%", "Centro de llanta en compuesto duro, hombros en compuesto agarre"),
            ("🏙️", "Urban + Highway", "Perfilado para pavimento latinoamericano: baches, adoquín, autopista"),
            ("🌡️", "Clima Tropical", "Formulado específicamente para temperaturas 20°C–40°C del litoral y sierra"),
        ],
        "specs": [
            ("Medida", "140/70-17 TL"),
            ("Posición", "Trasera"),
            ("Tecnología", "2CT (Dual Compound)"),
            ("Índice velocidad", "H (hasta 210 km/h)"),
            ("Índice carga", "66 (300 kg)"),
            ("Uso", "Road / Urban"),
            ("Compatible", "125cc, 150cc, 200cc, 250cc Honda/Yamaha/Suzuki"),
            ("País origen", "Francia"),
        ],
        "desc": "En las calles ecuatorianas llueve fuerte y de repente. Un adoquín mojado a 60 km/h con una llanta genérica es una lotería. Con la Michelin Pilot Street 2, es física — y la física dice que frenas.<br><br>La tecnología 2CT usa dos compuestos distintos en la misma llanta: el centro (para kilómetros de autopista) en caucho más duro y duradero; los hombros (para las curvas y frenadas) en compuesto más blando y adherente. Resultado: dura más que una llanta de compuesto único y agarra mejor en mojado.<br><br>La Pilot Street 2 fue formulada específicamente para el clima tropical: temperatura promedio 25°C y lluvia frecuente. No es una llanta europea adaptada — fue diseñada para rutas como las nuestras.",
        "reviews": [
            ("Omar S.", "Guayaquil", 5, "Con mi llanta anterior patiné dos veces en lluvia. Con la Michelin, frenar en mojado se siente completamente diferente. Mucho más controlado y seguro."),
            ("Patricia H.", "Manabí", 5, "Perfecta para las rutas de la costa. Llevo 8,000 km y sigue en buen estado. Con las genéricas a los 5,000 ya veía desgaste asimétrico."),
            ("Rodrigo F.", "Quito", 5, "Monté en mi Honda CB190 y la diferencia en curva es inmediata. En la bajada hacia Mindo, cero miedo. Michelin es Michelin."),
        ],
        "related": [6, 5, 7],
    },
]

# Shared CSS for product pages (extracted design system)
SHARED_CSS = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --green: #9BC42A;
      --green-glow: rgba(155, 196, 42, 0.4);
      --green-subtle: rgba(155, 196, 42, 0.08);
      --bg: #0a0a0a;
      --card: #141414;
      --card-border: rgba(255,255,255,0.07);
      --white: #f5f5f5;
      --muted: rgba(255,255,255,0.45);
      --radius: 16px;
    }
    html { scroll-behavior: smooth; }
    body { font-family: 'Inter Tight', sans-serif; background: var(--bg); color: var(--white); overflow-x: hidden; }

    /* NAV */
    nav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      height: 68px; display: flex; align-items: center; justify-content: space-between;
      padding: 0 48px;
      backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
      background: rgba(10,10,10,0.85);
      border-bottom: 1px solid var(--card-border);
    }
    .nav-logo { text-decoration: none; display: flex; align-items: center; }
    .nav-logo img { height: 44px; width: auto; }
    .nav-links { display: flex; gap: 32px; list-style: none; }
    .nav-links a { color: var(--muted); text-decoration: none; font-size: 13px; font-weight: 500; letter-spacing: 0.06em; transition: color 0.2s; }
    .nav-links a:hover { color: var(--white); }
    .nav-right { display: flex; align-items: center; gap: 20px; }
    .cart-btn {
      position: relative; display: flex; align-items: center; gap: 8px;
      padding: 9px 20px; border-radius: 999px;
      background: var(--green); color: #0a0a0a;
      font-size: 13px; font-weight: 700; letter-spacing: 0.04em;
      text-decoration: none; border: none; cursor: pointer;
      transition: background 0.2s, transform 0.15s;
    }
    .cart-btn:hover { background: #b8e03a; transform: scale(1.03); }
    .cart-count {
      position: absolute; top: -6px; right: -6px;
      width: 18px; height: 18px; border-radius: 50%;
      background: #ff4444; color: #fff;
      font-size: 10px; font-weight: 800;
      display: flex; align-items: center; justify-content: center;
    }

    /* BREADCRUMB */
    .breadcrumb {
      padding: 100px 80px 0;
      display: flex; gap: 8px; align-items: center;
      font-size: 12px; color: var(--muted);
    }
    .breadcrumb a { color: var(--muted); text-decoration: none; transition: color 0.2s; }
    .breadcrumb a:hover { color: var(--green); }
    .breadcrumb span { color: rgba(255,255,255,0.2); }
    .breadcrumb .current { color: var(--white); }

    /* PRODUCT MAIN */
    .product-main {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 72px;
      padding: 36px 80px 80px;
      max-width: 1400px;
      margin: 0 auto;
    }

    /* GALLERY */
    .gallery { display: flex; flex-direction: column; gap: 12px; }
    .gallery-main {
      border-radius: 20px; overflow: hidden;
      border: 1px solid var(--card-border);
      aspect-ratio: 4/3; position: relative;
    }
    .gallery-main img { width: 100%; height: 100%; object-fit: cover; }
    .gallery-badge-img {
      position: absolute; top: 16px; left: 16px;
      padding: 6px 14px; border-radius: 999px;
      font-size: 12px; font-weight: 700;
      backdrop-filter: blur(8px);
      background: rgba(10,10,10,0.7);
      border: 1px solid var(--card-border);
    }
    .gallery-thumbs { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
    .thumb {
      border-radius: 12px; overflow: hidden;
      border: 1px solid var(--card-border);
      aspect-ratio: 4/3; cursor: pointer; transition: border-color 0.2s;
    }
    .thumb:hover, .thumb.active { border-color: var(--green); }
    .thumb img { width: 100%; height: 100%; object-fit: cover; }

    /* PRODUCT INFO */
    .product-info { display: flex; flex-direction: column; gap: 20px; padding-top: 4px; }

    .product-badge {
      display: inline-flex; align-items: center; gap: 6px;
      padding: 5px 14px; border-radius: 999px; width: fit-content;
      font-size: 11px; font-weight: 700; letter-spacing: 0.06em;
      background: rgba(155,196,42,0.12);
      border: 1px solid rgba(155,196,42,0.3);
      color: var(--green);
    }
    .product-cat {
      font-size: 11px; font-weight: 700; letter-spacing: 0.18em;
      text-transform: uppercase; color: var(--green);
    }
    .product-name {
      font-size: clamp(28px, 3vw, 44px); font-weight: 800;
      line-height: 1; letter-spacing: -0.03em;
    }
    .product-stars { display: flex; align-items: center; gap: 10px; }
    .stars { display: flex; gap: 2px; }
    .star { color: #f5c542; font-size: 16px; }
    .star.half { opacity: 0.5; }
    .rating-num { font-size: 14px; font-weight: 700; color: var(--white); }
    .rating-count { font-size: 13px; color: var(--muted); }

    .price-block { display: flex; align-items: baseline; gap: 12px; }
    .price-current { font-size: 48px; font-weight: 800; letter-spacing: -0.04em; color: var(--green); }
    .price-original { font-size: 20px; color: var(--muted); text-decoration: line-through; }
    .price-save {
      padding: 4px 10px; border-radius: 6px;
      background: rgba(155,196,42,0.15);
      color: var(--green); font-size: 12px; font-weight: 700;
    }

    .divider { height: 1px; background: var(--card-border); }

    /* VARIANTS */
    .label-sm { font-size: 12px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); margin-bottom: 8px; }
    .variant-row { display: flex; gap: 8px; flex-wrap: wrap; }
    .variant-btn {
      padding: 8px 18px; border-radius: 8px;
      border: 1px solid var(--card-border);
      background: transparent; color: var(--white);
      font-size: 13px; font-weight: 600; cursor: pointer;
      transition: all 0.2s; font-family: 'Inter Tight', sans-serif;
    }
    .variant-btn:hover { border-color: var(--green); color: var(--green); }
    .variant-btn.active { border-color: var(--green); background: rgba(155,196,42,0.12); color: var(--green); }

    /* CTA */
    .qty-row { display: flex; align-items: center; gap: 16px; }
    .qty-control { display: flex; align-items: center; gap: 0; border: 1px solid var(--card-border); border-radius: 10px; overflow: hidden; }
    .qty-btn {
      width: 40px; height: 44px;
      background: transparent; border: none; color: var(--white);
      font-size: 20px; font-weight: 300; cursor: pointer;
      transition: background 0.2s; font-family: 'Inter Tight', sans-serif;
    }
    .qty-btn:hover { background: rgba(255,255,255,0.05); }
    .qty-num { width: 44px; text-align: center; font-size: 15px; font-weight: 700; }

    .cta-primary {
      flex: 1; padding: 16px 32px; border-radius: 12px;
      background: var(--green); color: #0a0a0a;
      font-size: 15px; font-weight: 800; letter-spacing: 0.04em;
      border: none; cursor: pointer;
      transition: background 0.2s, transform 0.15s;
      font-family: 'Inter Tight', sans-serif;
    }
    .cta-primary:hover { background: #b8e03a; transform: scale(1.02); }

    .cta-ghost {
      padding: 16px 28px; border-radius: 12px;
      background: transparent; color: var(--white);
      font-size: 14px; font-weight: 700;
      border: 1px solid var(--card-border); cursor: pointer;
      transition: all 0.2s; font-family: 'Inter Tight', sans-serif;
    }
    .cta-ghost:hover { border-color: rgba(255,255,255,0.3); }

    /* TRUST BADGES */
    .trust-row { display: flex; gap: 0; border: 1px solid var(--card-border); border-radius: 12px; overflow: hidden; }
    .trust-item {
      flex: 1; padding: 12px 10px; text-align: center;
      border-right: 1px solid var(--card-border);
    }
    .trust-item:last-child { border-right: none; }
    .trust-icon { font-size: 20px; margin-bottom: 4px; }
    .trust-label { font-size: 10px; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; }

    /* FEATURES STRIP */
    .features-strip {
      padding: 56px 80px;
      background: var(--card);
      border-top: 1px solid var(--card-border);
      border-bottom: 1px solid var(--card-border);
    }
    .features-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px; max-width: 1400px; margin: 0 auto; }
    .feature-item { display: flex; gap: 16px; align-items: flex-start; }
    .feature-icon { font-size: 28px; flex-shrink: 0; margin-top: 2px; }
    .feature-title { font-size: 14px; font-weight: 800; letter-spacing: -0.01em; margin-bottom: 4px; }
    .feature-desc { font-size: 12px; color: var(--muted); line-height: 1.6; }

    /* TABS */
    .tabs-section { padding: 72px 80px; max-width: 1400px; margin: 0 auto; }
    .tabs-nav { display: flex; gap: 0; border-bottom: 1px solid var(--card-border); margin-bottom: 40px; }
    .tab-btn {
      padding: 14px 28px; background: none; border: none;
      color: var(--muted); font-size: 14px; font-weight: 700;
      letter-spacing: 0.04em; cursor: pointer;
      border-bottom: 2px solid transparent; margin-bottom: -1px;
      transition: all 0.2s; font-family: 'Inter Tight', sans-serif;
    }
    .tab-btn.active { color: var(--green); border-bottom-color: var(--green); }
    .tab-content { display: none; }
    .tab-content.active { display: block; }

    /* Description */
    .desc-text { font-size: 15px; color: rgba(255,255,255,0.75); line-height: 1.8; max-width: 680px; }

    /* Specs table */
    .specs-table { width: 100%; border-collapse: collapse; max-width: 680px; }
    .specs-table tr { border-bottom: 1px solid var(--card-border); }
    .specs-table td { padding: 12px 0; font-size: 14px; }
    .specs-table td:first-child { color: var(--muted); width: 40%; font-weight: 500; }
    .specs-table td:last-child { color: var(--white); font-weight: 600; }

    /* Reviews */
    .reviews-grid { display: flex; flex-direction: column; gap: 24px; max-width: 680px; }
    .review-card {
      padding: 24px; border-radius: 16px;
      background: var(--card); border: 1px solid var(--card-border);
    }
    .review-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px; }
    .reviewer-name { font-size: 14px; font-weight: 800; }
    .reviewer-loc { font-size: 12px; color: var(--muted); margin-top: 2px; }
    .review-stars { display: flex; gap: 2px; }
    .review-text { font-size: 14px; color: rgba(255,255,255,0.7); line-height: 1.7; }

    /* RELATED */
    .related-section { padding: 72px 80px; border-top: 1px solid var(--card-border); }
    .related-section .section-title { font-size: clamp(28px,3vw,40px); font-weight: 800; letter-spacing: -0.03em; margin-bottom: 40px; }
    .related-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 1400px; }
    .related-card {
      border-radius: 16px; overflow: hidden;
      border: 1px solid var(--card-border); background: var(--card);
      text-decoration: none; color: var(--white);
      transition: border-color 0.2s, transform 0.2s;
    }
    .related-card:hover { border-color: rgba(155,196,42,0.4); transform: translateY(-4px); }
    .related-img { aspect-ratio: 4/3; overflow: hidden; }
    .related-img img { width: 100%; height: 100%; object-fit: cover; filter: brightness(0.75); transition: filter 0.3s; }
    .related-card:hover .related-img img { filter: brightness(0.9); }
    .related-info { padding: 16px 20px 20px; }
    .related-cat { font-size: 10px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--green); margin-bottom: 4px; }
    .related-name { font-size: 14px; font-weight: 800; letter-spacing: -0.01em; margin-bottom: 8px; }
    .related-price { font-size: 18px; font-weight: 800; color: var(--green); letter-spacing: -0.02em; }

    /* FOOTER */
    footer {
      background: #060606; border-top: 1px solid var(--card-border);
      padding: 48px 80px 28px; margin-top: 0;
    }
    .footer-bottom { display: flex; justify-content: space-between; align-items: center; padding-top: 28px; border-top: 1px solid var(--card-border); }
    .footer-copy { font-size: 12px; color: var(--muted); }
    .footer-links { display: flex; gap: 24px; }
    .footer-links a { font-size: 12px; color: var(--muted); text-decoration: none; }
    .footer-links a:hover { color: var(--white); }

    /* TOAST NOTIFICATION */
    .toast {
      position: fixed; bottom: 32px; right: 32px; z-index: 999;
      padding: 16px 24px; border-radius: 12px;
      background: var(--card); border: 1px solid rgba(155,196,42,0.4);
      display: flex; align-items: center; gap: 12px;
      font-size: 14px; font-weight: 600;
      transform: translateY(80px); opacity: 0;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
      pointer-events: none;
    }
    .toast.show { transform: translateY(0); opacity: 1; }
    .toast-icon { font-size: 20px; }

    @media (max-width: 960px) {
      nav { padding: 0 24px; }
      .breadcrumb { padding: 88px 24px 0; }
      .product-main { grid-template-columns: 1fr; padding: 24px 24px 60px; gap: 40px; }
      .features-strip { padding: 40px 24px; }
      .features-grid { grid-template-columns: 1fr 1fr; gap: 24px; }
      .tabs-section, .related-section { padding: 48px 24px; }
      .related-grid { grid-template-columns: 1fr 1fr; }
      footer { padding: 40px 24px 24px; }
    }
"""

def stars_html(rating):
    full = int(float(rating))
    frac = float(rating) - full
    html = ""
    for i in range(full):
        html += '<span class="star">★</span>'
    if frac >= 0.5:
        html += '<span class="star half">★</span>'
    return html

def related_card(p, rel_idx):
    rel = PRODUCTS[rel_idx]
    return f"""
      <a href="{rel['slug']}.html" class="related-card">
        <div class="related-img"><img src="https://images.unsplash.com/photo-{rel['img']}?w=600&q=80" alt="{rel['name']}" loading="lazy"/></div>
        <div class="related-info">
          <div class="related-cat">{rel['cat']}</div>
          <div class="related-name">{rel['name']}</div>
          <div class="related-price">${rel['price']}</div>
        </div>
      </a>"""

def generate_product_page(p, idx):
    related_html = "".join(related_card(p, r) for r in p['related'] if r < len(PRODUCTS))
    features_html = "".join(f"""
      <div class="feature-item">
        <div class="feature-icon">{f[0]}</div>
        <div>
          <div class="feature-title">{f[1]}</div>
          <div class="feature-desc">{f[2]}</div>
        </div>
      </div>""" for f in p['features'])

    specs_html = "".join(f"""
      <tr><td>{s[0]}</td><td>{s[1]}</td></tr>""" for s in p['specs'])

    reviews_html = "".join(f"""
      <div class="review-card">
        <div class="review-header">
          <div>
            <div class="reviewer-name">{r[0]}</div>
            <div class="reviewer-loc">📍 {r[1]}</div>
          </div>
          <div class="review-stars">{"★" * r[2]}</div>
        </div>
        <p class="review-text">"{r[3]}"</p>
      </div>""" for r in p['reviews'])

    # Variants (tallas for helmets/gloves, liters for oil, size for tires)
    if p['cat'] in ['Cascos']:
        variants_section = """
      <div>
        <div class="label-sm">Talla</div>
        <div class="variant-row">
          <button class="variant-btn" onclick="selectVar(this)">XS</button>
          <button class="variant-btn active" onclick="selectVar(this)">S</button>
          <button class="variant-btn" onclick="selectVar(this)">M</button>
          <button class="variant-btn" onclick="selectVar(this)">L</button>
          <button class="variant-btn" onclick="selectVar(this)">XL</button>
          <button class="variant-btn" onclick="selectVar(this)">XXL</button>
        </div>
      </div>
      <div>
        <div class="label-sm">Color</div>
        <div class="variant-row">
          <button class="variant-btn active" onclick="selectVar(this)">Negro Mate</button>
          <button class="variant-btn" onclick="selectVar(this)">Blanco Perla</button>
          <button class="variant-btn" onclick="selectVar(this)">Rojo Racing</button>
        </div>
      </div>"""
    elif p['cat'] == 'Accesorios Piloto' and 'Guantes' in p['name']:
        variants_section = """
      <div>
        <div class="label-sm">Talla</div>
        <div class="variant-row">
          <button class="variant-btn" onclick="selectVar(this)">S</button>
          <button class="variant-btn active" onclick="selectVar(this)">M</button>
          <button class="variant-btn" onclick="selectVar(this)">L</button>
          <button class="variant-btn" onclick="selectVar(this)">XL</button>
          <button class="variant-btn" onclick="selectVar(this)">2XL</button>
        </div>
      </div>"""
    elif p['cat'] == 'Motor':
        variants_section = """
      <div>
        <div class="label-sm">Cantidad</div>
        <div class="variant-row">
          <button class="variant-btn active" onclick="selectVar(this)">1 Litro</button>
          <button class="variant-btn" onclick="selectVar(this)">4 Litros (Pack)</button>
        </div>
      </div>"""
    elif p['cat'] == 'Llantas':
        variants_section = """
      <div>
        <div class="label-sm">Posición</div>
        <div class="variant-row">
          <button class="variant-btn" onclick="selectVar(this)">Delantera 100/80-17</button>
          <button class="variant-btn active" onclick="selectVar(this)">Trasera 140/70-17</button>
        </div>
      </div>"""
    elif p['cat'] == 'Partes y Piezas' and 'Cadena' in p['name']:
        variants_section = """
      <div>
        <div class="label-sm">Configuración Piñón</div>
        <div class="variant-row">
          <button class="variant-btn active" onclick="selectVar(this)">14T (estándar)</button>
          <button class="variant-btn" onclick="selectVar(this)">15T (+velocidad)</button>
        </div>
      </div>
      <div>
        <div class="label-sm">Corona</div>
        <div class="variant-row">
          <button class="variant-btn active" onclick="selectVar(this)">45T (estándar)</button>
          <button class="variant-btn" onclick="selectVar(this)">48T (+torque)</button>
        </div>
      </div>"""
    elif p['cat'] == 'Eléctrico':
        variants_section = """
      <div>
        <div class="label-sm">Temperatura Color</div>
        <div class="variant-row">
          <button class="variant-btn active" onclick="selectVar(this)">6000K Blanco Día</button>
          <button class="variant-btn" onclick="selectVar(this)">8000K Azul Glacial</button>
        </div>
      </div>"""
    else:
        variants_section = ""

    checkout_params = f"producto={p['slug']}&nombre={p['name'].replace(' ', '+')}&precio={p['price']}&img={p['img']}&cat={p['cat'].replace(' ', '+')}"

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p['name']} — Alfapro Ecuador</title>
  <meta name="description" content="{p['short_desc']}" />
  <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <style>{SHARED_CSS}</style>
</head>
<body>

<!-- NAV -->
<nav>
  <a href="../index.html" class="nav-logo"><img src="../logo.png" alt="Alfapro" /></a>
  <ul class="nav-links">
    <li><a href="../index.html#categorias">Categorías</a></li>
    <li><a href="../index.html#productos">Productos</a></li>
    <li><a href="../index.html#nosotros">Nosotros</a></li>
    <li><a href="../index.html#sucursales">Sucursales</a></li>
  </ul>
  <div class="nav-right">
    <a href="../checkout.html?{checkout_params}" class="cart-btn">
      🛒 Carrito
      <span class="cart-count" id="cartCount">0</span>
    </a>
  </div>
</nav>

<!-- BREADCRUMB -->
<div class="breadcrumb">
  <a href="../index.html">Inicio</a>
  <span>/</span>
  <a href="../index.html#categorias">{p['cat']}</a>
  <span>/</span>
  <span class="current">{p['name']}</span>
</div>

<!-- PRODUCT MAIN GRID -->
<div class="product-main">

  <!-- GALLERY -->
  <div class="gallery">
    <div class="gallery-main">
      <img id="mainImg" src="https://images.unsplash.com/photo-{p['img']}?w=900&q=85" alt="{p['name']}" />
      <div class="gallery-badge-img">{p['badge']}</div>
    </div>
    <div class="gallery-thumbs">
      <div class="thumb active" onclick="setImg('https://images.unsplash.com/photo-{p['img']}?w=900&q=85', this)">
        <img src="https://images.unsplash.com/photo-{p['img']}?w=300&q=70" alt="Vista 1" loading="lazy"/>
      </div>
      <div class="thumb" onclick="setImg('https://images.unsplash.com/photo-{p['img2']}?w=900&q=85', this)">
        <img src="https://images.unsplash.com/photo-{p['img2']}?w=300&q=70" alt="Vista 2" loading="lazy"/>
      </div>
      <div class="thumb" onclick="setImg('https://images.unsplash.com/photo-{p['img3']}?w=900&q=85', this)">
        <img src="https://images.unsplash.com/photo-{p['img3']}?w=300&q=70" alt="Vista 3" loading="lazy"/>
      </div>
    </div>
  </div>

  <!-- PRODUCT INFO -->
  <div class="product-info">
    <div>
      <div class="product-cat">{p['cat']}</div>
    </div>
    <div class="product-badge">{p['badge']}</div>
    <h1 class="product-name">{p['name']}</h1>
    <p style="font-size:16px;color:rgba(255,255,255,0.6);line-height:1.7;font-style:italic;">"{p['hook']}"</p>

    <div class="product-stars">
      <div class="stars">{stars_html(p['stars'])}</div>
      <span class="rating-num">{p['stars']}</span>
      <span class="rating-count">({p['reviews_count']} reseñas)</span>
    </div>

    <div class="divider"></div>

    <div class="price-block">
      <span class="price-current">${p['price']}</span>
      <span class="price-original">${p['original']}</span>
      <span class="price-save">−{p['discount']}%</span>
    </div>

    <p style="font-size:14px;color:rgba(255,255,255,0.6);line-height:1.65;">{p['short_desc']}</p>

    <div class="divider"></div>

    {variants_section}

    <div>
      <div class="label-sm">Cantidad</div>
      <div class="qty-row">
        <div class="qty-control">
          <button class="qty-btn" onclick="changeQty(-1)">−</button>
          <span class="qty-num" id="qtyNum">1</span>
          <button class="qty-btn" onclick="changeQty(1)">+</button>
        </div>
        <button class="cta-primary" onclick="addToCart()">🛒 Agregar al carrito</button>
        <button class="cta-ghost" title="Guardar">♡</button>
      </div>
    </div>

    <a href="../checkout.html?{checkout_params}" class="cta-primary" style="display:block;text-align:center;text-decoration:none;">
      ⚡ Comprar ahora
    </a>

    <div class="trust-row">
      <div class="trust-item">
        <div class="trust-icon">🚚</div>
        <div class="trust-label">Envío 48h</div>
      </div>
      <div class="trust-item">
        <div class="trust-icon">🔒</div>
        <div class="trust-label">Pago Seguro</div>
      </div>
      <div class="trust-item">
        <div class="trust-icon">↩️</div>
        <div class="trust-label">30 Días Dev.</div>
      </div>
      <div class="trust-item">
        <div class="trust-icon">📞</div>
        <div class="trust-label">Soporte 24/7</div>
      </div>
    </div>

    <div style="font-size:12px;color:var(--muted);display:flex;gap:8px;align-items:center;">
      <span>✅ En stock — </span><span>SKU: {p['sku']}</span>
    </div>
  </div>
</div>

<!-- FEATURES STRIP -->
<section class="features-strip">
  <div class="features-grid">
    {features_html}
  </div>
</section>

<!-- TABS: Descripción / Specs / Reviews -->
<section class="tabs-section">
  <div class="tabs-nav">
    <button class="tab-btn active" onclick="openTab(event, 'desc')">Descripción</button>
    <button class="tab-btn" onclick="openTab(event, 'specs')">Especificaciones</button>
    <button class="tab-btn" onclick="openTab(event, 'reviews')">Reseñas ({p['reviews_count']})</button>
  </div>

  <div id="desc" class="tab-content active">
    <p class="desc-text">{p['desc']}</p>
  </div>

  <div id="specs" class="tab-content">
    <table class="specs-table">
      {specs_html}
    </table>
  </div>

  <div id="reviews" class="tab-content">
    <div class="reviews-grid">
      {reviews_html}
    </div>
  </div>
</section>

<!-- RELATED PRODUCTS -->
<section class="related-section">
  <div style="max-width:1400px;">
    <h2 class="section-title">También te puede interesar</h2>
    <div class="related-grid">
      {related_html}
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-bottom">
    <span class="footer-copy">© 2024 Alfapro Ecuador — Todos los derechos reservados</span>
    <div class="footer-links">
      <a href="#">Política de Privacidad</a>
      <a href="#">Términos de Uso</a>
      <a href="#">Garantías</a>
    </div>
  </div>
</footer>

<!-- TOAST -->
<div class="toast" id="toast">
  <span class="toast-icon">✅</span>
  <span id="toastMsg">Producto agregado al carrito</span>
</div>

<script>
  let qty = 1;
  let cart = parseInt(localStorage.getItem('alfapro_cart') || '0');
  document.getElementById('cartCount').textContent = cart;

  function changeQty(delta) {{
    qty = Math.max(1, qty + delta);
    document.getElementById('qtyNum').textContent = qty;
  }}

  function addToCart() {{
    cart += qty;
    localStorage.setItem('alfapro_cart', cart);
    document.getElementById('cartCount').textContent = cart;
    showToast('{p['name'].replace("'", "\\'")} agregado al carrito 🛒');
  }}

  function showToast(msg) {{
    const t = document.getElementById('toast');
    document.getElementById('toastMsg').textContent = msg;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 3200);
  }}

  function setImg(src, el) {{
    document.getElementById('mainImg').src = src;
    document.querySelectorAll('.thumb').forEach(t => t.classList.remove('active'));
    el.classList.add('active');
  }}

  function selectVar(el) {{
    const row = el.parentElement;
    row.querySelectorAll('.variant-btn').forEach(b => b.classList.remove('active'));
    el.classList.add('active');
  }}

  function openTab(e, id) {{
    document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    e.target.classList.add('active');
  }}
</script>
</body>
</html>"""

# Generate all product pages
output_dir = os.path.join(BASE, "productos")
os.makedirs(output_dir, exist_ok=True)

for i, p in enumerate(PRODUCTS):
    html = generate_product_page(p, i)
    path = os.path.join(output_dir, f"{p['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ {p['slug']}.html ({len(html):,} chars)")

print(f"\nTotal: {len(PRODUCTS)} product pages generated in {output_dir}/")

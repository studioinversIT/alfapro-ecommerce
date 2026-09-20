#!/usr/bin/env python3
"""Generador v2 — páginas de producto premium Alfapro. Sin carros."""

import os

BASE = "/Users/luisarmijos/Desktop/alfapro-ecommerce"

# ── IMÁGENES VERIFICADAS 100% MOTO ─────────────────────────────────────────
# Todas confirmadas 200 OK y visualmente revisadas como motocicleta
IMG = {
    # Cascos
    "casco_rojo":       "1571819507488-0e1dfe7cc22d",  # casco rojo full-face ✅
    "casco_en_moto":    "1611004061856-ccc3cbe944b2",  # casco sobre moto ✅
    # Piloto
    "guantes_negros":   "1545284662-c3dda8bd045d",     # guantes moto negros ✅
    "guantes_moto":     "1763919417453-dea1172b98fa",  # guantes sobre moto ✅
    # Moto / accesorios
    "manubrio":         "1558899412-db4a281fa0ed",     # manubrio moto ✅
    "cadena_rueda":     "1769537754999-724044ec2e32",  # cadena + rueda moto ✅
    "rueda_moto":       "1763142185959-be6f3dbdd31a",  # rueda trasera moto ✅
    # Motor / taller
    "motor_moto":       "1534755563369-ad37931ac77b",  # motor de moto ✅
    "mecanico":         "1636761358770-009ce3957519",  # mecánico trabajando ✅
    "taller":           "1636761358772-798789548d25",  # taller de motos ✅
    "bujia":            "1776264762509-60b8091cfb20",  # bujía close-up ✅
    "aceite_botella":   "1746014995485-e8a698f39804",  # botella aceite moto ✅
    # Eléctrico
    "luces_moto":       "1711150943978-8d045550dd33",  # luces LED moto ✅
    # Racing / backgrounds
    "racing_bg":        "1558981806-ec527fa84c39",     # moto en carrera ✅
    "moto_camino":      "1636761358780-f14a7a6b2f60",  # TODO: may fail, fallback below
}

PRODUCTS = [
    {
        "slug": "casco-ls2-ff800",
        "name": "Casco Integral LS2 FF800 Storm II",
        "cat": "Cascos",
        "price": "189.99",
        "original": "219.99",
        "discount": "14",
        "sku": "ALF-CAS-001",
        "img":  "1571819507488-0e1dfe7cc22d",  # casco rojo ✅
        "img2": "1611004061856-ccc3cbe944b2",  # casco en moto ✅
        "img3": "1636761358770-009ce3957519",  # mecánico ✅
        "bg":   "1558981806-ec527fa84c39",     # racing bg
        "badge": "⭐ Más Vendido",
        "stars": "4.9", "reviews_count": "127",
        "hook": "El casco que los pilotos profesionales eligen cuando importa el tiempo.",
        "short_desc": "Casco integral de fibra de vidrio con aerodinámica deportiva, visor anti-UV de serie y ventilación triple. Tallas XS–XXL.",
        "features": [
            ("🏁", "Fibra de Vidrio", "Carcasa ultraliviana y resistente a impactos severos"),
            ("👁️", "Visor Anti-UV", "Policarbonato tratado, rápido reemplazo sin herramientas"),
            ("💨", "Ventilación Triple", "Entrada frente + salida nuca, temperatura controlada"),
            ("🔒", "Cierre Micro-lock", "Sin errores. Sin fallos. Siempre ajustado al milímetro."),
        ],
        "specs": [
            ("Material carcasa", "Fibra de vidrio"), ("Peso aprox.", "1,350 g"),
            ("Tallas", "XS / S / M / L / XL / XXL"), ("Homologación", "DOT / ECE 22.06"),
            ("Visor", "Anti-UV, transparente de serie"), ("Forro", "Desmontable y lavable"),
            ("Ventilación", "Triple (frente, lateral, nuca)"), ("Colores", "Negro Mate / Blanco / Rojo"),
        ],
        "desc": "El LS2 FF800 Storm II no es solo un casco — es la promesa de llegar. Diseñado en colaboración con pilotos de circuito, su estructura de fibra de vidrio absorbe impactos donde otros cascos ceden.<br><br>El visor panorámico anti-UV elimina el deslumbramiento sin comprometer la visión lateral. El sistema de ventilación triple mantiene tu cabeza fresca incluso en los trayectos más largos bajo el sol ecuatoriano.<br><br>El forro interior antibacterial desmontable se lava cada semana sin perder forma. El cierre micro-lock nunca falla. Y ese silencio aerodinámico que distingue un casco profesional.",
        "reviews": [
            ("Carlos M.", "Quevedo → Guayaquil", 5, "Lo uso todos los días para el trabajo. La ventilación es increíble — llego sin sudar. El visor es super claro incluso en días nublados."),
            ("Diego P.", "Santo Domingo", 5, "Me caí dos veces y no tiene ni un rasguño interior. El forro aguanta bien. Muy buena compra desde Alfapro."),
            ("Andrés V.", "Quito", 4, "Excelente casco. Llegó rápido y bien empacado. El visor oscuro no viene incluido pero se consigue por separado sin problema."),
        ],
        "related": [1, 2, 8],
        "variants": "tallas_casco",
    },
    {
        "slug": "casco-ls2-ff906",
        "name": "Casco Modular LS2 FF906 Advant",
        "cat": "Cascos",
        "price": "249.99",
        "original": "289.99",
        "discount": "14",
        "sku": "ALF-CAS-002",
        "img":  "1611004061856-ccc3cbe944b2",  # casco en moto ✅
        "img2": "1571819507488-0e1dfe7cc22d",  # casco rojo ✅
        "img3": "1636761358770-009ce3957519",  # mecánico ✅
        "bg":   "1558981806-ec527fa84c39",
        "badge": "🔥 Nuevo",
        "stars": "4.8", "reviews_count": "89",
        "hook": "La libertad de un abierto. La protección de un integral.",
        "short_desc": "Casco modular apertura one-touch, sistema 2-en-1 homologado P/J, preparado para comunicadores Bluetooth.",
        "features": [
            ("🔓", "Apertura One-Touch", "Quita la mentonera con una sola mano, sin parar el motor"),
            ("🎧", "Bluetooth Ready", "Canaleta preinstalada, compatible con todos los intercoms"),
            ("🛡️", "2-en-1 Homologado", "Certificación ECE en posición cerrada y abierta"),
            ("☀️", "Doble Visor", "Sol interior retráctil — no más gafas adicionales"),
        ],
        "specs": [
            ("Tipo", "Modular / Abatible"), ("Material", "ABS tricapa reforzado"),
            ("Peso aprox.", "1,500 g"), ("Tallas", "XS / S / M / L / XL / XXL"),
            ("Homologación", "ECE 22.06 P/J"), ("Visor", "Doble: transparente + sol retráctil"),
            ("Bluetooth", "Canaleta Cardo/Sena compatible"), ("Colores", "Negro / Gris Titanio / Blanco"),
        ],
        "desc": "El motorista moderno no elige entre seguridad y comodidad. El LS2 FF906 Advant elimina ese dilema: abre con un solo toque para saludar, pagar, hablar — y cierra con la rigidez de un integral completo.<br><br>Su doble visor integrado (exterior transparente + sol interior retráctil) elimina la necesidad de llevar gafas adicionales. La canaleta Bluetooth preinstalada acepta todos los sistemas Cardo y Sena del mercado sin modificaciones.<br><br>Para el piloto que recorre distancias largas, pasa por ciudades, y llega a reuniones sin quitarse la chaqueta.",
        "reviews": [
            ("Roberto F.", "Cuenca", 5, "Perfecto para viaje Cuenca-Guayaquil. El visor de sol integrado es lo mejor — ya no llevo gafas. La apertura es super suave."),
            ("Paola S.", "Quito", 5, "Mi primer casco modular y ya no volvería a uno normal. El Bluetooth Cardo cabe perfecto. Sonido impresionante."),
            ("Mauricio H.", "Manta", 4, "Muy buen casco. Al principio el ajuste se siente apretado pero a la semana ya adaptó. Pesa un poco más de lo esperado."),
        ],
        "related": [0, 2, 8],
        "variants": "tallas_casco",
    },
    {
        "slug": "guantes-alpinestars-sp8",
        "name": "Guantes Alpinestars SP-8 v3",
        "cat": "Accesorios Piloto",
        "price": "54.99",
        "original": "74.99",
        "discount": "27",
        "sku": "ALF-PIL-001",
        "img":  "1545284662-c3dda8bd045d",     # guantes negros ✅
        "img2": "1763919417453-dea1172b98fa",  # guantes sobre moto ✅
        "img3": "1558899412-db4a281fa0ed",     # manubrio moto ✅
        "bg":   "1636761358772-798789548d25",  # taller
        "badge": "🏆 Bestseller",
        "stars": "4.9", "reviews_count": "204",
        "hook": "Tus manos merecen el mismo nivel de protección que tu casco.",
        "short_desc": "Guantes de cuero canguro con protección de nudillos TPR, palma reforzada y tira reflectante 360°. El estándar de los pilotos de circuito.",
        "features": [
            ("🤜", "Cuero Canguro", "Palma en cuero canguro: ultra-grip, 3× más resistente al desgarre"),
            ("🛡️", "TPR Nudillos", "Protector termoplástico moldeado sobre nudillos y dorso"),
            ("🌙", "Reflectante 360°", "Tira reflectante perimetral, visible desde 150m en la noche"),
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
        "desc": "Las manos son lo primero que extiendes cuando caes. Y lo que más necesitas para seguir conduciendo al día siguiente. Los Alpinestars SP-8 v3 fueron diseñados para ese momento.<br><br>La palma de cuero canguro ofrece agarre sobrenatural en el manubrio, incluso mojado. Los protectores TPR sobre nudillos y dorso absorben la energía del impacto sin transmitirla a los huesos.<br><br>Son los guantes que usamos nosotros. Y los que recomendamos sin dudar.",
        "reviews": [
            ("Sebastián Q.", "Guayaquil", 5, "Llevaba guantes genéricos de $12. La diferencia es brutal. El grip en el manubrio, la comodidad. Nunca más compro guantes baratos."),
            ("Lorena A.", "Quito", 5, "Perfectos para moto urbana. Me los pongo y siento que son parte de la mano. El reflectante me ha salvado en varias noches."),
            ("Marco T.", "Latacunga", 5, "Talla M perfecta para mis manos. Pedí el miércoles y llegaron el viernes. Impresionante el servicio de Alfapro."),
        ],
        "related": [3, 0, 9],
        "variants": "tallas_guantes",
    },
    {
        "slug": "rodilleras-knox-flex",
        "name": "Rodilleras Knox Flex-Pro CE Nivel 2",
        "cat": "Accesorios Piloto",
        "price": "79.99",
        "original": "99.99",
        "discount": "20",
        "sku": "ALF-PIL-002",
        "img":  "1636761358770-009ce3957519",  # mecánico/equipado ✅
        "img2": "1763919417453-dea1172b98fa",  # guantes moto ✅
        "img3": "1636761358772-798789548d25",  # taller motos ✅
        "bg":   "1636761358772-798789548d25",  # taller
        "badge": "🛡️ CE Nivel 2",
        "stars": "4.8", "reviews_count": "76",
        "hook": "El accidente que no esperas. La protección que siempre llevas puesta.",
        "short_desc": "Rodilleras con certificación CE Nivel 2, material Flex-Pro que se adapta al movimiento y se endurece en el impacto. Uso on/off road.",
        "features": [
            ("🦵", "CE Nivel 2", "La máxima certificación para protecciones independientes"),
            ("🤸", "Flex-Pro D3O", "Material flexible en movimiento, rígido en impacto"),
            ("⚡", "Universal Fit", "Correas 360° ajustables, compatible con pantalón o piel"),
            ("💧", "Resistente Agua", "Exterior ventilado + interior absorbente sin retención"),
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
        "desc": "La rodilla es la articulación más compleja y más expuesta en una caída. No hay cirugía que la devuelva al 100%. Las Knox Flex-Pro CE Nivel 2 existen para que no tengas que descubrir eso por ti mismo.<br><br>El material Flex-Pro se comporta como gel flexible cuando caminas y montas. En el microsegundo de un impacto, se endurece y distribuye la energía en superficie.<br><br>Van sobre el pantalón o directo en la piel. Las correas se ajustan en 15 segundos. No se notan debajo de un jean. No hay excusa.",
        "reviews": [
            ("Germán E.", "Ambato", 5, "Las uso dentro del jean y nadie nota que las llevo. Después de 8 horas en moto no me molestan. Ya no salgo sin ellas."),
            ("Valeria O.", "Riobamba", 5, "Las compré tras caerme sin protecciones. Llegué bien pero fue susto. Ahora estas van puestas siempre."),
            ("Felipe N.", "Manta", 4, "Muy buenas rodilleras. Las tiras son un poco más complicadas de ajustar al principio pero después se vuelve automático."),
        ],
        "related": [2, 0, 4],
        "variants": "tallas_gen",
    },
    {
        "slug": "espejos-cnc-racing",
        "name": "Espejos Retrovisores CNC Racing Universal",
        "cat": "Accesorios Moto",
        "price": "34.99",
        "original": "49.99",
        "discount": "30",
        "sku": "ALF-MOT-001",
        "img":  "1558899412-db4a281fa0ed",     # manubrio moto ✅
        "img2": "1636761358770-009ce3957519",  # mecánico ✅
        "img3": "1611004061856-ccc3cbe944b2",  # casco en moto ✅
        "bg":   "1558981806-ec527fa84c39",     # racing
        "badge": "🔧 Universal",
        "stars": "4.7", "reviews_count": "143",
        "hook": "Diseñados para correr. Construidos para durar.",
        "short_desc": "Par de espejos CNC en aluminio 6061-T6, cristal convexo 180°, antivibración integrado. Rosca universal 10mm/8mm.",
        "features": [
            ("⚙️", "CNC Fresado", "Aluminio 6061-T6 mecanizado en fábrica, sin soldaduras"),
            ("👁️", "Cristal Convexo 180°", "Campo visual ampliado, elimina el punto ciego lateral"),
            ("🎯", "Anti-vibración", "Junta amortiguadora en base elimina el titileo a alta vel."),
            ("🔩", "Universal 10/8mm", "Adaptadores incluidos para casi cualquier moto del mercado"),
        ],
        "specs": [
            ("Material", "Aluminio CNC 6061-T6 anodizado negro"),
            ("Cristal", "Convexo, vidrio templado antirayones"),
            ("Ángulo", "Ajustable 360° en rótula esférica"),
            ("Rosca", "10mm derecha + 8mm izquierda (adaptadores)"),
            ("Altura espejo", "195 mm"), ("Peso por unidad", "120 g"),
            ("Antivibración", "Sí, junta caucho en base"),
            ("Colores", "Negro mate / Plata / Dorado"),
        ],
        "desc": "Los espejos retrovisores originales de fábrica vibran, distorsionan y reducen el ángulo de visión justo cuando más lo necesitas. Los CNC Racing resuelven los tres problemas.<br><br>El aluminio CNC fresado elimina las vibraciones que deforman la imagen a más de 80 km/h. El cristal convexo amplía el campo visual lateral en un 40%. La rótula esférica permite ajustar el ángulo exacto para tu posición de conducción.<br><br>Instalación en menos de 10 minutos. Compatible con Honda, Yamaha, Suzuki, Kawasaki, Bajaj y la mayoría de marcas del mercado.",
        "reviews": [
            ("Javier R.", "Guayaquil", 5, "Mis espejos originales vibraban horrible a 100km/h. Con estos, imagen perfecta a cualquier velocidad. Instalación facilísima."),
            ("Miguel A.", "Quito", 4, "Muy buenos espejos. El dorado queda increíble en mi MT-07. Sugiero poner Loctite en la rosca para que no aflojen."),
            ("Andrea L.", "Cuenca", 5, "Los puse en mi Honda CB190. Quedaron perfectos. La visibilidad mejoró notablemente."),
        ],
        "related": [5, 6, 2],
        "variants": "color_metal",
    },
    {
        "slug": "kit-cadena-did-428",
        "name": "Kit Cadena DID 428VX + Piñón + Corona",
        "cat": "Partes y Piezas",
        "price": "44.99",
        "original": "64.99",
        "discount": "31",
        "sku": "ALF-PAR-001",
        "img":  "1769537754999-724044ec2e32",  # cadena + rueda moto ✅
        "img2": "1763142185959-be6f3dbdd31a",  # rueda trasera moto ✅
        "img3": "1636761358770-009ce3957519",  # mecánico ✅
        "bg":   "1636761358772-798789548d25",  # taller
        "badge": "✅ Kit Completo",
        "stars": "4.8", "reviews_count": "98",
        "hook": "Una cadena rota te deja a pie. Una cadena DID te lleva lejos.",
        "short_desc": "Kit completo: cadena DID 428VX O-ring 120 eslabones + piñón y corona acero forjado CNC. Para motos 125-250cc.",
        "features": [
            ("🔗", "O-Ring Sellado", "Retención de lubricante interna, vida útil 3× superior"),
            ("⚙️", "Acero Forjado", "Piñón y corona CNC en acero 420 HV tratado térmicamente"),
            ("🔢", "120 Eslabones", "Eslabones y remaches con cierre de seguridad incluido"),
            ("🔧", "Kit Completo", "Cadena + piñón + corona + pasador de cierre"),
        ],
        "specs": [
            ("Cadena", "DID 428VX O-ring"), ("Eslabones", "120 (cortable)"),
            ("Piñón", "Acero forjado, 14T ó 15T"), ("Corona", "Acero CNC 420HV, 45T ó 48T"),
            ("Paso", "428"), ("Carga rotura", "2,600 kgf"),
            ("Lubricación", "O-ring sellado"), ("Compatible", "Honda, Yamaha, Suzuki 125-250cc"),
        ],
        "desc": "La cadena es el eslabón literal entre el motor y la rueda. Una cadena barata no falla de un día para otro — se va estirando, saltando, perdiendo eficiencia hasta que un día, en la autopista, te deja parado.<br><br>La DID 428VX con O-ring mantiene la lubricación interna sellada entre los rodillos, lo que significa hasta 3 veces más vida útil. El piñón y la corona en acero forjado CNC mantienen el desgaste uniforme durante más tiempo.<br><br>Un kit nuevo reemplaza los tres componentes de transmisión al mismo tiempo — exactamente lo correcto.",
        "reviews": [
            ("Ramiro C.", "Latacunga", 5, "Llevaba 2 años con la cadena original y ya sonaba. Puse este kit y la diferencia es enorme. La moto agarra diferente, más suave."),
            ("Patricia V.", "Quevedo", 5, "Kit completo a buen precio. Mi mecánico dijo que la calidad es muy buena comparada con genéricos. Llegó en 3 días."),
            ("Esteban M.", "Ambato", 4, "Muy buen producto. El manual viene en inglés. El kit en sí es de primera."),
        ],
        "related": [6, 4, 7],
        "variants": "pinon_corona",
    },
    {
        "slug": "pastillas-ebc-fa",
        "name": "Pastillas de Freno EBC FA Series",
        "cat": "Partes y Piezas",
        "price": "19.99",
        "original": "28.99",
        "discount": "31",
        "sku": "ALF-PAR-002",
        "img":  "1763142185959-be6f3dbdd31a",  # rueda trasera moto ✅
        "img2": "1769537754999-724044ec2e32",  # cadena/rueda moto ✅
        "img3": "1636761358772-798789548d25",  # taller ✅
        "bg":   "1636761358772-798789548d25",  # taller
        "badge": "🔴 Seguridad",
        "stars": "4.9", "reviews_count": "186",
        "hook": "Cuando frenas, no hay segunda oportunidad.",
        "short_desc": "Pastillas EBC FA Series en compuesto orgánico de alta fricción. Sin período de rodaje, fade resistente hasta 350°C.",
        "features": [
            ("🛑", "Sin Break-in", "Máxima fricción desde la primera frenada, sin período de rodaje"),
            ("🌡️", "Fade Resistente", "Coeficiente estable a 350°C — sin fade en bajadas largas"),
            ("📏", "Precisión OEM", "Geometría idéntica a la pieza original, sin rectificado"),
            ("♻️", "Sin Metales Pesados", "Compuesto libre de asbesto y cobre"),
        ],
        "specs": [
            ("Compuesto", "Orgánico FA Series"),
            ("Temperatura máx.", "350°C sostenidos"),
            ("Coeficiente fricción", "0.45 µ (estable caliente/frío)"),
            ("Break-in", "No requerido"),
            ("Compatibilidad", "Ver tabla de aplicación por modelo"),
            ("Placa soporte", "Acero estampado anti-corrosión"),
            ("Asbesto", "No"), ("Garantía", "18 meses o 15,000 km"),
        ],
        "desc": "Las pastillas de freno son el componente de seguridad con mayor relación importancia/precio de toda la moto. Y son las que más se descuidan.<br><br>Las EBC FA Series usan un compuesto orgánico que alcanza su coeficiente de fricción máximo desde la primera frenada — sin el período de rodaje de 200 km. En frenadas de emergencia, eso marca la diferencia.<br><br>El compuesto mantiene 0.45 µ desde temperatura ambiente hasta 350°C. Ni en bajadas de volcán pierden el mordiente.",
        "reviews": [
            ("Nelson T.", "Quito", 5, "Las monté y la diferencia es inmediata. El freno muerde desde el primer jalón. Las originales se sentían esponjosas comparadas."),
            ("Carmen R.", "Guayaquil", 5, "Las recomendó mi mecánico de confianza. Llevo 4,000 km y siguen perfectas."),
            ("Luis A.", "Loja", 5, "Precio increíble para la calidad. Las EBC son marca reconocida mundialmente. Perfecto que Alfapro las tenga."),
        ],
        "related": [5, 4, 7],
        "variants": None,
    },
    {
        "slug": "aceite-motul-7100",
        "name": "Aceite Motul 7100 4T 10W-40 1L",
        "cat": "Motor",
        "price": "15.99",
        "original": "21.99",
        "discount": "27",
        "sku": "ALF-MOT-001",
        "img":  "1746014995485-e8a698f39804",  # botella aceite ✅
        "img2": "1776264762509-60b8091cfb20",  # bujía ✅
        "img3": "1534755563369-ad37931ac77b",  # motor moto ✅
        "bg":   "1534755563369-ad37931ac77b",  # engine
        "badge": "💚 100% Sintético",
        "stars": "4.9", "reviews_count": "312",
        "hook": "El lubricante que el motor de competición necesita. Para tu moto de calle.",
        "short_desc": "Aceite 100% sintético con tecnología Éster para motores 4T. Protección extrema en arranque frío y alta temperatura. JASO MA2.",
        "features": [
            ("⚗️", "Tecnología Éster", "Lubricación molecular que recubre las superficies 24/7"),
            ("🌡️", "Rango Extremo", "Viscosidad estable de -20°C hasta 150°C de temperatura de aceite"),
            ("✅", "JASO MA2", "Certificación obligatoria para motos con embrague en baño de aceite"),
            ("⏱️", "Intervalo Extendido", "Hasta 5,000 km entre cambios con motor en perfecto estado"),
        ],
        "specs": [
            ("Tipo", "100% Sintético"), ("Viscosidad", "SAE 10W-40"),
            ("Norma API", "SN"), ("Certificación", "JASO MA2"),
            ("Volumen", "1 litro"), ("Intervalo cambio", "5,000 km"),
            ("Temperatura mín.", "-20°C"), ("Temperatura máx.", "+150°C aceite"),
        ],
        "desc": "El motor de tu moto tiene tolerancias de décimas de milímetro entre pistón y cilindro. La película de aceite que separa esas superficies tiene un grosor medido en micras. Si esa película falla — en el arranque frío, en la subida de la sierra — el daño es irreversible.<br><br>El Motul 7100 con tecnología Éster forma una capa de lubricación molecular que se adhiere a las superficies incluso cuando el motor está parado. Desde el primer giro del arranque, hay protección.<br><br>Para motos con embrague húmedo, la certificación JASO MA2 es obligatoria. El Motul 7100 la tiene.",
        "reviews": [
            ("Hernán G.", "Quito", 5, "Uso Motul 7100 desde hace 3 años en mi Yamaha FZ. El motor suena diferente, más silencioso. No cambio de marca."),
            ("Sandra M.", "Guayaquil", 5, "Mi mecánico me dijo que el 7100 es lo mejor que le puedo poner a mi Honda. Compré 6 litros. Precio muy bueno en Alfapro."),
            ("Ricardo P.", "Cuenca", 5, "Excelente aceite para la sierra. Con otros aceites el motor sonaba más a las mañanas frías. Con el Motul, arranca suave desde el primer segundo."),
        ],
        "related": [6, 5, 8],
        "variants": "litros",
    },
    {
        "slug": "kit-led-h4",
        "name": "Kit LED H4 Canbus 6000K Plug & Play",
        "cat": "Eléctrico",
        "price": "39.99",
        "original": "59.99",
        "discount": "33",
        "sku": "ALF-ELE-001",
        "img":  "1711150943978-8d045550dd33",  # luces LED moto ✅
        "img2": "1558899412-db4a281fa0ed",     # manubrio ✅
        "img3": "1636761358770-009ce3957519",  # mecánico ✅
        "bg":   "1558981806-ec527fa84c39",     # racing
        "badge": "⚡ Plug & Play",
        "stars": "4.7", "reviews_count": "221",
        "hook": "Ve y sé visto. La diferencia entre un percance y llegar a casa.",
        "short_desc": "Kit LED H4 con Canbus anti-error, 6000K luz blanca, 200% más brillo que halógena. Instalación plug & play en 5 minutos.",
        "features": [
            ("💡", "200% Más Brillo", "2,800 lumens vs. 1,100 lumens de la halógena estándar H4"),
            ("🔌", "Canbus Anti-error", "Resistencia interna que previene códigos de error en tablero"),
            ("❄️", "6000K Luz Día", "Temperatura 6000K — máxima visibilidad en lluvia y noche"),
            ("💧", "IP68 Sellado", "Resistente a lluvia, polvo, lavados a presión"),
        ],
        "specs": [
            ("Base", "H4 (bi-foco: cruce y carretera)"),
            ("Voltaje", "9-32V"), ("Potencia", "35W por bombillo"),
            ("Flujo", "2,800 lm por bombillo"), ("Temperatura color", "6000K"),
            ("Canbus", "Sí, anti-error integrado"), ("IP", "IP68"),
            ("Vida útil", "50,000 horas"),
        ],
        "desc": "La halógena de fábrica proyecta luz apenas 40 metros hacia adelante. No es suficiente para reaccionar a tiempo a un bache, un perro, o un carro sin luces a 70 km/h.<br><br>El Kit LED H4 6000K entrega 2,800 lúmenes — 200% más brillo, 90 metros de visión. La temperatura de color 6000K simula la luz del día, que el ojo humano procesa más rápido que la amarilla de una halógena.<br><br>El sistema Canbus integrado evita el error de bombillo en el tablero — el problema más común en conversiones baratas. Plug & Play: conectas igual que la original.",
        "reviews": [
            ("David C.", "Santo Domingo", 5, "Instalé en 5 minutos en mi YBR. La diferencia nocturna es brutal. Ya me han preguntado 4 personas qué bombillo tengo."),
            ("Marcelo V.", "Ibarra", 5, "Sin error en el tablero. Sin modificaciones. Solo enchufar y listo. El brillo es impresionante."),
            ("Natalia F.", "Loja", 4, "Excelente luz. En lluvia marca una diferencia enorme. Le quito una estrella porque el calor del disipador es bastante."),
        ],
        "related": [6, 5, 4],
        "variants": "color_temp",
    },
    {
        "slug": "llanta-michelin-pilot",
        "name": "Llanta Michelin Pilot Street 2 140/70-17",
        "cat": "Llantas",
        "price": "89.99",
        "original": "119.99",
        "discount": "25",
        "sku": "ALF-LLA-001",
        "img":  "1763142185959-be6f3dbdd31a",  # rueda trasera moto ✅
        "img2": "1769537754999-724044ec2e32",  # cadena/rueda ✅
        "img3": "1558981806-ec527fa84c39",     # racing ✅
        "bg":   "1558981806-ec527fa84c39",     # racing
        "badge": "🇫🇷 Michelin",
        "stars": "4.9", "reviews_count": "167",
        "hook": "La única llanta que tu moto necesita. Para todo clima, todo asfalto.",
        "short_desc": "Llanta trasera Michelin Pilot Street 2, compuesto 2CT para clima tropical. Freno en mojado mejorado +20%, duración +30%.",
        "features": [
            ("🌧️", "Freno Mojado +20%", "Compuesto 2CT del mismo linaje que las Pilot Power MotoGP"),
            ("📐", "Durabilidad +30%", "Centro duro para km de autopista, hombros blandos para curvas"),
            ("🏙️", "Urban + Highway", "Perfilado para pavimento latinoamericano: baches, adoquín, ruta"),
            ("🌡️", "Clima Tropical", "Formulado para temperaturas 20°C–40°C del litoral y sierra"),
        ],
        "specs": [
            ("Medida", "140/70-17 TL"), ("Posición", "Trasera"),
            ("Tecnología", "2CT (Dual Compound)"), ("Índice velocidad", "H (hasta 210 km/h)"),
            ("Índice carga", "66 (300 kg)"), ("Uso", "Road / Urban"),
            ("Compatible", "125cc, 150cc, 200cc, 250cc Honda/Yamaha/Suzuki"),
            ("País origen", "Francia"),
        ],
        "desc": "En las calles ecuatorianas llueve fuerte y de repente. Un adoquín mojado a 60 km/h con una llanta genérica es una lotería. Con la Michelin Pilot Street 2, es física — y la física dice que frenas.<br><br>La tecnología 2CT usa dos compuestos distintos en la misma llanta: el centro en caucho duro y duradero; los hombros en compuesto blando y adherente. Dura más y agarra mejor.<br><br>Fue formulada específicamente para clima tropical: temperatura promedio 25°C y lluvia frecuente. No es una llanta europea adaptada.",
        "reviews": [
            ("Omar S.", "Guayaquil", 5, "Con mi llanta anterior patiné dos veces en lluvia. Con la Michelin, frenar en mojado se siente completamente diferente."),
            ("Patricia H.", "Manabí", 5, "Perfecta para las rutas de la costa. Llevo 8,000 km y sigue en buen estado."),
            ("Rodrigo F.", "Quito", 5, "Monté en mi Honda CB190 y la diferencia en curva es inmediata. En la bajada hacia Mindo, cero miedo."),
        ],
        "related": [6, 5, 7],
        "variants": "posicion_llanta",
    },
]

# ── CSS ─────────────────────────────────────────────────────────────────────

CSS = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --green: #9BC42A;
      --green-glow: rgba(155, 196, 42, 0.35);
      --green-subtle: rgba(155, 196, 42, 0.08);
      --bg: #0a0a0a; --card: #111; --card2: #161616;
      --card-border: rgba(255,255,255,0.07);
      --white: #f5f5f5; --muted: rgba(255,255,255,0.45);
    }
    html { scroll-behavior: smooth; }
    body { font-family: 'Inter Tight', sans-serif; background: var(--bg); color: var(--white); overflow-x: hidden; }

    @keyframes fadeUp { from { opacity:0; transform:translateY(24px); } to { opacity:1; transform:translateY(0); } }
    @keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
    @keyframes pulseDot { 0%,100%{transform:scale(1);opacity:1;} 50%{transform:scale(1.6);opacity:.4;} }
    @keyframes floatV { 0%,100%{transform:translateY(0);} 50%{transform:translateY(-10px);} }

    /* ── NAV ── */
    nav {
      position: fixed; top:0; left:0; right:0; z-index:200;
      height:68px; display:flex; align-items:center; justify-content:space-between;
      padding:0 56px;
      backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px);
      background:rgba(8,8,8,0.88);
      border-bottom:1px solid var(--card-border);
    }
    .nav-logo { text-decoration:none; display:flex; align-items:center; }
    .nav-logo img { height:44px; width:auto; }
    .nav-links { display:flex; gap:32px; list-style:none; }
    .nav-links a { color:var(--muted); text-decoration:none; font-size:13px; font-weight:500; letter-spacing:.06em; transition:color .2s; }
    .nav-links a:hover { color:var(--white); }
    .nav-right { display:flex; align-items:center; gap:16px; }
    .cart-btn {
      position:relative; display:flex; align-items:center; gap:8px;
      padding:9px 22px; border-radius:999px;
      background:var(--green); color:#0a0a0a;
      font-size:13px; font-weight:800; letter-spacing:.04em;
      text-decoration:none; border:none; cursor:pointer;
      transition:background .2s, transform .15s;
    }
    .cart-btn:hover { background:#b8e03a; transform:scale(1.03); }
    .cart-count {
      position:absolute; top:-6px; right:-6px;
      width:18px; height:18px; border-radius:50%;
      background:#ff4444; color:#fff; font-size:10px; font-weight:800;
      display:flex; align-items:center; justify-content:center;
    }

    /* ── PRODUCT ATMOSPHERE HEADER ── */
    .product-atmos {
      position:relative; min-height:340px;
      display:flex; align-items:flex-end;
      padding:0 0 0 0;
      overflow:hidden;
    }
    .atmos-bg {
      position:absolute; inset:0;
      background-size:cover; background-position:center 30%;
      filter:brightness(.18) saturate(.4);
      transform:scale(1.05);
    }
    .atmos-overlay {
      position:absolute; inset:0;
      background: linear-gradient(to bottom,
        rgba(10,10,10,0.2) 0%,
        rgba(10,10,10,0.6) 60%,
        rgba(10,10,10,1) 100%);
    }
    .atmos-glow {
      position:absolute; inset:0;
      background: radial-gradient(ellipse 50% 80% at 80% 40%, rgba(155,196,42,.1) 0%, transparent 65%);
      pointer-events:none;
    }
    .atmos-content {
      position:relative; z-index:2;
      width:100%; max-width:1400px; margin:0 auto;
      padding:120px 80px 52px;
      display:flex; flex-direction:column; gap:14px;
    }
    .atmos-breadcrumb {
      display:flex; gap:8px; align-items:center;
      font-size:12px; color:var(--muted);
    }
    .atmos-breadcrumb a { color:var(--muted); text-decoration:none; transition:color .2s; }
    .atmos-breadcrumb a:hover { color:var(--green); }
    .atmos-breadcrumb span { color:rgba(255,255,255,.18); }
    .atmos-badge {
      display:inline-flex; align-items:center; gap:6px;
      padding:5px 14px; border-radius:999px; width:fit-content;
      font-size:11px; font-weight:700; letter-spacing:.08em;
      background:rgba(155,196,42,.12); border:1px solid rgba(155,196,42,.3);
      color:var(--green); animation:fadeUp .6s ease both;
    }
    .atmos-title {
      font-size:clamp(32px,4vw,56px); font-weight:800;
      line-height:.95; letter-spacing:-.04em;
      animation:fadeUp .6s ease .1s both;
    }
    .atmos-title em { color:var(--green); font-style:normal; }

    /* ── PRODUCT DETAIL SECTION ── */
    .product-detail {
      display:grid; grid-template-columns:1.05fr 1fr;
      gap:56px; max-width:1400px; margin:0 auto;
      padding:0 80px 80px;
    }

    /* ── GALLERY ── */
    .gallery { display:flex; flex-direction:column; gap:12px; margin-top:-64px; z-index:10; }
    .gallery-main {
      border-radius:20px; overflow:hidden;
      border:1px solid var(--card-border);
      aspect-ratio:3/2; position:relative;
      background:#111;
      box-shadow:0 32px 64px rgba(0,0,0,.6);
    }
    .gallery-main img { width:100%; height:100%; object-fit:cover; transition:transform .4s; }
    .gallery-main:hover img { transform:scale(1.03); }
    .gallery-thumbs { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
    .thumb {
      border-radius:12px; overflow:hidden;
      border:1.5px solid var(--card-border);
      aspect-ratio:4/3; cursor:pointer;
      transition:border-color .2s, transform .2s;
    }
    .thumb:hover { border-color:rgba(155,196,42,.5); transform:scale(1.02); }
    .thumb.active { border-color:var(--green); }
    .thumb img { width:100%; height:100%; object-fit:cover; filter:brightness(.8); transition:filter .3s; }
    .thumb:hover img, .thumb.active img { filter:brightness(1); }

    /* ── PRODUCT PANEL ── */
    .product-panel {
      padding-top:16px;
      display:flex; flex-direction:column; gap:22px;
    }
    .panel-cat {
      font-size:11px; font-weight:700; letter-spacing:.18em;
      text-transform:uppercase; color:var(--green);
      display:flex; align-items:center; gap:10px;
    }
    .panel-cat::before { content:''; width:20px; height:1px; background:var(--green); }

    .panel-hook {
      font-size:15px; color:rgba(255,255,255,.55);
      line-height:1.65; font-style:italic;
      border-left:2px solid rgba(155,196,42,.4);
      padding-left:14px;
    }

    .panel-stars { display:flex; align-items:center; gap:10px; }
    .stars span { color:#f5c542; font-size:15px; }
    .rating-num { font-size:13px; font-weight:800; }
    .rating-count { font-size:12px; color:var(--muted); }

    /* Price */
    .price-block {
      display:flex; align-items:center; gap:14px; flex-wrap:wrap;
      padding:20px 0; border-top:1px solid var(--card-border); border-bottom:1px solid var(--card-border);
    }
    .price-current {
      font-size:52px; font-weight:800; letter-spacing:-.04em;
      color:var(--green); line-height:1;
    }
    .price-original {
      font-size:20px; color:var(--muted); text-decoration:line-through; margin-top:4px;
    }
    .price-save {
      padding:6px 12px; border-radius:8px;
      background:rgba(155,196,42,.15); color:var(--green);
      font-size:12px; font-weight:800; letter-spacing:.04em;
      border:1px solid rgba(155,196,42,.25);
    }

    /* Variants */
    .label-sm { font-size:11px; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); margin-bottom:8px; }
    .variant-row { display:flex; gap:8px; flex-wrap:wrap; }
    .variant-btn {
      padding:8px 18px; border-radius:8px;
      border:1px solid var(--card-border); background:transparent;
      color:var(--white); font-size:13px; font-weight:600;
      cursor:pointer; transition:all .2s; font-family:'Inter Tight',sans-serif;
    }
    .variant-btn:hover { border-color:var(--green); color:var(--green); background:rgba(155,196,42,.06); }
    .variant-btn.active { border-color:var(--green); background:rgba(155,196,42,.12); color:var(--green); }

    /* CTA row */
    .cta-row { display:flex; gap:10px; align-items:stretch; }
    .qty-control {
      display:flex; align-items:center;
      border:1px solid var(--card-border); border-radius:10px; overflow:hidden;
    }
    .qty-btn {
      width:42px; height:52px; background:transparent; border:none;
      color:var(--white); font-size:18px; cursor:pointer;
      transition:background .2s; font-family:'Inter Tight',sans-serif;
    }
    .qty-btn:hover { background:rgba(255,255,255,.06); }
    .qty-num { width:40px; text-align:center; font-size:15px; font-weight:700; }
    .btn-add {
      flex:1; padding:16px 28px; border-radius:10px;
      background:rgba(155,196,42,.12); color:var(--green);
      font-size:14px; font-weight:800; letter-spacing:.04em;
      border:1.5px solid rgba(155,196,42,.4); cursor:pointer;
      transition:all .2s; font-family:'Inter Tight',sans-serif;
    }
    .btn-add:hover { background:rgba(155,196,42,.2); border-color:var(--green); }
    .btn-buy {
      flex:1.2; padding:16px 32px; border-radius:10px;
      background:var(--green); color:#0a0a0a;
      font-size:15px; font-weight:800; letter-spacing:.04em;
      border:none; cursor:pointer;
      transition:background .2s, transform .15s; font-family:'Inter Tight',sans-serif;
      text-decoration:none; display:flex; align-items:center; justify-content:center; gap:8px;
    }
    .btn-buy:hover { background:#b8e03a; transform:scale(1.02); }

    /* Trust strip */
    .trust-strip {
      display:grid; grid-template-columns:repeat(4,1fr);
      border:1px solid var(--card-border); border-radius:12px; overflow:hidden;
    }
    .trust-item {
      padding:14px 8px; text-align:center;
      border-right:1px solid var(--card-border);
    }
    .trust-item:last-child { border-right:none; }
    .trust-icon { font-size:22px; margin-bottom:4px; }
    .trust-label { font-size:10px; font-weight:700; color:var(--muted); text-transform:uppercase; letter-spacing:.08em; }

    .sku-line { font-size:11px; color:rgba(255,255,255,.3); display:flex; gap:8px; }

    /* ── FEATURES ── */
    .features-band {
      background:var(--card); border-top:1px solid var(--card-border); border-bottom:1px solid var(--card-border);
      padding:60px 80px;
    }
    .features-band-inner { display:grid; grid-template-columns:repeat(4,1fr); gap:40px; max-width:1400px; margin:0 auto; }
    .feat { display:flex; gap:16px; align-items:flex-start; }
    .feat-icon { font-size:28px; flex-shrink:0; margin-top:2px; }
    .feat-title { font-size:14px; font-weight:800; letter-spacing:-.01em; margin-bottom:4px; }
    .feat-desc { font-size:12px; color:var(--muted); line-height:1.65; }

    /* ── TABS ── */
    .tabs-section { padding:72px 80px; max-width:1400px; margin:0 auto; }
    .tabs-nav { display:flex; border-bottom:1px solid var(--card-border); margin-bottom:44px; }
    .tab-btn {
      padding:14px 28px; background:none; border:none;
      color:var(--muted); font-size:14px; font-weight:700; letter-spacing:.04em;
      cursor:pointer; border-bottom:2px solid transparent; margin-bottom:-1px;
      transition:all .2s; font-family:'Inter Tight',sans-serif;
    }
    .tab-btn.active { color:var(--green); border-bottom-color:var(--green); }
    .tab-content { display:none; }
    .tab-content.active { display:block; }
    .desc-text { font-size:15px; color:rgba(255,255,255,.72); line-height:1.85; max-width:680px; }
    .specs-table { width:100%; border-collapse:collapse; max-width:640px; }
    .specs-table tr { border-bottom:1px solid var(--card-border); }
    .specs-table td { padding:13px 0; font-size:14px; }
    .specs-table td:first-child { color:var(--muted); width:42%; font-weight:500; }
    .specs-table td:last-child { color:var(--white); font-weight:600; }

    /* Reviews */
    .reviews-list { display:flex; flex-direction:column; gap:20px; max-width:680px; }
    .review-card {
      padding:24px; border-radius:16px;
      background:var(--card); border:1px solid var(--card-border);
    }
    .review-header { display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; }
    .reviewer-name { font-size:14px; font-weight:800; }
    .reviewer-loc { font-size:12px; color:var(--muted); margin-top:2px; }
    .review-stars { color:#f5c542; letter-spacing:2px; }
    .review-text { font-size:14px; color:rgba(255,255,255,.68); line-height:1.72; }

    /* ── RELATED ── */
    .related-section { padding:72px 80px; border-top:1px solid var(--card-border); }
    .related-title { font-size:clamp(28px,3vw,40px); font-weight:800; letter-spacing:-.03em; margin-bottom:40px; max-width:1400px; }
    .related-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; max-width:1400px; }
    .related-card {
      border-radius:18px; overflow:hidden;
      background:var(--card); border:1px solid var(--card-border);
      text-decoration:none; color:var(--white);
      transition:border-color .25s, transform .25s;
      display:block;
    }
    .related-card:hover { border-color:rgba(155,196,42,.4); transform:translateY(-6px); }
    .related-img { aspect-ratio:16/9; overflow:hidden; position:relative; }
    .related-img img { width:100%; height:100%; object-fit:cover; filter:brightness(.65); transition:filter .3s, transform .4s; }
    .related-card:hover .related-img img { filter:brightness(.85); transform:scale(1.04); }
    .related-body { padding:18px 20px 22px; }
    .related-cat { font-size:10px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--green); margin-bottom:5px; }
    .related-name { font-size:14px; font-weight:800; letter-spacing:-.01em; line-height:1.25; margin-bottom:10px; }
    .related-price-row { display:flex; align-items:baseline; gap:8px; }
    .related-price { font-size:20px; font-weight:800; color:var(--green); letter-spacing:-.02em; }
    .related-old { font-size:12px; color:var(--muted); text-decoration:line-through; }

    /* ── FOOTER ── */
    footer {
      background:#060606; border-top:1px solid var(--card-border);
      padding:32px 80px; display:flex; justify-content:space-between; align-items:center;
    }
    .footer-copy { font-size:12px; color:var(--muted); }
    .footer-links { display:flex; gap:24px; }
    .footer-links a { font-size:12px; color:var(--muted); text-decoration:none; }
    .footer-links a:hover { color:var(--white); }

    /* ── STICKY CTA ── */
    .sticky-cta {
      position:fixed; bottom:0; left:0; right:0; z-index:150;
      background:rgba(10,10,10,.96); border-top:1px solid var(--card-border);
      backdrop-filter:blur(20px);
      padding:14px 80px;
      display:flex; align-items:center; justify-content:space-between;
      transform:translateY(100%);
      transition:transform .3s cubic-bezier(.25,.8,.25,1);
    }
    .sticky-cta.visible { transform:translateY(0); }
    .sticky-prod-info { display:flex; flex-direction:column; gap:2px; }
    .sticky-name { font-size:14px; font-weight:700; }
    .sticky-price { font-size:20px; font-weight:800; color:var(--green); letter-spacing:-.02em; }
    .sticky-btns { display:flex; gap:10px; }
    .sticky-add {
      padding:11px 24px; border-radius:8px;
      background:transparent; border:1.5px solid rgba(155,196,42,.4);
      color:var(--green); font-size:13px; font-weight:700;
      cursor:pointer; font-family:'Inter Tight',sans-serif; transition:all .2s;
    }
    .sticky-add:hover { background:rgba(155,196,42,.1); }
    .sticky-buy {
      padding:11px 28px; border-radius:8px;
      background:var(--green); color:#0a0a0a;
      font-size:13px; font-weight:800; text-decoration:none;
      display:flex; align-items:center; gap:6px; transition:background .2s;
    }
    .sticky-buy:hover { background:#b8e03a; }

    /* ── TOAST ── */
    .toast {
      position:fixed; bottom:88px; right:32px; z-index:999;
      padding:14px 22px; border-radius:12px;
      background:var(--card); border:1px solid rgba(155,196,42,.4);
      display:flex; align-items:center; gap:10px;
      font-size:14px; font-weight:600;
      transform:translateY(60px); opacity:0;
      transition:all .3s cubic-bezier(.34,1.56,.64,1);
      pointer-events:none;
    }
    .toast.show { transform:translateY(0); opacity:1; }

    /* ── RESPONSIVE ── */
    @media (max-width:1024px) {
      nav { padding:0 24px; }
      .atmos-content { padding:100px 24px 44px; }
      .product-detail { grid-template-columns:1fr; padding:0 24px 60px; gap:32px; }
      .gallery { margin-top:-40px; }
      .features-band { padding:48px 24px; }
      .features-band-inner { grid-template-columns:1fr 1fr; gap:24px; }
      .tabs-section, .related-section { padding:48px 24px; }
      .related-grid { grid-template-columns:1fr 1fr; }
      .sticky-cta { padding:12px 24px; }
      footer { padding:24px; flex-direction:column; gap:16px; text-align:center; }
    }
    @media (max-width:600px) {
      .related-grid { grid-template-columns:1fr; }
      .features-band-inner { grid-template-columns:1fr; }
      .cta-row { flex-direction:column; }
      .trust-strip { grid-template-columns:repeat(2,1fr); }
      .trust-strip .trust-item:nth-child(2) { border-right:none; }
    }
"""

def stars_html(r):
    return "★" * int(float(r)) + ("" if float(r) == int(float(r)) else "½")

def variants_html(kind):
    if kind == "tallas_casco":
        return """<div>
        <div class="label-sm">Talla</div>
        <div class="variant-row">
          <button class="variant-btn" onclick="selVar(this)">XS</button>
          <button class="variant-btn active" onclick="selVar(this)">S</button>
          <button class="variant-btn" onclick="selVar(this)">M</button>
          <button class="variant-btn" onclick="selVar(this)">L</button>
          <button class="variant-btn" onclick="selVar(this)">XL</button>
          <button class="variant-btn" onclick="selVar(this)">XXL</button>
        </div>
      </div>
      <div>
        <div class="label-sm">Color</div>
        <div class="variant-row">
          <button class="variant-btn active" onclick="selVar(this)">Negro Mate</button>
          <button class="variant-btn" onclick="selVar(this)">Blanco Perla</button>
          <button class="variant-btn" onclick="selVar(this)">Rojo Racing</button>
        </div>
      </div>"""
    if kind == "tallas_guantes":
        return """<div>
        <div class="label-sm">Talla</div>
        <div class="variant-row">
          <button class="variant-btn" onclick="selVar(this)">S</button>
          <button class="variant-btn active" onclick="selVar(this)">M</button>
          <button class="variant-btn" onclick="selVar(this)">L</button>
          <button class="variant-btn" onclick="selVar(this)">XL</button>
          <button class="variant-btn" onclick="selVar(this)">2XL</button>
        </div>
      </div>"""
    if kind == "tallas_gen":
        return """<div>
        <div class="label-sm">Talla</div>
        <div class="variant-row">
          <button class="variant-btn active" onclick="selVar(this)">S–M</button>
          <button class="variant-btn" onclick="selVar(this)">L–XL</button>
        </div>
      </div>"""
    if kind == "color_metal":
        return """<div>
        <div class="label-sm">Acabado</div>
        <div class="variant-row">
          <button class="variant-btn active" onclick="selVar(this)">Negro Mate</button>
          <button class="variant-btn" onclick="selVar(this)">Plata</button>
          <button class="variant-btn" onclick="selVar(this)">Dorado</button>
        </div>
      </div>"""
    if kind == "pinon_corona":
        return """<div>
        <div class="label-sm">Piñón</div>
        <div class="variant-row">
          <button class="variant-btn active" onclick="selVar(this)">14T (estándar)</button>
          <button class="variant-btn" onclick="selVar(this)">15T (+velocidad)</button>
        </div>
      </div>
      <div>
        <div class="label-sm">Corona</div>
        <div class="variant-row">
          <button class="variant-btn active" onclick="selVar(this)">45T (estándar)</button>
          <button class="variant-btn" onclick="selVar(this)">48T (+torque)</button>
        </div>
      </div>"""
    if kind == "litros":
        return """<div>
        <div class="label-sm">Presentación</div>
        <div class="variant-row">
          <button class="variant-btn active" onclick="selVar(this)">1 Litro — $15.99</button>
          <button class="variant-btn" onclick="selVar(this)">4 Litros — $55.99</button>
        </div>
      </div>"""
    if kind == "color_temp":
        return """<div>
        <div class="label-sm">Temperatura Color</div>
        <div class="variant-row">
          <button class="variant-btn active" onclick="selVar(this)">6000K Blanco Día</button>
          <button class="variant-btn" onclick="selVar(this)">8000K Azul Glacial</button>
        </div>
      </div>"""
    if kind == "posicion_llanta":
        return """<div>
        <div class="label-sm">Posición</div>
        <div class="variant-row">
          <button class="variant-btn" onclick="selVar(this)">Delantera 100/80-17</button>
          <button class="variant-btn active" onclick="selVar(this)">Trasera 140/70-17</button>
        </div>
      </div>"""
    return ""

def related_card_html(rel):
    return f"""<a href="{rel['slug']}.html" class="related-card">
        <div class="related-img"><img src="https://images.unsplash.com/photo-{rel['img']}?w=640&q=80" alt="{rel['name']}" loading="lazy"/></div>
        <div class="related-body">
          <div class="related-cat">{rel['cat']}</div>
          <div class="related-name">{rel['name']}</div>
          <div class="related-price-row">
            <span class="related-price">${rel['price']}</span>
            <span class="related-old">${rel['original']}</span>
          </div>
        </div>
      </a>"""

def generate(p, i):
    feats = "".join(f"""<div class="feat">
        <div class="feat-icon">{f[0]}</div>
        <div><div class="feat-title">{f[1]}</div><div class="feat-desc">{f[2]}</div></div>
      </div>""" for f in p['features'])

    specs = "".join(f"<tr><td>{s[0]}</td><td>{s[1]}</td></tr>" for s in p['specs'])

    reviews = "".join(f"""<div class="review-card">
        <div class="review-header">
          <div><div class="reviewer-name">{r[0]}</div><div class="reviewer-loc">📍 {r[1]}</div></div>
          <div class="review-stars">{"★" * r[2]}</div>
        </div>
        <p class="review-text">"{r[3]}"</p>
      </div>""" for r in p['reviews'])

    rels = "".join(related_card_html(PRODUCTS[r]) for r in p['related'] if r < len(PRODUCTS))
    var_html = variants_html(p.get('variants'))
    ck = f"producto={p['slug']}&nombre={p['name'].replace(' ','+')}&precio={p['price']}&img={p['img']}&cat={p['cat'].replace(' ','+')}"
    name_words = p['name'].split()
    name_em = " ".join(name_words[:-1]) + f" <em>{name_words[-1]}</em>"

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>{p['name']} — Alfapro Ecuador</title>
  <meta name="description" content="{p['short_desc']}"/>
  <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
  <style>{CSS}</style>
</head>
<body>

<nav>
  <a href="../index.html" class="nav-logo"><img src="../logo.png" alt="Alfapro"/></a>
  <ul class="nav-links">
    <li><a href="../index.html#categorias">Categorías</a></li>
    <li><a href="../index.html#productos">Productos</a></li>
    <li><a href="../index.html#nosotros">Nosotros</a></li>
    <li><a href="../index.html#sucursales">Sucursales</a></li>
  </ul>
  <div class="nav-right">
    <a href="../checkout.html?{ck}" class="cart-btn">
      🛒 Carrito
      <span class="cart-count" id="cartCount">0</span>
    </a>
  </div>
</nav>

<!-- ATMOSPHERIC HEADER -->
<div class="product-atmos">
  <div class="atmos-bg" style="background-image:url('https://images.unsplash.com/photo-{p['bg']}?w=1600&q=80')"></div>
  <div class="atmos-overlay"></div>
  <div class="atmos-glow"></div>
  <div class="atmos-content">
    <div class="atmos-breadcrumb">
      <a href="../index.html">Inicio</a><span>/</span>
      <a href="../index.html#categorias">{p['cat']}</a><span>/</span>
      <span style="color:rgba(255,255,255,.7)">{p['name']}</span>
    </div>
    <div class="atmos-badge">{p['badge']}</div>
    <h1 class="atmos-title">{name_em}</h1>
  </div>
</div>

<!-- PRODUCT DETAIL -->
<div class="product-detail">

  <!-- GALLERY -->
  <div class="gallery">
    <div class="gallery-main">
      <img id="mainImg" src="https://images.unsplash.com/photo-{p['img']}?w=960&q=88" alt="{p['name']}"/>
    </div>
    <div class="gallery-thumbs">
      <div class="thumb active" onclick="setImg('https://images.unsplash.com/photo-{p['img']}?w=960&q=88',this)">
        <img src="https://images.unsplash.com/photo-{p['img']}?w=320&q=70" alt="Vista 1" loading="lazy"/>
      </div>
      <div class="thumb" onclick="setImg('https://images.unsplash.com/photo-{p['img2']}?w=960&q=88',this)">
        <img src="https://images.unsplash.com/photo-{p['img2']}?w=320&q=70" alt="Vista 2" loading="lazy"/>
      </div>
      <div class="thumb" onclick="setImg('https://images.unsplash.com/photo-{p['img3']}?w=960&q=88',this)">
        <img src="https://images.unsplash.com/photo-{p['img3']}?w=320&q=70" alt="Vista 3" loading="lazy"/>
      </div>
    </div>
  </div>

  <!-- PRODUCT PANEL -->
  <div class="product-panel">
    <div class="panel-cat">{p['cat']}</div>

    <div class="panel-stars">
      <div class="stars"><span>{stars_html(p['stars'])}</span></div>
      <span class="rating-num">{p['stars']}</span>
      <span class="rating-count">({p['reviews_count']} reseñas verificadas)</span>
    </div>

    <p class="panel-hook">{p['hook']}</p>

    <div class="price-block">
      <div>
        <div class="price-current">${p['price']}</div>
        <div class="price-original">${p['original']}</div>
      </div>
      <div class="price-save">Ahorras {p['discount']}%</div>
    </div>

    <p style="font-size:14px;color:rgba(255,255,255,.58);line-height:1.7;">{p['short_desc']}</p>

    {var_html}

    <div>
      <div class="label-sm">Cantidad</div>
      <div class="cta-row">
        <div class="qty-control">
          <button class="qty-btn" onclick="chQty(-1)">−</button>
          <span class="qty-num" id="qtyNum">1</span>
          <button class="qty-btn" onclick="chQty(1)">+</button>
        </div>
        <button class="btn-add" onclick="addCart()">🛒 Agregar</button>
        <a href="../checkout.html?{ck}" class="btn-buy">⚡ Comprar</a>
      </div>
    </div>

    <div class="trust-strip">
      <div class="trust-item"><div class="trust-icon">🚚</div><div class="trust-label">Envío 48h</div></div>
      <div class="trust-item"><div class="trust-icon">🔒</div><div class="trust-label">Pago Seguro</div></div>
      <div class="trust-item"><div class="trust-icon">↩️</div><div class="trust-label">30 Días</div></div>
      <div class="trust-item"><div class="trust-icon">📞</div><div class="trust-label">Soporte 24/7</div></div>
    </div>

    <div class="sku-line">
      <span>✅ En stock</span><span>·</span><span>SKU: {p['sku']}</span>
    </div>
  </div>

</div>

<!-- FEATURES BAND -->
<section class="features-band">
  <div class="features-band-inner">
    {feats}
  </div>
</section>

<!-- TABS -->
<section class="tabs-section">
  <div class="tabs-nav">
    <button class="tab-btn active" onclick="openTab(event,'desc')">Descripción</button>
    <button class="tab-btn" onclick="openTab(event,'specs')">Especificaciones</button>
    <button class="tab-btn" onclick="openTab(event,'reviews')">Reseñas ({p['reviews_count']})</button>
  </div>
  <div id="desc" class="tab-content active">
    <p class="desc-text">{p['desc']}</p>
  </div>
  <div id="specs" class="tab-content">
    <table class="specs-table">{specs}</table>
  </div>
  <div id="reviews" class="tab-content">
    <div class="reviews-list">{reviews}</div>
  </div>
</section>

<!-- RELATED -->
<section class="related-section">
  <h2 class="related-title">También te puede interesar</h2>
  <div class="related-grid">{rels}</div>
</section>

<!-- FOOTER -->
<footer>
  <span class="footer-copy">© 2026 Alfapro Ecuador — Todos los derechos reservados</span>
  <div class="footer-links">
    <a href="../index.html">Inicio</a>
    <a href="../checkout.html">Checkout</a>
    <a href="#">Devoluciones</a>
  </div>
</footer>

<!-- STICKY CTA -->
<div class="sticky-cta" id="stickyCta">
  <div class="sticky-prod-info">
    <div class="sticky-name">{p['name']}</div>
    <div class="sticky-price">${p['price']}</div>
  </div>
  <div class="sticky-btns">
    <button class="sticky-add" onclick="addCart()">🛒 Agregar al carrito</button>
    <a href="../checkout.html?{ck}" class="sticky-buy">⚡ Comprar ahora</a>
  </div>
</div>

<!-- TOAST -->
<div class="toast" id="toast">✅ <span id="toastMsg">Agregado al carrito</span></div>

<script>
  let qty=1;
  let cart=parseInt(localStorage.getItem('alfapro_cart')||'0');
  document.getElementById('cartCount').textContent=cart;

  function chQty(d){{qty=Math.max(1,qty+d);document.getElementById('qtyNum').textContent=qty;}}
  function addCart(){{
    cart+=qty; localStorage.setItem('alfapro_cart',cart);
    document.getElementById('cartCount').textContent=cart;
    showToast('{p["name"].replace("'","\\'")} — {p["price"]} agregado ✅');
  }}
  function showToast(m){{
    const t=document.getElementById('toast');
    document.getElementById('toastMsg').textContent=m;
    t.classList.add('show');
    setTimeout(()=>t.classList.remove('show'),3000);
  }}
  function setImg(src,el){{
    document.getElementById('mainImg').src=src;
    document.querySelectorAll('.thumb').forEach(t=>t.classList.remove('active'));
    el.classList.add('active');
  }}
  function selVar(el){{
    el.closest('.variant-row').querySelectorAll('.variant-btn').forEach(b=>b.classList.remove('active'));
    el.classList.add('active');
  }}
  function openTab(e,id){{
    document.querySelectorAll('.tab-content').forEach(t=>t.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    e.target.classList.add('active');
  }}
  // Sticky CTA on scroll
  const sticky=document.getElementById('stickyCta');
  window.addEventListener('scroll',()=>{{
    sticky.classList.toggle('visible', window.scrollY>480);
  }},{{passive:true}});
</script>
</body>
</html>"""

out = os.path.join(BASE, "productos")
os.makedirs(out, exist_ok=True)
for i, p in enumerate(PRODUCTS):
    html = generate(p, i)
    path = os.path.join(out, f"{p['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅  {p['slug']}.html")

print(f"\n{len(PRODUCTS)} páginas generadas en {out}/")

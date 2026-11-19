# Builds site/case-page.html, the Parkin'go case study served at wendelfreitas.com/parkingo/
# English is baked into the HTML; Spanish and Portuguese swap in from the same dictionary.
import json, pathlib, html

root = pathlib.Path(__file__).resolve().parent.parent
R = 'https://raw.githubusercontent.com/wendel-crypto/parkingo/main/docs/'
C = {
'title': ['Parkin’go — Parking app case study | Wendel Freitas', 'Parkin’go — Caso de estudio de app de estacionamiento | Wendel Freitas', 'Parkin’go — Case de app de estacionamento | Wendel Freitas'],
'back': ['← Cases / App', '← Casos / App', '← Cases / App'],
'eyebrow': ['Product concept · Mobile app · Mobility UX', 'Concepto de producto · App móvil · UX de movilidad', 'Conceito de produto · App mobile · UX de mobilidade'],
'lede': ['A parking app for Miami, dressed in neon. Find a garage from Brickell to Lincoln Road, reserve a bay, follow the route, check in with a QR pass, add time and keep every receipt. Taken from Figma wireframes to a working prototype.',
         'Una app de estacionamiento para Miami, vestida de neón. Encuentra un garaje de Brickell a Lincoln Road, reserva un espacio, sigue la ruta, haz el check-in con un pase QR, agrega tiempo y guarda cada recibo. De wireframes en Figma a un prototipo funcional.',
         'Um app de estacionamento para Miami, vestido de neon. Encontre uma garagem de Brickell à Lincoln Road, reserve uma vaga, siga a rota, faça o check-in com um passe QR, adicione tempo e guarde cada recibo. De wireframes no Figma a um protótipo funcional.'],
'b1': ['Try the prototype ↓', 'Prueba el prototipo ↓', 'Teste o protótipo ↓'], 'b2': ['Full screen', 'Pantalla completa', 'Tela cheia'],
'b3': ['View the code ↗', 'Ver el código ↗', 'Ver o código ↗'], 'open': ['Open the live prototype', 'Abrir el prototipo en vivo', 'Abrir o protótipo ao vivo'],
'close': ['Close ✕', 'Cerrar ✕', 'Fechar ✕'], 'ovt': ['Parkin’go · live prototype', 'Parkin’go · prototipo en vivo', 'Parkin’go · protótipo ao vivo'],
'all': ['All cases', 'Todos los casos', 'Todos os cases'],
'f1': ['Screens in the app', 'Pantallas en la app', 'Telas no app'], 'f2': ['Garages to search', 'Garajes para buscar', 'Garagens para buscar'], 'f3': ['Languages', 'Idiomas', 'Idiomas'], 'f4': ['File, no build step', 'Archivo, sin compilación', 'Arquivo, sem build'],
'pe': ['The problem', 'El problema', 'O problema'],
'ph': ['Finding a spot should not take longer than the drive.', 'Encontrar estacionamiento no debería tardar más que el viaje.', 'Achar uma vaga não deveria demorar mais que a viagem.'],
'p1': ['In Miami you circle Brickell looking for a bay, pay at a meter that wants its own app, and watch the clock because the sign says two hours. Garages have room, but the driver cannot see it, cannot hold a bay and cannot add time without walking back.',
       'En Miami das vueltas por Brickell buscando un espacio, pagas en un parquímetro que pide su propia app y miras el reloj porque el letrero dice dos horas. Los garajes tienen lugar, pero el conductor no lo ve, no puede apartar un espacio ni agregar tiempo sin volver caminando.',
       'Em Miami você dá voltas em Brickell atrás de uma vaga, paga em um parquímetro que exige o próprio app e olha o relógio porque a placa diz duas horas. As garagens têm espaço, mas o motorista não vê, não consegue reservar e não pode adicionar tempo sem voltar a pé.'],
'p2': ['Parkin’go puts the whole stop in one flow: choose a garage, reserve a numbered bay, drive there with a route, show a QR pass at the gate, extend from your phone and check out with a receipt.',
       'Parkin’go pone toda la parada en un solo flujo: elige un garaje, reserva un espacio numerado, maneja con una ruta, muestra un pase QR en la entrada, extiende desde el teléfono y haz el check-out con recibo.',
       'O Parkin’go coloca a parada inteira em um só fluxo: escolha uma garagem, reserve uma vaga numerada, dirija com uma rota, mostre um passe QR na entrada, estenda pelo celular e faça o check-out com recibo.'],
'p3': ['Every screen asks for one decision, with large targets, for a driver who has one eye on the road.', 'Cada pantalla pide una sola decisión, con botones grandes, para un conductor con un ojo en el camino.', 'Cada tela pede uma única decisão, com alvos grandes, para um motorista com um olho na estrada.'],
'te': ['Interactive prototype', 'Prototipo interactivo', 'Protótipo interativo'], 'th': ['Use it right here.', 'Úsalo aquí mismo.', 'Use aqui mesmo.'],
'tp': ['This is the working prototype, not a video. Sign in with the demo details, search garages, tap a map pin, reserve a bay, follow the route, check in, add time and check out to watch your activity and statistics update. Or jump to a part:',
       'Este es el prototipo real, no un video. Entra con los datos de prueba, busca garajes, toca un pin del mapa, reserva un espacio, sigue la ruta, haz el check-in, agrega tiempo y haz el check-out para ver cómo cambian tu actividad y tus estadísticas. O ve directo a una parte:',
       'Este é o protótipo de verdade, não um vídeo. Entre com os dados de teste, busque garagens, toque em um pin do mapa, reserve uma vaga, siga a rota, faça o check-in, adicione tempo e faça o check-out para ver atividade e estatísticas mudarem. Ou vá direto a uma parte:'],
'j1': ['Explore', 'Explorar', 'Explorar'], 'j1s': ['Map pins with prices and the closest garage', 'Pines con precios y el garaje más cercano', 'Pins com preços e a garagem mais próxima'],
'j2': ['Search and filter', 'Buscar y filtrar', 'Buscar e filtrar'], 'j2s': ['Try Covered, EV charging or Favorites', 'Prueba Techado, Carga eléctrica o Favoritos', 'Teste Coberto, Recarga elétrica ou Favoritos'],
'j3': ['Pick a bay', 'Elegir un espacio', 'Escolher uma vaga'], 'j3s': ['Choose A12, see the subtotal, reserve', 'Elige A12, mira el subtotal, reserva', 'Escolha A12, veja o subtotal, reserve'],
'j4': ['Route', 'Ruta', 'Rota'], 'j4s': ['A neon route across downtown to the garage', 'Una ruta de neón por el centro hasta el garaje', 'Uma rota neon pelo centro até a garagem'],
'j5': ['Live session', 'Sesión en curso', 'Sessão em andamento'], 'j5s': ['A countdown you can extend or end', 'Una cuenta regresiva que puedes extender o terminar', 'Uma contagem regressiva que dá para estender ou encerrar'],
'j6': ['Statistics', 'Estadísticas', 'Estatísticas'], 'j6s': ['Today, week or month; chart or table', 'Hoy, semana o mes; gráfico o tabla', 'Hoje, semana ou mês; gráfico ou tabela'],
'note': ['Demo data · invented garages · photos from Unsplash · nothing is saved', 'Datos de prueba · garajes inventados · fotos de Unsplash · nada se guarda', 'Dados de teste · garagens fictícias · fotos do Unsplash · nada é salvo'],
'se': ['Screens', 'Pantallas', 'Telas'], 'sh': ['Five stages: get set up, find, go, park, review.', 'Cinco etapas: configurar, encontrar, ir, estacionar, revisar.', 'Cinco etapas: configurar, encontrar, ir, estacionar, revisar.'],
'xe': ['Process', 'Proceso', 'Processo'], 'xh': ['From a Toronto wireframe to a Miami product.', 'De un wireframe de Toronto a un producto de Miami.', 'De um wireframe de Toronto a um produto de Miami.'],
'x1': ['The concept started in Figma as a low-fidelity flow with sample garages near downtown Toronto, priced in Canadian dollars. The wireframes fixed the order of decisions before any color existed: set up a vehicle and a card, find a spot, get there, check in, manage the stay.',
       'El concepto empezó en Figma como un flujo de baja fidelidad con garajes de ejemplo cerca del centro de Toronto, en dólares canadienses. Los wireframes fijaron el orden de las decisiones antes de que existiera el color: configurar vehículo y tarjeta, encontrar un lugar, llegar, hacer el check-in, gestionar la estadía.',
       'O conceito começou no Figma como um fluxo de baixa fidelidade com garagens de exemplo perto do centro de Toronto, em dólares canadenses. Os wireframes fixaram a ordem das decisões antes de existir cor: configurar veículo e cartão, achar uma vaga, chegar, fazer o check-in, gerenciar a permanência.'],
'x2': ['The high-fidelity pass added a calm teal system on white cards. This build keeps the flow and moves it to Miami: US dollars, a Brickell, Wynwood and Miami Beach map, five invented garages, favorites, a running session timer, receipts and statistics, in English, Spanish and Portuguese from one file.',
       'La alta fidelidad agregó un sistema turquesa sereno sobre tarjetas blancas. Esta versión mantiene el flujo y lo lleva a Miami: dólares, un mapa de Brickell, Wynwood y Miami Beach, cinco garajes inventados, favoritos, un temporizador de sesión, recibos y estadísticas, en inglés, español y portugués desde un solo archivo.',
       'A alta fidelidade trouxe um sistema turquesa sereno sobre cartões brancos. Esta versão mantém o fluxo e o leva para Miami: dólares, um mapa de Brickell, Wynwood e Miami Beach, cinco garagens fictícias, favoritos, um cronômetro de sessão, recibos e estatísticas, em inglês, espanhol e português em um único arquivo.'],
'w1': ['Low-fidelity wireframes', 'Wireframes de baja fidelidad', 'Wireframes de baixa fidelidade'], 'w2': ['High-fidelity design', 'Diseño de alta fidelidad', 'Design de alta fidelidade'],
'de': ['Design decisions', 'Decisiones de diseño', 'Decisões de design'], 'dh': ['Six choices that keep a short stop short.', 'Seis decisiones para que una parada corta siga siendo corta.', 'Seis escolhas para que uma parada curta continue curta.'],
'd1h': ['A price on every pin', 'Un precio en cada pin', 'Um preço em cada pin'], 'd1': ['The map shows the hourly rate on each pin, so choosing between a garage and a beach lot happens before you open a single screen.', 'El mapa muestra la tarifa por hora en cada pin, así que elegir entre un garaje y un lote de playa ocurre antes de abrir una pantalla.', 'O mapa mostra a tarifa por hora em cada pin, então escolher entre uma garagem e um estacionamento de praia acontece antes de abrir qualquer tela.'],
'd2h': ['One bay, one number', 'Un espacio, un número', 'Uma vaga, um número'], 'd2': ['The reserved bay, A12, follows you from the bay picker to the route, the arrival screen and the QR pass, so you never have to look it up again.', 'El espacio reservado, A12, te acompaña del selector a la ruta, la pantalla de llegada y el pase QR, así que nunca tienes que buscarlo de nuevo.', 'A vaga reservada, A12, acompanha você do seletor à rota, à tela de chegada e ao passe QR, então você nunca precisa procurar de novo.'],
'd3h': ['Time you can see', 'Tiempo a la vista', 'Tempo à vista'], 'd3': ['After check-in the stay becomes a countdown that lives on Explore and Activity. Extending is two taps away.', 'Tras el check-in la estadía se vuelve una cuenta regresiva que vive en Explorar y Actividad. Extender está a dos toques.', 'Depois do check-in a permanência vira uma contagem regressiva que fica em Explorar e Atividade. Estender está a dois toques.'],
'd4h': ['Filters for real needs', 'Filtros para necesidades reales', 'Filtros para necessidades reais'], 'd4': ['Covered, EV charging and Favorites sit above the list because those are the questions Miami drivers ask: shade, power and the garage they already trust.', 'Techado, Carga eléctrica y Favoritos van sobre la lista porque son las preguntas de los conductores de Miami: sombra, energía y el garaje en el que ya confían.', 'Coberto, Recarga elétrica e Favoritos ficam acima da lista porque são as perguntas dos motoristas de Miami: sombra, energia e a garagem em que já confiam.'],
'd5h': ['Receipts that add up', 'Recibos que suman', 'Recibos que somam'], 'd5': ['Check out and the session lands in Activity, then in Statistics by day, week or month, as a chart or a table, so the totals are never a surprise.', 'Haz el check-out y la sesión llega a Actividad y luego a Estadísticas por día, semana o mes, como gráfico o tabla, para que los totales no sorprendan.', 'Faça o check-out e a sessão vai para Atividade e depois para Estatísticas por dia, semana ou mês, em gráfico ou tabela, para os totais não surpreenderem.'],
'd6h': ['A demo that says what it is', 'Una demo que dice lo que es', 'Uma demo que diz o que é'], 'd6': ['Setup screens name their sample data: a demo plate, a demo card, a demo pass. The prototype stays honest and nothing you type is saved.', 'Las pantallas de configuración nombran sus datos de ejemplo: placa, tarjeta y pase de prueba. El prototipo es honesto y nada de lo que escribas se guarda.', 'As telas de configuração nomeiam seus dados de exemplo: placa, cartão e passe demo. O protótipo é honesto e nada do que você digita é salvo.'],
'ye': ['Design system', 'Sistema de diseño', 'Design system'], 'yh': ['Night purple, sunset pink, ocean cyan.', 'Morado nocturno, rosa atardecer, cian océano.', 'Roxo noturno, rosa pôr do sol, ciano oceano.'],
'y1': ['The Figma file was a calm teal system. For Miami it became Vice City: Ocean Drive neon, a striped sunset, palm silhouettes. Pink to orange marks every action, cyan marks the route and the live session, and yellow marks you on the map.',
       'El archivo de Figma era un sistema turquesa sereno. Para Miami se volvió Vice City: el neón de Ocean Drive, un atardecer a rayas, siluetas de palmeras. El rosa a naranja marca cada acción, el cian marca la ruta y la sesión en vivo, y el amarillo te marca en el mapa.',
       'O arquivo do Figma era um sistema turquesa sereno. Para Miami virou Vice City: o neon da Ocean Drive, um pôr do sol listrado, silhuetas de palmeiras. O rosa ao laranja marca cada ação, o ciano marca a rota e a sessão ao vivo, e o amarelo marca você no mapa.'],
'y2': ['Type is Outfit for the interface with a Yellowtail script for the sign. Targets are 42 pixels or larger, numbers use tabular figures, and the app works with a keyboard and respects reduced motion.',
       'La tipografía es Outfit para la interfaz con una script Yellowtail para el letrero. Los objetivos táctiles miden 42 píxeles o más, los números usan cifras tabulares, y la app funciona con teclado y respeta el movimiento reducido.',
       'A tipografia é Outfit na interface com a script Yellowtail no letreiro. Os alvos de toque têm 42 pixels ou mais, os números usam algarismos tabulares, e o app funciona com teclado e respeita movimento reduzido.'],
're': ['My role', 'Mi rol', 'Meu papel'], 'rh': ['Concept, UX and visual design. Built with Claude.', 'Concepto, UX y diseño visual. Construido con Claude.', 'Conceito, UX e design visual. Construído com Claude.'],
'r1': ['I defined the flow, drew the wireframes and high-fidelity screens in Figma, and directed the Miami adaptation and the Vice City restyle. The prototype was written with Claude as a single HTML file with no framework. Photos are from Unsplash.',
       'Definí el flujo, dibujé los wireframes y las pantallas de alta fidelidad en Figma, y dirigí la adaptación a Miami y el rediseño Vice City. El prototipo se escribió con Claude como un solo archivo HTML, sin framework. Las fotos son de Unsplash.',
       'Defini o fluxo, desenhei os wireframes e as telas de alta fidelidade no Figma, e dirigi a adaptação para Miami e o redesenho Vice City. O protótipo foi escrito com Claude como um único arquivo HTML, sem framework. As fotos são do Unsplash.'],
'r2': ['For a real launch the open work is the live part: garage inventory and bay availability from operators, payment authorization and receipts, plate recognition at the gate, turn-by-turn navigation and a plan for overstays.',
       'Para un lanzamiento real falta la parte en vivo: inventario y disponibilidad de espacios de los operadores, autorización de pagos y recibos, reconocimiento de placas en la entrada, navegación paso a paso y un plan para los excesos de tiempo.',
       'Para um lançamento real falta a parte ao vivo: inventário e disponibilidade de vagas dos operadores, autorização de pagamento e recibos, reconhecimento de placa na entrada, navegação passo a passo e um plano para excesso de permanência.'],
'fh': ['Have a product idea that needs to feel real?', '¿Tienes una idea de producto que necesita sentirse real?', 'Tem uma ideia de produto que precisa parecer real?'],
'fp': ['I take concepts from a wireframe to a prototype people can use, then shape the growth plan around it.', 'Llevo conceptos de un wireframe a un prototipo que la gente puede usar, y luego armo el plan de crecimiento alrededor.', 'Levo conceitos de um wireframe a um protótipo que as pessoas conseguem usar, e depois monto o plano de crescimento em volta.'],
'fb': ['Start a conversation →', 'Empecemos a conversar →', 'Vamos conversar →'],
}
def cap(n, en, es, pt): return (n, [en[0], es[0], pt[0]], [en[1], es[1], pt[1]])
S = [cap('01-intro', ('Welcome', 'A sunset over the city and one promise: find a better spot.'), ('Bienvenida', 'Un atardecer sobre la ciudad y una promesa: encuentra un mejor lugar.'), ('Boas-vindas', 'Um pôr do sol sobre a cidade e uma promessa: encontre uma vaga melhor.')),
     cap('05-plate', ('License plate', 'A Florida plate identifies the vehicle on the session. Sample data is prefilled.'), ('Placa', 'Una placa de Florida identifica el vehículo en la sesión. Datos de ejemplo ya cargados.'), ('Placa', 'Uma placa da Flórida identifica o veículo na sessão. Dados de exemplo já preenchidos.')),
     cap('06-payment', ('Payment setup', 'A demo card in sunset colors. No charge is ever made.'), ('Configurar pago', 'Una tarjeta de prueba en colores de atardecer. Nunca se cobra nada.'), ('Pagamento', 'Um cartão demo em cores de pôr do sol. Nenhuma cobrança é feita.')),
     cap('07-vehicle-type', ('Vehicle type', 'Hatchback, SUV, motorcycle or other, drawn as neon line art.'), ('Tipo de vehículo', 'Hatchback, SUV, moto u otro, dibujados como líneas de neón.'), ('Tipo de veículo', 'Hatch, SUV, moto ou outro, desenhados como linhas neon.')),
     cap('09-explore', ('Explore', 'A neon map of Brickell, Wynwood and Miami Beach with a price on every pin.'), ('Explorar', 'Un mapa de neón de Brickell, Wynwood y Miami Beach con precio en cada pin.'), ('Explorar', 'Um mapa neon de Brickell, Wynwood e Miami Beach com preço em cada pin.')),
     cap('10-search', ('Search and filter', 'Type a name or filter by Favorites, Covered or EV charging.'), ('Buscar y filtrar', 'Escribe un nombre o filtra por Favoritos, Techado o Carga eléctrica.'), ('Buscar e filtrar', 'Digite um nome ou filtre por Favoritos, Coberto ou Recarga elétrica.')),
     cap('11-spot', ('Spot details', 'Rate, distance, free bays, hours and what is included, with one button to continue.'), ('Detalles del lugar', 'Tarifa, distancia, espacios libres, horario y qué incluye, con un botón para seguir.'), ('Detalhes do local', 'Tarifa, distância, vagas livres, horário e o que está incluso, com um botão para seguir.')),
     cap('12-bay', ('Choose a bay', 'Pick from open bays; taken ones are dimmed. The subtotal updates.'), ('Elegir espacio', 'Elige entre espacios libres; los ocupados se atenúan. El subtotal se actualiza.'), ('Escolher vaga', 'Escolha entre vagas livres; as ocupadas ficam apagadas. O subtotal atualiza.')),
     cap('13-route', ('Route overview', 'A glowing route from downtown to the garage, with the reserved bay at the end.'), ('Resumen de ruta', 'Una ruta brillante del centro al garaje, con el espacio reservado al final.'), ('Visão da rota', 'Uma rota brilhante do centro até a garagem, com a vaga reservada no fim.')),
     cap('14-directions', ('Driving directions', 'The next turn up top. Tap it to step through the demo directions.'), ('Indicaciones', 'El siguiente giro arriba. Tócalo para recorrer las indicaciones de prueba.'), ('Direções', 'A próxima curva no topo. Toque para percorrer as direções demo.')),
     cap('15-trip', ('Trip in progress', 'The marker moves along the route with a progress bar and an arrival time.'), ('Viaje en curso', 'El marcador avanza por la ruta con una barra de progreso y la hora de llegada.'), ('Viagem em andamento', 'O marcador avança pela rota com barra de progresso e horário de chegada.')),
     cap('17-checkin', ('Check-in pass', 'A QR pass with the bay number and what happens when you start.'), ('Pase de check-in', 'Un pase QR con el número de espacio y lo que pasa al empezar.'), ('Passe de check-in', 'Um passe QR com o número da vaga e o que acontece ao começar.')),
     cap('18-session', ('Live session', 'A countdown with a progress meter. Extend or check out from here.'), ('Sesión en curso', 'Una cuenta regresiva con medidor. Extiende o haz el check-out desde aquí.'), ('Sessão em andamento', 'Uma contagem regressiva com medidor. Estenda ou faça o check-out daqui.')),
     cap('19-extend', ('Extend time', 'Add 30 or 60 minutes and see the extra cost before you confirm.'), ('Extender tiempo', 'Agrega 30 o 60 minutos y mira el costo extra antes de confirmar.'), ('Estender tempo', 'Adicione 30 ou 60 minutos e veja o custo extra antes de confirmar.')),
     cap('20-checkout', ('Check out', 'Review the total and rate the spot with one to five stars.'), ('Check-out', 'Revisa el total y califica el lugar con una a cinco estrellas.'), ('Check-out', 'Revise o total e avalie o local de uma a cinco estrelas.')),
     cap('21-activity', ('Activity', 'Recent sessions and receipts, with the live session pinned on top.'), ('Actividad', 'Sesiones y recibos recientes, con la sesión en vivo fijada arriba.'), ('Atividade', 'Sessões e recibos recentes, com a sessão ao vivo fixada no topo.')),
     cap('23-statistics', ('Statistics', 'Visits, spend and time parked by day, week or month, as a chart or a table.'), ('Estadísticas', 'Visitas, gasto y tiempo estacionado por día, semana o mes, en gráfico o tabla.'), ('Estatísticas', 'Visitas, gasto e tempo estacionado por dia, semana ou mês, em gráfico ou tabela.')),
     cap('24-profile', ('Profile', 'Vehicle, payment, favorites and language in one place.'), ('Perfil', 'Vehículo, pago, favoritos e idioma en un solo lugar.'), ('Perfil', 'Veículo, pagamento, favoritos e idioma em um só lugar.'))]
JUMPS = ['home', 'search', 'bay', 'route', 'session', 'stats']
SW = [('#0F0724', '#0F0724'), ('#1A0F3A', '#1A0F3A'), ('linear-gradient(135deg,#FF2E97,#FF8A3D)', 'Pink → Orange'), ('#1BE7FF', '#1BE7FF'), ('#8B5CFF', '#8B5CFF'), ('#FFD23F', '#FFD23F')]

e = lambda k: html.escape(C[k][0], quote=False)
k = lambda key, tag='span', cls='', extra='': f'<{tag}{(" class=" + chr(34) + cls + chr(34)) if cls else ""} data-k="{key}"{extra}>{e(key)}</{tag}>'
jump = ''.join(f'<button data-go="{g}"><span class="n">{i:02d}</span><span><b data-k="j{i}">{e("j%d" % i)}</b><small data-k="j{i}s">{e("j%ds" % i)}</small></span></button>'
               for i, g in enumerate(JUMPS, 1))
thumbs = ''.join(f'<button class="th{" on" if i == 0 else ""}" data-i="{i}"><img src="{R}thumbs/{n}.jpg" alt="" loading="lazy"><span>{i + 1:02d}</span></button>' for i, (n, _, _) in enumerate(S))
decisions = ''.join(f'<div><span class="num">{i:02d}</span><h3 data-k="d{i}h">{e("d%dh" % i)}</h3><p data-k="d{i}">{e("d%d" % i)}</p></div>' for i in range(1, 7))
sw = ''.join(f'<div><i style="background:{c}"></i><span>{n}</span></div>' for c, n in SW)

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e('title')}</title>
<meta name="description" content="Parkin’go is a parking app concept for Miami in a Vice City look: find a garage, reserve a bay, follow the route, check in with a QR pass, extend time and review receipts. Wireframes, design and a working prototype.">
<meta property="og:title" content="Parkin’go — Parking app case study"><meta property="og:description" content="Find, reserve and manage parking from Brickell to Miami Beach: map, bays, route, QR check-in, extensions and receipts."><meta property="og:image" content="{R}cover.jpg">
<link rel="canonical" href="https://www.wendelfreitas.com/parkingo/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{{--bg:#080808;--panel:#111;--line:#232323;--ink:#f4f4f1;--mute:#9a9a94;--lime:#c8f135;--blue:#194DED}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.6 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
a{{color:inherit}}button{{font:inherit;color:inherit;cursor:pointer}}.wrap{{max-width:1120px;margin:0 auto;padding:0 24px}}
:focus-visible{{outline:2px solid var(--lime);outline-offset:3px}}
header{{position:sticky;top:0;z-index:5;background:rgba(8,8,8,.86);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}}
header .wrap{{display:flex;align-items:center;gap:22px;min-height:64px}}
.logo{{font:800 22px Syne,sans-serif;text-decoration:none;letter-spacing:-.02em}}.logo span{{color:var(--lime)}}
nav{{display:flex;gap:22px;margin-left:auto;flex-wrap:wrap;align-items:center}}nav a{{font:500 12px 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;text-decoration:none;color:var(--mute)}}nav a:hover,nav a[aria-current]{{color:var(--ink)}}
.cta{{background:var(--lime);color:#080808!important;padding:10px 16px;border-radius:6px;font:600 13px Inter,sans-serif!important;letter-spacing:0!important;text-transform:none!important}}
.ov{{position:fixed;inset:0;z-index:60;background:rgba(4,2,10,.9);backdrop-filter:blur(8px);display:flex;flex-direction:column;align-items:center}}.ov[hidden]{{display:none}}
.ovbar{{width:100%;max-width:430px;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 14px;font:500 11px 'JetBrains Mono',monospace;letter-spacing:.1em;text-transform:uppercase;color:var(--mute)}}
.ovbar button{{border:1px solid #3a3a3a;border-radius:6px;background:none;padding:8px 12px;font:600 13px Inter,sans-serif;letter-spacing:0;text-transform:none;color:var(--ink)}}.ovbar button:hover{{border-color:var(--lime);color:var(--lime)}}
.ov iframe{{flex:1;min-height:0;width:100%;max-width:430px;border:0;background:#0F0724}}
@media(min-width:560px){{.ov iframe{{max-height:880px;border-radius:36px;border:1px solid #4A2C8F;margin-bottom:18px;box-shadow:0 30px 120px rgba(255,46,151,.3)}}}}
.mopen{{display:none;margin-top:20px;width:100%;text-align:center}}
.eyebrow{{font:500 12px 'JetBrains Mono',monospace;letter-spacing:.16em;text-transform:uppercase;color:var(--lime);margin:0 0 10px}}
h1{{font:800 clamp(38px,10vw,84px)/1 Syne,sans-serif;letter-spacing:-.03em;margin:14px 0 20px;text-wrap:balance}}h1 em{{font-style:normal;color:var(--lime)}}
h2{{font:700 clamp(26px,3.6vw,38px)/1.1 Syne,sans-serif;letter-spacing:-.02em;margin:0 0 18px;text-wrap:balance}}
.hero{{padding:72px 0 40px}}.lede{{max-width:660px;color:#c9c9c3;font-size:19px}}
.back{{font:500 12px 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);text-decoration:none}}
.btns{{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}}.btn{{display:inline-block;padding:13px 20px;border-radius:6px;border:1px solid #3a3a3a;text-decoration:none;font-weight:600;font-size:15px;background:none}}.btn.p{{background:var(--lime);color:#080808;border-color:var(--lime)}}
.cover{{margin-top:44px;border-radius:14px;overflow:hidden;border:1px solid var(--line)}}.cover img{{display:block;width:100%;height:auto}}
.facts{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:10px;overflow:hidden;margin:24px 0 0}}
.facts div{{background:var(--panel);padding:22px}}.facts b{{display:block;font:800 34px Syne,sans-serif;color:var(--lime);letter-spacing:-.02em}}.facts span{{font:500 11px 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--mute)}}
section{{padding:64px 0;border-top:1px solid var(--line)}}
.two{{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:48px}}.two p{{margin:0 0 16px;color:#c9c9c3}}
.play{{display:grid;grid-template-columns:minmax(0,1fr) 410px;gap:56px;align-items:center}}
.device{{width:410px;height:864px;border-radius:52px;background:#090314;padding:10px;box-shadow:0 0 0 1px #4A2C8F,0 40px 120px rgba(255,46,151,.25)}}
.device iframe{{width:390px;height:844px;border:0;border-radius:44px;display:block;background:#0F0724}}
.jump{{display:flex;flex-direction:column;gap:8px;margin-top:22px}}
.jump button{{display:flex;align-items:center;gap:14px;text-align:left;padding:14px 16px;border-radius:10px;background:var(--panel);border:1px solid var(--line);transition:.15s}}
.jump button:hover,.jump button.on{{border-color:var(--lime)}}.jump b{{font:700 15px Syne,sans-serif;display:block}}.jump small{{color:var(--mute);font-size:13.5px}}
.jump .n{{font:500 12px 'JetBrains Mono',monospace;color:var(--lime);min-width:22px}}
.note{{font:500 11px 'JetBrains Mono',monospace;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);margin-top:16px}}
.gal{{display:grid;grid-template-columns:360px minmax(0,1fr);gap:48px;align-items:start;margin-top:28px}}
.stage img{{width:100%;display:block;border-radius:34px;border:1px solid #2a2a2a;aspect-ratio:390/844;object-fit:cover;background:#0F0724}}
.cap b{{font:800 30px Syne,sans-serif;display:block;letter-spacing:-.02em;margin-bottom:6px}}.cap p{{color:#c9c9c3;margin:0 0 26px;max-width:520px;min-height:54px}}
.cap .ctr{{font:500 12px 'JetBrains Mono',monospace;color:var(--lime);letter-spacing:.12em}}
.thumbs{{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:10px}}
.th{{background:none;border:0;padding:0;text-align:left}}.th img{{width:100%;display:block;border-radius:12px;border:2px solid #222;aspect-ratio:240/519;object-fit:cover;transition:.15s;opacity:.6;background:#0F0724}}
.th span{{display:block;font:500 11px 'JetBrains Mono',monospace;letter-spacing:.08em;color:var(--mute);margin-top:6px}}
.th:hover img{{opacity:1}}.th.on img{{border-color:var(--lime);opacity:1}}.th.on span{{color:var(--ink)}}
.arrows{{display:flex;gap:8px;margin-bottom:22px}}.arrows button{{width:44px;height:44px;border-radius:50%;border:1px solid #3a3a3a;background:none;font-size:18px}}.arrows button:hover{{border-color:var(--lime);color:var(--lime)}}
.boards{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:8px}}.boards figure{{margin:0}}.boards a{{display:block;height:340px;overflow:hidden;border-radius:10px;border:1px solid var(--line)}}.boards img{{display:block;width:100%}}
.boards figcaption{{font:500 11px 'JetBrains Mono',monospace;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);margin-top:10px}}
.list{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:10px;overflow:hidden;margin-top:28px}}
.list div{{background:var(--panel);padding:24px}}.list h3{{font:700 18px Syne,sans-serif;margin:8px 0 6px}}.list p{{margin:0;color:var(--mute);font-size:15px}}.num{{font:500 12px 'JetBrains Mono',monospace;color:var(--lime)}}
.sw{{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0}}.sw div{{width:92px}}.sw i{{display:block;height:56px;border-radius:8px;border:1px solid #2a2a2a}}.sw span{{font:500 11px 'JetBrains Mono',monospace;color:var(--mute);display:block;margin-top:6px}}
.tags{{display:flex;flex-wrap:wrap;gap:8px}}.tags span{{font:500 12px 'JetBrains Mono',monospace;border:1px solid #333;border-radius:999px;padding:7px 12px;color:#c9c9c3}}
footer{{border-top:1px solid var(--line);padding:36px 0 56px;color:var(--mute);font-size:14px}}footer .wrap{{display:flex;gap:18px;flex-wrap:wrap;justify-content:space-between}}
@media(max-width:979px){{.play{{grid-template-columns:1fr}}.device{{display:none}}.mopen{{display:block}}#full{{display:none}}.gal{{grid-template-columns:1fr}}.stage{{max-width:340px;margin:0 auto}}.list{{grid-template-columns:1fr 1fr}}}}
@media(max-width:820px){{.two{{grid-template-columns:1fr;gap:20px}}.facts{{grid-template-columns:repeat(2,minmax(0,1fr))}}.list{{grid-template-columns:1fr}}.hide-m{{display:none}}.hero{{padding:44px 0 28px}}section{{padding:44px 0}}.thumbs{{gap:8px}}.boards a{{height:220px}}}}
@media(max-width:450px){{nav .cta{{padding:9px 12px}}}}
</style></head><body>
<header><div class="wrap"><a class="logo" href="/">W<span>F</span></a><nav><a class="hide-m" href="/">Home</a><a class="hide-m" href="/services">Services</a><a href="/cases" aria-current="page">Cases</a><a class="hide-m" href="/about">About</a><a class="cta" href="/contact">Get Free Audit →</a></nav></div></header>
<main>
<div class="wrap hero">
<a class="back" href="/cases" data-k="back">{e('back')}</a>
<p class="eyebrow" style="margin-top:28px" data-k="eyebrow">{e('eyebrow')}</p>
<h1>Parkin<em>’go</em></h1>
<p class="lede" data-k="lede">{e('lede')}</p>
<div class="btns"><a class="btn p" href="#try" data-k="b1">{e('b1')}</a><button class="btn" id="full" data-k="b2">{e('b2')}</button><a class="btn" href="https://github.com/wendel-crypto/parkingo" target="_blank" rel="noopener" data-k="b3">{e('b3')}</a></div>
<div class="cover"><img src="{R}cover.jpg" alt="Parkin’go explore, spot details, route, live session and statistics screens" width="1600" height="1000"></div>
<div class="facts"><div><b>24</b>{k('f1')}</div><div><b>5</b>{k('f2')}</div><div><b>3</b>{k('f3')}</div><div><b>1</b>{k('f4')}</div></div>
</div>
<section><div class="wrap two"><div>{k('pe','p','eyebrow')}{k('ph','h2')}</div><div>{k('p1','p')}{k('p2','p')}{k('p3','p')}</div></div></section>

<section id="try"><div class="wrap play"><div>
{k('te','p','eyebrow')}{k('th','h2')}
<p style="color:#c9c9c3;max-width:520px" data-k="tp">{e('tp')}</p>
<div class="jump" id="jump">{jump}</div>
<button class="btn p mopen" id="openm" data-k="open">{e('open')}</button>
{k('note','p','note')}
</div>
<div class="device"><iframe id="app" title="Parkin’go interactive prototype"></iframe></div>
</div></section>

<section><div class="wrap">{k('se','p','eyebrow')}{k('sh','h2')}
<div class="gal"><div class="stage"><img id="stageImg" src="{R}screens/{S[0][0]}.jpg" alt=""></div>
<div><div class="arrows"><button id="prev" aria-label="Previous screen">←</button><button id="next" aria-label="Next screen">→</button></div>
<div class="cap"><span class="ctr" id="ctr">01 / 18</span><b id="capT"></b><p id="capP"></p></div>
<div class="thumbs" id="thumbs">{thumbs}</div></div></div></div></section>

<section><div class="wrap two"><div>{k('xe','p','eyebrow')}{k('xh','h2')}</div><div>{k('x1','p')}{k('x2','p')}
<div class="boards"><figure><a href="{R}wireframes.jpg" target="_blank" rel="noopener"><img src="{R}wireframes.jpg" alt="Board of low-fidelity wireframes" loading="lazy"></a>{k('w1','figcaption')}</figure><figure><a href="{R}high-fidelity.jpg" target="_blank" rel="noopener"><img src="{R}high-fidelity.jpg" alt="Board of high-fidelity frames" loading="lazy"></a>{k('w2','figcaption')}</figure></div></div></div></section>

<section><div class="wrap">{k('de','p','eyebrow')}{k('dh','h2')}<div class="list">{decisions}</div></div></section>

<section><div class="wrap two"><div>{k('ye','p','eyebrow')}{k('yh','h2')}</div><div>{k('y1','p')}<div class="sw">{sw}</div>{k('y2','p')}</div></div></section>

<section><div class="wrap two"><div>{k('re','p','eyebrow')}{k('rh','h2')}</div><div>{k('r1','p')}{k('r2','p')}
<div class="tags" style="margin-top:22px"><span>Product concept</span><span>UX / UI</span><span>Figma</span><span>Mobility</span><span>Prototyping</span><span>HTML · CSS · JS</span><span>EN · ES · PT</span><span>Claude</span></div></div></div></section>

<section><div class="wrap" style="text-align:center">{k('fh','h2')}<p style="color:var(--mute);max-width:540px;margin:0 auto 24px" data-k="fp">{e('fp')}</p><a class="btn p" href="/contact" data-k="fb">{e('fb')}</a></div></section>
</main>
<div class="ov" id="ov" hidden role="dialog" aria-modal="true" aria-label="Parkin’go live prototype"><div class="ovbar"><span data-k="ovt">{e('ovt')}</span><button id="ovx" data-k="close">{e('close')}</button></div><iframe id="ovf" title="Parkin’go interactive prototype"></iframe></div>
<footer><div class="wrap"><span>© 2026 Wendel Freitas · Miami</span><span><a href="/cases" data-k="all">{e('all')}</a> · <a href="https://linkedin.com/in/wendel-de-freitas">LinkedIn</a> · <a href="https://github.com/wendel-crypto">GitHub</a></span></div></footer>
<script>
const C={json.dumps(C, ensure_ascii=False)},S={json.dumps([[R + 'screens/' + n + '.jpg', t, p] for n, t, p in S], ensure_ascii=False)},LG=['en','es','pt'];
const APP='/parkingo/app/?embed';
/* Language is owned by the shared site script (/wf-site.vN.js): it keeps 'wf-lang' and sets <html lang>. This page only follows it. */
const LI=()=>{{let l=document.documentElement.lang||'en';try{{if(!window.__wfSite)l=localStorage.getItem('wf-lang')||l}}catch(e){{}}l=l.slice(0,2);return l==='es'?1:l==='pt'?2:0}};
let li=LI(),cur=0;
const img=document.getElementById('stageImg'),T=document.getElementById('capT'),P=document.getElementById('capP'),N=document.getElementById('ctr'),th=[...document.querySelectorAll('.th')];
const fr=document.getElementById('app'),ov=document.getElementById('ov'),ovf=document.getElementById('ovf'),desk=matchMedia('(min-width:980px)');
const send=(f,m)=>{{try{{f.contentWindow.postMessage(m,'*')}}catch(e){{}}}};
function show(i){{cur=(i+S.length)%S.length;img.src=S[cur][0];img.alt=S[cur][1][li];T.textContent=S[cur][1][li];P.textContent=S[cur][2][li];N.textContent=String(cur+1).padStart(2,'0')+' / '+S.length;th.forEach((t,k)=>{{t.classList.toggle('on',k===cur);t.setAttribute('aria-label',S[k][1][li])}})}}
function applyLang(){{li=LI();document.title=C.title[li];document.querySelectorAll('[data-k]').forEach(n=>{{const v=C[n.dataset.k][li];if(n.textContent!==v)n.textContent=v}});show(cur);[fr,ovf].forEach(f=>f.getAttribute('src')&&send(f,{{mr:'lang',v:LG[li]}}))}}
function loadDesk(){{if(desk.matches&&!fr.getAttribute('src'))fr.src=APP+'&lang='+LG[li]}}
function openOv(go){{if(!ovf.getAttribute('src'))ovf.src=APP+'&lang='+LG[li]+(go?'&screen='+go:'');else if(go)send(ovf,{{mr:'go',v:go}});ov.hidden=false;document.body.style.overflow='hidden';document.getElementById('ovx').focus()}}
function closeOv(){{ov.hidden=true;document.body.style.overflow=''}}
[fr,ovf].forEach(f=>f.addEventListener('load',()=>send(f,{{mr:'lang',v:LG[li]}})));
document.getElementById('full').onclick=()=>openOv();document.getElementById('openm').onclick=()=>openOv();document.getElementById('ovx').onclick=closeOv;
ov.addEventListener('click',e=>{{if(e.target===ov)closeOv()}});
th.forEach(t=>t.onclick=()=>show(+t.dataset.i));document.getElementById('prev').onclick=()=>show(cur-1);document.getElementById('next').onclick=()=>show(cur+1);
document.addEventListener('keydown',e=>{{if(!ov.hidden){{if(e.key==='Escape')closeOv();return}}if(e.key==='ArrowRight')show(cur+1);if(e.key==='ArrowLeft')show(cur-1)}});
document.querySelectorAll('#jump button').forEach(b=>b.onclick=()=>{{document.querySelectorAll('#jump button').forEach(x=>x.classList.toggle('on',x===b));if(desk.matches){{loadDesk();send(fr,{{mr:'go',v:b.dataset.go}})}}else openOv(b.dataset.go)}});
const io='IntersectionObserver' in window?new IntersectionObserver(e=>{{if(e.some(x=>x.isIntersecting)){{loadDesk();io.disconnect()}}}},{{rootMargin:'600px'}}):null;io?io.observe(document.getElementById('try')):loadDesk();desk.addEventListener('change',()=>{{if(desk.matches)closeOv();loadDesk()}});
new MutationObserver(applyLang).observe(document.documentElement,{{attributes:true,attributeFilter:['lang']}});
S.forEach(s=>{{new Image().src=s[0]}});applyLang();
</script>
<script src="/wf-site.v13.js" defer></script>
</body></html>
'''
(root / 'site').mkdir(exist_ok=True)
(root / 'site' / 'case-page.html').write_text(page, encoding='utf-8')
print('site/case-page.html', len(page), 'bytes')

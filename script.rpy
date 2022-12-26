
# backgrounds
image blackBg = "backgrounds/blackBackground.jpg"
image wakeUp = "backgrounds/wakeUp.jpg"
image windowView = "backgrounds/windowView.jpg"
image window = "backgrounds/window.jpg"
image windowBluered = "backgrounds/windowBluered.jpg"
image winterStreet = "backgrounds/winterStreet.jpg"
image cityStreet = "backgrounds/cityStreet.jpg"
image businessCenter = "backgrounds/businessCenter.jpg"
image businessCenterInside = "backgrounds/businessCenterInside.jpg"
image office = "backgrounds/office.jpg"

# characters
define main = Character("Артем")
image main = "characters/main.png"
image mainWondered = "characters/mainWondered.png"
image mainSilent = "characters/mainSilent.png"
image mainTalk = "characters/mainTalk.png"

define alice = Character("Алиса")
image alice = "characters/aliceDefault.png"
image aliceTalk = "characters/aliceTalk.png"
image aliceSilent = "characters/aliceSilent.png"
image aliceGuilty = "characters/aliceGuilty.png"
image aliceAngry = "characters/aliceAngry.png"
image aliceAngryTalk = "characters/aliceAngryTalk.png"

define policeman = Character("Охранник")
image policeman = "characters/policeman.png"

define guideWoman = Character("Гид")
image guideWoman = "characters/guideWoman.png"

define anton = Character("Антон")
image anton = "characters/anton.png"

define andrey = Character("Андрей")
image andrey = "characters/andrey.png"


# music
define audio.alarmRing = "audio/alarmRing.wav"
define audio.birdsong = "audio/birdsong.wav"
define audio.doorKnock = "audio/doorKnock.wav"
define audio.doorOpenLight = "audio/doorOpenLight.wav"
define audio.doorOpen = "audio/doorOpen.wav"
define audio.doorClose = "audio/doorClose.wav"
define audio.snowNoise = "audio/snowNoise.wav"
define audio.winterMusic = "audio/winterMusic.wav"
define audio.streetMusic = "audio/streetMusic.wav"
define audio.businessCenterMusic = "audio/businessCenterMusic.wav"
define audio.stepsSound = "audio/stepsSound.wav"


# variables
define volumeSound = 0.2
define volumeMusic = 0.1


# code
label start:

    #jump wakeUp
    #jump windowView
    #jump window
    #jump winterStreet
    #jump cityWinterStreet
    jump businessCenter
    jump hallway
    jump office


    return

label wakeUp:
    
    play sound alarmRing volume(volumeSound)
    pause 3
    play sound alarmRing volume(volumeSound)
    pause 3

    scene blackBg

    "~Как молотом по наковальне…~"
    "~Этот звук казался мне не таким раздражающим~"
    "~Впрочем, он не так плох~"
    "~Если не просыпаться под него…~"
    "~И зачем я вообще купил этот будильник~"
    "~А может это всего лишь дело привычки. Человек ведь в ходе эволюции должен уметь приспособиться к плохим условиям~"

    "Холод"
    "Атмосферное давление"
    "Треск будильника"

    scene wakeUp with Dissolve(3)

    "~Ну, что ж, хватит философствовать, пора вставать. Интересно, что у нас там сегодня~"
    "~Ах, да, очередной день~"

label windowView:

    scene windowView with Dissolve(1)

    "~Опять зима. Отличное время года как по мне. Всё останавливается в своём хаотичном движении. Ленивые дни полные спокойствия~"
    scene windowView

    play sound birdsong volume(volumeSound)
    pause 6

    "~Люблю их тонкие голоса, особенно в декабре. Это одно из немногих украшений в этот период, помимо снега и всяких узоров на стёклах~"

label window:

    scene window with Dissolve(1)

    scene windowBluered with Dissolve(1)
    show main with Dissolve(1)
    


    main "~Даже не знаю чем сегодня можно заняться...~"

    play sound doorKnock volume(volumeSound)

    hide main



    show mainWondered
    main "~Интересно кто там? Надо посмотреть~" 
    main "~Хм, Алиса, моя давняя знакомая, интересно, что ей нужно~"

    play sound doorOpenLight volume(volumeSound)
    play sound doorOpen volume(volumeSound)

    hide mainWondered



    show mainTalk at left
    show aliceSilent at right

    main "Привет Алис..."

    hide mainTalk
    hide aliceSilent 



    show mainSilent at left
    show aliceTalk at right

    alice "Привет Артём, твои родители сказали, что ты дома. Я надеюсь, ты уже собрался ведь нам нужно немного поторопиться, чтобы всё успеть"

    hide mainSilent
    hide aliceTalk



    show aliceSilent at right 
    show mainTalk at left

    main "Что? Куда? О чём ты вообще говоришь? Не понимаю"

    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "Я надеюсь, ты шутишь. На прошлой неделе я рассказывала тебе об одной хорошей IT компании. Неужели ты забыл?"

    hide mainSilent
    hide aliceTalk



    show aliceSilent at right 
    show mainTalk at left

    main "Ах да, кажется, припоминаю, ну и что с ней?"

    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "..."
    alice "Ах да, кажется, припоминаю, ну и что с ней?"

    hide aliceSilent
    hide mainTalk



    show aliceSilent at right 
    show mainTalk at left

    main "Ну что ж… обещания нужно выполнять. Тем более я уже давно никуда не выбирался, да и сфера мне интересна"
    main "~Ничего не поделаешь~"
    main "Ладно, пойдём"

    hide aliceSilent
    hide mainTalk    

    play sound doorClose volume(volumeSound)
    scene blackBg with Dissolve(2)

label winterStreet:

    play sound snowNoise volume(volumeSound)
    scene winterStreet with Dissolve(2)
    play music winterMusic fadein 1.0



    show aliceSilent at right 
    show mainTalk at left

    main "Итак, куда мы направляемся?"

    hide aliceSilent
    hide mainTalk        



    show mainSilent at left
    show aliceTalk at right

    alice "Сама компания находится в одном из бизнес центров. Я думаю, что нам проведут экскурсию по нему. Тебе тоже будет полезно, как человеку увлечённому"

    hide aliceSilent
    hide mainTalk



    show aliceSilent at right 
    show mainTalk at left

    main "Увлечённому в отличие от тебя. Ты ведь ничем подобным ранее не интересовалась, откуда внезапно такое любопытство?"

    hide aliceSilent
    hide mainTalk        



    show mainSilent at left
    show aliceTalk at right

    alice "Мне всегда нравилось пробовать что-то новое. Ты же знаком с ребятами из нашего школьного информационного клуба?"

    hide aliceSilent
    hide mainTalk



    show aliceSilent at right 
    show mainTalk at left

    main "Наши «программисты?». Нууу да, знаю нескольких"

    hide aliceSilent
    hide mainTalk           



    show mainSilent at left
    show aliceTalk at right

    alice "Так вот, недавно они попросили меня побыть одним из организаторов их мероприятия. Ну и в процессе я заинтересовалась всем этим."

    hide aliceSilent
    hide mainTalk



    show aliceSilent at right 
    show mainTalk at left

    main "Так вот, недавно они попросили меня побыть одним из организаторов их мероприятия. Ну и в процессе я заинтересовалась всем этим"

    hide aliceSilent
    hide mainTalk   



    show mainSilent at left
    show aliceTalk at right

    alice "Я посетила несколько их занятий и узнала о важных основах"
    alice "Ребята рассказали мне о том насколько важна и востребована их сфера деятельности сегодня"
    alice "Поведали о различных перспективах и практическом применении их работы"

    hide aliceSilent
    hide mainTalk   



    show mainTalk at left
    show aliceSilent at right

    main "Понятно, а об этом «мероприятии» на которое мы направляемся, тоже рассказали они?"

    hide aliceSilent
    hide mainTalk 



    show mainSilent at left
    show aliceTalk at right

    alice "Конечно, когда я о нём услышала то сразу поняла, что мне обязательно нужно туда сходиться, даже если я мало, что пойму это будет полезный опыт для меня"

    hide aliceTalk
    hide mainSilent



    show mainTalk at left
    show aliceSilent at right

    main "Это конечно всё отлично, но долго нам ещё идти до этого центра?"

    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "Он находится рядом с историческим районом города, поэтому должно быть близко"

    hide aliceTalk
    hide mainSilent


    stop music fadeout 1.0
    play sound snowNoise volume(volumeSound)
    scene blackBg with Dissolve(2)

label cityWinterStreet:

    scene cityStreet
    play music streetMusic fadein 1.0



    show mainSilent at left
    show aliceTalk at right

    alice "Артём мне сейчас стало интересно, а почему ты вообще начал этим заниматься и что тебя так привлекает во всём этом?"

    hide aliceTalk
    hide mainSilent



    show mainTalk at left
    show aliceSilent at right

    main "Ты понимаешь, ведь за всем этим стоит наше будущее, по крайне мере мне так кажется"
    main "Все эти сети, интернет, связь. Человек всегда стремится к чему-то новому"
    main "Люди всегда хотели найти ответы на интересующие их вопросы, и допустим, в интернете они ищут их так же, как в жизни"

    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "Ну, это ведь просто замечательно"

    hide aliceTalk
    hide mainSilent




    show mainTalk at left
    show aliceSilent at right

    main "Конечно, это всё замечательно, но, к сожалению, иногда за свой комфорт приходится расплачиваться собственной безопасностью,"
    main "киберпреступность и прочее  обычное мошенничество никто не отменял"
    main "Никогда не знаешь, что способен преподнести тебе интернет. Как-нибудь расскажу обо всём этом в другой раз"

    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "Хорошо, возьму себе на заметку"

    hide aliceTalk
    hide mainSilent



    show mainTalk at left
    show aliceSilent at right

    main "Как же я давно не был в этом районе города. А тут неплохо, надо прогуливаться здесь почаще"

    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "Согласна. Когда я была маленькая мы с семьёй тут жили, но потом родители переехать подальше от центра"
    alice "Возможно, родителям надоела эта суета. Хорошее было время, из забот только уход за хомячком"

    hide aliceTalk
    hide mainSilent



    show mainTalk at left
    show aliceSilent at right

    main "У тебя было домашнее животное? Не помню, чтобы ты когда-либо это рассказывала, хоть я и знаю тебя довольно давно"
    
    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "Да, был один маленький до того как я пошла в школу, а потом он погиб"

    hide aliceTalk
    hide mainSilent



    show mainTalk at left
    show aliceSilent at right

    main "Ну что ж, мне очень жаль, хоть и это было так давно"
    
    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "Да ладно, ничего такого, ведь помимо этого в детстве были и хорошие моменты, которых было куда больше, конечно же"
    alice "На то оно и детство хах"

    hide aliceTalk
    hide mainSilent



    show mainTalk at left
    show aliceSilent at right

    main "Когда ты начала говорить на эту тему у меня тоже освежились некоторые воспоминания. Помнишь, как мы проводили лето на даче?"
    main "Старая папина машина, сбор грибов, речка и многое другое"
    main "Время без забот…"
    
    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "Прошлое это конечно хорошо, но надо и о будущем подумать. Ты уже задумывался о возможной профессии? Мне кажется у тебя неплохие перспективы в этой информационной области"
    alice "Думаю, что сегодня ты лишний раз в этом убедишься и не пожалеешь что согласился пойти со мной"

    hide aliceTalk
    hide mainSilent



    show mainTalk at left
    show aliceSilent at right

    main "Ну, даже не знаю, скоро увидим"
    
    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "Отказываться поздно, тем более что мы почти пришли"

    hide aliceTalk
    hide mainSilent



    show mainTalk at left
    show aliceSilent at right

    main "Как? Уже?"
    
    hide aliceSilent
    hide mainTalk


    scene blackBg with Dissolve(1)

label businessCenter:

    scene businessCenterInside
    play music businessCenterMusic volume(volumeMusic) fadein 1.0

    show mainTalk at left 
    show aliceSilent at right

    main "Мда, неплохой небоскрёб. Я думал он будет гораздо меньше"
    
    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "А я почему-то именно так себе его и представляла"

    hide aliceTalk
    hide mainSilent


    show mainTalk at left
    show aliceSilent at right

    main "Возможно, потому-что ты слышала о нём ранее"
    
    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "…и видела"

    hide aliceTalk
    hide mainSilent


    show mainTalk at left
    show aliceSilent at right

    main "Так… и куда же нам надо?"
    
    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "Честно говоря, пока точно не знаю, но думаю, что нам помогут. Надо спросить у кого-нибудь вдруг кто знает"

    hide aliceTalk
    hide mainSilent


    show mainTalk at left
    show aliceSilent at right

    main "Может вон у того охранника?"
    
    hide aliceSilent
    hide mainTalk



    show mainSilent at left
    show aliceTalk at right

    alice "Отличная мысль"

    show policeman at center with Dissolve(1)
    
    alice "Здравствуйте, не могли бы вы подсказать, кто сегодня проводит экскурсию в этой компании по случаю дня открытых дверей?"

    hide aliceTalk
    show aliceSilent at right

    policeman "Точно не знаю, но я видел рядом группу молодых людей во главе с одной дамой, возможно, это они"

    hide aliceSilent
    show aliceTalk at right

    alice "Понятно, спасибо большое"

    hide policeman with Dissolve(1)

    alice "Ну, отлично.… И как нам теперь их искать?"

    hide aliceTalk
    hide mainSilent    


    show mainTalk at left
    show aliceSilent at right

    main "Мне кажется это не нужно"
    
    hide aliceSilent
    hide mainTalk


    show mainSilent at left
    show aliceTalk at right

    alice "Почему же?"

    hide aliceTalk
    hide mainSilent


    show mainTalk at left
    show aliceSilent at right

    main "Потому что я их уже вижу. Пойдем"


    play sound stepsSound volume(volumeSound)
    pause 1.5


    show mainSilent at left
    show aliceTalk at right
    show guideWoman at center with Dissolve(1)

    alice "Здравствуйте, видимо это вы проводите экскурсию? Тогда нам к вам"


    show mainSilent at left
    show aliceSilent at right

    guideWoman "Ах, здравствуйте, видимо вы те самые двое опоздавших. Мы как раз вас ждали" 

    hide mainSilent
    hide aliceSilent


    show mainSilent at left
    show aliceTalk at right

    alice "Артём я так и знала, что нам надо было быть чуть быстрее"

    hide aliceTalk
    hide mainSilent


    show mainTalk at left
    show aliceSilent at right

    main "Ну, ничего страшного, главное, что мы всё таки достигли цели"
    
    hide aliceSilent
    hide mainTalk


    show mainSilent at left
    show aliceSilent at right

    guideWoman "Итак, раз все в сборе то думаю, что можно начинать. Пройдёмте"

    hide aliceSilent
    hide mainSilent


    show mainSilent at left
    show aliceTalk at right

    alice "Да, давайте приступим. Я так долго этого ждала"

    hide aliceTalk
    hide mainSilent


    play sound stepsSound volume(volumeSound)


    show mainSilent at left
    show aliceSilent at right

    guideWoman "Как вы возможно уже знаете или же не знаете, сегодня сотрудники нашей компании расскажут вам о профессии DevOps инженера"
    guideWoman "Сама я знаю об этом не много т.к. работаю в другой области, но надеюсь, что сегодня вам это не помешает" 

    hide mainSilent
    hide aliceTalk


    show mainTalk at left
    show aliceSilent at right

    main "А чем вы занимаетесь?"
    
    hide aliceSilent
    hide mainTalk


    show mainSilent at left
    show aliceSilent at right

    guideWoman "Сама я занимаюсь больше непосредственно техническим обслуживанием техники. Работаю с всякими железками  и прочими"
    guideWoman "Возможно, расскажу вам об этом в другой раз. А сегодня я в роли проводника"

    hide mainSilent
    hide aliceSilent


    show mainSilent at left
    show aliceTalk at right

    alice "Звучит здорово, а как вы к этому пришли? Когда поняли что хотите этим заниматься?"

    hide aliceTalk
    hide mainSilent


    show mainSilent at left
    show aliceSilent at right

    guideWoman "Могу сказать, что это был долгий путь. Мои увлечения всегда менялись, поэтому я пришла к этому не сразу"
    guideWoman "Но в какой-то момент я просто поняла, что не могу без этого жить. Никогда не знаешь, что тебе приглянется"

    hide mainSilent
    hide aliceSilent


    show mainSilent at left
    show aliceTalk at right

    alice "Это точно, у меня что-то похожее"

    hide aliceTalk
    hide mainSilent
    hide guideWoman

    stop music fadeout 1.0
    scene blackBg with Dissolve(1)


label hallway:

    scene businessCenter

    show guideWoman at center
    show mainSilent at left
    show aliceSilent at right

    guideWoman "А вот и наша первая остановка. Сейчас Антон поведает вам о том чем он тут занимается"

    hide guideWoman with Dissolve(1)
    show anton at center with Dissolve(1)

    anton "Всем привет. Как вам уже рассказали сегодня, вы узнаете о профессии DevOps инженера"
    anton "А вообще вам что-нибудь известно о ней?"

    hide mainSilent
    hide aliceSilent


    show mainTalk at left 
    show aliceSilent at right

    main "Честно, затрудняюсь ответить"

    hide mainTalk
    hide aliceSilent


    show mainSilent at left
    show aliceSilent at right

    anton "Тогда я займусь тем, что расскажу вам о том, что это такое"
    anton "Грубо говоря, DevOps — это методология разработки, которая помогает наладить эффективное взаимодействие разработчиков с другими IT-специалистами"
    anton "Это набор процессов и инструментов, которые позволяют компании создавать и улучшать продукты быстрее,"
    anton "чем при использовании традиционных подходов к разработке программного обеспечения"

    hide mainSilent
    hide aliceSilent


    show mainTalk at left
    show aliceSilent at right

    main "Что же, звучит круто"

    hide mainTalk
    hide aliceSilent


    show mainSilent at left
    show aliceSilent at right

    anton "Да, но, тем не менее, определение DevOps очень сложное именно поэтому я сегодня здесь, чтобы помочь вам"

    hide mainSilent
    hide aliceSilent    


    show aliceTalk at right
    show mainSilent at left

    alice "В первую очередь конечно хотелось бы узнать для чего он вообще нужен?"

    hide mainSilent
    hide aliceTalk


    show mainSilent at left
    show aliceSilent at right

    anton "Многие считают, что DevOps — это просто автоматизация или похожая штука, которая уже была в каждой компании"
    anton "За 9 лет развития сообщества и методологии уже стало понятно,"
    anton "что это все-таки не маркетинговые блестки, но все равно не до конца понятно зачем он нужен"
    anton "Как у любого инструмента и процесса, у DevOps есть конкретные цели, которые он в итоге решает"

    hide mainSilent
    hide aliceSilent    


    show mainTalk at left
    show aliceSilent at right

    main "Интересно что же это за цели?"

    hide mainTalk
    hide aliceSilent


    show mainSilent at left
    show aliceSilent at right

    anton "Здесь IT используется исключительно для автоматизации процессов"
    anton "Автоматизация не часто меняется, потому что когда компания катится по наезженной колее — что там менять?"
    anton "Работает — не трогай" # true
    anton "Другими словами, т.е. речь, идёт об автоматизации процессов здесь решается проблема распределения времени"
    anton "DevOps пытается следовать принципу Time-to-market"
    anton "— это про минимизацию времени от идеи до конечной реализации"

    hide mainSilent
    hide aliceSilent        



    show aliceTalk at right
    show mainSilent at left

    alice "Т.е DevOps нужен для упрощения работы сотрудников между собой?"

    hide mainSilent
    hide aliceTalk


    show mainSilent at left
    show aliceSilent at right

    anton "Именно так. Единственное, что базово меняется в DevOps — это именно структура коммуникации между командами"
    anton "С точки зрения процесса, до DevOps все стадии:"
    anton "аналитика, разработка, тестирование, эксплуатация, проходили линейно"
    anton "В случае DevOps все эти процессы идут одновременно"

    hide mainSilent
    hide aliceSilent      


    show mainTalk at left
    show aliceSilent at right

    main "Т.е одновременное выполнение процессов это как раз то, что нужно для принципа Time-to-market?"

    hide mainTalk
    hide aliceSilent


    show mainSilent at left
    show aliceSilent at right

    anton "Да, Time-to-market только так и может выполняться"
    anton "Для людей, которые работали в старом процессе, это выглядит несколько космически, и вообще так себе"
    anton "Ну вот и всё что я хотел вам сказать"

    hide mainSilent
    hide aliceSilent  


    show aliceTalk at right
    show mainSilent at left

    alice "Большое спасибо, тогда будем двигаться дальше"

    hide mainSilent
    hide aliceTalk

    show mainSilent at left
    show aliceSilent at right
    hide anton with Dissolve(1)
    show guideWoman with Dissolve(1)

    guideWoman "Ох, вы уже закончили. Время прошло так быстро"

    hide mainSilent
    hide aliceSilent    


    show mainTalk at left
    show aliceSilent at right

    main "И куда мы пойдём дальше?"

    hide mainTalk
    hide aliceSilent


    show mainSilent at left
    show aliceSilent at right

    guideWoman "Сейчас мы пойдём в наши офисные помещения. Сегодня там выходной поэтому мы не помешаем"

    hide mainSilent
    hide aliceSilent    


    show aliceTalk at right
    show mainSilent at left

    alice "А давно вы работаете здесь?"

    hide mainSilent
    hide aliceTalk


    show mainSilent at left
    show aliceSilent at right

    guideWoman "Недавно отметила свой первый юбилей – 5 лет в компании"
    guideWoman "Как видите это огромный комплекс, в котором трудятся тысячи людей"
    guideWoman "Вы тоже можете попасть сюда, если захотите пойти к нам"
    guideWoman "Здесь требуются специалисты любого спектра. От простых уборщиков до высококлассных программистов"

    hide mainSilent
    hide aliceSilent    


    show mainTalk at left
    show aliceSilent at right

    main "Стоит задуматься об этом"

    hide mainTalk
    hide aliceSilent
    hide guideWoman

    scene blackBg with Dissolve(1)

label office:
    
    scene office

    show guideWoman at left

    guideWoman "Хэй, Андрей, будет минутка?"

    show andrey at right with Dissolve(1)

    andrey "Да, что такое?"
    guideWoman "Ну, вообще-то это наши гости. И ты обещал мне, что расскажешь им про профессию"
    andrey "Конечно, я помню, как же можно такое забыть"
    andrey "Итак, вы уже где-то были до меня, возможно, вас что-то заинтересовало или было не понятно?"

    hide guideWoman with Dissolve(1)
    hide andrey with Dissolve(0.5)

    show andrey at center with Dissolve(0.5)
    show mainTalk at left with Dissolve(0.1)
    show aliceSilent at right with Dissolve(0.1)

    main "Нам говорили о том, что DevOps это современная технология будущего и о том, как она полезна"
    main "Но я так и не понял когда его стоит применять, а когда нет"

    hide mainTalk
    hide aliceSilent


    show aliceSilent at right
    show mainSilent at left

    andrey "Конечно же, его не стоит применять всегда. Если случаи когда он совсем не нужен"
    andrey "Например, если у компании нет цифровых продуктов требующих разработки или при сохранении сложности этой же разработки"
    andrey "А так же когда не требуется параллельное выполнение всех процессов"

    hide aliceSilent
    hide mainSilent


    show aliceTalk at right
    show mainSilent at left

    alice "Получается, что это технология только всё усложняет, и это мешает в случаях, где в этом нет необходимости"

    hide aliceTalk
    hide mainSilent


    show aliceSilent at right
    show mainSilent at left

    andrey "Так точно, потому что DevOps меняет полностью процесс и организацию в компании — точнее, меняет не DevOps, а цифровой продукт"
    andrey "Чтобы прийти к DevOps, надо все-таки этот процесс полностью поменять"    

    hide aliceSilent
    hide mainSilent


    show mainTalk at left
    show aliceSilent at right

    main "Вы как специалист в данной области, наверное, можете ответить нам, как понять, что компания идёт в сторону DevOps?"

    hide mainTalk
    hide aliceSilent


    show aliceSilent at right
    show mainSilent at left

    andrey "Конечно, могу. Есть ряд факторов влияющих на это"
    andrey "Среди них можно выделить основные три"    
    andrey "Во-первых, важно чтобы у вас была стратегия по созданию цифрового продукта"
    andrey "Если есть — уже хорошо. Это значит, что ваша компания движется в сторону DevOps"
    andrey "Если же ваша компания уже создаёт цифровой продукт это значит, что вы можете подняться еще на ступень выше, заниматься делами интереснее — с точки зрения DevOps опять-таки"
    andrey "Ну и последнее, если ваша компания один из лидеров рынка в нише с цифровым продуктом"

    hide aliceSilent
    hide mainSilent


    show aliceTalk at right
    show mainSilent at left

    alice "А правила оказались не такими уж и сложными"

    hide aliceTalk
    hide mainSilent


    show mainTalk at left
    show aliceSilent at right

    main "Если это такая замечательная технология, то, что же тогда ей мешает проникнуть повсеместно?"

    hide mainTalk
    hide aliceSilent


    





























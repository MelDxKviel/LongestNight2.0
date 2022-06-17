# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define g = Character("Роуз", image = 'geroy', color="#000000")
define l = Character("Лео", image = 'leo', color="#000000")
define c = Character("Купер", image = 'coop', color="#000000")
define v = Character("Вики", image = 'viki', color="#000000")
define s = Character("Сосед", image = 'stranger', color="#000000")
define m = Character("Маньяк", image = 'maniac', color="#000000")
define p = Character("Прохожие", image = 'people', color="#000000")
define music = Character("Музыкант", image = 'musician', color="#000000")
define a = Character(" ")

# Объявление музыки
define audio.main = "audio/main.mp3"
define audio.mystic = "audio/mystic.mp3"

# Начало игры
# Сцена 1
label start:

    show furgon leoviki with fade
    show geroy oghm

    play music "<loop 0>audio/music/lo-fi.mp3"
    play sound "audio/inside-car-wet-driving.mp3" volume 0.4

    g "“Мы едем уже целую вечность, идея внезапной поездки больше не кажется такой привлекательной, особенно в этом душном фургоне. В компании этой парочки мне как-то неловко. Я даже не помню, куда мы едем...”"
    g bok "Напомните, куда мы, собственно, едем?"

    show furgon viki with dissolve
    show leo sc1 with dissolve
    show geroy bok 
    

    l "Ты едешь с нами уже 3 часа и только сейчас опомнилась?"

    show coop2

    c "Один богатей решил воспользоваться случаем и организовал фестиваль в честь затмения, я разве не рассказывал, чудилка?"

    hide coop2
    show leo phone_sc1
    show geroy sc1

    menu:
        "Почему я согласилась?":
            $ question = True

        "Долго еще ехать?":
            $ question = False

    if question == True:
        g bok "Точно! А напомните, почему я согласилась?"

        show furgon viki talk
        show geroy bok
        show leo phone_sc1

        v "Тебе было скучно, подруга, и мы взяли тебя с собой из добрых побуждений."

        g oghm "Ладно, вы правы, сама виновата…"

        $question = False

    show furgon viki
    show geroy sc1
    show leo phone_sc1
    
    g bok "Долго ещё ехать?"    

    show leo sc1

    l "Неужели тебе не нравиться поездка, [g], тебе же всегда нравилось смотреть в окно и следить за дорогой."

    g oghm "Допустим, но в этот раз, братишка, от вас двоих пахнет ванилью. Вы флиртуете чересчур усердно."

    show coop sc1

    c "Плохая новость, подруга, они не прекратят. Однако, не всё так плохо, мы почти на месте"

    hide coop sc1
    show geroy sc1

    v "Жаль, что мы огорчили тебя, сестрёнка."
 
    g bok "Да, забей, мы почти на месте." 

    show geroy sc1

    g "Кстати, Куп, как, говоришь, фестиваль называется?"

    window hide
    
    
    show main_menu
    pause

    
    show black_scene with dissolve
    c "И-и-и-и-и-и-и-и-и-и-и… {w}Мы прибыли!"

    stop sound fadeout 1.0
    stop music fadeout 2.0
    jump scene2

# Сцена 2
label scene2:
    play music "<loop 0>audio/music/like_a_coffe.mp3" volume 0.4
    scene parking with fade

    show coop sc2:
        xalign 0.45

    show leo sc2:
        xalign 0.9

    show geroy sc2:
        xalign 0.1

    l "Фестиваль начнется в 10 вечера, когда окончательно стемнеет"

    show leo sc2_puzzled

    g "Ладно, что будем делать до начала?"

    show leo wviki6 with move:
        xalign 0.95

    v "Мы просто прогуляемся и посмотрим, где что находится"

    show leo wviki4

    c sc2_watches "К 6 часам утра начнутся выступления музыкальных групп"

    g sc2_facepalm "…"

    show coop sc2_head:
        xalign 0.4
    c "Да, брось, [g]! Ты же не думаешь, что люди соберутся только под утро. Движуха начнется еще до полуночи: выпивка, новые знакомства, да и атмосфера тут - что надо…"
    play sound "audio/car-parking-into-garage.mp3" volume 0.5
    show geroy sc2

    l wviki2 "Так что у нас будет достаточно времени нагуляться, да, Вики?"

    
    "Подъехал кабриолет, из которого выглянул мужчина в светлой рубашке."

    show stranger sc2_2

    s "Привет, ребята, а фестиваль уже начался или я слишком рано?"

    hide stranger

    show leo wviki8
    c "Нет, чувак, ты как раз вовремя"
    stop sound fadeout 1.0
    show stranger sc2_2

    s sc2_1 "Тогда рад знать, что не я один такой расторопный"

    hide stranger

    l wviki9 "Тебе же лучше - сейчас много парковочных мест свободно"

    show stranger sc2_3

    play sound "audio/car-parking-into-garage.mp3" volume 0.5
    s sc2_3 "Верно"
    s sc2_2 "Ну что ж, хорошего вам вечера"

    hide stranger

    g "Хм…"
    stop sound fadeout 1.0
    show leo wviki8
    show coop sc2_hh:
        xalign 0.45
    c  "О чем я и говорил, даже часа не прошло. А народ, ведь, только начал прибывать"

    g "Мне показалось, что он вел себя довольно странно"

    show leo wviki5
    v "А  мне показалось, что он достаточно приятный человек"
    show leo wviki6

    c sc2_smile "Подруга, не драматизируй, просто мужик приехал пообщаться"

    l wviki7 "Предлагаю не обращать внимания и последовать примеру того парня, и осмотреться"

    
    jump scene3

# Сцена 3
label scene3:

    scene scene3 with fade
    show scene3_1 with dissolve

    c "Стоит отдать должное организации, территория обставлена очень даже неплохо"

    l "Полностью согласен. А кстати, куда ты нас ведешь?"

    c "На смотровую площадку, конечно. Это, типа, основная фишка этого фестиваля, разве я не говорил?"

    g "Видишь, не только у меня проблемы с памятью"

    v "Это здорово! Виды дикой природы завораживают, жду не дождусь!"

    l "Вижу, ты полна энтузиазма, малыш. Пару минут и мы на месте"

    scene scene3_2 with fade

    show coop sc3 with dissolve:
        xalign 0.45

    show geroy hands_folded_smile with dissolve:
        xalign 0.15

    show leo wviki8 with dissolve:
        xalign 0.9

    play sound "audio/park-s-ljudmi-i-vorobjami.mp3" volume 0.5
    "Герои подошли к смотровой площадке. Все осматривают открывшийся лесной пейзаж."
    g hands_folded_smile "В чем прикол этих смотровых? Здесь нет ничего, кроме леса"

    show leo wviki10
    v "В этом вся суть: небо и лес во время затмения. Разве не здорово?"

    l wviki9 "Что насчет защиты глаз? На затмение вредно смотреть невооруженным взглядом"

    show leo wviki8
    c watches "Я читал, что где-то здесь продают какие-нибудь специальные солнечные очки или типа того"
    c sad "Так что за глаза можете не бояться"

    g hands_folded "А если эти очки уже раскупили?"

    c winks "Наденешь пакет на голову"

    g cringe "Ок"

    l wviki9 "Не собачтесь"

    c hungry "Ладно, пойдем осмотрим ресторанный дворик в ряду павильонов, я уже хочу есть"

    show leo wviki
    v "Заодно выясним, где туалет"

    l wviki4 "И бар"

    c smile "Зачет!"

    stop sound

    scene scene3_3 with fade

    play sound "audio/park-s-ljudmi-i-vorobjami.mp3" volume 0.5

    show geroy surprised with dissolve:
        xalign 0.9
    show coop smile with dissolve:
        xalign 0.55
    show leo wviki9 with dissolve:
        xalign 0.1    
    
    

    "Прошло 3 часа. Компания проводит время в ряду павильонов. "

    g surprised "Не думала, что будет столько народу…"

    show geroy hands_folded
    c hoh "Это еще немного, подруга. Ближе к утру еще больше народу будет"

    l wviki6 "Ладно, ребят, мы с Вики пойдем на смотровую"
   
    show leo wviki1
    v "Смотреть на звездное небо!"

    l wviki4 "С собой не зовем"

    g hands_folded_smile "Развлекайтесь, только не забудь мне брата потом вернуть"

    l wviki9 "Эй, я еще здесь!"

    show leo wviki10
    v "Не переживай, подруга, верну в целости и сохранности"

    hide leo with dissolve

    show coop hungry with move:
        xalign 0.45
    c hungry "Окей, а я к фургону, вздремну часок"

    show geroy
    g "Я с тобой!"

    c hoh "Не хочешь позависать здесь? Познакомиться с кем-нибудь?"

    g bruh "Хочешь бросить меня одну среди толпы незнакомцев?"
    g yep "Да ни в жизнь!"

    show geroy thx
    c hoh_smile "Как скажешь, трусишка. Тогда погнали!"

    stop music fadeout 2.0
    stop sound fadeout 10.0
    jump scene4

# Сцена 4
label scene4:
    scene parking stranger with fade

    show geroy hands_folded with dissolve:
        xalign 0.55
    show coop smile with dissolve:
        xalign 0.05
    

    c smile "Ладно, я спать."
    c hoh_smile "Ты, конечно, можешь лечь со мной, но брату сама объяснять будешь"

    g hands_folded_smile "Я не хочу спать"

    c hoh "Как скажешь"
    
    hide coop with dissolve
    g hands_folded_smile_yra "“Наконец-то, тишина”"

    show stranger straight with dissolve:
        xalign 0.9
    s "Решила отдохнуть от суеты?"

    show geroy surprised with move:
        xalign 0.4
    g "А! Да, верно"

    s straight_smile"Извини, если застал врасплох"

    g standing "Ничего, переживу… Как долго вы здесь? Пока мы шли, вас не было видно"

    play music "<loop 0>audio/music/guitar_not_cheerful.mp3" volume 0.3

    s straight_smile2"Я сам только что пришел. Не удивительно, что вы с другом меня не видели"

    g qes "Тоже устали от шума?"

    s straight_hot "А ты проницательная. Да, я не очень люблю большие скопления людей"

    g angry2 "Хах! Я тоже. Но зачем вы тогда приехали на фестиваль?"

    s s_smile "Давай так, мы оба перейдем на “ты” и я тебе отвечу"

    g hands_folded "Хорошо"

    s s_what "Мне было интересно, как организуют фестиваль по такому поводу. Но, в первую очередь, я здесь из-за затмения"

    g hands_folded_smile "А что вам… то есть тебе помешало приехать ближе к началу самого затмения?"

    s s_left "Я боялся, что мне не хватит места на стоянке, да и потом в спешке искать что где находится как-то не хотелось"

    g hands_folded "Ммм… Понятно"

    s s_qes "Ваша компания разделилась?"

    g cringe "Да, голубкам нужно время, чтобы побыть вдвоем"

    s s_smile "Нельзя винить парочки за их желание побыть наедине в такой атмосфере"

    g hands_folded_smile "Это ты с ними в одной машине не был, так что тебе повезло"

    s s_smile_not "Слишком неловко?"

    g smile "Читаешь мои мысли"

    show stranger s_boo
    g sad "Просто мой брат уделяет своей девушке слишком много внимания"

    s s_qes "Разве это плохо? Может быть у них все серьезно, а ты напрягаешься понапрасну"

    g sad_very "Неприятно, когда единственный родной человек игнорирует мое присутствие из-за подружки…"

    s s_boo "Да, это грубовато"

    g sad_very "..."

    s s_qes "Эй, ты в порядке?"

    g smile "Да… Забей, со мной такое иногда случается"

    s s_smile_not "Послушай, жизнь же не стоит на месте. Все постоянно меняется и это не повод вешать нос"

    show geroy hands_folded
    s s_smile "Особенно, когда тебе есть к чему стремиться"
    s s_what "Только принимая удары судьбы мы по-настоящему учимся крепко стоять на ногах"

    g smile2 "Это звучало старомодно, ты точно из нашего времени?"

    s ops"Хах, в точку! Современным меня не назовешь"
    s "На самом деле, мне кажется, что ты малость драматизируешь"

    g hands_folded_smile "Может ты и прав…"

    s straight_smile2 "Знаешь, ты напоминаешь мне кое-кого…"
    s straight_hot "Что ж, до встречи!"

    g bruh "Ладно, пока"
    hide stranger with dissolve
    show geroy angry with move:
        xalign 0.5
    stop music fadeout 3.0
    g angry2 "*провожает незнакомца взглядом*"
    g angry3 "“Это было странно. Думаю, я достаточно времени пробыла на стоянке. Вернусь к людям, заодно поищу Лео и Вики”"

    
    jump scene5

# Сцена 5
label scene5:
    play music "<loop 0>audio/music/guitar_cheerful.mp3" volume 0.5
    play sound "audio/park-s-ljudmi-i-vorobjami.mp3" volume 0.5
    scene scene3_3 with fade
    show geroy side_surprised with dissolve:
        xalign 0.20

    g "Кажется, людей стало меньше"
    g "Даже если так, голубков все равно не видно"
    g standing "Осмотрюсь немного, может найду их"
    g angry3 "..."
    g tensing "Что-то мне не нравится, что их до сих пор не видно"

    menu:
        "Поспрашивать у людей":
            $ question = True

        "Искать дальше":
            $ question = False

    if question == True:
        
        g side_surprised "Может стоит поспрашивать у людей…"
        g "..."

        show levi with dissolve:
            xalign 1.0
        show geroy with move:
            xalign 0.1
        g surprised "Здравствуйте, вам не встречался высокий темноволосый парень в клетчатой куртке с родинкой у глаза или рыжая девушка в платье с двумя косичками у лица?"

        p "Не помню"
        p "Не, я не видел"
        show levi handup
        p 2 "Кажется, я видел, как похожий парень шел к смотровой площадке"
        g thx "Спасибо!"
        
        $question = False

    scene sed rhit with fade

    show geroy angry3 with dissolve

    g  "Итак, где же они…"
    g side "*осматривает смотровую площадку*"
    g standing "Не вижу их, может, ушли…"
    g tensing "Стоп, мне показалось или…"
    show geroy with move:
        xalign 0.65
    "Роуз находит на краю смотровой площадки 2 лепестка багрового цвета."
    g angry2 "Не видела, чтобы где-то здесь продавали цветы…"
    g tensing "Ну или, чтобы они вообще росли где-то здесь"
    g "Очевидно, что Лео и Вики здесь нет… Может они среди павильонов…"

    scene scene3_3 with fade

    show geroy yep with dissolve:
        xalign 0.9
    

    g  "Да, куда же они подевались?!"
    show viki left with dissolve:
        xalign 0.1
    g bruh "Секунду. Вижу знакомое платье…"
    
    g shout2 "Э-э-й, Вики!"
    play sound "audio/run.mp3" volume 1.0

    show viki pensive with move:
        xalign 0.3
    v  "..."

    show geroy with move:
        xalign 0.7
    stop sound fadeout 2.0
    g hands_folded "Фух! Я вас уже обыскалась"

    
    v pensive "Слушай, а ты не видела Лео?"

    g hands_folded_smile "Как это, вы же друг от друга не отлипаете?"

    v guilty "Мы с Лео были на смотровой площадке, но мне надо было отлучиться, а когда я вернулась, его уже там не было"
    show geroy hands_folded
    v guilty2 "Я думала, что он пошел сюда, но, по всей видимости, ошиблась"

    menu:
        "Спросить":
            $ question = True

        "Промолчать":
            $ question = False

    if question == True:
        
        g hands_folded "Ты не видела красных цветов, пока вы были на смотровой площадке?"
        
        v om2 "Нет, не видела, в округе вообще нет декоративной растительности…"

        g tensing "Так, теперь мне это вообще не нравится"
        
        $question = False

    show geroy
    g "Может пойдем на стоянку, вдруг он решил вернуться в фургон?"

    v guilty2 "Думаешь, он мог уйти без предупреждения?"

    g standing "В любом случае на смотровой площадке я его не видела…"
    g angry3 "И здесь его тоже нет"
    hide viki
    hide geroy
    show viki wgeroy2 with dissolve
    g "Лучше быстрее проверить"

    v "Может мы зря переживаем, и он решил подготовить сюрприз?"

    show viki wgeroy4 with move:
        xalign 0.4
    g "Послушай, Ви, я не оставлю тебя одну, пока мы его не найдем, а искать мы пойдем прямо сейчас, возражения не принимаются!"

    show viki wgeroy2 with move:
        xalign 0.3
    v "Э-э-эй, да ладно тебе!"

    stop music
    scene parking stranger with fade
    show viki pensive2 with dissolve:
        xalign 0.2
    show geroy angry3 with dissolve:
        xalign 0.55

    v "Мы пришли, но здесь никого нет"

    g bruh "А куда пропал Купер?!"

    c "Эй, девчонки, кого-то ищете?!"

    g hands_folded "Ты же спал!"

    show coop with dissolve:
        xalign 0.95
    c hoh_looks "Спал, но у ребят сигналка сработала и не выключилась"

    p "Привет"
    p "Хей"
    p "Чё как"

    c hoh "Пришлось вмешаться. А ребята оказались клевыми…"

    v guilty2 "Слушай, Куп, а ты не видел Лео?"

    c winks "Как раз хотел тебя спросить, ведь наша сладкая парочка обычно всегда вместе"

    g angry3"Я тоже удивилась, когда обнаружила Вики одну"

    show coop
    c "Не думаю, что Лео мог просто потеряться, скорее он что-то задумал"

    v "Спасибо, что успокоил, Куп"

    g tensing "Но мы его нигде не видели"

    c cyclop "Эй, мы с твоим братом сто лет знакомы, подруга, он не даст себя в обиду на фестивале хипстеров"

    show geroy angry3
    show coop
    v guilty "Да, [g], ты зря паникуешь, еще меня заставила нервничать, даже толком не дала мне подумать. Насмотрелась своих ужастиков и теперь переживаешь из-за каждой мелочи. Есть масса причин, по которым Лео мог задержаться"
    v smile "Должно быть, он прямо сейчас сам меня ищет"

    g angry3 "Может подождем его здесь?"

    v om2 "Да, успокойся уже, пожалуйста!"
    hide viki with dissolve

    c hoh_looks "Ты заставила ее понервничать, но не думаю, что она будет держать обиду"

    g tensing "Все это меня настораживает"

    c hoh "Останешься у фургона или еще дров наломаешь?"

    g yep "..."
    g standing "Я хочу поговорить с кое-кем"
    hide coop with dissolve
    show geroy with move:
        xalign 0.35
    "Роуз уходит к машине разговорчивого соседа по парковке."
    g shout "Эй! Старомодный парень!"
    g bruh "Куда же он запропастился? Ох…"

    "[g] обнаруживает возле колеса автомобиля одинокий багровый лепесток."

    g angry2 "Снова? У него ведь не было цветов"
    g tensing "Все это не просто так…"
    g angry "Я должна догнать Вики"

    jump scene6

# Сцена 6
label scene6:
    scene scene3_3 with fade
    show geroy standing

    g "В 5 утра здесь так много людей, что не протолкнуться. Кажется, весь фестиваль собирается в одном месте"
    g angry3 "Блин, не хватало еще её потерять"
    g side "Может все они в толпе?"
    g side_surprised "Кажется, я вижу Вики"
    g shout2 "Эй! Вики!"

    "Девушка уходит из людного места по тропе в сторону леса и теряется из виду."

    g yep "Куда она, черт возьми, идет? Может она заметила Лео?"

    "[g] в спешке покидает людное место и идет по тропе, на которой последний раз видела Вики. Тропа заканчивается у трейлера, припаркованного у лесного ограждения."
    stop music fadeout 1.0
    scene scene6 with fade

    play music "audio/music/glitch.mp3"

    show geroy angry3 with dissolve
    g angry3 "Здесь, на удивление, тихо"
    g "Да и люди все ушли"
    g tensing "Боже, куда тебя занесло, Вики"
    g "Хм… Кажется за тем трейлером кто-то есть, я вижу тени."
    show geroy with move:
        xalign 0.6
    g "..."
    window hide
    show nightmare with fade
    pause

    show semifinal with dissolve
    pause
    "Из-за дерева возле трейлера видится нечто пугающее:"
    window hide
    play sound "audio/fire-fireplace-crackle.mp3"

    show dead_meat with dissolve
    pause
    "У костра, горящего возле трейлера, лежит бледная девушка, со стеклянным взглядом, на земле видны пятна крови. Над ней нависает фигура в белой маске и держит в правой руке розу кроваво-красного цвета. В лице девушки [g] узнает Вики."
    hide dead_meat
    "Фигура бросает розу на бездыханное тело, которое после этого бесследно уходит под землю"
    show finfin with dissolve
    pause
    stop sound
    play sound "audio/run.mp3"
    
    show black_scene with fade
    g "Черт, черт, черт…"
    
    stop music
    window hide
    pause
    show to_be_continued with dissolve
    pause
    return



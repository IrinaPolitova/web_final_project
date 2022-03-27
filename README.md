# French Website
Проект-сайт, посвященный изучению французского языка по стихотворениям и песням.  
Сайт находится вот здесь: (здесь будет ссылка)  
### Что есть на сайте:  
* **Раздел "Аудирование":** сайт предложит вам текст песни с пропусками и отправит вам саму песню. Эту песню вам нужно будет послушать и на основе неё заполнить пропуски. В конце вы увидите правильные ответы и полный текст без пропусков, сможете ещё раз послушать песню и сравнить её с текстом.
* **Раздел "Глаголы":** сайт предложит вам текст стихотворения с пропусками, в скобках у пропусков будут даны начальные формы глаголов. Вам будет предложено вписать нужные формы глаголов так, чтобы они согласовались с остальным текстом. В конце вы увидите правильные ответы и полный текст стихотворения без пропусков.
* **Раздел "Поэзия или компьютер?":** сайт предложит вам строчку, и вам нужно будет попробовать угадать, настоящая ли это строчка из реального французского стихотворения или же эта строчка была сгенерирована компьютером. В этом же разделе на вкладке **"Статистика"** вы сможете посмотреть статистику правильных ответов, данных в сумме всеми пользователями на это задание.
### Кому подходит сайт:
* **Изучающим французский язык.** Если вы изучаете французский и хотели бы потренировать аудирование и грамматику, то этот сайт для вас! С помощью него вы сможете продвинуться в своих навыках распознавания французских слов на слух, а также сможете лучше запомнить формы французских глаголов.
* **Влюбленным во французскую поэзию и музыку.** Если вам нравится читать стихи на французском или слушать песни на этом языке, то этот сайт вам отлично подойдёт! Здесь вы не только потренируетесь во французском, но и почитаете оригинальные французские произведения и узнаете новые песни.
* **Желающим поиграть в игру с компьютером.** Если вы хотели бы проверить свои умения отличать настоящие строчки от созданных компьютером, то вам подойдет раздел "Поэзия или компьютер?". Там вы сможете потренироваться отличать подлинное от искусственного и посмотреть, как с этим справляются другие игроки.
### Подробнее о проекте - как разрабатывался сайт:
Разработка сайта проходила в несколько этапов:  
  1.  **Сбор данных.** На этом этапе была собрана база данных, состоящая из текстов стихотворений и песен, все они были взяты с нескольких сайтов (использованные сайты помещены ниже в разделе "Использованные сайты").
  2.  **Написание сайта.** На этом этапе был написан некоторый черновой вариант сайта, включающий в себя панель навигации, описание функционала сайта и некоторые приветственные песни (пока что без функций, связанных с поэзией и песнями).
  3.  **Добавление функций.** На этом этапе были добавлены все функции, связанные с разделами "Аудирование" и "Глаголы" - были написаны программы, которые выбирают с помощью рандома текст песни или стихотворения, выдают его пользователю с пропусками, принимают у пользователя ответ, проверяют и выдают правильный ответ.
  4.  **Добавление игры.** На этом этапе был добавлен раздел "Поэзия или компьютер?". Для него сначала на всех строчках стихотворений была обучена модель, и затем на сайт была добавлена функция генерации строчек - подлинных или искусственных, созданных с помощью модели, а также добавлен сбор ответов пользователей в базу данных.
  5.  **Добавление статистики.** На этом этапе был добавлен график, показывающий правильность ответов пользователей на вопросы игры "Поэзия или компьютер?".  

Были использованы следующие **инструменты:** flask, базы данных, краулер, морфологический анализатор Spacy и цепи Маркова.
### Использованные сайты:
(здесь будут перечислены сайты, с которых были взяты стихотворения и песни)

# French App Rendre
Проект-сайт, посвященный изучению французского языка по стихотворениям.  
Сайт находится вот здесь: (здесь будет ссылка)
### Что есть на сайте:  
* **Раздел "Аудирование":** сайт предложит вам текст стихотворения с пропусками и отправит вам аудио с прочтением стихотворения. Его вам нужно будет послушать и заполнить пропуски. В конце вы увидите правильные ответы и полный текст без пропусков, сможете ещё раз послушать стихотворение и сравнить его с текстом.
* **Раздел "Поэзия или компьютер?":** сайт предложит вам строчку, и вам нужно будет попробовать угадать, настоящая ли это строчка из реального французского стихотворения или же эта строчка была сгенерирована компьютером. В этом же разделе на вкладке "Статистика" вы сможете посмотреть статистику правильных ответов, данных в сумме всеми пользователями на это задание.
### Кому подходит сайт:
* **Изучающим французский язык.** Если вы изучаете французский и хотели бы потренировать аудирование, то этот сайт для вас! С помощью него вы сможете продвинуться в своих навыках распознавания французских слов на слух.
* **Влюбленным во французскую поэзию.** Если вам нравится читать стихи на французском языке, то этот сайт вам отлично подойдёт! Здесь вы не только потренируетесь во французском, но и почитаете и изучите оригинальные французские произведения.
### Подробнее о проекте - как разрабатывался сайт:
Разработка сайта проходила в несколько этапов, они все представлены в таблице ниже.  
Были использованы следующие **инструменты:** flask, базы данных, краулер, морфологический анализатор Spacy и цепи Маркова.
| Этап | Что было сделано |
| :------------- | :------------- |
| **Сбор данных** | Собрана таблица, состоящая из текстов, аудио и мета-данных стихотворений, все они были взяты с сайта https://wheatoncollege.edu/vive-voix/titres/; файл с кодом - french_poems.ipynb, таблица - french_poems.csv |
| **Написание сайта** | Написан черновой вариант сайта, включающий в себя панель навигации, описание функционала сайта и некоторые приветственные слова (пока что без разделов, связанных с поэзией) |
| **Добавление игры** | Добавлен раздел "Поэзия или компьютер?"; сначала на всех строчках стихотворений была обучена модель, и затем на сайт была добавлена функция генерации строчек - подлинных или искусственных, созданных с помощью модели, а также добавлен сбор ответов пользователей в базу данных |
| **Добавление статистики** | Добавлен график, показывающий правильность ответов пользователей на вопросы игры |
| **Добавление заданий** | Добавлен раздел "Аудирование" - написана программа, которая выбирает с помощью рандома текст стихотворения, выдаёт его пользователю с пропусками, принимает у пользователя ответ, проверяет и выдаёт правильный ответ |

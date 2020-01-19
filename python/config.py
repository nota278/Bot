# -*- coding: utf-8 -*-

# Pluses and minuses will be removed in these chats
chats_deleting = [
    2000000003
]

# Check your search line, when you`re in the needed chat. Then copy it`s id after "vk.com/im?peers=c"
userbot_chats = {
    2000000003: 212
}

# Chats where you can change reputation of other users
chats_whitelist = [
    2000000003
]

INT32 = 2147483647

help_string = """Вот что я умею:
"помощь" или "help" — вывод этого сообщения.
"топ" или "top" — вывести список пользователей с рейтингом, или указанными языками программирования.
"рейтинг" или "rating" — вывести свой рейтинг, или рейтинг другого пользователя.
"+" или "-" — принять участие в коллективном голосование за или против другого пользователя.
"+5" или "-4" — передать свой рейтинг другому пользователю или пожертвовать своим рейтингом, чтобы проголосовать против него.
"+= C++" — добавить язык программирования в свой список языков программирования.

1 единица рейтинга прибавляется, если два разных человека голосуют за "+".
1 единица рейтинга отнимается, если три разных человека голосуют против "-".

Команды по отношению к другим пользователям запускаются путём ответа или репоста их сообщений.
Голосовать против других пользователей могут только те пользователи, у кого не отрицательный рейтинг, т.е. 0 и более.
Голосование за самого себя не работает.
Все команды указаны в кавычках, однако отправлять в чат их нужно без кавычек, чтобы они выполнились.
"""

default_programming_languages = [
    "Assembler",
    "JavaScript",
    "TypeScript",
    "Java",
    "Python",
    "PHP",
    "Ruby",
    "C\+\+",
    "C",
    "Shell",
    "C\#",
    "Objective\-C",
    "R",
    "VimL",
    "Go",
    "Perl",
    "CoffeeScript",
    "TeX",
    "Swift",
    "Kotlin",
    "F\#",
    "Scala",
    "Scheme",
    "Emacs Lisp",
    "Lisp",
    "Haskell",
    "Lua",
    "Clojure",
    "TLA\+",
    "PlusCal",
    "Matlab",
    "Groovy",
    "Puppet",
    "Rust",
    "PowerShell",
    "Pascal",
    "Delphi",
    "SQL",
    "Nim",
    "1С",
    "КуМир",
    "Scratch",
    "Prolog",
    "GLSL",
    "HLSL",
    "Whitespace",
    "Basic",
    "Visual Basic",
    "Parser",
]

default_programming_languages_pattern_string = "|".join(default_programming_languages)


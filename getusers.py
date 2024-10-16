def getLoop(name):
    teamUsers = {
        "Шарафутдинова Н.": "@natalya_sharafutdinova_ext",
        "Серов Н.": "@nikita_serov1",
        "Лозник М.": "@mikhail_loznik",
        "Гринев Д.": "@dmitriy_grinev",
        "Куличев М.": "@mark_kulichev",
        "Шелухин А.": "@aleksandr_sheluhin",
        "Калмыков Д.": "@dmitriy_kalmykov",
        "Лукина Н.": "@natalya_lukina",
        "Коновальчук И.": "@igor_konovalchuk",
        "Крюков В.": "@vitaliy_kryukov_ext",
        "Ладин В.": "@vyacheslav_ladin",
        "Рябов Д.": "@daniil_ryabov",
        "Годик М.": "@mariya_godik",
        "Бородин Е.": "@evgeniy_borodin_ext",
        "Абрамов Б.": "@boris_abramov_ext",
        "Павел Н.": "@pavel_nechaev_ext",
        "Иван Ф.": "@ivan_frolov",
        "Елена К.": "@elena_kuschenko1 ",
        "Сергей П.": "@sergey_potapov_ext",
        "Алексей Сойманов": "@aleksey_soymanov",
        "Сергей Смирнов": "@sergei_smirnov"


    }
    return teamUsers[name]

def getChannel(name):
    channels = {
        'PackmanDC':'WMS-botchannel'
    }
    return channels[name]

def getiCal(name):
    ical = {
        'PackmanDC': 'https://obs-grafana-oncall-yc-techno.apps.lmru.tech/45/api/v1/schedules/SU1T3PIJUVFNB/export?token=12897f7554c2d6d6b9994109c3588541'
    }
    return ical[name]


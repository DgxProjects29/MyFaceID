import datetime


# Associate the id of a person with his data

def get_id_data():
    return {"0": ["0", "Diego Puche", "17", "InevaUp"],
            "1": ["1", "Sergio Beltran", "17", "Company"],
            '2': ["2", "Gabriel Daza", "17", "Company"],
            "3": ["3", "Andres Rueda", "17", "Company"],
            '4': ["4", "Valentina L", "17", "Company"]}


# Get the dictionary and return a text which is used for the history
def dic_to_text(dic, is_av):
    text_dic = ''
    st = '\n'

    if len(dic) != 0:
        for il, i in enumerate(dic):
            if len(dic) - 1 == il:
                st = ''
            if is_av:
                text_dic += str(i) + ': ' + str(dic[i])[:4] + st
            else:
                text_dic += str(i) + ': ' + str(dic[i]) + st
    else:
        text_dic = 'None'

    return text_dic


def get_current_time():
    return str(datetime.datetime.now())[:19]

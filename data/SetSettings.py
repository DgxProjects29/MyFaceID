import pickle

# times is given in milliseconds

# blue_mode: 0 = not use bluetooth mode, 1 = use bluetooth mode

# refresh_history: the time to take a sample of the face and save it in the history
# depends on the speed of your CPU

# refresh_blue: a cooldown time which is used when a person is recognized using bluetooth mode

# average_num, a smaller number represents a more accurate match
# votes_num, a higher number represents a more accurate match
# it is stricter if it is more accurate


action = int(input("input action: "))

settings = {'blue_mode': 0,
            'blue_com': "COM11",
            'blue_bauds': 9600,
            'refresh_blue': 330,
            'refresh_history': 50,
            'average_num': 0.4,
            'votes_num': 5}

if action == 1:
    f = open("settings.pickle", "wb")
    f.write(pickle.dumps(settings))
    f.close()
else:
    load_settings = pickle.loads(open("settings.pickle", "rb").read())
    print(load_settings)

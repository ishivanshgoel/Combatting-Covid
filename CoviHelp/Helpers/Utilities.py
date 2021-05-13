import datetime

class Utilities():
    def __init__(self):
        pass
    
    # convert time to integer
    def to_str(self,dt_time):
        return str(10000000*dt_time.year + 1000000*dt_time.month + 100000*dt_time.day + 10000*dt_time.hour + 10000*dt_time.minute + 1000*dt_time.second + 100*dt_time.microsecond)

    def gen_id(self,user, name, state, ty,contact):
        time = datetime.datetime.now()
        return hash(str(user) + str(name) + str(state) + str(ty) + str(contact) + self.to_str(time))

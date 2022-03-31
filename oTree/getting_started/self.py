
#not working
class Restaurant(object):
    bankrupt = False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")


x = Restaurant()
y = Restaurant()

x.bankrupt
y.bankrupt


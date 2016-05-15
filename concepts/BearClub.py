class BearClub(object):
  dues_paid = False
  def bears_happy(self):
    if not dues_paid:
      print "bears are please"

x = BearClub()
print x.dues_paid

y = BearClub()
y.dues_paid = True
print y.dues_paid

print x.dues_paid

#Multiple Modules:

from Excercise_9_5 import User
from Excercise_9_11 import Admin

admin = Admin('Tony','stark',32,'mr.')
User1 = User('Thor','The son of odin',2134,'mr.')

admin.privileges1.show_privileges()
User1.increment_login_attempts()

# check compatibility
import py4web

assert py4web.check_compatible("0.1.20190709.1")

from .all_controllers.common import db

from .all_controllers.students import students



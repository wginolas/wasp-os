# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2020 Daniel Thompson

import wasp
from gadgetbridge import *

from apps.timer import TimerApp
wasp.system.register(TimerApp())

from apps.alarm import AlarmApp
wasp.system.register(AlarmApp())

wasp.system.schedule()

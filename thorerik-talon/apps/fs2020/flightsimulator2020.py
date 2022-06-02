from talon import Module, Context, actions

mod = Module()
apps = mod.apps
apps.fs2020 = "app.name: Microsoft Flight Simulator"
apps.fs2020 = "app.name: FlightSimulator.exe"

ctx = Context()
ctx.matches = r"""
os: windows
app: fs2020
"""

@mod.action_class
class fs2020_actions:
    def fs2020_gear_up():
        """Gear up"""
    def fs2020_gear_down():
        """Gear down"""

@ctx.action_class('user')
class UserActions:
    def fs2020_gear_up(): actions.key('ctrl-alt-g')
    def fs2020_gear_down(): actions.key('ctrl-g')
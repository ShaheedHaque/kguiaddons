#
# Copyright 2016 by Shaheed Haque (srhaque@theiet.org)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301  USA.
#
"""
SIP binding customisation for PyKF5.KGuiAddons. This describes:

    * The additional module-specific SIP file generator rules.
"""

import os, sys

import rules_engine
sys.path.append(os.path.dirname(os.path.dirname(rules_engine.__file__)))
import Qt5Ruleset

def qualify_kfontutils_enum(container, function, parameter, sip, matcher):
    sip["init"] = "KFontUtils::" + sip["init"]

def local_parameter_rules():
    return [
        ["KFontUtils", "adaptFontSize", "flags", ".*", ".*", qualify_kfontutils_enum],
    ]

class RuleSet(Qt5Ruleset.RuleSet):
    """
    SIP file generator rules. This is a set of (short, non-public) functions
    and regular expression-based matching rules.
    """
    def __init__(self):
        Qt5Ruleset.RuleSet.__init__(self)
        self._param_db = rules_engine.ParameterRuleDb(lambda: local_parameter_rules() + Qt5Ruleset.parameter_rules())

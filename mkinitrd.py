#!/usr/bin/env python3

# Copyright 2012-2014 Jonathan Vasquez <jvasquez1011@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from subprocess import call

import pkg.libs.Variables as var

from pkg.libs.Core import Core
from pkg.libs.Tools import Tools
from pkg.hooks.Addon import Addon

class Main(object):
    # Let the games begin ...
    @classmethod
    def start(cls):
        Tools.ProcessArguments(Addon)
        call(["clear"])
        Tools.PrintHeader()
        Core.PrintMenu()

        if var.kernel or Addon.GetFiles():
            Core.GetDesiredKernel()

        Core.VerifySupportedArchitecture()
        Tools.Clean()
        Core.VerifyPreliminaryBinaries()
        Core.CreateBaselayout()
        Core.VerifyBinaries()
        Core.CopyRequiredFiles()
        Core.CopyModules()
        Core.CopyFirmware()
        Core.CreateLinks()
        Core.CopyDependencies()
        Core.LastSteps()
        Core.CreateInitramfs()
        Tools.CleanAndExit(var.initrd)

if __name__ == '__main__':
    Main.start()
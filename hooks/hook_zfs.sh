# Copyright (C) 2012 Jonathan Vasquez
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Source LVM Specific Functions
. resources/functions_zfs.sh

# Required Binaries, Modules, and other files
JV_INIT_BINS="busybox zpool_layout hostid spl splat mount.zfs zdb zfs zinject zpios zpool ztest"
JV_INIT_MODS="spl splat zavl znvpair zunicode zcommon zfs zpios"

# Init file in files/
INIT_FILE="init_zfs"

# Ask for desired kernel
getTargetKernel	

# Ask for zfs pool name
echo -n "Please enter ZFS pool name: " && read ZFS_POOL_NAME && echo ""

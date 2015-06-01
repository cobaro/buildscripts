#! /usr/bin/env python

import getopt, os, platform, string, sys

if __name__ == "__main__":
    "Report a range system identifiers in various formats"

    USAGE = """Usage: %s [options]
         Options:
         [-h] This help
         [-s] separator character [default space]

         [-b] bits [e.g, 32, 64]
         [-d] distribution [e.g, ubuntu, centos]
         [-l] linkage [e.g, elf, windowspe]
         [-m] machine [e.g, x86, x86_64, amd64]
         [-v] version [e.g 8.1]
    All components are printed in command line order\n""" \
        %(os.path.basename(sys.argv[0]))

     
    try:
        (optlist,args) = getopt.getopt(sys.argv[1:], "bdhlms:v")
    except:
        sys.stderr.write(USAGE)
        sys.exit(0)

    if not optlist:
        sys.stderr.write(USAGE)
        sys.exit(0)

    # bits, linkage
    machine = platform.machine().lower()
    b, l = platform.architecture()
    if b == "64bit":
        bits = "64"
    elif b == "32bit":
        bits = "32"
    linkage = l.lower()
    
    # Cope with some initial platforms
    distribution = platform.system().capitalize()
    if distribution == "Windows":
        version = platform.win32_ver()[0]
    elif distribution == "Darwin":
        distribution = "MacOSX"
        version =  '.'.join(string.split(platform.mac_ver()[0], '.')[:2])
        linkake = "macho" # Not reported by platform.machine()
    elif distribution == 'Linux':
        distribution, version, name = platform.dist()
        distribution = distribution.capitalize()

    separator = ' ' # space by default

    outputs = []

    for (opt, arg) in optlist:
        if opt == '-h':
            sys.stderr.write(USAGE)
            sys.exit(0)

        elif opt == '-s':
            separator = arg
            
        elif opt == '-b':
            outputs.append(bits)

        elif opt == '-d':
            outputs.append(distribution)

        elif opt == '-l':
            outputs.append(linkage)

        elif opt == '-m':
            outputs.append(machine)

        elif opt == '-v':
            outputs.append(version)

    if not outputs:
        sys.stderr.write(USAGE)
        sys.exit(0)

    print separator.join(outputs)

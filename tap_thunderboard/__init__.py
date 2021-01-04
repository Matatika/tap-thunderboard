"""Singer.io tap that syncs data from Thunderboards."""
#!/usr/bin/env python3
import argparse
import pkg_resources

import tap_thunderboard.scan as scan

def main():
    """Main entrypoint into this module."""

    version = pkg_resources.require("tap_thunderboard")[0].version

    # Parse our args, before handing off to singer
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v', '--version',
        help='Print version',
        action='version', version=version)
    parser.add_argument(
        '-s', '--scan', 
        help="Scan and dump thunderboards data",
        action='store_true')

    # handle execution
    args = parser.parse_args()
    if args.scan:
        scan.run()
    else:
        parser.print_help()



if __name__ == "__main__":
    main()

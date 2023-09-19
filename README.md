# OpenCue Submit Add-on

## Overview

This is an add-on to submit jobs to OpenCue, directly from Blender.

## Contributing

To install the required python libraries, do the following:

In the Blender terminal execute:
	
	import sys
	sys.exec_prefix

The result is '/path/to/blender/python', which we will need in the next commands.

Now, in an administrator terminal execute:

	cd /path/to/blender/python/bin
	./python.exe -m ensurepip
	./python.exe -m pip install -r /path/to/requirements.txt
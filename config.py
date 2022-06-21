# Listen port
LISTEN_PORT = 8888

#YYYYMMDD, YYYYMM and YYYY formats are accepted
DATE = '20090621' # 13 years ago today. Would recommend keeping it in the style
# of "X years ago today", but not required by any means.

# Allow the client to load pages and assets up to X days after DATE.
# Set to None to disable this restriction.
DATE_TOLERANCE = 365

# Send Geocities requests to oocities.org if set to True.
GEOCITIES_FIX = True

# Use the original Wayback Machine URL as a shortcut when loading images.
# May result in faster page loads, but all images will point to
# http://web.archive.org/... as a side effect. Set this value to 2 to enable an
# experimental mode using authentication on top of the original URLs instead
# (which is not supported by Internet Explorer and some other browsers).
QUICK_IMAGES = True

# Use the Wayback Machine Availability API to find the closest available snapshot to the desired date
# If using non-specific date, its generally okay to disable this. Date tolerance
# will be capped at 365 though.
WAYBACK_API = True

# Allow the Content-Type header to contain an encoding. Some old browsers
# (Mosaic?) don't understand that and fail to load anything - set this to
# False if you're using one of them.

# If going to use this on a real retro computer disable this.
CONTENT_TYPE_ENCODING = True

# Development mode / Logs mode. In production, set to True. When wanting to log, set to False.
SILENT = True

# Enables the settings page on http://web.archive.org if set to True.
# WARNING: Settings changed here affect EVERYONE on the proxy!
# Useful if you are the only client and want to change dates fast.
SETTINGS_PAGE = False

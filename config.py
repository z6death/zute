# First, handle the autoconfig loading requirement
config.load_autoconfig(False)

## ===== CORE COLOR SETTINGS =====
# Text colors
c.colors.completion.fg = '#00FF4C'
c.colors.completion.odd.bg = '#000000'  # Fixed from .fg to .bg
c.colors.completion.even.bg = '#000000' # Fixed from .fg to .bg
c.colors.statusbar.normal.fg = '#00FF4C'
c.colors.statusbar.insert.fg = '#00FF4C'
c.colors.statusbar.command.fg = '#00FF4C'
c.colors.statusbar.url.fg = '#00FF4C'
c.colors.statusbar.url.success.https.fg = '#00CC3D'
c.colors.hints.fg = '#00FF4C'

# Background colors
c.colors.completion.category.bg = '#000000'
c.colors.completion.category.fg = '#00FF4C'  # Added for completion text
c.colors.statusbar.normal.bg = '#000000'
c.colors.statusbar.insert.bg = '#000000'
c.colors.statusbar.command.bg = '#000000'
c.colors.tabs.bar.bg = '#000000'
c.colors.hints.bg = '#000000'

## ===== TAB COLORS =====
# Selected tab
c.colors.tabs.selected.odd.fg = '#000000'
c.colors.tabs.selected.odd.bg = '#00C400'
c.colors.tabs.selected.even.fg = '#000000'
c.colors.tabs.selected.even.bg = '#00C400'

# Other tabs
c.colors.tabs.odd.fg = '#00C400'
c.colors.tabs.odd.bg = '#000000'
c.colors.tabs.even.fg = '#00C400'
c.colors.tabs.even.bg = '#000000'

## ===== SIDEBAR CONFIGURATION =====
c.tabs.position = 'left'
c.tabs.show = 'always'
c.tabs.width = '12%'  # Smaller sidebar width like in the image
c.tabs.indicator.width = 0  # Remove tab underline
c.tabs.padding = {'bottom': 2, 'left': 2, 'right': 2, 'top': 2}  # Tighter padding
c.tabs.title.alignment = 'left'
c.tabs.favicons.show = 'always'
c.tabs.min_width = 80  # Minimum width in pixels
c.tabs.max_width = 150  # Maximum width in pixels

## ===== FONT SETTINGS =====
c.fonts.default_family = 'monospace'
c.fonts.default_size = '11pt'  # Slightly smaller font
c.fonts.tabs.selected = '11pt monospace'
c.fonts.tabs.unselected = '11pt monospace'
c.fonts.statusbar = '11pt monospace'
c.fonts.hints = 'bold 11pt monospace'

## ===== DARK MODE SETTINGS =====
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.page = 'always'
c.colors.webpage.darkmode.policy.images = 'never'  # Keep images normal

## ===== CONTEXT MENU =====
c.colors.contextmenu.menu.bg = '#000000'
c.colors.contextmenu.menu.fg = '#00FF4C'
c.colors.contextmenu.selected.bg = '#00C400'
c.colors.contextmenu.selected.fg = '#000000'
c.content.user_stylesheets = ['~/.config/qutebrowser/green-black.css']

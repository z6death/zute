
# ===== BASIC CONFIGURATION =====
config.load_autoconfig(False)
config.bind('<Escape>', 'fake-key <F13>')
# ===== CORE COLOR SETTINGS =====

# Initialize with stylesheet disabled
config.load_autoconfig()
config.set('content.user_stylesheets', ['~/.config/qutebrowser/green-black.css'])
# Corrected single toggle key
config.bind(',st', 
    'config-cycle content.user_stylesheets [] ["~/.config/qutebrowser/green-black.css"] ;; ' +
    'jseval -q py:message.info("Mono/Black theme " + ' +
    '("ENABLED" if config.val.content.user_stylesheets else "DISABLED"))',
    mode='normal')

# Darkreader toggle key
config.bind(',dr', 
    'config-cycle content.user_stylesheets [] ["~/.config/qutebrowser/dark-reader.css"] ;; ' +
    'jseval -q py:message.info("Darkreader " + ' +
    '("ENABLED" if config.val.content.user_stylesheets else "DISABLED"))',
    mode='normal')

# Text colors (All white #ffffff)
c.colors.completion.fg = '#ffffff'
c.colors.completion.category.fg = '#ffffff'
c.colors.statusbar.normal.fg = '#ffffff'
c.colors.statusbar.insert.fg = '#ffffff'
c.colors.statusbar.command.fg = '#ffffff'
c.colors.statusbar.url.fg = '#ffffff'
c.colors.hints.fg = '#ffffff'
c.colors.contextmenu.menu.fg = '#ffffff'

# Background colors (All black #000000)
c.colors.completion.category.bg = '#000000'
c.colors.completion.odd.bg = '#000000'
c.colors.completion.even.bg = '#000000'
c.colors.statusbar.normal.bg = '#000000'
c.colors.statusbar.insert.bg = '#000000'
c.colors.statusbar.command.bg = '#000000'
c.colors.tabs.bar.bg = '#000000'
c.colors.hints.bg = '#000000'
c.colors.contextmenu.menu.bg = '#000000'

# ===== TAB COLORS =====
# Selected tab (white background, black text)
c.colors.tabs.selected.odd.fg = '#000000'
c.colors.tabs.selected.odd.bg = '#ffffff'
c.colors.tabs.selected.even.fg = '#000000'
c.colors.tabs.selected.even.bg = '#ffffff'

# Other tabs (black background, white text)
c.colors.tabs.odd.fg = '#ffffff'
c.colors.tabs.odd.bg = '#000000'
c.colors.tabs.even.fg = '#ffffff'
c.colors.tabs.even.bg = '#000000'

# Context menu selection
c.colors.contextmenu.selected.fg = '#000000'
c.colors.contextmenu.selected.bg = '#ffffff'

# ===== SIDEBAR CONFIGURATION =====
c.tabs.position = 'left'
c.tabs.show = 'always'
c.tabs.width = '12%'
c.tabs.indicator.width = 0  # No tab underline
c.tabs.padding = {'bottom': 2, 'left': 2, 'right': 2, 'top': 2}
c.tabs.title.alignment = 'left'
c.tabs.favicons.show = 'always'
c.tabs.min_width = 80
c.tabs.max_width = 150

# ===== FONT SETTINGS =====
c.fonts.default_family = 'monospace'
c.fonts.default_size = '11pt'
c.fonts.tabs.selected = '11pt monospace'
c.fonts.tabs.unselected = '11pt monospace'
c.fonts.statusbar = '11pt monospace'
c.fonts.hints = 'bold 11pt monospace'

# ===== WEB CONTENT SETTINGS =====
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.bg = 'black'

# ===== START PAGES =====
c.url.start_pages = ['about:blank']
c.url.default_page = 'about:blank'

# ===== DARK MODE POLICY =====
# Enable for mono to force dark mode on websites
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = 'never'
c.colors.webpage.darkmode.policy.page = 'always'

# Session management (built-in commands)
config.bind(',ws', 'set-cmd-text -s :session-save ')
config.bind(',wl', 'set-cmd-text -s :session-load ')
config.bind(',sd', 'set-cmd-text -s :session-delete ')
config.bind(',wo', 'session-open')

# Quick workspace switch
config.bind(',wd1', 'spawn --userscript switch-workspace hacking')
config.bind(',wd2', 'spawn --userscript switch-workspace study')
config.bind(',wd3', 'spawn --userscript switch-workspace z6')
config.bind(',W1', 'spawn --userscript open-workspace hacking')
config.bind(',W2', 'spawn --userscript open-workspace study')
config.bind(',W3', 'spawn --userscript open-workspace z6')

# Tab stack
config.bind(',tg', 'tab-give')
config.bind(',tn', 'tab-focus next')
config.bind(',tp', 'tab-focus prev')
config.bind(',tm', 'tab-move')

# In config.py
c.auto_save.session = True  # Auto-save session on exit
c.session.default_name = 'default'  # Default session name

config.bind(',wd1', 'spawn --userscript switch-workspace hacking')
config.bind(',wd2', 'spawn --userscript switch-workspace study')
config.bind(',wd3', 'spawn --userscript switch-workspace z6')

# Opens new workspace while keeping current window open (capital W)
config.bind(',W1', 'spawn --userscript open-workspace hacking')
config.bind(',W2', 'spawn --userscript open-workspace study')
config.bind(',W3', 'spawn --userscript open-workspace z6')

# ===== COMPLETE AD-BLOCKING CONFIGURATION =====
# Enable ad-blocking system
c.content.blocking.enabled = True

# Blocking method (options: 'auto', 'adblock', 'hosts', 'both')
c.content.blocking.method = 'both'  # 'auto' = smart combination of methods

# ===== ADBLOCK LISTS (EasyList format) =====
c.content.blocking.adblock.lists = [
    # Essential filters
    'https://easylist.to/easylist/easylist.txt',  # General advertisements
    'https://easylist.to/easylist/easyprivacy.txt',  # Tracking protection
    'https://easylist-downloads.adblockplus.org/easylist.txt',  # Mirror
    
    # Anti-annoyance
    'https://secure.fanboy.co.nz/fanboy-annoyance.txt',  # Cookie notices, popups
    'https://easylist.to/easylist/fanboy-social.txt',  # Social media widgets
    
    # Regional filters (uncomment if needed)
    # 'https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt',  # Anti-CoinHive
    # 'https://stanev.org/abp/adblock_bg.txt',  # Bulgarian ads
]

# ===== HOSTS-BASED BLOCKING =====
c.content.blocking.hosts.lists = [
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',  # Standard
    'https://someonewhocares.org/hosts/zero/hosts',  # More aggressive
    # 'https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt',  # Mobile-focused
]

# ===== ADVANCED SETTINGS =====
# Whitelist certain sites (if needed)
c.content.blocking.whitelist = [
    # '*.example.com',  # Uncomment and add sites that break
]

# Block WebRTC IP leakage (privacy)
c.content.webrtc_ip_handling_policy = 'disable-non-proxied-udp'

# Block JavaScript popups
c.content.javascript.modal_dialog = False

# ===== KEYBINDS FOR ADBLOCK CONTROL =====
config.bind(',au', 'adblock-update', mode='normal')  # Update blocklists
config.bind(',at', 'adblock-toggle', mode='normal')  # Toggle ad-blocking
